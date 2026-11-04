#!/usr/bin/env python3

"""Problem 121: Disc Game Prize Fund"""

from itertools import combinations
from math import factorial, prod


def main():
    turns = 15
    prob = sum(map(prod, (*combinations(range(1, turns+1), n)
                          for n in range((turns+1)//2))))
    return factorial(turns+1) // prob


if __name__ == "__main__":
    print(main())
