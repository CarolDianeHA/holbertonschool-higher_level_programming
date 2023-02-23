#!/usr/bin/python3
"""_summary_"""


import json


def save_to_json_file(my_obj, filename):
    """_summary_"""
    with open(filename, "x", encoding='utf-8') as file:
        text = json.dumps(my_obj)
        file.write(text)
    return len(text)
