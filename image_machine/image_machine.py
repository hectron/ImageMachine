# -*- coding: utf-8 -*-
from argparse import ArgumentParser
from ftp_client import FtpClient
from image_csv import ImageCsv
import pdb
import sys
import util

def main():
    """
    The main program execution flow. It provides the user with command-line
    arguments. Also, it downloads the files from the FTP and performs the
    processing on each file.
    """
    options = command_line_parser()

    if not options.config_file:
        print("No configuration file used. Defaulting to config.json")
        options.config_file = 'image_machine/config.json'

    files = download_files_from_ftp(options.config_file)
    process_files(files, options.config_file)
    upload_files(files, options.config_file)
    delete_old_files(files, options.config_file)

def download_files_from_ftp(configuration):
    """
    The main worker for downloading the files from the FTP. It attempts to
    safely download files from the FTP server.
    """
    files = []
    try:
        with FtpClient(configuration) as ftp_client:
            files = ftp_client.get_all_files()
    except:
        e = sys.exc_info()[0]
        util.conditional_print(
                'An error occured while trying to retrieve files via FTP.',
                'ERROR')
        util.conditional_print(e, 'ERROR')
    finally:
        return files

def process_files(files, configuration):
    """
    The main worker for processing each file that was downloaded.
    """
    for f in files:
        importer = ImageCsv(f)
        importer.perform_magic()

def upload_files(files, configuration):
    try:
        with FtpClient(configuration) as ftp_client:
            ftp_client.upload_files(files)
    except:
        e = sys.exc_info()[0]
        util.conditional_print(
                'An error occured while trying to UPLOAD files to the FTP server.',
                'ERROR')
        util.conditional_print(e, 'ERROR')

def delete_old_files(files, configuration):
    with FtpClient(configuration) as ftp_client:
        ftp_client.delete_files(files)

def command_line_parser():
    """
    Provides command line options. It also provides details as to how to use each flag.
    """
    parser = ArgumentParser(
            description="ಠ_ಠ Batch download files and create an export.")
    parser.add_argument("-c", "--config", dest="config_file",
            help="The configuration file that should be used by the application")
    parser.add_argument("-d", "--debug", dest="debug",
            help="Want to see debug statements?", action="store_true")

    args = parser.parse_args()

    return args

def quit_program():
    """
    The final print statement! Make it count.
    """
    print("I hope you got the data you wanted. Rock on. \m/")

if __name__ == "__main__":
    main()
    quit_program()

