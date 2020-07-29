# ubd-prototype

Need a Neo4j database running:

1. If using Docker:

`$ docker run -d -e NEO4J_AUTH=neo4j/ubdprototype -p 7687:7687 -p 7474:7474 --name neo4j --rm neo4j`

(To stop Neo4j, `docker stop neo4j`. The docker container will be automatically removed.)

2. Using Neo4J Desktop

- Install Neo4j Desktop application at https://neo4j.com/download/

- Start up Neo4j Desktop, click New Project, and then Add Database.

- Select "Set up a local database" and enter a name for your database.

- Set password as 'ubdprototype'.

- Start the database.

- Clone this repository. cd into the project directory. 

3. Install the required python packages

`$ pip install -r requirements.txt`

4. Run the application

`$ python app.py`

5. Browse to http://localhost:5000


