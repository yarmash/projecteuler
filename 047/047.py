#!/usr/bin/python2

from math import sqrt

lim = 1000000
sieve = [0]*lim

for i in range(2, int(sqrt(lim))+1):
    if not sieve[i]: # prime
        for k in range(i+i, lim-lim%i, i):
            sieve[k] += 1

for i in range(2, len(sieve)-5):
    if sieve[i:i+4] == [4,4,4,4]:
        print i
        break
