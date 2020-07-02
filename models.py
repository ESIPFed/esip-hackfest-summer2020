from py2neo import Graph, Node, Relationship
import csv

graph = Graph()


with open('input.csv', 'r') as csv_file: 
    csv_reader = csv.DictReader(csv_file) # add , delimiter=',' to specify delimiter

    # next(csv_reader)  # skips over both header rows 

    for line in csv_reader:
        topic = Node("Topic", name=line['topic']) # merge later on
        application = Node("Application", name=line['name'], website=line['website'],
            publication=line['publication'])
        dataset = Node("Dataset", identifier=line['identifier']) # may include a identifier TYPE property

        graph.create(Relationship(application, "relates to", topic))
        graph.create(Relationship(application, "uses", dataset, conf_level=line['conf-level']))