from py2neo import Graph, Node, Relationship
from neo4j import GraphDatabase, SessionConfig
import csv



# uri = "neo4j://localhost:7687"
# driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

# session = driver.session(SessionConfig.forDatabase( "Applications" ))

def db():

    with open('input.csv', 'r') as csv_file: 
        csv_reader = csv.DictReader(csv_file) # add , delimiter=',' to specify delimiter

        # next(csv_reader)  # skips over both header rows 
        graph = Graph("bolt://neo4j:ubdprototype@localhost:7687")
        graph.delete_all()
        
        for line in csv_reader:
            
            topic = Node("Topic", name=line['topic']) # merge later on
            
            application = Node("Application", name=line['name'], website=line['website'],
                publication=line['publication'])
            dataset = Node("Dataset", identifier=line['identifier']) # may include a identifier TYPE property
        
            graph.merge(topic)
            graph.merge(application)
            graph.merge(dataset)
            
            graph.create(Relationship(application, "relates to", topic))
            graph.create(Relationship(application, "uses", dataset, conf_level=line['conf-level']))
            # RELATES_TO = Relationship.type("RELATES_TO")
            # graph.merge(RELATES_TO, "Topic", "name")
            
            # Using official Neo4j Python Driver
            # session.write_transaction(assign_topic, line['name'], line['topic'])

        # graph.schema.create_uniqueness_constraint("Topic", "name")
        # graph.schema.create_uniqueness_constraint("Application", "name")
        # graph.schema.create_uniqueness_constraint("Dataset", "identifier")
    return graph



def assign_topic(tx, application, topic):
    tx.run("CREATE (a:Application {name: $application})-[:RELATES_TO]->(t:Topic {name: $topic})", application=application, topic=topic)



