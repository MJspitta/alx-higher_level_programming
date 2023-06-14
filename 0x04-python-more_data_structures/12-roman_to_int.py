#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 100
            }
    total_num = 0
    last_val = 0

    if type(roman_string) != str or roman_string is None:
        return 0
    for r in reversed(roman_string):
        val = roman_num[r]
        if val < last_val:
            total_num -= val
        else:
            total_num += val
        last_val = val
    return total_num
