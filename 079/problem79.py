#!/usr/bin/python

"""Problem 79: Passcode derivation"""

from projecteuler import data_file


def main():
    with open(data_file("keylog.txt")) as f:
        keys = [line.rstrip() for line in f]

    # dict storing numbers that appear before a given number
    preceding = {c: set() for c in {x for key in keys for x in key}}

    for key in keys:
        preceding[key[1]].add(key[0])
        preceding[key[2]].add(key[1])
        preceding[key[2]].add(key[0])

    return "".join(sorted(preceding, key=preceding.get))


if __name__ == "__main__":
    print(main())
