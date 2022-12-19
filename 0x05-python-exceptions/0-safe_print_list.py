#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    for item in range(0, x):
        try:
            print(f"{my_list[item]}", end="")
        except IndexError:
            return (item - 1)
    print("")
    return (x)
