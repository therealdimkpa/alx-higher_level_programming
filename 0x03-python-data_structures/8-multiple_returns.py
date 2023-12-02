#!/usr/bin/python3

def multiple_returns(sentence):
    """
    multiple_returns

    Args:
        sentence (string): Any type of sentence or string

    Returns:
        tuple(length of input, first char of input)
    """
    if len(sentence) == 0:
        return (len(sentence), None)
    else:
        return (len(sentence), sentence[0])
