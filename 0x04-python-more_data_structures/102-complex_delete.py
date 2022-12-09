#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    del_keys = []

    for item in a_dictionary:
        if a_dictionary[item] == value:
            del_keys.append(item)

    for item in del_keys:
        del (a_dictionary[item])

    return a_dictionary
