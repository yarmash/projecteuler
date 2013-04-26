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
