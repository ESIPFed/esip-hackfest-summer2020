import csv

'''
sample csv: file.csv

(CSV file header)
topic,name,website,publication,conf-level,identifier

DictReader returns:
OrderedDict([('topic', 'Flooding'), ('name', 'GFMS')...etc])

'''

topics = []
applications = []
datasets = []

with open('file.csv', 'r') as csv_file: 
    csv_reader = csv.DictReader(csv_file) # add , delimiter=',' to specify delimiter

next(csv_reader)  # skips over both header rows 

for line in csv_reader:
    
    
    
    
    print(line) # prints "['GFMS', 'http://flood.umd.edu/', '2014'...etc]"
    print(line['name']) # prints "GFMS"