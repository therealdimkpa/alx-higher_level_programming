#!/usr/bin/python3

def best_score(a_dictionary):
    best = ["score", 0]
    valid = False

    if a_dictionary is None:
        return None

    for item in a_dictionary:
        if type(a_dictionary[item]) == int:
            valid = True

    if valid is True:
        for item in a_dictionary:
            if a_dictionary[item] > best[1]:
                best[0] = item
                best[1] = a_dictionary[item]
        return (best[0])
    else:
        return None
