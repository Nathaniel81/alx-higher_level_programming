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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return '[]'
    
    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file """
        dict_list = []
        with open('Rectangle.json', 'w', encoding='utf-8') as myFile:
            if list_objs:
                [dict_list.append(obj.to_dictionary()) for obj in list_objs]
                myFile.write(Base.to_json_string(dict_list))
            else:
                myFile.write(dict_list)

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation """
        if json_string:
            return json.loads(json_string)
        return '[]'

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                r = cls(1, 2)
                r.update(**dictionary)
                return r
            else:
                s = cls(1)
                s.update(**dictionary)
                return s
