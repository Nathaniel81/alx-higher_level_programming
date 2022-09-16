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
s2 = student('Female', 89, 3.75)
print(s1.gpa)
print(s1.gpa)
print(s1.__dict__)
s1._raiseAmt = 1.06
print(s1.__dict__)
print(s1._raiseAmt)
print(s2._raiseAmt)

class Square:
	pass

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
class Robot(object):
    pass
x = Robot()
Robot.brand = "Kuka"
print(x.brand)
class Dog:
	def __init__(self, n="", h=0, w=0):
		self.n = n
		self.h = h
		self.w = w
	def run(self):
		print("{} runs".format(self.n))
	def eat(self):
		print("{} eats".format(self.n))
	def barks(self):
		print("{} barks".format(self.n))
def main():
	spotie = Dog("Spot", 8, 7)
	roxie = Dog()
	Dog.barks(roxie)
	roxie.eat()
	
main()
class Square:
	def __init__(self, h="0", w="0"):
		self.h = h
		self.w = w
#CShafer >>
class Emp():

	def __init__(self, fst='', lst=''):
		self.fst = fst
		self.lst = lst
	@property
	def email(self):
		return "{}.{}@gmail.com".format(self.fst, self.lst)
	@property
	def full(self):
		return "{} {}".format(self.fst, self.lst)
	@full.setter
	def full(self, name):
		fst, lst = name.split(' ')
		self.fst = fst
		self.lst = lst

	@full.deleter
	def full(self):
		self.fst = None
		self.lst = None

emp1 = Emp('kyle', 'Douglas')
emp2 = Emp()
emp1.full = 'Bekele Mamo'

emp1.fst = 'Nate'
print(emp1.fst)
print(emp1.email)
emp2.fst = 'Jim'
emp2.lst = 'l'
print(emp1.full)
del emp1.full
print(emp1.full)
print(emp1.fst)

#print("{}\n{}".format(emp2.full(), emp2.email))
#<< 
class Square:
	def __init__(self, size):
		self.__size = size

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)
from lib2to3.pgen2.token import RIGHTSHIFT
from msilib.schema import Class

class Square:
	def __init__(self, size=0):
		if isinstance(size, int):
			if size < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = size
		else:
			raise TypeError("size must be an integer")

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

class Square:
	def __init__(self, size=0):
		if isinstance(size, int):
			if size < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = size
		else:
			raise TypeError("size must be an integer")
	@property
	def area(self):
		return self.__size ** 2


my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area))

class Square:
	def __init__(self, size=0):
		if isinstance(size, int):
			if size < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = size
		else:
			raise TypeError("size must be an integer")
	def area(self):
		return self.__size ** 2
	@property
	def size(self):
		return self.__size
	@size.setter
	def size(self, value):
		self.__size = value
		if isinstance(value, int):
			if value < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = value
		else:
			raise TypeError("size must be an integer")

my_square = Square(8)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

#file=sys.stderr
import sys
class Square:
	def __init__(self, size=0):
		self.size = size
	def area(self):
		return self.__size ** 2
	def my_print(self):
		for i in range(self.__size):
			for j in range(self.__size):
				print("{}".format('#'), file=sys.stderr, end='')
			print()

	@property
	def size(self):
		return self.__size
	@size.setter
	def size(self, value):
		if isinstance(value, int):
			if value < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = value
		else:
			raise TypeError("size must be an integer")

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")
class Square:
	def __init__(self, size=0, position=(0, 0)):
		self.size = size
		self.position = position
	def area(self):
		return self.__size ** 2
	@property
	def size(self):
		return self.__size
	@size.setter
	def size(self, value):
		if isinstance(value, int):
			if value < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = value
		else:
			raise TypeError("size must be an integer")
	@property
	def position(self):
		return self.__property
	@position.setter
	def position(self, value):
		if not isinstance(value, tuple):
			raise TypeError("position must be a tuple of 2 positive integers")
		elif len(value) is not 2:
			raise TypeError("position must be a tuple of 2 positive integers")
		elif not isinstance(value[0], int):
			raise TypeError("position must be a tuple of 2 positive integers")
		elif not isinstance(value[1], int):
			raise TypeError("position must be a tuple of 2 positive integers")
		elif value[1] < 0 or value[1] < 0:
			raise TypeError("position must be a tuple of 2 positive integers")
		else:
			self.__position = value
	def my_print(self):
		if self.__size == 0:
			print()
			return

		if self.__position[0] >= 0 and self.__position[1] >= 0:
			for height in range(self.__position[1]):
				print()

		for rows in range(self.__size):
			for spaces in range(self.__position[0]):
				print(' ', end='')
			for columns in range(self.__size):
				print('#', end='')
			print()

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")


