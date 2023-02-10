#!/usr/bin/python3
"""Class named Square that defines a square"""


class Square:
    """
    Create Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize instance"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """getter size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif type(value) < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """getter position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter position"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or \
           type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Return area of the square"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square"""
        if self.__size > 0:
            if self.position[1] > 0:
                print("\n" * self.position[1], end='')
            for i in range(self.__size):
                print("_" * self.position[0], end="")
                for j in range(self.__size):
                    print("#", end='')
                print()
        else:
            print()
