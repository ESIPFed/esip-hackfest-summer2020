from flask import Flask, render_template, jsonify
from flask_restplus import api

import json         # for saving results to JSON file
import os.path      # for parsing input from JSON file

api = Api()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/use_cases')
def use_cases():
    return render_template('use_cases.html', topic = "Flooding")


@app.route('/api')
def session_api():
    return jsonify(list()) #list of relevant dataset nodes

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


'''
# Parsing input from JSON file 

# File name is input.json

input = {}

if os.path.exists('input.json'):
    with open('input.json') as input_file:
        input = json.load(input_file)

'''