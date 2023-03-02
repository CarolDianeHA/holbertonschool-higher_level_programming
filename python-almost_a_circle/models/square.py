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

    @property
    def size(self):
        """Getter size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square class"""
        argc = len(args)
        kwargc = len(kwargs)
        modif_attrs = ["id", "size", "x", "y"]
        if argc > 4:
            argc = 4
        if argc > 0:
            for i in range(argc):
                setattr(self, modif_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in modif_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Return dictionary representation of a Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            }
