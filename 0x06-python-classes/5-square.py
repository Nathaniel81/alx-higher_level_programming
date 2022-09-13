#!/usr/bin/python3
"""Documentation for a square class"""


class Square():
    """Represents a square"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Gets the value of attribute size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """sets the value of the attribute size."""
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """returns the square based on the size."""
        return (self.__size ** 2)

    def my_print(self):
        """prints the square with the character '#' based on the size."""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
