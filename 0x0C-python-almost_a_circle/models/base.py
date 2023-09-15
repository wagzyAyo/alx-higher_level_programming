#!/usr/bin/python3
"""This module contains a Base class"""


class Base:
    """The class Base"""
    def __init__(self, id=None):
        """Initializing the base class"""
        __nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            id = Base.__nb_objects
