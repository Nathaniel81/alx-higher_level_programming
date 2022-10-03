from unicodedata import name


class D:
    def __init__(self, name):
        self.name = name
class Calculator(D):
    def __init__(self, name):
        super().__init__(name)
    #super().__init__(name)
    def addNumbers(x, y):
        return x + y
    @classmethod
    def ff(cls):
        print(cls.__name__)

# create addNumbers static method
#Calculator.addNumbers(3, 3)
#= staticmethod(Calculator.addNumbers)

#print('Product:', Calculator.addNumbers(15, 110))
print('Product:', Calculator.ff())