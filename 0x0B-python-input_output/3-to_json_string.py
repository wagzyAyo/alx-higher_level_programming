#!/usr/bin/python3
import json
"""This module contains a function
that returns json representation
of an object"""


def to_json_string(my_obj):
    """This function returns
    json of an object"""
    return (json.dumps(my_obj))
