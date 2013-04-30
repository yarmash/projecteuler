#!/usr/bin/python2

from math import sqrt

def factor(n):
    factors = set()

    for i in range(1, int(sqrt(n))+1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
    return factors

def memoize(fn):
    cache = [None]*10000

    def memoized(n):
        if not cache[n]:
            cache[n] = fn(n)
        return cache[n]

    return memoized

@memoize
def sum_proper_divisors(n):
    return sum(factor(n)) - n

s = 0

for a in range(2, 10000):
    b = sum_proper_divisors(a)
    if a < b < 9999 and sum_proper_divisors(b) == a:
        s += a + b

print s
