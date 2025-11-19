from flask import Blueprint, request, redirect, render_template, url_for, flash
from app.models import User
from app.extension import db

product_bp = Blueprint("products",__name__,template_folder=".../templates", static_folder="../static")


@product_bp.route("/")
def form():
    return render_template("index.html")

@product_bp.route("/create", methods=["POST"])
def create_products():
  if request.method=="POST":

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    title = request.form.get("title")
    description = request.form.get("description")

    if not username or not email or not password:
        flash("Enter all details..")

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        flash("Email already exists! Please use a different email.")
        return redirect(url_for("users.form"))

    user_details = User(username, email, password, title, description)
    db.session.add(user_details)
    db.session.commit()

    flash("Record inserted successfully")
    return redirect(url_for("users.result"))
  return render_template("index.html")

@product_bp.route("/update/<int:id>", methods=["GET","POST"])
def update_products(id):
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
    
        return redirect(url_for("users.result"))
    
    return render_template("update.html", student=studentDetail)

@product_bp.route("/delete/<int:id>", methods=["GET","POST"])
def delete_products(id):
  user = User.query.get(id)
  if not user:
      return "User not found", 404
  
  db.session.delete(user)
  db.session.commit()
  return redirect(url_for("users.result"))

@product_bp.route("/result", methods=["GET"])
def result():
    return render_template("result.html", studentData=User.query.all())
