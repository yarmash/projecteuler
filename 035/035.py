#!/usr/bin/python2

from projecteuler import prime_sieve

def rotations(n):
    k = 5 if 100000 < n < 1000000 else \
        4 if 10000 < n < 100000 else \
        3 if 1000 < n < 10000 else \
        2 if 100 < n < 1000 else \
        1 if 10 < n < 100 else \
        0

    for i in range(k+1):
        n = 10**k*(n % 10) + n/10
        yield n

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
