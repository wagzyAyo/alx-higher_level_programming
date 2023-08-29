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
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
