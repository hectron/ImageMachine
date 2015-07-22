# -*- coding: utf-8 -*-
from argparse import ArgumentParser
import image_machine

def main():
    options = command_line_parser()

def command_line_parser():
    parser = ArgumentParser(description="ಠ_ಠ Batch download files and create an export.")
    parser.add_argument("-f", "--file", dest="source_file", help="The file that contains all the images for the export")
    parser.add_argument("-c", "--config", dest="config_file", help="The configuration file that should be used by the application")
    parser.add_argument("-d", "--debug", dest="debug", help="Want to see debug statements?", action="store_true")

    args = parser.parse_args()

    return args

def quit_program():
    print("I hope you got the data you wanted. Rock on. \m/")

if __name__ == "__main__":
    main()

    quit_program()
