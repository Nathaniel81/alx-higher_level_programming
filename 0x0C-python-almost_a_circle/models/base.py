#!/usr/bin/python3
"""Documentation for a single class called Base"""


import json
class Base:
    """The base of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instatantiation"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'
