#!/usr/bin/python3

def roman_to_int(roman_string):
    """roman numerals to integer

    Args:
        roman_string (string): The roman numeral to be converted to int

    Returns:
        integer:    0 if roman_string is empty or not a string
                    Number value of roman_string
    """
    if not roman_string or type(roman_string) != str:
        return 0
    else:
        # creates the dictionary storing the value of roman rumerals
        store = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        number = 0
        # converts the input to uppercase
        roman_string = roman_string.upper()
        
        for char in range(0, len(roman_string)):
            number += store[roman_string[char]]

            if (char > 0 and store[roman_string[char]] > store[roman_string[char - 1]]):
                number -= 2 * store[roman_string[char - 1]]

    return number
