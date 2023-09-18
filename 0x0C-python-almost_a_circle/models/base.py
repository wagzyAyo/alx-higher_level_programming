#!/usr/bin/python3
"""This module contains a Base class"""
import json


class Base:
    """The class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing the base class"""
        __nb_objects = 0
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
   
    @staticmethod
    def to_json_string(list_dictionaries):
        """returs json representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return  json.dumps(list_dictionaries)
