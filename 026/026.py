#!/usr/bin/python2

from projecteuler import prime_factors, is_prime

def is_primitive_root(k, n):
    factors = prime_factors(n-1)

    for f in factors:
        if k**((n-1)/f[0]) % n <= 1:
            return False

    return True


for n in xrange(1000, 1, -1):
    if is_prime(n) and is_primitive_root(10, n):
        print n
        break
