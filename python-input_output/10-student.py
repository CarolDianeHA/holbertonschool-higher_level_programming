#!/usr/bin/python3
"""_summary_"""


class Student:

    def __init__(self, first_name, last_name, age):
        """_summary_"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        dic = {}
        if (type(attrs) is not list):
            return self.__dict__
        else:
            for i in attrs:
                if (i in self.__dict__):
                    dic[i] = self.__dict__[i]
            return dic
