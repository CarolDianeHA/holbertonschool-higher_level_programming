#!/usr/bin/python3
"""Class named Square that defines a square"""


class Square:
    """Definition of a private instance attribute for size
    Raises:
        TypeError: if 'size'is not an integer
        ValueError: if 'size' is less than zero
    """

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """getter function"""
        return self.__size

    @size.setter
    def size(self, size):
        """setter function"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)
