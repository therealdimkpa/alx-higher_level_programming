#!/usr/bin/python3
from sys import *

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return False
