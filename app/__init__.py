from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

from . import models, view

