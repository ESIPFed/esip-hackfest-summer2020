# ubd-prototype

Need a Neo4j database running:

1. If using Docker:

`$ docker run -p 7867:7867 -p 7474:7474 neo4j`

Go to http://localhost:7474 and change the password for the user neo4j to be "ubdprototype"

2. Using Neo4J Desktop

Install Neo4j Desktop application

Create a new project and database (using a local database for now)

Set a password for the local database; username should be 'neo4j'

Start the database

3. Install the required python packages

`$ pip install -r requirements`

4. Run the application

`$ python app.py`

5. Browse to http://localhost:5000


