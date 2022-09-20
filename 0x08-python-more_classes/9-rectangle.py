"""#!/usr/bin/python3"""
"""Documentation for a Rectangle class"""


from turtle import width


class Rectangle:
    """class defination called Rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Returns the width value.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the height value
        """
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >= 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """
        Gets the height value
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height value.
        """
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """
        Computes the area of rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Nicely printable string representation of an object of class
        rectangle.
        """
        emptStr = ""
        if (self.__height == 0 or self.__width == 0):
            return emptStr
        for i in range(self.__height):
            [print(self.print_symbol, end="") for c in range(self.__width)]
            if i < self.__height - 1:
                print()
        return emptStr

    def __repr__(self):
        """
        return a string representation of the rectangle to be able
        to recreate a new instance
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        An instance method that deletes an instance of the class Rectangle.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance"""
        width = height = size
        return cls(width, height)
