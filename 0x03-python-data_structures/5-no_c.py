#!/usr/bin/python3
def no_c(my_string):
    newString = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new_string += c
    return newString
