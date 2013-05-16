#!/usr/bin/python2

from projecteuler import prime_sieve

def rotations(p):
    if p < 10:
        yield p
    else:
        m = 0
        t = p
        while t / 10:
            m += 1
            t /= 10

        yield p

        for i in range(m):
            p = (10**m)*(p % 10) + p/10
            yield p

primes = prime_sieve(1000000)
primes_set = set(primes)

cnt = 0

for p in primes:
    for r in rotations(p):
        if not r in primes_set:
            break
    else:
        cnt += 1

print cnt
