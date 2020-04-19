from flask import jsonify
from project import app
from project.models import Category


@app.route("/api/healthcheck")
def healthcheck():
    return jsonify(status = "OK")


@app.route('/api/categories')
def list_categories():
    return jsonify(Category.query.all())


@app.route('/api/categories/<int:category_id>')
def find_category(category_id):
    return 'Category %d' % category_id


@app.route('/api/categories/<int:category_id>/products')
def find_category_products(category_id):
    return 'Category %d products' % category_id
