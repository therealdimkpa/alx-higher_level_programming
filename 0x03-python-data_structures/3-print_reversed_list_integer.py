#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    end = len(my_list) - 1
    while (end >= 0):
        print("{:d}".format(my_list[end]))
        end -= 1
