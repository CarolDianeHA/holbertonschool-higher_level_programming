#!/usr/bin/python3
"""Text Indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines after some characters"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = 0
    for i in text:
        if (i  == '.' or i == '?' or i == ':'):
            print(i)
            print()
            print()
            flag = 1
        else:
            if (flag == 0):
                print(i, end='')
            else:
                if(i == '' or i == '\t'):
                    pass
                else:
                    print(i, end='')
                    flag = 0
