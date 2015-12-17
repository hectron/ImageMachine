import csv
import os
import shutil
from collections import OrderedDict
from image_machine.util import _print


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
TMP_DIR = os.path.join(BASE_DIR, 'tmp')
NEW_DIR = os.path.join(TMP_DIR, 'archived')

def get_new_columns():
    columns = OrderedDict()
    columns['Campaign ID'] = 'Campaign ID'
    columns['Campaign Name'] = 'Campaign Name'
    columns['Campaign Status'] = 'Campaign Status'
    columns['Campaign Objective'] = 'Campaign Objective'
    columns['Buying Type'] = 'Buying Type'
    columns['Campaign Spend Limit'] = 'Campaign Spend Limit'
    columns['Tags'] = 'Tags'
    columns['Product Catalog ID'] = None
    columns['Ad Set ID'] = 'Ad Set ID'
    columns['Ad Set Run Status'] = 'Ad Set Run Status'
    columns['Ad Set Lifetime Impressions'] = None
    columns['Ad Set Name'] = 'Ad Set Name'
    columns['Ad Set Time Start'] = 'Ad Set Time Start'
    columns['Ad Set Time Stop'] = 'Ad Set Time Stop'
    columns['Ad Set Daily Budget'] = 'Ad Set Daily Budget'
    columns['Ad Set Lifetime Budget'] = 'Ad Set Lifetime Budget'
    columns['Rate Card'] = None
    columns['Ad Set Schedule'] = None
    columns['Use Accelerated Delivery'] = None
    columns['Use New App Clicks'] = None
    columns['Product Ad Behavior'] = None
    columns['Frequency Control'] = None
    columns['Link Object ID'] = None
    columns['Optimized Conversion Tracking Pixels'] = None
    columns['Optimized Pixel Event'] = None
    columns['Link'] = 'Link'
    columns['Application ID'] = 'Application ID'
    columns['Product Set ID'] = None
    columns['Targeting Level'] = 'Targeting Level'
    columns['Countries'] = 'Countries'
    columns['Cities'] = 'Cities'
    columns['Regions'] = 'Regions'
    columns['Zip'] = 'Zip'
    columns['Addresses'] = None
    columns['Geo Markets (DMA)'] = None
    columns['Location Types'] = None
    columns['Excluded Countries'] = None
    columns['Excluded Cities'] = None
    columns['Excluded Regions'] = None
    columns['Excluded Zip'] = None
    columns['Excluded Addresses'] = None
    columns['Excluded Geo Markets (DMA)'] = None
    columns['Gender'] = 'Gender'
    columns['Age Min'] = 'Age Min'
    columns['Age Max'] = 'Age Max'
    columns['Education Status'] = 'Education Status'
    columns['Fields of Study'] = None
    columns['Education Schools'] = None
    columns['Work Job Titles'] = None
    columns['Work Employers'] = None
    columns['College Start Year'] = 'College Start Year'
    columns['College End Year'] = 'College End Year'
    columns['Interested In'] = 'Interested In'
    columns['Relationship'] = 'Relationship'
    columns['Family Statuses'] = None
    columns['Industries'] = None
    columns['Life Events'] = None
    columns['Politics'] = None
    columns['Income'] = None
    columns['Net Worth'] = None
    columns['Home Type'] = None
    columns['Home Ownership'] = None
    columns['Home Value'] = None
    columns['Ethnic Affinity'] = None
    columns['Generation'] = None
    columns['Household Composition'] = None
    columns['Moms'] = None
    columns['Office Type'] = None
    columns['Behaviors'] = None
    columns['Connections'] = 'Connections'
    columns['Excluded Connections'] = 'Excluded Connections'
    columns['Friends of Connections'] = 'Friends of Connections'
    columns['Locales'] = 'Locales'
    columns['Site Category'] = None
    columns['Unified Interests'] = None
    columns['Excluded User AdClusters'] = None
    columns['Broad Category Clusters'] = 'Broad Category Clusters'
    columns['Targeting Categories - ALL OF'] = None
    columns['Custom Audiences'] = 'Custom Audiences'
    columns['Excluded Custom Audiences'] = 'Excluded Custom Audiences'
    columns['Flexible Inclusions'] = None
    columns['Flexible Exclusions'] = None
    columns['Product Audience Specs'] = None
    columns['Excluded Product Audience Specs'] = None
    columns['Page Types'] = None
    columns['User Device'] = None
    columns['User Operating System'] = None
    columns['User OS Version'] = None
    columns['Wireless Carrier'] = None
    columns['Pricing Level'] = 'Pricing Level'
    columns['Automatically Set Bid'] = None
    columns['Optimization Goal'] = None
    columns['Billing Event'] = None
    columns['Bid Amount'] = None
    columns['Story ID'] = 'Story ID'
    columns['Ad ID'] = 'Ad ID'
    columns['Ad Status'] = 'Ad Status'
    columns['Preview Link'] = 'Preview Link'
    columns['Instagram Preview Link'] = None
    columns['Ad Name'] = 'Ad Name'
    columns['Title'] = 'Title'
    columns['Body'] = 'Body'
    columns['Link Description'] = 'Link Description'
    columns['Display Link'] = 'Display Link'
    columns['Conversion Tracking Pixels'] = None
    columns['Related Page'] = None
    columns['Image Hash'] = None
    columns['Image Crops'] = None
    columns['Video Thumbnail URL'] = None
    columns['Creative Type'] = 'Creative Type'
    columns['URL Tags'] = 'URL Tags'
    columns['View Tags'] = None
    columns['Video ID'] = None
    columns['Instagram Account ID'] = None
    columns['Ad Objective'] = 'Ad Objective'
    columns['Mobile App Deep Link'] = None
    columns['Product Link'] = None
    columns['Call to Action'] = None
    columns['Call to Action Link'] = None
    columns['Additional Custom Tracking Specs'] = None
    columns['Video Retargeting'] = None
    columns['Lead Form ID'] = None
    columns['Attachment Style'] = None
    columns['Permalink'] = None
    columns['Product Count'] = None
    columns['Creative Optimization'] = 'Creative Optimization'
    columns['Add End Card'] = None
    columns['Product 1 - Link'] = 'Product 1 - Link'
    columns['Product 1 - Name'] = 'Product 1 - Name'
    columns['Product 1 - Description'] = 'Product 1 - Description'
    columns['Product 1 - Image Hash'] = 'Product 1 - Image Hash'
    columns['Product 1 - Image Crops'] = None
    columns['Product 1 - Video ID'] = None
    columns['Product 1 - Mobile App Deep Link'] = None
    columns['Product 2 - Link'] = 'Product 2 - Link'
    columns['Product 2 - Name'] = 'Product 2 - Name'
    columns['Product 2 - Description'] = 'Product 2 - Description'
    columns['Product 2 - Image Hash'] = 'Product 2 - Image Hash'
    columns['Product 2 - Image Crops'] = None
    columns['Product 2 - Video ID'] = None
    columns['Product 2 - Mobile App Deep Link'] = None
    columns['Product 3 - Link'] = 'Product 3 - Link'
    columns['Product 3 - Name'] = 'Product 3 - Name'
    columns['Product 3 - Description'] = 'Product 3 - Description'
    columns['Product 3 - Image Hash'] = 'Product 3 - Image Hash'
    columns['Product 3 - Image Crops'] = None
    columns['Product 3 - Video ID'] = None
    columns['Product 3 - Mobile App Deep Link'] = None
    columns['Product 4 - Link'] = None
    columns['Product 4 - Name'] = None
    columns['Product 4 - Description'] = None
    columns['Product 4 - Image Hash'] = None
    columns['Product 4 - Image Crops'] = None
    columns['Product 4 - Video ID'] = None
    columns['Product 4 - Mobile App Deep Link'] = None
    columns['Product 5 - Link'] = None
    columns['Product 5 - Name'] = None
    columns['Product 5 - Description'] = None
    columns['Product 5 - Image Hash'] = None
    columns['Product 5 - Image Crops'] = None
    columns['Product 5 - Video ID'] = None
    columns['Product 5 - Mobile App Deep Link'] = None
    columns['Product 6 - Link'] = None
    columns['Product 6 - Name'] = None
    columns['Product 6 - Description'] = None
    columns['Product 6 - Image Hash'] = None
    columns['Product 6 - Image Crops'] = None
    columns['Product 6 - Video ID'] = None
    columns['Product 6 - Mobile App Deep Link'] = None
    columns['Product 7 - Link'] = None
    columns['Product 7 - Name'] = None
    columns['Product 7 - Description'] = None
    columns['Product 7 - Image Hash'] = None
    columns['Product 7 - Image Crops'] = None
    columns['Product 7 - Video ID'] = None
    columns['Product 7 - Mobile App Deep Link'] = None
    columns['Product 8 - Link'] = None
    columns['Product 8 - Name'] = None
    columns['Product 8 - Description'] = None
    columns['Product 8 - Image Hash'] = None
    columns['Product 8 - Image Crops'] = None
    columns['Product 8 - Video ID'] = None
    columns['Product 8 - Mobile App Deep Link'] = None
    columns['Product 9 - Link'] = None
    columns['Product 9 - Name'] = None
    columns['Product 9 - Description'] = None
    columns['Product 9 - Image Hash'] = None
    columns['Product 9 - Image Crops'] = None
    columns['Product 9 - Video ID'] = None
    columns['Product 9 - Mobile App Deep Link'] = None
    columns['Product 10 - Link'] = None
    columns['Product 10 - Name'] = None
    columns['Product 10 - Description'] = None
    columns['Product 10 - Image Hash'] = None
    columns['Product 10 - Image Crops'] = None
    columns['Product 10 - Video ID'] = None
    columns['Product 10 - Mobile App Deep Link'] = None
    columns['Image'] = 'Image'

    return columns


