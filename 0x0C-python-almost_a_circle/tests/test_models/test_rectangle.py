#!/usr/bin/python3
"""Test for rectangle class"""
import unittest
from contextlib import redirect_stdout
import inspect
import io
import os
import sys
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """Test case for Rectangle class"""

    def setUp(self):
        '''
        Initializing instance with width and height parameters
        '''
        self.r = Rectangle(5, 10)

    def test_width(self):
        """Test width"""
        self.assertEqual(5, self.r.width)

    def test_height(self):
        """Test height"""
        self.assertEqual(10, self.r.height)

    def test_width_neg(self):
        """Test width with negative number"""
        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 2)

    def test_height_neg(self):
        """Test height with negative number"""
        with self.assertRaises(ValueError):
            rect = Rectangle(5, -2)

    def test_id(self):
        """Test rectangle id"""
        rect = Rectangle(1, 2, 0, 0, 5)
        self.assertEqual(5, rect.id)

    def test_area(self):
        """Test the area() method"""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)
