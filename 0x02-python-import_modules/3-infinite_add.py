#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    tot = 0
    for s in argv[1:]:
        tot += int(s)
    print("{:d}".format(tot))
