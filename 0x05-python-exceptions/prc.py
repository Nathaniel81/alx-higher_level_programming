'''
try:
	f = open('t.txt', 'r')
	if f.name == 't.txt':
		raise Exception
except Exception as e:
	print('e')
except FileNotFoundError as e:
	print(e)
else:
	k = f.read()
	print(k)
finally:
	print('k')

def safe_print_list(my_list=[], x=0):
	c = 0
	try:
		for i in range(x):
				print("{}".format(my_list[i]), end='')
				c += 1
	except IndexError:
		pass
	print()
	return c

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
from pickle import TRUE
def safe_print_integer(value):
	try:
		print("{:d}".format(value))
		status = True
	except ValueError:
		status = False
	finally:
		return status

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

from itertools import count

def safe_print_list_integers(my_list=[], x=0):
	count = 0
	for i in range(x):
		try:
			print("{:d}".format(my_list[i]), end='')
			count += 1
		except (ValueError, TypeError):
			continue
		except IndexError:
			pass
	print()
	return count
		#return count
		#print()
		#pass
	#finally:
	#return count

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))

nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
'''












































