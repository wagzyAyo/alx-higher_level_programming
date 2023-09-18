#!/usr/bin/python3
"""This module contains a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The rectangle class inherits from the base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing new attribute for rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the value for width"""
        return self.__width

    @property
    def height(self):
        """get vthe value for height"""
        return self.__height

    @property
    def x(self):
        """get value of x"""
        return self.__x

    @property
    def y(self):
        """get the value for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set the value of width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set the value of height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """set the value for x"""
        if (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """set the value of y"""
        if (value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return the area of rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Prints # on row and column"""
        for y in range(self.__y):
            print("")
        for row in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """overriding string method"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """This method assigns an
        argument to each attribute"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'id':
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == 'width':
                    self.width = value
                elif key == 'height':
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """This method returns a dictionary representation
        of rectangle class"""
        rect_dictionary = {'id': self.id, 'width': self.__width, 'height':
                           self.__height, 'x': self.__x, 'y': self.__y}
        return rect_dictionary
