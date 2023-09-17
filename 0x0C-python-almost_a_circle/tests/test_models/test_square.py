#!/usr/bin/python3
from contextlib import redirect_stdout
import contextlib
import inspect
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import sys
import json
from io import StringIO


'''
    Runs test cases for the square module
'''


class test_square(unittest.TestCase):
    '''
        Testing square
    '''

    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.s = Square(5)

    def tearDown(self):
        '''
            Deleting created instance
        '''
        try:
            os.remove("Square.json")
        except:
            pass
        del self.s

    def test_width(self):
        '''
            Testing the square width getter
        '''
        self.assertEqual(5, self.s.width)

    def test_height(self):
        '''
            Testing the square height getter
        '''
        self.assertEqual(5, self.s.height)

    def test_x(self):
        '''
            Testing square x getter and setter
        '''

        self.s.x = 54
        self.assertEqual(54, self.s.x)
        self.assertEqual(0, self.s.y)

    def test_y(self):
        '''
            Testing square y getter and setter
        '''

        self.s.y = 45
        self.assertEqual(45, self.s.y)
        self.assertEqual(0, self.s.x)

    def test_asquare_id(self):
        '''
            Test the id for square
        '''
        sq = Square(2, 0, 0, 199)
        self.assertEqual(199, sq.id)

    def test_width_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square("1")

    def test_width_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(True)

    def test_width_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square([10, 6])

    def test_x_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, "46")

    def test_x_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, True)
