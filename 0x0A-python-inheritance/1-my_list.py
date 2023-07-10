#!/usr/bin/python3
class MyList(list):
    """ A class that inherits the attributes references of class list

    Args:
        list: class list

    """

    def print_sorted(self):
        """ Method that prints sorted list """
        ltsorted = self.copy()
        lst_sorted.sort()
        print(lst_sorted)
