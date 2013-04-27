#!/usr/bin/python2

from math import log, sqrt
from projecteuler import primes

n = 20

primes = primes(n) # prime numbers <= N

limit = sqrt(n)
result = 1

for p in primes:
    exponent = 1 if p > limit else int(log(n)/log(p))
    result *= p ** exponent

print result
