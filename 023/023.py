#!/usr/bin/python2

from projecteuler import factor


def get_abundant_numbers(limit):
    an = []

    for i in xrange(1, limit+1):
        if sum(factor(i)) - i > i:
            an.append(i)
    return an

def is_sum_of_an(n, an, an_dict):

    for a in an:
        if a >= n:
            break
        a2 = n - a

        if a2 in an_dict:
            return True

    return False


max = 28123
an = get_abundant_numbers(max)
an_dict = {}
for n in an:
    an_dict[n] = True

s = 0

for i in xrange(max, 0, -1):
    if not is_sum_of_an(i, an, an_dict):
        s += i

print s
