#!/usr/bin/python3
for a in range(ord("a"), ord("z") + 1):
    if chr(a) == "q" or chr(a) == "e":
        continue
    else:
        print("{:s}".format(chr(a)), end="")
