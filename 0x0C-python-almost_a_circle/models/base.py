#!/usr/bin/python3
"""This module contains a Base class"""


class Base:
    """The class Base"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializing the base class"""
        if id != None:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects
