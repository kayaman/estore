from flask import jsonify, request
from project import app
from project.models import Category, Product, Item


@app.route("/api/healthcheck")
def healthcheck():
    return jsonify(status = "OK")


@app.route('/api/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        return jsonify(Category.query.all())
    if request.method == 'POST':
        return "TDB"
    else:
        return "Fudeu"

@app.route('/api/categories/<int:category_id>')
def find_category(category_id):
    return jsonify(Category.query.filter_by(id = category_id).first())


@app.route('/api/categories/<int:category_id>/products')
def find_category_products(category_id):
    return 'Category %d products' % category_id


# @app.route('/api/categories/<int:category_id>/products/<int:product_id>')
# def find_category_product(category_id, product_id):
#     return 'Category product %d' % product_id


@app.route('/api/products/<int:product_id>')
def find_product(product_id):
    return jsonify(Product.query.filter_by(id = product_id).first())


@app.route('/api/products/<int:product_id>/skus')
def find_product_skus(product_id):
    return 'Product %d SKUS' % product_id
