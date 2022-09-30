#!/usr/bin/python3
"""Documentation for a single class called Base"""


class Base:
    """The “base” of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instatntiation"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
