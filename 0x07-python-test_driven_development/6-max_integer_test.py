#!/usr/bin/python3
""" This module contain a function 
that find max int in a list"""


def max_integer(list=[]):
    """This function get the max 
    int in a list, if the 
    list is empty it returns None
    """

    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
