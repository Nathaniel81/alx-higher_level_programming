#!/usr/bin/python3
"""
Documentation for class that computes the perimeter of a rectangle perimeter
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value for the width"""
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """"Gets the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """Computes the area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the permeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
