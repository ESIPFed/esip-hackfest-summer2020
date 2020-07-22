from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from flask_wtf import FlaskForm
from wtforms import SelectField
from models import db


app = Flask(__name__)
app.secret_key = 'secret_key'
graph = db()


class Form(FlaskForm):
    topic = SelectField('topic', choices=[])
    application = SelectField('application', choices=[("", "---")])


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form()
    form.topic.choices = [topic['name'] for topic in graph.nodes.match("Topic")]
    # form.application.choices = [(app['name']) for app in graph.nodes.match("Application")]
    
    if request.method == 'POST':
        topic = request.form['topic']
        app = request.form['application']

        # get datasets used by app
        data = get_datasets(app)
        datasets = [d[0] for d in data]
            
        #return jsonify({'datasets' : datasets})
        return render_template('data.html', topic=topic, app=app, datasets=datasets)

    return render_template('home.html', form=form) # topics=topics 


@app.route('/use_cases/<topic>')
def use_cases(topic):
    
    apps = get_apps(topic)
    applications = [app[0] for app in apps]
    
    return jsonify({'applications' : applications})
     

@app.route('/data/<application>')
def data(application):
    
    data = get_datasets(application)
    datasets = [d[0] for d in data]

    return jsonify({'datasets' : datasets})



if __name__ == '__main__':
    app.run(debug=True)





def get_apps(topic):
    query = '''
        match p=(t:Topic)-[r:`relates to`]-(a:Application) 
        WHERE t.name = $topic
        RETURN a.name
        '''
    
    return graph.run(query, topic=topic)


def get_datasets(app):
    query = '''
        match p=(a:Application)-[r:`uses`]-(d:Dataset) 
        WHERE a.name = $app
        RETURN d
        '''

    return graph.run(query, app=app)





