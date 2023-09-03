#!/usr/bin/python3
"""This module contain function that
print first name and last name"""


def say_my_name(first_name, last_name=""):
    """This function takes two arguments
    and print them in form of string

    Arguments:
    first argument: firstname
    second argument: lastname

    raise:
    TypeError if either of the argument
    is not string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
