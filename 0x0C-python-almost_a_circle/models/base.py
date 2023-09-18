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
        """returns json representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return  json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w") as data_file:
            if list_objs is None:
                data_file.write("[]")
            else:
                new_list = [item.to_dictionary() for item in list_objs]
                data_file.write(Base.to_json_string(new_list))
