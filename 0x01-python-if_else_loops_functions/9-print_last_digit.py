#!/usr/bin/python3

def print_last_digit(number):
    number = str(number)
    num = int(number[-1])
    print("{}".format(num), end="")
    return (num)
