from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from models import db

# import json
# import os.path       for parsing input from JSON file

# from flask_restplus import Api, Resource

# API
'''
@api.route('/api')
class Get(Resource):

    def get(self):
        return jsonify(objects)

'''

# api = Api()

app = Flask(__name__)
graph = db()


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/')
@app.route('/home')
def home():
    topics = graph.nodes.match("Topic")
    return render_template('home.html', topics=topics) 

@app.route('/use_cases/<topic>', methods=['GET', 'POST'])
def use_cases(topic):
    # if request.method == 'POST':
        # topic = request.form.get['topic']
    # applications = graph.nodes.match("Application", )

    return render_template('use_cases.html', topic=topic)
    

@app.route('/data')
def data():
    return render_template('data.html')

'''
@app.route('/api')
def session_api():
    return jsonify(list()) #list of relevant dataset nodes
'''



'''
# Save results for specified topic to a JSON file

# Usage cases dictionary
usages = {} 

# Iterates through returned applications
for(a in applications):
    usages[a] = {'name': application.name, 
    'website': application.website, 'year_published' = application.year}

# Iterates through returned papers
for(p in papers):
    usages[p] = {'title': paper.title, 'doi': paper.doi, 'year': paper.year}

with open('usages.json', 'w') as usage_file:
    json.dump(usages, usage_file)


'''

