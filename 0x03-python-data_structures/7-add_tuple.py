#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds the first elements of two tuples
    and the second elements of two tuples
    """

    final_tuple = [0, 0]
    if len(tuple_a) > 0:
        final_tuple[0] += tuple_a[0]
    if len(tuple_b) > 0:
        final_tuple[0] += tuple_b[0]

    if len(tuple_a) > 1:
        final_tuple[1] += tuple_a[1]
    if len(tuple_b) > 1:
        final_tuple[1] += tuple_b[1]

    return (tuple(final_tuple))

