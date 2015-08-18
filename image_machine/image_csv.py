import csv
import os
import pdb
import util
import zipfile
from urllib import urlretrieve

class ImageCsv(object):
    """
    This interfaces with a CSV file to download images and zip those images. It
    also updates the original CSV file to have the relative path.
    """
    def __init__(self, relative_csv_path=''):
        self.image_paths = []
        self.saved_path = os.getcwd()
        self.can_download = False
        self.allowed_image_types = ['jpg', 'png', 'jpeg', 'gif']
        self.csv_file_path = util.build_path(relative_csv_path)
        self.file_name = self.csv_file_path.split('.')[0]
        self.new_file_name = "{0}_done".format(self.file_name)
        self.completed = False

    def __del__(self):
        if self.completed:
            self.update_image_paths()

    def perform_magic(self):
        """
        This is the main method of the program. It is in charge of reading the
        given CSV file, downloading the images and compressing them.
        """
        self.read_csv_image_path()

        if self.can_download:
            self.work_in_tmp_dir()
            self.download_all_images()
            self.compress_images()
            self.wrap_it_up_kid()
            self.completed = True
        else:
            print("No magic can be done. Was this class initialized with a file path?")

    def wrap_it_up_kid(self):
        """
        When called, it changes to the path it was initialized with.
        """
        os.chdir(self.saved_path)

    def read_csv_image_path(self):
        """
        Reads the CSV and creates relative paths for all the images that are
        found. Once all the images are identified, the class is allowed to
        download the images.
        """
        with open(self.csv_file_path, 'rU') as f:
            csv_reader = csv.DictReader(f)
            self.image_paths = [row['Image'] for row in csv_reader if row['Image'] not in self.image_paths]
            self.can_download = True

    def work_in_tmp_dir(self):
        """
        Sets the instance to work in the temporary directory.
        """
        util.work_in_tmp_directory(self.file_name)

    def download_all_images(self):
        """
        Retrieves all the images stored within the `image_paths` attributes. It
        should be called after `can_download` is True.
        """
        util.conditional_print("Downloading images.")
        for image_url in self.image_paths:
            self.download_image(image_url)

    def get_image_name(self, image_url):
        """
        Extracts the file name and extension from a URL.
        """
        return image_url.split('/')[-1]

    def download_image(self, image_url):
        """
        Downloads the image and saves it locally.
        """
        name = self.get_image_name(image_url)
        pdb.set_trace()
        urlretrieve(image_url, name)

    def compress_images(self):
        """
        Grabs all the images that are allowed in the class via the
        `allowed_image_types`, and compresses them.
        """
        util.conditional_print("Zipping images.")
        zip_name = '{0}_images.zip'.format(self.file_name)

        with zipfile.ZipFile(zip_name, 'w') as zipper:
            for img in os.listdir('.'):
                for extension in self.allowed_image_types:
                    if img.endswith(extension):
                        zipper.write(os.path.join('.', img))

    def update_image_paths(self):
        """
        Retrieves the list of all the file names and updates them to the
        relative path. This should be executed before the class is destroyed.
        """
        util.conditional_print("Updating image paths.")
        updated_rows = []
        headers = []

        with open(self.csv_file_path, 'rU') as f:
            csv_reader = csv.DictReader(f)
            headers = csv_reader.fieldnames

            for row in csv_reader:
                if row['Image']:
                    new_path = self.get_image_name(row['Image'])
                    row['Image'] = new_path
                updated_rows.append(row)

        with open(self.new_file_name, 'wb') as f:
            csv_writer = csv.DictWriter(f, fieldnames=headers)

            csv_writer.writeheader()
            for row in updated_rows:
                csv_writer.writerow(row)

