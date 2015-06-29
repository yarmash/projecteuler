#!/usr/bin/python

"""Problem 41: Pandigital prime"""

from itertools import permutations
from utils import is_prime, is_pandigital


def main():
    digits = "987654321"

    # only 7- or 4-digit numbers need to be considered
    # in other cases the sum is divisible by 3
    for ndigits in (7, 4):
        for p in permutations(digits[-ndigits:], ndigits):
            n = int("".join(p))

            if is_pandigital(n, ndigits) and is_prime(n):
                return n

if __name__ == "__main__":
    print(main())
