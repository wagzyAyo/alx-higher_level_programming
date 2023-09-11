#!/usr/bin/python3
"""This module defines a class MyInt
which inherits dfrom int
"""


class MyInt(int):
    """Inverts int operator
    == and != """

    def __eq__(self, value):
        """Overide == operator with != behaviour """
        return (self.real != value)

    def __ne__(self, value):
        """Overide != operator with == behaviour"""
        return (self.real == value)
