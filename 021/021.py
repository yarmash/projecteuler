#!/usr/bin/python2

from projecteuler import factor, memoize

@memoize
def sum_proper_divisors(n):
    return sum(factor(n)) - n

s = 0

for a in range(2, 10000):
    b = sum_proper_divisors(a)
    if a < b < 9999 and sum_proper_divisors(b) == a:
        s += a + b

print s
