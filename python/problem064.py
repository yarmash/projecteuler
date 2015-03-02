#!/usr/bin/python

"""Problem 64: Odd period square roots"""

from math import sqrt
from utils import sqrt_fraction_expansion as sfe


def main():
    lim = 10000
    return sum(1 for n in range(2, lim+1) if not (sqrt(n).is_integer() or len(sfe(n)) & 1))

if __name__ == "__main__":
    print(main())
