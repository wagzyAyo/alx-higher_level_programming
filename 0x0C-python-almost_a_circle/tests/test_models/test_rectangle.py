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


class test_rectangle(unittest.TestCase):
    """test case for Rectangle class"""
    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.r = Rectangle(5, 10)
        
    def test_width(self):
        """test width"""
        self.assertEqual(7, self.r.width)

    def tets_height(self):
        """test height"""
        self.assertEqual(10, self.r.width)

    def test_width_neg(self):
        """test width with negative number"""
        with self.assertRaises(ValueError)
        rect = Rectangle(-5, 2)

    def test_height_neg(self):
        """test height with negative number"""
        with self.assertRaises(ValueError)
        rect = Rectangle(5, -2)

    def test_id(self):
        """test rectangle id"""
        rect = Rectangle(1,2,0,0,5)
        self.assertEqual(5, rect.id)
