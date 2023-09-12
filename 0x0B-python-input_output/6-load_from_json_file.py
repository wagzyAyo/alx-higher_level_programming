#!/usr/bin/python3
"""This module defines a json file reading
function"""
import json


def load_from_json_file(filename):
    """Create a python object fom given json file"""
    with open(filename) as FILE:
        return json.load(FILE)
