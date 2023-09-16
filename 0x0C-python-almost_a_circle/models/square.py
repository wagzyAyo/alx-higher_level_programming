#!/usr/bin/python3
"""This module contains The square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing the square class"""
        super().__init__(size, size , x, y, id)
        self.size = size
        self.x = x
        self.y = y
        self.id = None

    def __str__(self):
        """string representation of class"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """getting value of size"""
        return self.__width

    @size.setter
    def size(self, value):
        """setting the value of size"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

