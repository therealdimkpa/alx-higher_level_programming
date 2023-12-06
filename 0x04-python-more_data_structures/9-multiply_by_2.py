#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    n_dict = a_dictionary.copy()

    for item in n_dict:
        n_dict[item] = n_dict[item] * 2

    return (n_dict)
