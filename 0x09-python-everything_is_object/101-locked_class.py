#!/usr/bin/python3
"""This define a lock class"""


class LockedClass:
    """
    Only allow instance of first_name
    """

    __slots__ = ["first_name"]
