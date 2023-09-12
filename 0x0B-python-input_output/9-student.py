#!/usr/bin/python3
"""This module defines a class student"""


class Student:
    """A class student"""
    def __init__(self, first_name, last_name, age):
         """initializing a new student """
         self.first_name = first_name
         self.last_name = last_name
         self.age = age

    def to_json(self):
        """Gets dictionary representation of student"""
        return self.__dict__
