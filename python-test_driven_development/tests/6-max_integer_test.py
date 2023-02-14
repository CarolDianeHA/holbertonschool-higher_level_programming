#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test for max integers"""

    def test_max_integer(self):
        """different scenarios"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([20, 10, 30, 40, 50]), 50)
        self.assertEqual(max_integer([1, 2, 3, 10, 4]), 10)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-1, 15, 10000, -2, -3]), 10000)
        self.assertEqual(max_integer([[13], [6], [23], [1]]), [23])
        self.assertEqual(max_integer([1.3, 1.6, 1.2, 1.4]), 1.6)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([8]), 8)
