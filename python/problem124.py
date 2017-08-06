#!/usr/bin/env python

"""Problem 124: Ordered radicals"""

from functools import reduce
from math import sqrt

from utils import prime_sieve, prime_factors


def main():
    lim = 100_000

    primes = prime_sieve(int(sqrt(lim)))

    def rad(n):
        """
        Calculates the radical of n, i.e. the product of distinct
        prime factors of n.
        """
        factors = prime_factors(n, primes)
        return reduce(lambda x, y: x*y[0], factors, 1)

    return sorted(range(1, lim+1), key=rad)[9999]


if __name__ == "__main__":
    print(main())
