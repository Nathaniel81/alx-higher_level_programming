#!/usr/bin/python3
"""Definition for MyInt class"""


class MyInt(int):
    """Inherits the int class"""

    def __eq__(self, value):
        """Equal representation"""
        return self.real != value

    def __ne__(self, value):
        """Not equal representation"""
        return self.real == value
