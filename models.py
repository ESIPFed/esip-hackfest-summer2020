from py2neo import Graph, Node, Relationship
import os
import csv


url = os.environ.get('GRAPHENEDB_URL', 'http://localhost:7474')
username = os.environ.get('NEO4J_USERNAME')
password = os.environ.get('NEO4J_PASSWORD')


def db():
    with open('input.csv', 'r') as csv_file: 
        csv_reader = csv.DictReader(csv_file) # add , delimiter=',' to specify delimiter

        # next(csv_reader)  # skips over both header rows 
        graph = Graph(url + '/db/data/', username=username, password=password)
        for line in csv_reader:
            topic = Node("Topic", name=line['topic']) # merge later on
            application = Node("Application", name=line['name'], website=line['website'],
                publication=line['publication'])
            dataset = Node("Dataset", identifier=line['identifier']) # may include a identifier TYPE property

            graph.create(Relationship(application, "relates to", topic))
            graph.create(Relationship(application, "uses", dataset, conf_level=line['conf-level']))
    return graph



'''
sample csv: file.csv

(CSV file header) 6 fields total 
topic,name,website,publication,conf-level,identifier

DictReader returns:
OrderedDict([('topic', 'Flooding'), ('name', 'GFMS')...etc])

'''
