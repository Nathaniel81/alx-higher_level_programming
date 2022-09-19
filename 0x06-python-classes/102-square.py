#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be a number")
        def area(self):
            return self.__size ** 2
        def __ne__(self, other):
            return self.__size != other.__size
        def __eq__(self, other):
            return self.__size == other.__size
        def __ge__(self, other):
            return self.__size >= other.__size
        def __gt__(self, other):
            return self.__size > other.__size
        def __le__(self, other):
            return self.__size <= other.__size
        def __lt__(self, other):
            return self.__size < other.__size
