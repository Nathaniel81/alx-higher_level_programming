#!/usr/bin/python3
"""Documentaion for print_sorted function"""


class MyList(list):
    """Inherits from the list class"""

    def __init__(self):
        """Initializing this class with the parent init method"""
        list.__init__(self)

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
