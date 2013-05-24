#!/usr/bin/python2

from projecteuler import prime_factors

n, count = 2*3*5*7, 0

while count < 4:
    factors = prime_factors(n)

    if len(factors) == 4:
        count += 1
    else:
        count = 0
    n += 1

print n - count
