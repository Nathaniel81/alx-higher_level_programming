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
'''
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