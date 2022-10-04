import json
import pandas

from Models.Books_volumes import BookVolumes

from Services.Books.Books_insert import save_book

import requests

from Utilities.Methods import error_response



def df_pandas_book(books: str) -> str:
    

        ress = requests.get(f"https://www.googleapis.com/books/v1/volumes?q={books}&maxResults=20")

        if ress.status_code == 200:

            df_items = pandas.DataFrame(ress.json()["items"])

            df = pandas.DataFrame()
            
            
            for x in range(df_items["volumeInfo"].index.size):
                
                ress.json()['items'][x]['volumeInfo'].get('description', 'No discription')
                    
                book = BookVolumes(ress.json()['items'][x]['volumeInfo']['title'],
                                 ress.json()['items'][x]['volumeInfo']["imageLinks"]["thumbnail"],
                                 ress.json()['items'][x]['volumeInfo'].get('description', 'No discription was given'),
                                 ress.json()['items'][x]['volumeInfo'].get('authors', 'No authors was given')
                                 )

                print(book)
                df = df.append(book.__dict__(), ignore_index=True)
                print(df)    
                save_book(BookVolumes(book.title, book.pic, book.description, book.authors)) # Insert Class in MongoDB.

            return df.to_json(orient="records") # return a json classification for records
        else:
            return {"code": ress.status_code}

