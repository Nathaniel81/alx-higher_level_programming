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
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
