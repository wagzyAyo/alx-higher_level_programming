#!/usr/bin/python3
"""Create test for base.py"""
import unittest
from models.base import Base


class test_base(unittest.TestCase):
    """Test for base class"""

    def test_no_id(self):
        """sending no id"""
        test_x = Base()
        self.assertEqual(1, test_x.id)


    def test_val_id(self):
        """passing value to id"""
        test_x = Base(20)
        self.assertEqual(20, test_x.id)

    def test_zero_id(self):
        """passing 0 to id"""
        test_x = Base(0)
        self.assertEqual(0, test_x.id)

    def test_neg_id(self):
        """passing negative number
        to id"""
        test_x = Base(-7)
        self.assertEqual(-7, test_x.id)
