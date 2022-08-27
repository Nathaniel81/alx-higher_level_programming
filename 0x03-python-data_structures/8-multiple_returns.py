#!/usr/bin/python3

def multiple_returns(sentence):
    ln = len(sentence)
    if sentence == "":
        firstChar = None
    else:
        firstChar = sentence[0]
    tup = (ln, firstChar)
    return tup
