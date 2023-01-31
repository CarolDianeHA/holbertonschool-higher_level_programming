#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string.translate({ord(char): None for char in "cC"})
    return (new_string)
