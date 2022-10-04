import Services.Database.database_pymongo 

from Services.Books.Books_select import get_book



def save_book(Book):
    try:

        if get_book(Book.title) == None:
            book_selected = Services.Database.database_pymongo.ConnectPymongo.db.books
            book_id = book_selected.insert_one(Book.__dict__()).inserted_id
            book_id     

        else:
            pass
    except:
        pass
