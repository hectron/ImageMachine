from settings import Settings
from urllib import urlretrieve
import csv
import os
import util
import zipfile

class ImageCsv(object):
    def __init__(self, relative_csv_path=''):
        self.csv_file_path = util.build_relative_path(relative_csv_path)
        self.base_cdn_path = Settings().config.get('cdn', 'Url')
        self.relative_image_paths = []
        self.image_paths = []
        self.default_image_size = '1200.0.0.0'
        self.temp_dir_name = 'image_cache'
        self.can_download = False
        self.allowed_image_types = ['jpg', 'png', 'jpeg', 'gif']

    def build_image_path(self, filename):
        return "{0}/{1}/{2}".format(self.base_cdn_path, self.default_image_size, filename)

    def build_all_image_paths(self):
        self.image_paths = [self.build_image_path(ipath) for ipath in self.relative_image_paths]

    def read_csv_image_paths(self):
        with open(self.csv_file_path, 'rU') as f:
            csv_reader = csv.DictReader(f)

            self.relative_image_paths = [row['Image'].replace('\\', '/') for row in csv_reader]
            self.can_download = True

    def perform_magic(self):
        if self.can_download:
            print("HR: Working in temp directory")
            self.work_in_tmp_directory()
            print("HR: Cwd: {0}".format(os.getcwd()))
            print("HR: Downloading images....")
            self.download_all_images()
            print("HR: Zipping images....")
            self.compress_images()

    def download_all_images(self):
        for image in self.relative_image_paths:
            relative_name = image
            full_url = self.build_image_path(relative_name)
            self.download_image(full_url, relative_name)

    def work_in_tmp_directory(self):
        if not os.path.exists(self.temp_dir_name):
            os.makedirs(self.temp_dir_name)

        os.chdir(self.temp_dir_name)


    def download_image(self, image_url, name):
        name = name.replace('/','')
        urlretrieve(image_url, name)

    def compress_images(self):
        with zipfile.ZipFile('images.zip', 'w') as zipper:
            for img in os.listdir('.'):
                for extension in self.allowed_image_types:
                    if img.endswith(extension):
                        zipper.write(os.path.join('.', img))
