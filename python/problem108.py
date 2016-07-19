#!/usr/bin/python

"""Problem 108: Diophantine reciprocals I"""

from itertools import count
from utils import prime_factors, prime_sieve

# the number of distinct solutions for 1/x +1/y = 1/n is (d(n^2)+1)/2 where
# d(x) is the number of positive divisors of x.


def num_of_solutions(n, primes=prime_sieve(10000)):
    factors = prime_factors(n, primes)
    d = 1

    for prime, exponent in factors:
        d *= exponent*2 + 1
    return (d + 1) // 2


def main():
    for n in count(1):
        solutions = num_of_solutions(n)
        if solutions > 1000:
            return n


if __name__ == "__main__":
    print(main())
