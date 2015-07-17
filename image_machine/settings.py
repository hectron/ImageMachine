from ConfigParser import RawConfigParser
from io import BytesIO
from os import environ, path

class Settings(object):
    def __init__(self):
        self.set_config_file()
        self.set_config()

    def set_config_file(self):
        filename = environ.get('IMAGE_MACHINE_CONFIG')

        if filename is None:
            filename = 'config.ini'

        self.config_name = filename

    def set_config(self):
        config_file = path.join(path.abspath(path.dirname(__file__)), self.config_name)

        with open(config_file) as f:
            config_data = f.read()

        self.config = RawConfigParser(allow_no_value=True)
        self.config.readfp(BytesIO(config_data))

    def get_ftp_key(self, setting_name):
        value = ''

        try:
            value = self.config.get('ftp', setting_name)
        except:
            pass

        return value
