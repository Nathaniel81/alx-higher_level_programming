#!/usr/bin/python3
"""Documentation for a simple rectangle class"""


class Rectangle:
    """A classs definition for a rectangle"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of the width"""
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Gets the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of the height"""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")
