#!/usr/bin/python3

def uppercase(s):
    for char in s:
        i = ord(char)
        if (i >= 97 and i <= 122):
            i = ord(char) - 32

        print("{:s}".format(char(i)), end='')
    print('')
