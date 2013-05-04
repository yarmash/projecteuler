#!/usr/bin/python2

from projecteuler import sum_of_proper_divisors

MAX = 28123
a_numbers = [ i for i in xrange(12, MAX+1) if sum_of_proper_divisors(i) > i ]
a_numbers_set = frozenset(a_numbers)

def not_sum(n):
    lim = n/2

    for a in a_numbers:
        if a > lim:
            break

        if n - a in a_numbers_set:
            return False

    return True


print sum(filter(not_sum, xrange(MAX, 0, -1)))
