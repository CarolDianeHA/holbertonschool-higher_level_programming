#!/usr/bin/python3
def no_c(my_string):
    disallowed_char = "cC"
    for char in disallowed_char:
        my_string = my_string.replace(char, '')
    return (my_string)
