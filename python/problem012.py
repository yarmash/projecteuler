#!/usr/bin/env python

"""Problem 12: Highly divisible triangular number"""

from utils import prime_sieve
from itertools import count
from functools import lru_cache


@lru_cache(maxsize=None)
def num_of_divisors(num, primes=prime_sieve(1000)):
    """Returns the number of divisors of an integer"""
    cnt = 1

    for p in primes:
        if p*p > num:
            cnt *= 2
            break
        exponent = 1
        while num % p == 0:
            exponent += 1
            num //= p
        cnt *= exponent

        if num == 1:
            break
    return cnt


def main():
    for n in count(1):
        divisors = (num_of_divisors((n+1)//2) * num_of_divisors(n) if n & 1
                    else num_of_divisors(n//2) * num_of_divisors(n+1))

        if divisors >= 500:
            return n*(n + 1) >> 1

if __name__ == "__main__":
    print(main())
