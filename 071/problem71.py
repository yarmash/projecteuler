#!/usr/bin/python2

"""Ordered fractions"""

from fractions import Fraction

def main():
    lim = 1000000

    def get_fraction(den):
        """Returns the largest fraction below 3/7 with the given nummerator"""
        num = (den*3-1)/7
        return Fraction(num, den)

    return max(get_fraction(i) for i in xrange(2, lim+1)).numerator

if __name__ == "__main__":
    print main()
