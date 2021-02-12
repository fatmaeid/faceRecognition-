from flask import Flask ,url_for
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.secret_key = 'secret'
db = SQLAlchemy(app)

from app import models
from app import views
