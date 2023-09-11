#!/usr/bin/python3
"""Bae geometry class"""


class BaseGeometry:
    """This class represents base geometry"""

    def area(self):
        """raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates value
        raises:
        TypeError : if value is not an integer
        ValueError : if value is less or equal 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
