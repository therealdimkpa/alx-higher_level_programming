#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = []

    for item in a_dictionary:
        keys.append(item)

    keys.sort()
    for item in keys:
        print("{}: {}".format(item, a_dictionary[item]))
