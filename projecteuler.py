#!/usr/bin/python2
# coding=utf-8

from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    elif n < 4:
        return True # 2 and 3 are prime
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True # we have already excluded 4, 6 and 8
    elif n % 3 == 0:
        return False
    else:
        limit = int(sqrt(n))
        k = 5
        while k <= limit: # check through all the numbers of the form 6k ± 1
            if n % k == 0:
                return False
            if n % (k+2) == 0:
                return False
            k += 6

        return True


def primes(n): # implements The Sieve of Eratosthenes
    bound = (n-1)/2 # last index of the sieve

    sieve = [True]*(bound+1)

    for i in xrange(1, int(sqrt(n)/2)+1):
        if sieve[i]: # 2*i+1 is a prime, mark multiples
            for j in xrange(2*i*(i+1), bound+1, 2*i+1):
                sieve[j] = False
    primes = [2]
    for i in xrange(1, bound+1):
        if sieve[i]:
            primes.append(2*i+1)
    return primes
