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


