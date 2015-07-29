import json
from os import environ, path

# can be accessed via settings.options or settings.get_setting('key'[, 'value'])
options = { }

def set_configuration_file(config_file=None):
    """
    Tries to load the `json` configuration file. After it is set, the options
    dictionary has a key called `loaded` indicating whether or not the config
    file was read.
    """
    if options.get('loaded'): return

    data = None
    filename = environ.get('IMAGE_MACHINE_CONFIG') or config_file or 'settings.json'

    if path.isfile(filename):
        with open(filename) as config_file:
            data = json.load(config_file)

    if data:
        options.update(data)
        options['loaded'] = True

def get_setting(key, fallback=None):
    """
    A wrapper to get the setting from the `options`.
    """
    global options
    return options.get(key, fallback)

def init(config_file=None):
    """
    The reason this is not a class is because there is no need to have multiple
    instances of it. When imported, it can be shared across the file without
    having to worry about initializing it. This is just a static class.
    """
    set_configuration_file(config_file)

