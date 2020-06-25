from flask import Flask 
from flask_restplus import Api()

api = Api()

app = Flask(__name__)

# db = ___


from application import routes