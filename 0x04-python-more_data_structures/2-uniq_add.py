#!/usr/bin/python3

def uniq_add(my_list=[]):
    added_int = []
    total = 0

    for item in my_list:
        if item not in added_int:
            added_int.append(item)
            total += item

    return (total)
