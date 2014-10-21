#!/usr/bin/python

"""Problem 22: Names scores"""

from projecteuler import open_data_file

def main():
    names = open_data_file("names.txt").read().split(",")
    names.sort()
    s = 0

    for pos, name in enumerate(names, 1):
        s += sum([ord(c) - 64 for c in name if c != '"']) * pos

    return s

if __name__ == "__main__":
    print(main())
