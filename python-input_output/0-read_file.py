#!/usr/bin/python3
"""_summary_"""


def read_file(filename=""):
    """function to read files"""
    with open(filename, encoding='utf8') as file:
        contents = file.readlines()
        print(contents)
