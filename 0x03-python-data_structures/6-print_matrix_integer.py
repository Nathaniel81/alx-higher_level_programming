#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    itemLen = len(matrix[0]) - 1
    i = 0
    for items in matrix:
        for elements in items:
            if elements == matrix[i][itemLen]:
                print("{:d}".format(elements), end='')
            else:
                print("{:d}".format(elements), end=' ')
        i += 1
        print()
