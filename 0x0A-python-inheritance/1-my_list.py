#!/usr/bin/python3
"""This module prints a list in ascending
order"""


class MyList(list):
    """class inherits from list"""
    def print_sorted(self):
        print (sorted(self))
