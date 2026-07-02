#!/usr/bin/env python3

"""Problem 33: Digit Cancelling Fractions"""

from fractions import Fraction
from math import prod


def main():
    # the numbers need to be of the form AX/XB (e.g. 49/98): cancelling
    # a shared tens or units digit forces a == b, so no other form works
    return prod(
        Fraction(a, b)
        for a in range(10, 100)
        for b in range(a + 1, 100)
        if a % 10 == b // 10 and a * (b % 10) == b * (a // 10)  # a/b = c/d === a*d = b*c
    ).denominator


if __name__ == "__main__":
    print(main())
