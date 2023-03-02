#!/usr/bin/python3

"""Base Class"""

import json


class Base:
    """Class manage id attributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class Constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of list_dictionary"""
        return json.dumps(list_dictionaries)
