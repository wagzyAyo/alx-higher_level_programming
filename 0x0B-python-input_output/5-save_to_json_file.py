#!/usr/bin/python3
"""This module contains a function
that write to a file using json"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes to a file
    using json"""
    with open(filename, mode="w") as FILE:
        json.dump(my_obj, FILE)
