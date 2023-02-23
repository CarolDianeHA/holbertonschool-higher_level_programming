#!/usr/bin/python3
"""_summary_"""


def write_file(filename="", text=""):
    """_summary_"""
    with open(filename, "x", encoding='utf-8') as file:
        file.write(text)
    return len(text)
