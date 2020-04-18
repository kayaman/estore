from flask import jsonify
from project import app

@app.route("/healthcheck")
def healthcheck():
    return jsonify(status = "OK")
