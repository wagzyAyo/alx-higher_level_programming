#!/usr/bin/python3
"""A rectangle class"""


class Rectangle:
    """This represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes rectangle class
        Args:
        width: represents the width of the rectangle
        height: represents the height of the rectangle
        raise:
        TypeError :If width and height is not an integer
        ValueError : If width and heigth is less than 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the attribute of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """print the rectangle with the character #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Print message when instance of
        rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
