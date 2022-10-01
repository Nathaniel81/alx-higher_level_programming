from unicodedata import name


class x:
    def __init__(self, name):
        self.name = name
    def dct(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.__dict__.keys():
                self.__setattr__(k, v)

        """a = []
        for i in self.__dict__.keys():
            a.append(i)
        return a"""

z = x("fff")
print(z.name)
z.dct(nam="ddd")
print(z.name)
setattr(z, "name", "LL")
print(z.name)