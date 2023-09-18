#!/usr/bin/python3
"""This module contains a Base class"""
import json
import os


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
        """this method writes to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w") as data_file:
            if list_objs is None:
                data_file.write("[]")
            else:
                new_list = [item.to_dictionary() for item in list_objs]
                data_file.write(Base.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """This method return list of json represented
        by json_string"""
        string_list = []

        if json_string is None or json_string == '':
            return string_list
        else:
            string_list = json.loads(json_string)
            return string_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            val = cls(1, 1)
        elif cls.__name__ == 'Square':
            val = cls(1)

        val.update(**dictionary)
        return val

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""

        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances
