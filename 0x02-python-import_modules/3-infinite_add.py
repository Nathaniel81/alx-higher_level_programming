#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    argsum = 0
    for i in range(1, argc):
        argsum += int(sys.argv[i])

    print("{:d}".format(argsum))
