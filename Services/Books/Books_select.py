import pandas
import pymongo
import Services.Database.database_pymongo


def get_book(title: str) -> dict:
    try:
        
        book_selected = Services.database_pymongo.ConnectPymongo.db.books

        book_dict = book_selected.find_one({"title": title})

        return {"title": book_dict["title"], "pic": book_dict["pic"], "description": book_dict["description"], "authors": book_dict["authors"]}
    except:
        pass


def get_books() -> pandas.DataFrame:
    try:

        book_selected = Services.Database.database_pymongo.ConnectPymongo.db.books

        book_dict = book_selected.find()

        df = pandas.DataFrame(book_dict, columns=["title", "pic", "description", "authors"])
        df["title"] = df["title"].apply(lambda x: f'<form action="/books/book" class="form-input bg-dark rounded m-2 " method="post">'
                                                f'<button class="btn btn-secondary p-3 m-2" type="submit" name="book" value="{x}">{x}</button>'
                                                f'</form>')
        df["pic"] = df["pic"].apply(lambda x: f'<img class="p-2 m-2" src="{x}" alt="Book">')
        df["description"] = df["description"].apply(lambda x: f'<p class="fw-light small m-2 p-2">{x}</p>')
        df["authors"] = df["authors"].apply(lambda x: f'<h1 class="fw-bold fs-5 text w-100 m-5 p-5">{x}</h1>')
    
        return df

    except:
        pass


def get_dropdown_booklist() -> pandas.DataFrame:
    try:

        book_selected = Services.Database.database_pymongo.ConnectPymongo.db.books

        book_dict = book_selected.find()

        df = pandas.DataFrame(book_dict, columns=["title"])
        
        df["title"] = df["title"].apply(lambda x: f'<select class="form-select" aria-label="Default select example">'
                                                f'<option selected>{x}</option>'
                                                f'<option >⭐⭐⭐⭐</option>'
                                                f'<option >⭐⭐⭐</option>'
                                                f'<option >⭐⭐</option>'
                                                f'<option >⭐</option>'
                                                f'</select>')
    
        return df

    except:
        pass

