import os
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))

app.config.from_object("project.Config")

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
