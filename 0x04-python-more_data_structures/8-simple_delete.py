#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """simple_delete

    Args:
        a_dictionary (_type_): _description_
        key (str, optional): _description_. Defaults to "".

    Returns:
        _type_: _description_
    """
    if key in a_dictionary:
        del (a_dictionary[key])
    return (a_dictionary)
