#!/usr/bin/python2

from itertools import permutations
from projecteuler import is_prime, is_pandigital


digits = "987654321"

def largest_prime():
    for i in [7, 4]: # only 7 or 4 digit numbers need to be considered (in other cases the sum is divisible by 3)
        for p in permutations(digits[9-i:], i):
            p = int("".join(p))

            if is_pandigital(p, i) and is_prime(p):
                return p
print largest_prime()
