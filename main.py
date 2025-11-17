from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "flask secret"

db = SQLAlchemy(app)
migrate = Migrate(app, db)  

class User(db.Model):
    __tablename__="users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(50), nullable=False)
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

@app.route("/")
def form():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create_student():
  if request.method=="POST":

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    title = request.form.get("title")
    description = request.form.get("description")

    if not username or not email or not password:
        flash("Enter all details..")

    user_details = User(username, email, password, title, description)
    db.session.add(user_details)
    db.session.commit()

    flash("Record inserted successfully")
    return redirect(url_for("result"))
  return render_template("index.html")

@app.route("/update/<int:id>", methods=["GET","POST"])
def update_data(id):
    studentDetail= User.query.get_or_404(id)
    if request.method == "POST":
        username = request.form.get("updateUsername")
        title=request.form.get("updateTitle")
        desc=request.form.get("updateDesc")
        studentDetail = User.query.filter_by(id=id).first()
        studentDetail.username = username
        studentDetail.title = title
        studentDetail.description = desc
        db.session.add(studentDetail)
        db.session.commit()
    
        return redirect(url_for("result"))
    
    return render_template("update.html", student=studentDetail)

@app.route("/delete/<int:id>", methods=["GET","POST"])
def delete_student(id):
  user = User.query.get(id)
  if not user:
      return "User not found", 404
  
  db.session.delete(user)
  db.session.commit()
  return redirect(url_for("result"))

@app.route("/result", methods=["GET"])
def result():
    return render_template("result.html", studentData=User.query.all())

if __name__ == "__main__":
    app.run(debug=True)
