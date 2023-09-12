#!/usr/bin/python3
"""This module contains a function
that returns a python data structure
represented by json string"""
import json


def from_json_string(my_str):
    """This function returns a python data structure
    represented by json string"""
    return (json.loads(my_str))
