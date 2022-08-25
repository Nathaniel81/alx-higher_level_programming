#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    size = len(sys.argv)
    if size - 1 == 0:
        print("{:d} arguments .".format(size - 1))
    elif size - 1 == 1:
        print("{:d} {:s}".format(size - 1, "argument:"))
        print("{:d}: {:s}\n".format(size - 1, sys.argv[size - 1]), end='')
    else:
        print("{:d} {:s}".format(size - 1, "arguments:"))
        for i in range(1, size):
            print("{:d}: {:s}\n".format(i, sys.argv[i]), end='')
