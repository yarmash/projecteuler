#!/usr/bin/env python

"""Problem 130: Composites with prime repunit property"""

from itertools import count
from math import log10, ceil

from utils import is_prime


def main():
    composites = []

    for n in count(9, 2):
        if n % 5 and not is_prime(n):
            k = ceil(log10(n*3))
            r = (10**k-1)//9

            while r:
                r = (r*10 + 1) % n
                k += 1

            if not (n - 1) % k:
                composites.append(n)
                if len(composites) == 25:
                    return sum(composites)


if __name__ == "__main__":
    print(main())
