#!/usr/bin/python2

from itertools import permutations
from projecteuler import is_prime, is_pandigital


digits = (7, 6, 5, 4, 3, 2, 1)

def largest_prime():
    for ndigits in [7, 4]: # only 7 or 4 digit numbers need to be considered (in other cases the sum is divisible by 3)
        for p in permutations(digits[7-ndigits:], ndigits):
            n = 0
            for i in range(ndigits):
                n += 10**(ndigits-i-1)*p[i]

            if is_pandigital(n, ndigits) and is_prime(n):
                return n
print largest_prime()
