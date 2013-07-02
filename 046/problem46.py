#!/usr/bin/python2

"""Problem 46: Goldbach's other conjecture"""

from projecteuler import is_prime
from math import sqrt


def main():
    primes = []
    n = 3

    while True:
        if is_prime(n):
            primes.append(n)
        else:
            if all(not sqrt((n - p)/2).is_integer() for p in primes):
                return n
        n += 2

if __name__ == "__main__":
    print main()
