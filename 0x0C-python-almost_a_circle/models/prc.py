"""from turtle import width


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length
"""
#from nntplib import ArticleInfo


def aa(*args, **kwargs):
    if not kwargs:
        print('Y')
    for i, j in kwargs.items():
        print(i, j, type(i), type(j))
        
aa(2, 4, 7, 8, a='d')
