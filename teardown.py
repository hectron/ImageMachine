#!/usr/bin/env python
import os

def clean_up(directory, path):
    for filename in directory:
        full_name = path + os.sep + filename
        if filename[-3:] == 'pyc':
            print("- {0}".format(filename))
            os.remove(full_name)
        elif os.path.isdir(full_name):
            clean_up(os.listdir(full_name), full_name)

base_directory = os.listdir('.')

print("Recursively deleting pyc files in: {0}".format(str(base_directory)))

clean_up(base_directory, '.')
