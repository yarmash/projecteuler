#!/usr/bin/env python3

"""Problem 134: Prime Pair Connection"""

from itertools import pairwise
from math import ceil, log10

from utils import prime_sieve_lazy


def main():
    lim = 1_000_000
    primes = prime_sieve_lazy()
    next(primes)
    next(primes)
    res = 0

    # p1 + d * k == 0 (mod p2).
    for p1, p2 in pairwise(primes):
        if p1 > lim:
            break
        d = 10**(ceil(log10(p1)))
        dinv = pow(d, p2 - 2, p2)
        k = ((p2 - p1) * dinv) % p2
        res += p1 + d * k

    return res


if __name__ == "__main__":
    print(main())
