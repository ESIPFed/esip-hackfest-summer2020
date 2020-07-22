from py2neo import Graph, Node, Relationship
import csv


def db():

    with open('input.csv', 'r') as csv_file: 
        csv_reader = csv.DictReader(csv_file) # add , delimiter=',' to specify delimiter

        # next(csv_reader)  # skips over both header rows 
        graph = Graph("bolt://localhost:7687", auth=("neo4j", "ubdprototype"))

        try:
            graph.run("Match () Return 1 Limit 1")
        except Exception:
            print('Invalid connection. Is Neo4j running? Check username and password.')
            raise Exception

        graph.delete_all()
        
        for line in csv_reader:
            
            topic = Node("Topic", name=line['topic'])
            application = Node("Application", name=line['name'], website=line['website'],
                publication=line['publication'])
            
            dataset = Node("Dataset", identifier=line['identifier']) # may include a identifier TYPE property

            graph.merge(topic, "Topic", "name")
            graph.merge(application, "Application", "name")
            graph.merge(dataset, "Dataset", "identifier")


            graph.create(Relationship(application, "relates to", topic))
            graph.create(Relationship(application, "uses", dataset, conf_level=line['conf-level']))
            
            

    return graph





