#!/usr/bin/python3
"""This module contains a function that returns
the dictionary representation of a simple data structure"""


def class_to_json(obj):
    """returns dictionary representation of a simple data structure"""
    return obj.__dict__
