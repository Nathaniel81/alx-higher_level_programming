#!/usr/bin/python3
"""Defining appemd_after function"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file,
    after each line containing a specific string"""
    new_f = ""
    with open(filename, encoding="utf-8") as Myfile:
        for stR in Myfile.readlines():
            new_f += stR
            if search_string in stR:
                new_f += new_string
    """print(new_f)"""
    with open("append_after_100.txt", "w", encoding="utf-8") as Myfile:
        Myfile.write(new_f)
