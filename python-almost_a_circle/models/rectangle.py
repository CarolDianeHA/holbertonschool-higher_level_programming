#!/usr/bin/python3

"""Rectangle Class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width"""
        self.__width = value

    @property
    def height(self):
        """Getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height"""
        self.__height = value

    @property
    def x(self):
        """Getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x"""
        self.__x = value

    @property
    def y(self):
        """Getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y"""
        self.__y = value
