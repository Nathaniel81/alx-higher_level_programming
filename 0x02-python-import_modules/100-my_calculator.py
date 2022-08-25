#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv)
    opr = ['+', '-', '/', '*']
    if argc == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        for i in range(0, 4):
            if sys.argv[2] == opr[i]:
                if opr[i] == '+':
                    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
                    exit(0)
                elif opr[i] == '-':
                    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
                    exit(0)
                elif opr[i] == '/':
                    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
                    exit(0)
                else:
                    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
                    exit(0)
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
