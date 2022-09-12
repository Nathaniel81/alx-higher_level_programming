#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        status = True
    except (ValueError, TypeError):
        status = False
    finally:
        return status
