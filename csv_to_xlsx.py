import os
import glob
import csv
import shutil
import sys
from xlsxwriter.workbook import Workbook
from image_machine.util import _print


reload(sys)
sys.setdefaultencoding('ISO-8859-1')
csv_files = glob.glob(os.path.join('.', 'tmp', '*.csv'))

for csv_file in csv_files:
    _print(('Found file:\t\t{0}'.format(csv_file)), foreground_color='GREEN')
    new_file_name = '{0}.xlsx'.format(csv_file.split('.csv')[0])

    workbook = Workbook(new_file_name)
    worksheet = workbook.add_worksheet()

    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
        _print(('Created file:\t\t{0}'.format(new_file_name)), foreground_color='GREEN')
        _print(('*' * 80), foreground_color='GREEN')

    workbook.close()
    shutil.move(csv_file, 'archived')
