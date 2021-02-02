from flask import Flask ,render_template
app = Flask(__name__)
from app import models
from app import views