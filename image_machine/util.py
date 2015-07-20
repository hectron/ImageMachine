from os import path

def build_relative_path(filename):
    return path.join(path.abspath(path.dirname(__file__)), filename)