class Node:
	def __init__(self, data, nex=None):
		self.data = data
		self.nex = nex
class ll:
	def __init__(self, head=None):
		self.head = head
	def sll(self, value):
		new = Node(value)
		if self.head is None:
			self.head = new
		else:
			tr = self.head
			while tr.nex is not None:
				tr = tr.nex
			tr.nex = new
			new.nex = None
	"""def prinList(self):
		cur = self.head
		while cur != None:
			print(cur.data)
			cur = cur.nex"""

	def __str__(self):
		val =[]
		tmp = self.head
		while tmp is not None:
			val.append(str(tmp.data))
			tmp = tmp.nex
		return('\n'.join(val))

az = ll()
az.sll(2)
az.sll(4)
az.sll(6)
#az.prinList()
print(az)

from tkinter.messagebox import NO


class Node:
	def __init__(self, data, next_node=None):
		self.data = data
		self.next_node = next_node
	@property
	def data(self):
		return self.__data
	@data.setter
	def data(self, value):
		if isinstance(value, int):
			self.__data = value
		else:
			raise TypeError("data must be an integer")
	@property
	def next_node(self):
		return self.__next_node
	@next_node.setter
	def next_node(self, value):
		if isinstance(value, Node) or value is None:
			self.__next_node = value
		else:
			raise TypeError("next_node must be a Node object")
class SinglyLinkedList:
	def __init__(self):
		self.__head = None
	def sorted_insert(self, value):
		new_node = Node(value)
		if self.__head is None:
			new_node.next_node = None
			self.__head = new_node
		elif self.__head.data:
			traverse = self.__head
			while traverse.next_node is not None:
				traverse = traverse.next_node
			new_node.next_node = None
			traverse.next_node = new_node
	def prinList(self):
		tmp = self.__head
		while tmp is not None:
			print(tmp.data)
			tmp = tmp.next_node

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
SinglyLinkedList.prinList(sll)


from multiprocessing import Value
from termios import VLNEXT


class Square:
	def __init__(self, size=0, position=(0,0)):
		self.size = size
		self.position = position
	@property
	def size(self):
		return self.__size
	@size.setter
	def size(self, value):
		if isinstance(value, int):
			if value < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = value
		else:
			raise TypeError("size must be an integer")
	@property
	def position(self):
		return self.__position
	@position.setter
	def position(self, value):
		if not isinstance(value, tuple):
			raise TypeError("position must be a tuple of 2 positive integer")
		if len(value) != 2:
			raise TypeError("position must be a tuple of 2 positive integer")
		if value[0] or value[1]:
			raise TypeError("position must be a tuple of 2 positive integer")
	def area(self):
		return self.__size ** 2
	def my_print(self):
		if self.__size == 0:
			print("")
		else:
			for s in range(self.__position[1]):
				print()
			for i in range(self.__size):
				for k in range(self.__position[0]):
					print(" ", end="")
				for j in range(self.__size):
					print('#', end="")
				print()
	def __str__(self):
'''
class Square:
	def __init__(self, size=0):
		self.size = size
	@property
	def size(self):
		return self.__size
	@size.setter
	def size(self, value):
		if isinstance(value, int) or isinstance(value, float):
			if value < 0:
				raise ValueError("size must be >= 0")
			else:
				self.__size = value
		else:
			raise TypeError("size must be a number")
	def area(self):
		return self.__size ** 2
	def __ne__(self, other):
		return self.__size != other.__size
	def __eq__(self, other):
		return self.__size == other.__size
	def __ge__(self, other):
		return self.__size >= other.__size
	def __gt__(self, other):
		return self.__size > other.__size
	def __le__(self, other):
		return self.__size <= other.__size
	def __lt__(self, other):
		return self.__size < other.__size

s_5 = Square(5)
s_6 = Square(6)

if s_5 < s_6:
    print("Square 5 < Square 6")
if s_5 <= s_6:
    print("Square 5 <= Square 6")
if s_5 == s_6:
    print("Square 5 == Square 6")
if s_5 != s_6:
    print("Square 5 != Square 6")
if s_5 > s_6:
    print("Square 5 > Square 6")
if s_5 >= s_6:
    print("Square 5 >= Square 6")




















































