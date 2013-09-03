#!/usr/bin/python2

"""Totient permutation"""

from projecteuler import prime_sieve, is_permutation
from itertools import combinations

def main():
    lim = 10000000
    res, num = float("inf"), None
    primes = prime_sieve(2*int(lim**.5))

    for x, y in combinations(primes, 2):
        if x*x > lim:
            break
        n = x*y
        if n > lim:
            continue
        phi = (x-1)*(y-1)

        if is_permutation(n, phi):
            if res > n*1.0/phi:
                res = n*1.0/phi
                num = n
    return num


if __name__ == "__main__":
    print main()
