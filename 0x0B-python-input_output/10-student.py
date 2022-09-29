#!/usr/bin/python3
"""Defining a Student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary"""
        clsdict = self.__dict__
        if not type(attrs) == list:
            return clsdict
        for keyS in attrs:
            if not type(keyS) == str:
                return clsdict
        retdict = {}
        for i in attrs:
            if i in clsdict.keys():
                retdict[i] = clsdict[i]
        return retdict
