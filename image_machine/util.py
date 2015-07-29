import os

def build_relative_path(filename, temp_folder=''):
    """
    Builds a relative path to the given file based on the temporary folder.
    """
    return os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            build_temp_path(filename, temp_folder))

def build_path(filename, temp_folder=''):
    """
    Returns the full path of the file.
    """
    return os.path.join('',
            build_temp_path(filename, temp_folder))

def build_temp_path(filename, temp_folder=''):
    """
    Builds a string returning the relative path of the file nested within the
    given temporary directory. If no temporary directory is provided, it simply
    returns the file name.
    """
    if temp_folder:
        return "{0}/{1}".format(temp_folder, filename)

    return filename

def work_in_tmp_directory(temp_dir_name='tmp'):
    """
    Creates a temporary directory if one does not exist. It then changes into
    that directory to do all the work.
    """
    conditional_print("CWD: {0}".format(os.getcwd()))
    if not os.path.exists(temp_dir_name):
        os.makedirs(temp_dir_name)

    os.chdir(temp_dir_name)

def conditional_print(thing_to_print, log_level='DEBUG'):
    """
    Uses the setting's key 'verbosity' to determine the log level. Prints out
    `thing_to_print` prepended by [<LOG LEVEL>].
    """
    print("[{0}] {1}".format(log_level, thing_to_print))

