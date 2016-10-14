#!/usr/bin/python

"""Problem 22: Names scores"""

import string

from utils import open_data_file


def main():
    with open_data_file("names.txt") as data_file:
        names = data_file.read().split('","')
    names[0] = names[0][1:]
    names[-1] = names[-1][:-1]
    names.sort()

    values = {c: i for i, c in enumerate(string.ascii_uppercase, 1)}

    return sum([sum([values[c] for c in name]) * pos
                for pos, name in enumerate(names, 1)])

if __name__ == "__main__":
    print(main())
