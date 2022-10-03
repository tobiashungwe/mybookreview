import pandas

from Models.Books import BookVolumes

from Services.Books_insert import save_book

import requests



def df_pandas_book(book: str) -> str:
    ress = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={book}")

    if ress.status_code == 200:

        df_items = pandas.DataFrame(ress.json()["items"])

        df = pandas.DataFrame()

        for x in range(df_items["volumeInfo"].index.size):
            book = BookVolumes(ress.json()["title"],
                                 ress.json()["imageLinks"]["smallThumbnail"],
                                 ress.json()["subtitle"],
                                 ress.json()["authors"],
                                 )

            df = df.append(book.__dict__(), ignore_index=True)
            
            save_book(BookVolumes(book.name, book.pic, book.subtitle, book.authors)) # Insert Class in MongoDB.

        return df.to_json(orient="records") # return a json classification for records
    else:
        return {"code": ress.status_code}
