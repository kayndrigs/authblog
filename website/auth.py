# routes related to authentication

from flask import Blueprint, render_template, redirect, url_for, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET','POST'])
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html")

@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    # .get means returning none if no input instead of crashing
    email = request.form.get("email")
    username = request.form.get("username")
    password1 = request.form.get("password1")
    password2 = request.form.get("password2")
    return render_template("signup.html")

# used views.home instead of / for more dynamics.
@auth.route("/logout",methods=['GET','POST'])
def logout():
    return redirect(url_for("views.home"))