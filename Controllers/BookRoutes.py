import json
import ast
from typing import List
from flask import Blueprint, request, render_template, jsonify, make_response, flash
from flask_login import current_user, login_required
from Models.Books import BookVolumes
from Services.Books.Books_dataframe import df_pandas_book
from Services.Books.Books_update import update_book
from Services.Books.Books_select import get_book, get_books


mod = Blueprint("books", __name__, url_prefix="/books")


@mod.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        try:
            #Convert book dictoniries
            book_dict = ast.literal_eval(request.cookies.get("cookiebooksDict"))
            user_dict = ast.literal_eval(request.cookies.get("cookieUsers")) 
            book_dict["volumeInfo"] = request.form["volumeinfo"]
            book_update = BookVolumes(book_dict["title"], book_dict["pic"], book_dict["description"], book_dict["authors"])
            
            update_book(book_update) #Mongodb update
            book_list = get_books()
            return render_template("/books/index.html", user=current_user, table=book_list.to_html(escape=False, index=False), message="List books update!")
        except:
            pass
    resp = make_response(render_template("/books/index.html", user=current_user))  
    return resp

@mod.route("/book", methods=['POST', 'GET'])
@login_required
def book():
    if request.method == "POST":
        try:
            #Convert book dictoniries
            book_dict = ast.literal_eval(request.cookies.get("cookiebooksDict"))
            user_dict = ast.literal_eval(request.cookies.get("cookieUsers"))
            book_dict["volumeinfo"] = request.form["volumeinfo"]
            book_update = BookVolumes(book_dict["title"], book_dict["pic"], book_dict["description"], book_dict["authors"])
            #Update mongo bd
            update_book(book_update)
            book_list = get_books()
            return render_template("/books/index.html", user=current_user, table=book_list.to_html(escape=False, index=False), message="List books update!")
        except:
            pass
    resp = make_response(render_template("/books/index.html", user=current_user))  
    return resp


@mod.route('/book_json', methods=['GET'])
def book_json():
    try:
        cookiebooks = request.cookies.get('cookieBooks')

        if cookiebooks is not None:
            df_json = df_pandas_book(str(request.args['book_add']).lower())  
            json_load = json.loads(df_json)
            return jsonify(html="application/json",
                           message="ok",
                           data=json_load,
                           status=200
                           )

    except:
        pass
    return render_template("/books/index.html", user=current_user)




@mod.route('/books', methods=['POST', 'GET'])
@login_required
def books():
    if request.method == "POST":
        try:
            if request.form['books'] is not None:
                book_dict = get_book(request.form['books'])
                print(book_dict)
                resp = make_response(render_template("/books/books.html", book_dict["title"], book_dict["pic"], book_dict["description"], book_dict["authors"]))

                resp.set_cookie("cookiebooksDict", str(book_dict), user=current_user)
                return resp

        except:
            pass

    return render_template('books/book.html', user=current_user)


'''
Function insert a new books in mongoDB
'''


@mod.route('/book_add', methods=['POST', 'GET'])
@login_required
def book_add():

    global book_list
    try:    
        
        df_json = df_pandas_book(str(request.form['book']).lower())
        book_list = get_books()
        user_dict = ast.literal_eval(request.cookies.get("cookieUsers"))
       
        return render_template("/books/index.html", user=current_user, table=book_list.to_html(escape=False, index=False), message="books added!")

      
    except:
            return render_template("/books/index.html", user=current_user, table=book_list.to_html(escape=False, index=False), message="books not found!")

    return render_template('/books/index.html')
