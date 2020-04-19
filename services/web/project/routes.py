from flask import jsonify, request
from project import app
from project.models import Category, Product, Item
from project.db import db


@app.route("/api/healthcheck")
def healthcheck():
    return jsonify(status = "OK")


@app.route('/api/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        return jsonify(Category.query.all())

    if request.method == 'POST':
        category = Category()
        category.name = request.form['name']
        db.session.add(category)
        db.session.commit()
        return jsonify(category)

    else:
        abort(405)


@app.route('/api/categories/<int:category_id>')
def find_category(category_id):
    return jsonify(Category.query.filter_by(id = category_id).first())


@app.route('/api/categories/<int:category_id>/products')
def find_category_products(category_id):
    return jsonify(Product.query.filter_by(category_id=category_id).all())


@app.route('/api/products/<int:product_id>')
def find_product(product_id):
    return jsonify(Product.query.filter_by(id=product_id).first())


@app.route('/api/products/<int:product_id>/items', methods=['GET', 'POST'])
def find_product_sitems(product_id):
    return 'Product %d item' % product_id


# @app.route('/api/items', methods=['POST'])
#
# @app.route('/api/products', methods=['POST'])
#
