#!/usr/bin/python2

"""Problem 41: Pandigital prime"""

from itertools import permutations
from projecteuler import is_prime, is_pandigital


def main():
    digits = (7, 6, 5, 4, 3, 2, 1)

    for ndigits in [7, 4]: # only 7 or 4 digit numbers need to be considered (in other cases the sum is divisible by 3)
        for p in permutations(digits[7-ndigits:], ndigits):
            n = 0
            for i in xrange(ndigits):
                n += 10**(ndigits-i-1)*p[i]

            if is_pandigital(n, ndigits) and is_prime(n):
                return n

if __name__ == "__main__":
    print main()
