#!/usr/bin/python3
"""_summary_"""


import json


def load_from_json_file(filename):
    """_summary_"""
    with open(filename, 'r') as file:
        json_string = file.read()
        obj = json.loads(json_string)
    return obj
