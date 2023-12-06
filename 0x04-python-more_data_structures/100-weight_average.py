#!/usr/bin/python3

def weight_average(my_list=[]):
    store = 0
    divisor = 0

    if my_list is None:
        return 0

    else:
        for item in my_list:
            store += item[0] * item[1]
            divisor += item[1]

    return (store/divisor)
