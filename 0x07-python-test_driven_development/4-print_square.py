#!/usr/bin/python3
"""
This module contain a function
that prints a square"""


def print_square(size):
    """ This function print a square with
    character #

    Args:
    size(int): This represents the length of the square

    raise:
    TypeError: if size is not an integer
    ValueError: If size is less than 0
    ValueError: if size is type float 
    and less than 0


    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for x in range(0, size):
        for y in range(size):
            print("#", end="")
        print("")
