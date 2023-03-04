#!/usr/bin/python3
"""Module for test Base"""
import unittest
import os
from models.base import Base

class BaseTest(unittest.TestCase):
    """Test Base"""

def SetUp(self):
    Base._Base__nb_objects = 0

def test_id(self):
        """ checks if correct id was generated"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 4)

    def test_any_docstring(self):
        """Checks for any docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_custom_id(self):
        '''Test custom str id'''
        i = "Behemoth"
        b = Base(i)
        self.assertEqual(b.id, i)

    def test_custom_id_int(self):
        '''Test custom id'''
        b = Base(30)
        self.assertEqual(b.id, 30)

    def test_kwargs_id(self):
        '''Test custom kwarg id'''
        b = Base(id=30)
        self.assertEqual(b.id, 30)

    def test_str_id(self):
        '''Test custom str id'''
        b = Base('hell')
        self.assertEqual(b.id, 'hell')

    def test_none_id(self):
        '''Test custom str id'''
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_none_json(self):
        """ snet nothing to function"""
        b = Base.to_json_string(None)
        self.assertEqual(b, "[]")

    def test_list_json(self):
        """ snet list to function"""
        li = ["iron", "maiden", ["thrash", "metal"]]
        b = Base.to_json_string(li)
        self.assertEqual(b, "[\"iron\", \"maiden\", [\"thrash\", \"metal\"]]")

    def test_empty_list_json(self):
        """sent empty list to function"""
        b = Base.to_json_string([])
        self.assertEqual(b, "[]")

    def test_no_args_json(self):
        """ raises error passed no args to function"""
        with self.assertRaises(TypeError) as e:
            b = Base.to_json_string()
        self.assertEqual("to_json_string() missing 1 required positional " +
                         "argument: 'list_dictionaries'", str(e.exception))

    def test_list_of_dicts_json(self):
        b = Base.to_json_string([{"talla": 5}, {"ancho": 12}])
        self.assertEqual(type(b), str)

    def test_no_args_save_to_file(self):
        with self.assertRaises(TypeError) as e:
            b = Base.save_to_file()
        self.assertEqual("save_to_file() missing 1 required positional " +
                         "argument: 'list_objs'", str(e.exception))

    def test_save_to_file_None(self):
        Base.save_to_file(None)
        with open("Base.json", "r") as file:
            self.assertEqual(file.read(), "[]")

if __name__ == '__main__':
    unittest.main()
