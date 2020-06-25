import csv

'''
sample csv: file.csv

(Applications - 2 rows)
name, website, year_started, topic, dataset_doi, conf_level
Global Flood Monitoring System,http://flood.umd.edu/,2014,Flooding,10.5067/TRMM/TMPA/3H-E/7,High


'''

with open('file.csv', 'r') as csv_file: 
    csv_reader = csv.DictReader(csv_file) # add , delimiter=',' to specify delimiter

next(csv_reader)  # skips over the header (first line) 

for line in csv_reader:
    print(line) # prints "['GFMS', 'http://flood.umd.edu/', '2014'...etc]"
    print(line['name']) # prints "GFMS"