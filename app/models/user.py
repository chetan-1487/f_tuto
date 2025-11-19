from ..extension import db
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    createdAt = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    updatedAt = db.Column(db.DateTime, default=datetime.now(), onupdate=datetime.now())

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def get_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, username, email, password_hash, title, description):
        self.username = username
        self.email = email
        self.set_password(password_hash)
        self.title = title
        self.description = description

    def __repr__(self):
        return f"username --> {self.username}"

