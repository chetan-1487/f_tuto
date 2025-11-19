from ..extension import db
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

class Products(db.Model):
    __tablename__="products"

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(100), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, default=10, nullable=False)

    createdAt = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, product_name, description, price, quantity):
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        return f"product name --> {self.product_name}"

