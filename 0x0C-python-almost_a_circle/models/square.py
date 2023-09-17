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
        self.__height = valiue

    def update(self, *args, **kwargs):
        """This method updates attribute
        of an instance"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if (type(args) != int and args[0] is not None:
                        raise TypeError("id must be an integer")
                self.id = args[0]

            if len(args) > 1:
                self.size = args[1]

            if len(args) > 2:
                self.x = args[2]

            if len(args) > 3:
                self.y = args[3]

        else:
        for key, value in kwargs.items():
            if key == 'id':
                if type(value) != int and value is not None:
                    raise ValueError("id must be an integer")
                self.id = value

            if key == "size":
                self.size = value
            if key == 'x':
                self.x = value
            if key == 'y':
                self.y = value



    def to_dictionary(self):
        """Return the dictionary representation
        of square"""
        sq_dictionary = {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
        return sq_dictionary
