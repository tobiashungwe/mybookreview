from typing import Any, Type

class Book:

    def __init__(self: object, title: str, pic: str) -> None:
        self.__title = title
        self.__pic = pic

    @property
    def title(self: object) -> str:
        return self.__title
    
    @title.setter
    def title(self: object, title: str) -> None:
        self.__title: str = title

    @property
    def pic(self: object) -> str:
        return self.__pic
    
    @pic.setter
    def pic(self: object, pic: str) -> None:
        self.__pic: str = pic




class BookVolumes(Book):
    def __init__(self: object, title: str, pic: str, description: str, authors: str) -> None:
        super(BookVolumes, self).__init__(title, pic) 
        self.__description = description,
        self.__authors = authors,
        
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description
   
    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        self.__authors

    def __dict__(self: object) -> dict:
        return {"title": self.title, "pic": self.pic, "description": self.description, "authors": self.authors}