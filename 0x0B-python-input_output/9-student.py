#!/usr/bin/python3
"""Defining a student class"""


class Student:
    """A student class"""
    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary description
        for JSON serialization of an object"""
        return vars(self)
