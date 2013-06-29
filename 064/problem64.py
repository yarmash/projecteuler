#!/usr/bin/python2

"""Problem 64: Odd period square roots"""

from math import sqrt

# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
def continued_fraction(num):
    m = 0
    d = 1
    a0 = a = int(sqrt(num))

    fraction = []

    while a != 2*a0:
        m = d*a - m
        d = (num - m*m)/d
        a = (a0 + m)/d
        fraction.append(a)

    return fraction


def main():
    res = 0
    lim = 10000

    for num in xrange(2, lim+1):
        if not sqrt(num).is_integer() and len(continued_fraction(num)) & 1:
            res += 1
    return res


if __name__ == "__main__":
    print main()
