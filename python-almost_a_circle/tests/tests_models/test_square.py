#!/usr/bin/python3
"""Module for test Square"""
import unittest
import os
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle

class SquareTest(unittest.TestCase):
    """Test Square"""

def SetUp(self):
    Base._Base__nb_objects = 0



if __name__ == '__main__':
    unittest.main()
