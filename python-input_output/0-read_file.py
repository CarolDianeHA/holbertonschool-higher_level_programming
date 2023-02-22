#!/usr/bin/python3
"""_summary_"""

def read_file(filename=""):
    with open(filename, encoding='utf8') as file:
        contents = file.read()
        print(contents)
