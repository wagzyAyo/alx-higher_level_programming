#!/usr/bin/python3
"""This module contains a function
that appends a string at the end of
a text file"""


def append_write(filename="", text=""):
    """This function appends a string at the end
    of a text file"""

    with open(filename, mode="a", encoding="utf-8") as file:
        return file.append(text)
