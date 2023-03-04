#!/usr/bin/python3
"""Module for test Rectangle"""
import unittest
import os
from models.rectangle import Rectangle
from models.base import Base

class RectangleTest(unittest.TestCase):
    """Test Rectangle"""

def SetUp(self):
    Base._Base__nb_objects = 0

def test_rectangle(self):
    self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
