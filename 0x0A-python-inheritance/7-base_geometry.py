#!/usr/bin/python3
"""Documentation for a BaseGeometry class"""


class BaseGeometry:
    """Definition for the class"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """That validates value:"""
        if not type(value) is int:
           raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
