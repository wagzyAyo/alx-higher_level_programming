#!/usr/bin/python3
'''defines a square'''


class Square:
    '''Class Representing a square'''

    def __init__(self, size=0):
        '''size must be an integer, otherwise raise
        a TypeError exception with the message size must
        be an integer if size is less than 0, raise a
        ValueError exception with the message size
        must be >= 0'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        '''retrieves the size of the square'''

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Area of the square'''
        return self.__size ** 2
