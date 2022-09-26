#!/usr/bin/python3
"""Documentation for a rectangle class"""


BR = __import__('7-base_geometry').BaseGeometry


class Rectangle(BR):
    """Represents a Rectangle"""

    def __init__(self, width, height):
        """Instantiate the class"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return f'[{self.__class__.__name__}] {self.__width}/{self.__height}'
    