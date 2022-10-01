from models.base import Base as B


class Rectangle(B):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if isinstance(w, int):
            if w <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = w
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if type(h) == int:
            if h <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = h
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def aa(self, *args):
        self.__x = args[0]