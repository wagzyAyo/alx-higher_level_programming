#!/usr/bin/python3
"""This module retuns boolean depending
on an object is an instance of another
object"""


def is_kind_of_class(obj, a_class):
    """This function return true if an object
    is an instance of a class or a class
    that the class in question inherits from"""
    return (isinstance(obj, a_class))

