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
