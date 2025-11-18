from flask import Blueprint, request, redirect, render_template, url_for, flash
from app.models import User
from utils import db

user_bp = Blueprint("users",__name__,template_folder=".../templates", static_folder="../static")


@user_bp.route("/")
def form():
    return render_template("index.html")

@user_bp.route("/create")
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

@user_bp.route("/update/<int:id>", methods=["GET","POST"])
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

@user_bp.route("/delete/<int:id>", methods=["GET","POST"])
def delete_student(id):
  user = User.query.get(id)
  if not user:
      return "User not found", 404
  
  db.session.delete(user)
  db.session.commit()
  return redirect(url_for("result"))

@user_bp.route("/result", methods=["GET"])
def result():
    return render_template("result.html", studentData=User.query.all())
