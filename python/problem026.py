#!/usr/bin/python

"""Problem 26: Reciprocal cycles"""

from utils import prime_factors, is_prime


def is_primitive_root(k, n):
    factors = prime_factors(n-1)

    for f in factors:
        if pow(k, (n-1)//f[0], n) <= 1:
            return False

    return True

def main():
    for n in range(999, 1, -2):
        if is_prime(n) and is_primitive_root(10, n):
            return n

if __name__ == "__main__":
    print(main())
