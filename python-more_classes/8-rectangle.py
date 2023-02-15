#!/usr/bin/python3
"""Rectangle class that includes width, height and area attibutes"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initalize instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        if self.height == 0 or self.width == 0:
            return(0)
        return (2 * (self.width + self.height))

    def __str__(self):
        """Print rectangle"""
        rec_str = ""
        if self.height == 0 or self.width == 0:
            return rec_str
        for i in range(self.height):
            for j in range(self.width):
                rec_str += str(self.print_symbol)
            rec_str += "\n"
        return rec_str[:-1]

    def __repr__(self):
        """String representation"""
        width = self.__width
        height = self.__height
        return "Rectangle({:d}, {:d})".format(width, height)

    def __del__(self):
        """delete function"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance (rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance (rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
