#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    lst_d = number % -10
else:
    lst_d = number % 10
msg = "Last digit of "
if lst_d < 0:
    lst_d = -lst_d
    print("{}{} is {} and is less than 6 and not 0".format(msg, number, lst_d))
elif lst_d < 6 and lst_d != 0:
    print("{}{} is {} and is less than 6 and not 0".format(msg, number, lst_d))
elif lst_d > 5 and lst_d != 0:
    print("{}{} is {} and is greater than 5".format(msg, number, lst_d))
else:
    print("{}{} is {} and is 0".format(msg, number, lst_d))
