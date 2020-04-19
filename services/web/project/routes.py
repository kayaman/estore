from flask import jsonify, request
from project import app
from project.models import Category


@app.route("/api/healthcheck")
def healthcheck():
    return jsonify(status = "OK")


@app.route('/api/categories')
def categories():
    if request.method == 'GET':
        return jsonify(Category.query.all())
    else:
        return "Fudeu"

@app.route('/api/categories/<int:category_id>')
def find_category(category_id):
    # return 'Category %d' % category_id
    return jsonify(Category.query.filter_by(id = category_id).first())


@app.route('/api/categories/<int:category_id>/products')
def find_category_products(category_id):
    return 'Category %d products' % category_id
