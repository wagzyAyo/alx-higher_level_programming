#!/usr/bin/python3
"""This module includes a function
that reads and print a  text file"""


def read_file(filename=""):
    """This function reads a file and print to standard
    output"""
    with open(filename,encoding="utf-8") as file:
        print(file.read())
