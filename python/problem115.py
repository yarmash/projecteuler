#!/usr/bin/python

"""Problem 115: Counting block combinations II"""

import itertools

from problem114 import count


def main():
    minlen = 50

    for length in itertools.count(minlen):
        if count(length, minlen) > 1000000:
            return length


if __name__ == "__main__":
    print(main())
