from flask import Blueprint, render_template, redirect, url_for, request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login(): 
    email = request.form.get("email")
    password = request.form.get("password")
    return render_template("login.html") 

@auth.route("/register", methods=['GET', 'POST'])
def register(): 
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    passwordConfirm = request.form.get("passwordConfirm")
    
    
    return render_template("register.html") 

@auth.route("/logout")
def logout(): 
 return redirect(url_for("views.home"))