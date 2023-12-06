#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff = []

    for item in set_1:
        if item not in set_2:
            diff.append(item)

    for item in set_2:
        if item not in set_1:
            diff.append(item)

    return (diff)
