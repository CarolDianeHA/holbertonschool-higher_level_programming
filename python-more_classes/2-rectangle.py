#!/usr/bin/python3
"""Rectangle class that includes width, height and area attibutes"""


class Rectangle:
    """Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initalize instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return rectangle area"""
        return (self.width * self.height)

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.height == 0:
            return(0)
        return (2 * (self.width + self.height))
