# Usage-Based Discovery Prototype - A simple web application
 

General instructions for set up:


Need a Neo4j database running:

1. If using Docker:

`$ docker run -d -e NEO4J_AUTH=neo4j/ubdprototype -p 7687:7687 -p 7474:7474 --name neo4j --rm neo4j`

(To stop Neo4j, `docker stop neo4j`. The docker container will be automatically removed.)

2. Using Neo4J Desktop

- Install Neo4j Desktop application at https://neo4j.com/download/

- Start up Neo4j Desktop, click 'New' to create a new project, and then 'Add Database'

- Select "Set up a local database" and enter a name for your database

- Set your own unique password. 

- Start the database

- Clone this repository. `$ cd` into the project directory. 

- Create a Python virtual environment with the command `$ virtualenv name-of-env`. For simplicity, name it 'venv'. 

- Start up the virtual environment using the following command `$ source venv/bin/activate`. 

3. Install the required python packages

`$ pip install -r requirements.txt`

4. Enter the following commands with your username (should be neo4j by default) and password to set the necessary environment variables: 

`$ export NEO4J_USERNAME=your_username`
`$ export NEO4J_PASSWORD=your_password`

5. Run the application

`$ python app.py`

6. Browse to http://localhost:5000


Any questions or suggestions for improvement?
- Questions - email maggieqzhu@yahoo.com 
- Suggestions - submit a pull request




Ways to contribute to this project: 
- Automate the relationship foraging process (will likely involve web scraping and/or ML)



