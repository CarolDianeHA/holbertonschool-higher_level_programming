#!/usr/bin/python3
"""_summary_"""


class Student:

    def __init__(self, first_name, last_name, age):
        """_summary_"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
