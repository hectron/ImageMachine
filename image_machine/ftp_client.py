from ftplib import FTP
from os import path
from settings import Settings

class FtpClient(object):
    def __init__(self):
        settings = Settings()
        self.host = settings.get_ftp_value('Host')
        self.port = settings.get_ftp_value('Port')
        self.username = settings.get_ftp_value('Username')
        self.password = settings.get_ftp_value('Password')
        self.connection = None

    def __enter__(self):
        if not self.connection:
            self.open_ftp()

    def __exit__(self, exception, exception_value, tracebook):
        self.close_ftp()

    def open_ftp(self):
        if not self.connection:
            self.connection = FTP(self.host, self.port)
            self.connection.login(self.username, self.password)
            print('Connected to {0}:{1}.'.format(self.host, self.port))

        return self.connection

    def close_ftp(self):
        if self.connection:
            self.connection.quit()

        print('Connection to {0} closed.'.format(self.host))

    def get_file(self, filename, destination):
        local_filename = path.join(destination, filename)

        with open(local_filename, 'wb') as local_file:
            self.connection.retbinary('RETR {0}'.format(filename), local_file.write, 8*1024)

    def get_files(self, *filenames):
        for filename in filenames:
            self.get_file(filename, '.')

