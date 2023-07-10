#!/usr/bin/python3
"""
Contains a function that returns a list of available
methods and objects
"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return dir(obj)
