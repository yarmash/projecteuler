#!/usr/bin/python2

"""Problem 47: Distinct primes factors"""

from math import sqrt

def main():
    lim = 1000000
    sieve = [0]*lim

    for i in xrange(2, int(sqrt(lim))+1):
        if not sieve[i]: # prime
            for k in xrange(i+i, lim, i):
                sieve[k] += 1
    l = [4]*4
    for i in xrange(2, len(sieve)-4):
        if sieve[i:i+4] == l:
            return i

if __name__ == "__main__":
    print main()
