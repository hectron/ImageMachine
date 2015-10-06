import os
import glob
import csv
import sys
from xlsxwriter.workbook import Workbook

reload(sys)
sys.setdefaultencoding("ISO-8859-1")

for csv_file in glob.glob(os.path.join('.', 'tmp', '*.csv')):
    print('Found file:\t\t{0}'.format(csv_file))
    new_file_name = '{0}.xlsx'.format(csv_file.split('.csv')[0])

    workbook = Workbook(new_file_name)
    worksheet = workbook.add_worksheet()

    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
        print('Created file:\t\t{0}'.format(new_file_name))
        print('*' * 80)

    workbook.close()
