from flask import Flask, jsonify
from os import environ

app = Flask(__name__)
# app.config.from_object('project.Config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = environ["DATABASE_URL"]
app.config['SQLALCHEMY_ECHO'] = True

from project import models
from project import routes
