#!/usr/bin/python3

def uppercase(s):
    for c in s:
        i = ord(c)
        if (i >= 97 and i <= 122):
            i = ord(c) - 32

        print("{:s}".format(chr(i)), end='')
    print('')
