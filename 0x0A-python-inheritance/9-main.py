#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
BR = __import__('7-base_geometry').BaseGeometry

class Rectangle(BR):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
    def area(self):
        return self.__width * self.__height
    def __str__(self):
        return "[{}] {}/{}".format(self.__class__.__name__, self.__width, self.__height)
    
r = Rectangle(3, 5)

print(r)
print(r.area())
