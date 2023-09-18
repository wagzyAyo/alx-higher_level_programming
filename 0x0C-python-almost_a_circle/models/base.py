#!/usr/bin/python3
"""This module contains a Base class"""
import json
import os
import csv
import turtle


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
        return list_of_instancesi

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializing list_objs and save as csv file"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, mode="w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    csv_format = ["id", "width", "height", "x", "y"]
                else:
                    csv_format = ["id", "size", "x", "y"]
                    data = DictWriter(csv_file, fieldnames=csv_format)
                    for item in list_objs:
                        data.writerow(item.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes csv format from a file"""
        file_name = cls.__name__ + ".csv"
        with open(file_name, newline="") as csv_file:
            if cls.__name__ == 'Rectangle':
                    csv_format = ["id", "width", "height", "x", "y"]
            else:
                csv_format = ["id", "size", "x", "y"]
                dict_list = csv.DictReader(csv_file, fieldnames=csv_format)
                dict_list = [dict([key, int(value)] for key, value in x.items())
                        for x in dict_list]
                return [cls.create(**x) for x in dict_list]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw rectangle and swuare using turtle module

        Args:
        list_rectangles: A list of all rectangle object to draw
        list_squares: A list of square object to draw
        """
        window = turtle
        tim = turtle.Turtle()
        tim.pensize(3)
        tim.shape(turtle)

        for rect in list_rectangles:
            tim.showturtle()
            tim.up()
            tim.goto(rect.x, rect.y)
            tim.down()
            for x in range(2):
                tim.forward(rect.width)
                tim.left(90)
                tim.forward(rect.height)
                tim.left(90)
            tim.hideturtle()

        timmy = turtle.Turtle()
        timmy.color("#b5e3d8")
        for squ in list_squares:
            timmy.showturtle()
            timmy.up()
            timmy.goto(squ.x, squ.y)
            timmy.down()
            for x in range(2):
                timmy.forward(squ.width)
                timmy.left(90)
                timmy.forward(squ.height)
                timmy.left(90)
            timmy.hidetutle()

        window.exitonclick()


