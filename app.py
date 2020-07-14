from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from flask_wtf import FlaskForm
from wtforms import SelectField
from models import db

'''
@api.route('/api')
class Get(Resource):

    def get(self):
        return jsonify(objects)

'''

# api = Api()

app = Flask(__name__)
graph = db()

class Form(FlaskForm):
    topic = SelectField('topic', choices=graph.nodes.match("Topic"))
    application = SelectField('application', choices=graph.nodes.match("Application"))

@app.route('/', methods=['GET', 'POST'])
def home():
    topics = graph.nodes.match("Topic")
    form = Form()
    if request.method == 'POST':
        return use_cases()

    return render_template('home.html', form=form) # topics=topics 

@app.route('/use_cases/<topic>', methods=['GET', 'POST'])
def use_cases(topic):
    # if request.method == 'POST':
        # topic = request.form.get['topic']
    rels = graph.match(topic, r_type="relates to", limit=None)

    applications = []
    for rel in rels:
        applications.append(rel.end_node)

    return render_template('use_cases.html', topic=topic, 
        applications=applications)
    

@app.route('/data/<application>')
def data(application):
    
    datasets = graph.match(application, r_type="uses", limit=None)

    dataArray = []

    for data in datasets:
        dataObj = {}
        dataObj['identifier'] = data.end_node.identifier
        dataArray.append(dataObj)

    return jsonify({'datasets' : dataArray})



if __name__ == '__main__':
    app.run(debug=True)










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

