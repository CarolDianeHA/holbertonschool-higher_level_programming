#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list.copy(my_list)
    for i in new_list:
        if i % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False
    i += 1
    return new_list
