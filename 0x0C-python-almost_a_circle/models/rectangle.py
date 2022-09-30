#!/usr/bin/python3
"""Documentation for a Rectagnle class"""


from models.base import Base


class Rectangle(Base):
    """a class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @width.setter
    def width(self, w):
        """Sets the width"""
        self.__width = w

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @height.setter
    def height(self, h):
        """Sets the height"""
        self.__height = h

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x"""
        self.__x = x

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y"""
        self.__y = y
