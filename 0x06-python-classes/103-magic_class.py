#!/usr/bin/python3

"""
Doc
"""
import math


class MagicClass():
    """
    MagicClass representation of python byte code given.
    """
    def __init__(self, radius=0):
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        """
        Computes the area of the given circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Computes the circumstance of the given circle.
        """
        return 2 * math.pi * self.__radius
