#!/usr/bin/python

"""Problem 21: Amicable numbers"""

from projecteuler import prime_sieve, sum_of_proper_divisors


def main():
    LIMIT = 10000
    primes = prime_sieve(int(LIMIT**.5))
    s = 0

    for a in range(2, LIMIT):
        b = sum_of_proper_divisors(a, primes)
        if a < b < LIMIT and sum_of_proper_divisors(b, primes) == a:
            s += a + b
    return s

if __name__ == "__main__":
    print(main())
