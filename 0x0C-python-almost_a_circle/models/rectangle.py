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
        self.__width

    @property
    def height(self):
        """get vthe value for height"""
        self.__height

    @property
    def x(self):
        """get value of x"""
        self.__x

    @property
    def y(self):
        """get the value for y"""
        self.__y

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
        if (value <=0):
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
        for row in range(self.__height):
            print(" ", end="")
        for column in range(self.__width):
            print("#", end="")


