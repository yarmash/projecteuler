#!/usr/bin/python2

from projecteuler import sum_of_proper_divisors

s = 0

for a in range(2, 10000):
    b = sum_of_proper_divisors(a)
    if a < b < 9999 and sum_of_proper_divisors(b) == a:
        s += a + b

print s
