#!/usr/bin/python3
"""Documentation for a class"""


def max_integer(list=[]):
    """Returns the max integer in a list of integers
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result