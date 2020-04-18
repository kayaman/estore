from flask import Flask, jsonify
import os

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]

from project import models
from project import routes

@app.route("/status")
def status():
    return jsonify(status = "OK")
