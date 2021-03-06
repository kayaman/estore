from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from dataclasses import dataclass, field
from project import app

from sqlalchemy import Integer, ForeignKey, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@dataclass
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable = False)
    # orders = relationship('Order', backref='user')

    def __repr__(self):
        return '<User %r>' % self.id


@dataclass
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    # user = relationship("User", back_populates="orders")

    # items = db.relationship('OrderItem', secondary=orders_items, backref='order', lazy=True)

    def __repr__(self):
        return '<Order %d>' % self.id


@dataclass
class Category(db.Model):
    __tablename__ = 'categories'
    id: int
    name: str
    products: list = field(default_factory=list)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    products = db.relationship('Product', backref='category', lazy=True)

    def __repr__(self):
        return '<Category %r>' % self.name


@dataclass
class Product(db.Model):
    __tablename__ = 'products'
    id: int
    name: str

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    # description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.id



@dataclass
class Item(db.Model):
    __tablename__ = 'items'

    id: int
    code: str

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(12), unique=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.code


# @dataclass
# class Address(db.Model):
#     __tablename__ = 'addresses'
#
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     # fields
#
#     def __repr__(self):
#         return '<Order %d>' % self.id

#
# @dataclass
# class Image(db.Model):
#     __tablename__ = 'images'
#
#     id = db.Column(db.Integer, primary_key=True)
#     src = db.Column(db.Text, nullable = False)
#     item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)
#
#     def __repr__(self):
#         return '<Image %d>' % self.id


# @dataclass
# class OrderItem(db.Model):
#     __tablename__ = 'orders_items'
#
#     id = db.Column(db.Integer, primary_key=True)
#     order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
#
#     def __repr__(self):
#         return '<OrderItem %d>' % self.id
#
#  # (Sku)Item
#
#
# db.create_all()
# db.session.commit()



# Order
# User
# Sku
# Cart
# Adress
