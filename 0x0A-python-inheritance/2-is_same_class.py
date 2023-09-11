#!usr/bin/python3
"""This module return true if an object
is an instance of specified class,False if
otherwise"""


def is_same_class(obj, a_class):
    """Return True if object is an instance
    of specified class,False if otherwise"""
    return (type(obj) == a_class)
