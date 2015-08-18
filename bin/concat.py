# awk '!/(150809_Trouble_pTRU1_16461232dt.jpg|150809_VTech_Sit_to_Stand_Learning_Walker_pTRU1_13288585dt.jpg|150809_LeapFrog_My_Pal_Violet_pTRU1_6439380dt.jpg|Product 3 - Image Hash)/' b.txt > temp && mv temp b-cleaned.txt && mv a.txt c-full.txt && cat b-cleaned.txt >> c-full.txt 

# drop two files into the directory with this script.  two files named primary
# file a.csv and secondary b.csv. run script, it will produce an b-clean.csv
# and an a-augmented.csv where b-clean is the b.csv without any a.csv listings
# and a-augmented is a.csv plus b.csv -- run this from the folder containing
# the script

# convert to xslx: http://stackoverflow.com/questions/17684610/python-convert-csv-to-xlsx

import re

#find listings in primary file
f = open('a.csv', 'r')
images = []
for line in f:
    match = re.search(",{1}?([A-Za-z0-9\-\_]+.jpg)", line, re.I)
    if match and len(match.groups())>0:
        if match.group(1) not in images:
            images.append(match.group(1))

print '\n'
print 'listings in a.csv'
count = 0;
for i in images:
    count += 1
    print i
print '\n'
print 'count of listings in a.csv: '
print count
print '\n'

imageSearch =  "(" + "|".join(images) + ")"

# loop through b, remove all images that already exist in a, put that full list in b-clean.
f = open('b.csv', 'r')
w = open('b-clean.csv', 'w')
# move past titles
count = 0;
f.readline()
for line in f:
    match = re.search(imageSearch, line, re.I)
    if not match:
        count += 1
        w.write(line)
f.close()
w.close()
print '\n'
print 'count of matches removed from b.csv, written to b-clean.csv: '
print count
print '\n'

# append b-clean to the end of a, rename a to c.
f = open('a.csv', 'r')
b = open ('b-clean.csv', 'r')
w = open('a-augmented.csv', 'w')
print 'writing lines from a.csv to a-augmented.csv'
for line in f:
    w.write(line)
print''
print 'writing lines from b-clean.csv to a-augmented.csv'
count = 0;
for line in b:
    count += 1
    w.write(line)
print 'count of lines written to a-augmented.csv from b clean:'
print count
f.close()
w.close()
b.close()
