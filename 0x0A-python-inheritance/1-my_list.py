#!/usr/bin/python3
class MyList(list):
    """ A class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
