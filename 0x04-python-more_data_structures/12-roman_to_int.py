#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_Letters = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    num = 0
    lst = 0

    for letter in roman_string:
        for elem in roman_Letters:
            if letter == elem[0]:
                if lst == 0 or lst >= elem[1]:
                    num += elem[1]
                elif lst < elem[1]:
                    num += elem[1] - (lst * 2)

                lst = elem[1]

    return num
