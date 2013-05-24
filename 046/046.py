#!/usr/bin/python2

from projecteuler import is_prime
from math import sqrt


def find_number():
    primes = []
    n = 3

    while True:
        if is_prime(n):
            primes.append(n)
        else:
            for p in primes:
                if p > n or sqrt((n - p)/2).is_integer():
                    break
            else:
                return n
        n += 2

print find_number()
