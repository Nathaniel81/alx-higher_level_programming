#!/usr/bin/python3
""" This module contains a class called Square
that inherits from the Base class """

from webbrowser import get
from models.rectangle import Rectangle

class Square(Rectangle):
    """ class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantantiation """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns the string representation of a Square an object."""
        return '[{}] ({}) {}/{} - {}'.format(self.__class__.__name__, self.id,
                                             self.x, self.y, self.size)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.__x = args[2]
                self.__y = args[3]
            except IndexError:
                pass
        elif kwargs:
            for keys, values in kwargs.items():
                self.__setattr__(keys, values)
        else:
            pass

    def to_dictionary(self):
        """Square instance to dictionary representation"""
        return {'id': getattr(self, 'id'),
            'size' : getattr(self, 'size'),
            'x' : getattr(self, 'x'),
            'y' : getattr(self, 'y')
        }
