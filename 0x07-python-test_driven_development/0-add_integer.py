#!/usr/bin/python3
"""This module take two arguments and return the sum"""


def add_integer(a, b=98):
    """This function sum  two integer or floats


    Args:
    a: first argument
    b:second argument


    Raise:
    Type error if either of the argument
    is not int or float

    Returns:
    sum of the two arguments
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return(int(a) + int(b))
