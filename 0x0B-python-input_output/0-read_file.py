#!/bin/usr/python3
"""Defining a read_file function"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout"""

    with open("my_file_0.txt", "r", encoding="utf-8") as m:
        print(m.read())
