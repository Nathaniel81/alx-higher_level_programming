#!/usr/bin/python3
"""Documentation for a function that returns the list of objects"""


def lookup(obj):
    """Returns the list of available attributes"""
    """return obj.__dict__
    return vars(obj)"""

    return dir(obj)
