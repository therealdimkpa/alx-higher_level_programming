#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    store = []
    for item in my_list:
        store.append(item % 2 == 0)
    return (store)
