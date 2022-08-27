#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    rng = len(my_list) - 1
    newlist = my_list.copy()
    if idx > 0 or idx <= rng:
        newlist[idx] = element
        return newlist
    else:
        return my_list
