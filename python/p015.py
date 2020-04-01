#!/usr/bin/env python3

"""Problem 15: Lattice paths"""

from math import comb


def main():
    size = 20
    return comb(size+size, size)


if __name__ == '__main__':
    print(main())
