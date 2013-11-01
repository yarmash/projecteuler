#!/usr/bin/python

"""Problem 49: Prime permutations"""

from projecteuler import is_permutation, prime_sieve

def main():
    primes = [ x for x in prime_sieve(10000) if x > 1000 and x != 1487 and x != 4817 and x != 8147 ]
    primes_set = frozenset(primes)

    for i in range(len(primes)-1, 1, -1):
        for j in range(i-1):
            c = primes[i]
            a = primes[j]
            b = (c + a) >> 1

            if b in primes_set and is_permutation(a, b) and is_permutation(b, c):
                return str(a)+str(b)+str(c)

if __name__ == "__main__":
    print(main())
