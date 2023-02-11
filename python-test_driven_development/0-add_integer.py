#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        return(int(a + b))
    except:
        if a != int:
            raise TypeError("a must be an integer")
        else:
            raise TypeError("b must be an integer")
