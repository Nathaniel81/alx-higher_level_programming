#!/usr/bin/python3

def remove_char_at(str, n):
    i = ""

    for ch in str:
        if n != 0:
            i += ch
        n -= 1

    return i
