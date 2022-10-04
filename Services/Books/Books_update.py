import Services.Database.database_pymongo

def update_book(Book):
    book_update = Services.Database.database_pymongo.ConnectPymongo.db.books
    dic_set = {'$set': Book.__dict__()}
    book_id = book_update.update_one({"title": Book.title}, dic_set)