#!/usr/bin/env python

"""Problem 127: abc-hits"""

from functools import lru_cache, reduce
from math import gcd
from operator import itemgetter, mul

from utils import prime_factors, prime_sieve


def main():
    lim = 120000
    primes = prime_sieve(int(lim**.5))

    @lru_cache(maxsize=None)
    def rad(n, primes=primes):
        return reduce(mul, frozenset(
            map(itemgetter(0), prime_factors(n, primes))), 1)

    s = 0

    for a in range(1, lim):
        for b in range(a+1, lim-a):
            c = a + b
            if gcd(a, b) == 1 and rad(a)*rad(b)*rad(c) < c:
                s += c
    return s


if __name__ == "__main__":
    print(main())
