#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Args:
        my_list (list, optional): Defaults to [].

    Returns:
        int: The maximum number in the list
        None: If the list is empty
    """
    
    if (len(my_list) == 0):
        return None
    else:
        my_list.sort()
        return (my_list[len(my_list) - 1])
