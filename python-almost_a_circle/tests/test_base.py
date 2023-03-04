#!/usr/bin/python3
"""Module for test Base"""
import unittest
import os
from models.base import Base

class BaseTest(unittest.TestCase):
    """Test Base"""

def SetUp(self):
    Base._Base__nb_objects = 0



if __name__ == '__main__':
    unittest.main()
