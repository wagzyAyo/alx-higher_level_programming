#!/usr/bin/python3
"""This module includes a function
that writes a string to text file"""


def write_file(filename="", text=""):
    """This function writes a string to a
    text file and returns number of characters
    written"""
    with open(filename, mode="w",  encoding="utf-8") as file:
        file.write(text)
