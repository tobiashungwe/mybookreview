import ast
import json
from flask import Blueprint, render_template, redirect, url_for, request, flash, jsonify, make_response
from Models.users_form_update import form_users_update
from Services.Books_select import get_books
from Utilities.Helpers import auth_response, redirect_if_jwt_invalid
from flask_jwt_extended import unset_jwt_cookies
from Models.User import User
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from Utilities.Methods import display_error, error_response, success_response
from Services.users_update import update_users



mod = Blueprint("auth_routes", __name__)

@mod.route("/login", methods=['GET', 'POST'])
def login(): 
    if request.method == 'POST':
        loginForm = request.form
        email = loginForm.get("email")
        password = loginForm.get("password")
        
        user = User.objects(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in!', category='success')
                login_user(user, remember=True)
                
                book_list = get_books()
                resp = redirect(url_for('review_routes.home'), code=200, Response=success_response(user.to_json()))
                resp.set_cookie('cookieUsers', str(user.to_json()))
                resp.set_cookie('cookieBooks', str(book_list))
                return resp 
            else: 
                error_message = 'Password is wrong, try again!'
                flash(error_message,  category='error')
                error_response(error_message)
        else:
            error_message = 'Email does not exist!' 
            flash(error_message, category='error')
            error_response(error_message)
            
    resp = make_response(render_template("login.html", user=current_user) )
    resp.set_cookie("cookieUsers", str(current_user))
    return resp

@mod.route('/user_info', methods=['POST'])
def user_info():
    if current_user.is_authenticated:
        resp = {"result": 200,
                "data": current_user.to_json()}
    else:
        resp = {"result": 401,
                "data": {"message": "user no login"}}
    return jsonify(**resp)



@mod.route("/register", methods=['GET', 'POST'])
def register(): 
    
    if request.method == 'POST':
        registerForm = request.form
        username = registerForm.get("username")
        email = registerForm.get("email")
        password = registerForm.get("password")
        passwordConfirm = registerForm.get("passwordConfirm")
        
        email_exists = User.objects(email=email).first()
        username_exists = User.objects(name=username).first()

        if email_exists:
            display_error("Email already in use.")
        elif username_exists:
            display_error("Username is already in use.")
        elif password != passwordConfirm:
            display_error("Password does not match!")
        elif len(username) < 3:
            display_error("Username is too short.")
        elif len(password) < 6:
            display_error("Password is too short.")
        elif len(email) < 4 :
            display_error("Email is invalid.")
        else:
            new_user = User(name=username, password=generate_password_hash(password, method='sha256'),email=email)
            new_user.save()
            login_user(new_user, remember=True)
            auth_response(new_user.name)
            
            flash('User created!')
            #resp.headers["Content-Type"] = "application/json"
            return redirect(url_for('review_routes.home'), code=200, Response=success_response(new_user.to_json()))
   
    book_list = get_books()
    resp = make_response(render_template("register.html", user=current_user))  
    resp.set_cookie("cookieUsers", str(current_user))
    resp.set_cookie('cookieBooks', str(book_list))
    return resp

@mod.route("/logout")
@login_required
def logout(): 
    resp = make_response(redirect('/login'))
    unset_jwt_cookies(resp)
    logout_user()
    return redirect(url_for("review_routes.home"))



#test route
@mod.route('/protected')
@redirect_if_jwt_invalid
def protected():
    return render_template("index.html")


@mod.route('/users_update', methods=['POST', 'GET'])
def users_update():
    try:
        my_form = form_users_update()
        if request.method == "POST":
            user_dict = ast.literal_eval(request.cookies.get("cookieUsers")) 
            if request.form["usr"] == "up":
                usrdict: dict = {}
                usrdict["password"] = my_form.input_password.data
                msg = update_users(usrdict,
                                   User(user_dict["email"], user_dict["name"], user_dict["password"]))
                return render_template("users_update.html", form=my_form, email=user_dict["email"], name=user_dict["name"], message=msg)
        return render_template("users_update.html", form=my_form, email=user_dict["email"], name=user_dict["name"], message="User Updated! ")

    except:
        return redirect(url_for("review_routes.home"))
