from ..extension import db
from datetime import datetime

class User(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=True)
    pincode = db.Column(db.Integer, nullable=True)

    createdAt = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def __init__(self, username, email, password_hash, address, pincode):
        self.username = username
        self.email = email
        self.password_hash=password_hash
        self.address = address
        self.pincode = pincode

    def __repr__(self):
        return f"username --> {self.username}"

