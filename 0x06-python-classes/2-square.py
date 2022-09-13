#!/usr/bin/python3
"""Documentation for a square class"""



class Square():

    """Sets the size of the square on instantation."""

    def __init__(self, size=0):
        if isinstance(size, int):
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
