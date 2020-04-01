#!/usr/bin/env python

"""Problem 106: Special subset sums: meta-testing"""

from math import comb


def nth_catalan_number(n):
    """
    Return the nth Catalan number
    https://en.wikipedia.org/wiki/Catalan_number
    """
    return comb(2*n, n) // (n + 1)


def main():
    n = 12
    return sum(
        # the catalan numbers specify subsets that don't need to be tested
        [comb(n, 2*i) * (comb(2*i, i)//2 - nth_catalan_number(i))
         for i in range(2, n//2+1)])


if __name__ == '__main__':
    print(main())
