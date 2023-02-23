#!/usr/bin/python3
"""_summary_"""


def append_write(filename="", text=""):
    """_summary_"""
    with open(filename, "a", encoding='utf-8') as file:
        file.write(text)
    return len(text)
