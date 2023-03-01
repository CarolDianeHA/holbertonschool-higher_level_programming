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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return rectangle area"""
        return (self.__width * self.__height)

    def display(self):
        """Prints stdout the Rectangle instance with #"""
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        for i in range(y):
            print()
        for i in range(h):
            for i in range(x):
                print("", end=" ")
            for i in range(w):
                print("#", end="")
            print()

    def __str__(self):
        """Print rectangle"""
        id = self.id
        x = self.__x
        y = self.__y
        w = self.__width
        h = self.__height
        return f"[Rectangle] ({id}) {x}/{y} - {w}/{h}"
