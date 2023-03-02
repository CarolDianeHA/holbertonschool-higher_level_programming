#!/usr/bin/python3

"""Square Class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representations"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
