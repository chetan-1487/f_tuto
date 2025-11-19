from flask import Blueprint, request, redirect, render_template, url_for, flash, make_response
from app.models import User
from app.extension import db, bcrypt
from flask_jwt_extended import create_access_token, jwt_required, unset_jwt_cookies

user_bp = Blueprint("users",__name__,template_folder=".../templates", static_folder="../static")

@user_bp.route("/")
def form():
    return render_template("index.html")

@user_bp.route("/signup", methods=["GET","POST"])
def create_student():
  if request.method=="POST":

    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    address = request.form.get("address")
    pincode = request.form.get("pincode")

    if not username or not email or not password:
        flash("Enter all details..")

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        flash("Email already exists! Please use a different email.")
        return redirect(url_for("users.form"))
    
    hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")


    user_details = User(username, email, hashed_pw, address, pincode)
    db.session.add(user_details)
    db.session.commit()

    flash("user signup successfully, Now login")
    return render_template("login.html", users=user_details)
  return render_template("index.html")

@user_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            flash("User does not exist.")
            return redirect(url_for("users.login"))

        if bcrypt.check_password_hash(user.password_hash, password):
            token = create_access_token(identity= str(user.id), additional_claims={"email":user.email})
            response = make_response(redirect(url_for("users.result")))
            response.set_cookie(
                "access_token_cookie",
                token,
                httponly=True,    # protects against JavaScript access
                samesite="Lax",   # prevents CSRF
                secure=False      # Set to True in production with HTTPS
            )
            return response

        flash("Incorrect email or password")
        return redirect(url_for("users.result"))

    return render_template("login.html")


@user_bp.route("/update/<int:id>", methods=["GET","POST"])
def update(id):
    userDetail= User.query.get_or_404(id)
    if request.method == "POST":
        address = request.form.get("updateAddress")
        pincode=request.form.get("updatePincode")
        
        userDetail = User.query.filter_by(id=id).first()
        userDetail.address = address
        userDetail.pincode = pincode
        db.session.add(userDetail)
        db.session.commit()
    
        return redirect(url_for("users.result"))
    
    return render_template("update.html", user=userDetail)



@user_bp.route("/result", methods=["GET"])
@jwt_required()
def result():
    return render_template("result.html", userData=User.query.all())


@user_bp.route("/logout", methods=["GET"])
def logout():
    response = make_response(redirect(url_for('users.login')))
    unset_jwt_cookies(response) 
    return response