def map_file(filepath):
    _print(('Mapping file found here: %s' % filepath),
            style='BRIGHT', foreground_color='GREEN')
    new_columns = get_new_columns()
    new_data = []
    with open(filepath, 'rU') as f:
        csv_reader = csv.DictReader(f)

        for row in csv_reader:
            result = {}
            for col in new_columns:
                if col == 'Campaign ID':
                    result[col] = ''
                elif col == 'Campaign Status':
                    result[col] = 'Active'
                else:
                    result[col] = row.get(col, '')
            new_data.append(result)
    return new_data


def create_mapped_file(filepath, data):
    _print(('Writing new file: %s' % filepath),
            style='BRIGHT', foreground_color='GREEN')
    headers = get_new_columns().keys()

    with open(filepath, 'wb') as f:
        csv_writer = csv.DictWriter(f, fieldnames=headers)
        csv_writer.writeheader()
        for row in data:
            csv_writer.writerow(row)


def get_files(extension):
    files = os.listdir(TMP_DIR)

    return { os.path.join(TMP_DIR, filename) for filename in files \
            if extension in filename }


def build_new_filename(original_filepath, extension):
    fileinfo = original_filepath.split(extension)
    filename = fileinfo[0]
    return '%s_new%s' % (filename, extension)


def move_files(file_paths):
    for path in file_paths:
        shutil.move(path, NEW_DIR)


def gogogo():
    desired_extension = '.csv'
    csv_files = get_files(desired_extension)
    new_file_paths = []

    for f in csv_files:
        new_file_name = build_new_filename(f, desired_extension)
        new_file_path = os.path.join(TMP_DIR, new_file_name)
        data = map_file(f)
        create_mapped_file(new_file_path, data)
        new_file_paths.append(new_file_path)

    move_files(csv_files)


if __name__ == '__main__':
    gogogo()
