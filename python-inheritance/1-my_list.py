#!/usr/bin/python3
"""MyList that inherits from list"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """prints elements of the list"""
        print(sorted(self))
