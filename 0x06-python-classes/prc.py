'''
class student:
	_raiseAmt = 1.05
	def __init__(self, sex, age, gpa):
		self.sex = sex
		self.age = age
		self.gpa = gpa
	def Gpa(self):
		return self.gpa
	def _raise(self):
		self.gpa = int(self.gpa * self._raiseAmt)

s1 = student('Male', 56, 3.90)
s2 = student('Female', 89, 8.90)
print(s1.gpa)
print(s1.gpa)
print(s1.__dict__)
s1._raiseAmt = 1.06
print(s1.__dict__)
print(s1._raiseAmt)
print(s2._raiseAmt)

class sq:
	def __init__(self, height="0", width="0"):
		self.height = height
		self.width = width

	@property
	def height(self):
		print("Rtv.. H")
		return self.__height

	@height.setter
	def height(self, value):
		if value.isdigit():
			self.__height = value
		else:
			print("Err")

	@property
	def width(self):
		print("Rtv.. W")
		return self.__width
		
	@width.setter
	def width(self, value):
		if value.isdigit():
			self.__width = value
		else:
			print("Err")
	def getArea(self):
		return int(self.__width) * int(self.__height)
def main():
	asq = sq()
	height = 7
	width = 8
	asq.height = height
	asq.width = width
	print("H:", asq.height)
	print("W: ", asq.width)
	print("A: ", asq.getArea())

main()
'''
class Square:
	pass



my_square = Square()
print(type(my_square))
print(my_square.__dict__)



































