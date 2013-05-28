#!/usr/bin/python2

from projecteuler import prime_sieve

lim = 1000000
primes = prime_sieve(lim)
primes_set = frozenset(primes)


cnt, res = 21, 953

for i in xrange(len(primes)-21):
    s = primes[i]

    for k in xrange(i+1, len(primes)):
        s += primes[k]

        if s > lim: break

        if s in primes_set and k - i > cnt:
            cnt = k - i
            res = s

print res
