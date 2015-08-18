import pdb
import settings
import sys
import util
from ftplib import FTP
from os import path

class FtpClient(object):
    """
    The FTP client is an interface to talk to our FTP using the credentials
    specified in the configuration file. It allows us to Create, Delete,
    Download files on the FTP.
    """
    def __init__(self, config_file=None):
        settings.init(config_file)
        self.host = settings.get_setting('ftp').get('host')
        self.username = settings.get_setting('ftp').get('username')
        self.password = settings.get_setting('ftp').get('password')
        self.connection = None

    def __enter__(self):
        """
        Allows us to use the `with` statement. It opens up an FTP connection.
        """
        self.open_ftp()
        return self

    def __exit__(self):
        """
        Safely closes the ftp connection when used in conjuction with `with`.
        """
        self.close_ftp()

    def open_ftp(self):
        """
        Returns the active connection is one is available. If not, it creates a
        new connection and returns that.
        """
        if not self.connection:
            self.connection = FTP(self.host)
            self.connection.login(self.username, self.password)
            util.conditional_print('Connected to {0}.'.format(self.host))

        return self.connection

    def close_ftp(self):
        """
        If a connection exists, it closes it. To avoid having to frequently
        call this, consider using the `with` statement.
        """
        if self.connection:
            self.connection.quit()

        util.conditional_print('Connection to {0} closed.'.format(self.host))

    def get_directory_contents(self, directory_path=''):
        """
        Returns the FTP directory contents.
        """
        files = []
        self.connection.dir(directory_path, files.append)

        return files

    def list_ftp_files(self, directory_path=''):
        """
        Returns the FTP directory files.
        """
        import re
        whitespace_re = re.compile(r'\s+')
        files = self.get_directory_contents(directory_path)
        formatted_files = []

        for f in files:
            result = whitespace_re.sub(' ', f).split(' ')
            if result[-2].isdigit():
                formatted_files.append(result[-1])

        return formatted_files

    def list_ftp_directories(self, directory_path=''):
        """
        Returns the FTP directory folders.
        """
        import re
        whitespace_re = re.compile(r'\s+')
        files = self.get_directory_contents(directory_path)

        formatted_results = []

        for f in files:
            result = whitespace_re.sub(' ', f).split(' ')
            if result[-2] == '<DIR>':
                formatted_results.append(result[-1])

        return formatted_results

    def get_file(self, filename, destination):
        """
        Retrieves a single file from the FTP.
        """
        local_filename = path.join(destination, filename)

        with open(local_filename, 'wb') as local_file:
            self.connection.retrbinary('RETR {0}'.format(filename), local_file.write, 8*1024)

    def get_files(self, filenames):
        """
        Retrieves the given filenames from the FTP.
        """
        for filename in filenames:
            util.conditional_print("Getting File: {0}".format(filename))
            self.get_file(filename, '.')

    def delete_files(self, files):
        """
        Removes the given filenames from the FTP.
        """
        for f in files:
            util.conditional_print("About to delete file: {0}".format(f))
            try:
                self.connection.delete(f)
            except:
                e = sys.exc_info()[0]
                print("Unable to delete file: {0}\nError: {1}".format(f, e))

    def get_all_files(self):
        """
        Lists all the directory contents, and retrieves the files that we can
        use.
        """
        files = self.select_allowed_files(self.list_ftp_files())

        util.work_in_tmp_directory('tmp')

        self.get_files(files)

        return files

    def select_allowed_files(self, files):
        """
        Defines what files we are able to use.
        """
        allowed_file_extensions = ['csv', 'txt']

        return [f for f in files if f.split('.')[-1] in allowed_file_extensions]

    def is_ftp_directory(self, dir_name, base_directory_path=''):
        """
        Checks whether or not the given `dir_name` is a directory within the
        `base_directory_path` location.
        """
        directories = self.list_ftp_directories(base_directory_path)
        return directories.count(dir_name) > 0

    def make_ftp_directory(self, dir_name, base_directory_path=''):
        """
        Safely creates an FTP directory if one does not exist.
        """
        if not self.is_ftp_directory(dir_name, base_directory_path):
            self.connection.mkd(dir_name)

    def upload_files(self, files, destination='NotSoDone'):
        """
        Uploads a list of files to the given destination.
        """
        if destination:
            self.make_ftp_directory(destination)
            self.connection.cwd(destination)

        for f in files:
            self.upload_file(f)

    def upload_file(self, the_file):
        """
        Uploads a single file to the FTP by transferring binary.
        """
        with open(the_file, 'rb') as f:
            self.connection.storbinary('STOR {0}'.format(the_file), f)

