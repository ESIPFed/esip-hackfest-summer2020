from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from flask_wtf import FlaskForm
from wtforms import SelectField
from models import db


app = Flask(__name__)
app.secret_key = 'secret_key'
graph = db()


class Form(FlaskForm):
    topic = SelectField('topic', choices=[])
    application = SelectField('application', choices=[])


@app.route('/', methods=['GET', 'POST'])
def home():
    topics = graph.nodes.match("Topic")
    form = Form()
    form.topic.choices = [(topic['name']) for topic in graph.nodes.match("Topic")]
    form.application.choices = [(app['name']) for app in graph.nodes.match("Application")]
    
    # if request.method == 'POST':

    return render_template('home.html', form=form) # topics=topics 


@app.route('/use_cases/<topic>')
def use_cases(topic):
    
    apps = get_apps(topic)

    applications = [app[0] for app in apps]

    return jsonify({'applications' : applications})
    

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





def get_apps(topic):
    query = '''
        match p=(t:Topic)-[r:`relates to`]-(a:Application) 
        WHERE t.name = 'Floods' 
        RETURN a.name
        '''
    
    return graph.run(query, topic=topic)




'''
@app.route('/api')
def session_api():
    return jsonify(list()) #list of relevant dataset nodes
'''

'''
@api.route('/api')
class Get(Resource):

    def get(self):
        return jsonify(objects)

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

