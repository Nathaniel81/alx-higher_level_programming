#!/usr/bin/python3

"""
Doc
"""


class Square():
    """
    Contains some attribute definations, and method
    definations.
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrives the value of attribute size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the value of the attribute size.
        """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """
        Retrives the value of the attribute position.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the value of the attribute position.
        """
        if (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(v, int) for v in value) and
                all(v >= 0 for v in value)):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Computes and returns the square based on the size.
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Prints the square with the character '#' based on the size.
        """
        if self.__size == 0:
            print("")
        else:
            for s in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print('#', end="")
                print("")

    def __repr__(self):
        """
        Prints representation of the class Square itself with magic
        """
        ret_val = ""

        if self.__size == 0:
            return ret_val

        for s in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for k in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print('#', end="")
            if i < (self.__size - 1):
                print("")

        return ret_val
