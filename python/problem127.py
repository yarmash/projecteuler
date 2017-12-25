#!/usr/bin/env python

"""Problem 127: abc-hits"""

from math import gcd


def main():
    lim = 120000

    rads = [1]*(lim+1)

    for i in range(2, lim+1):
        if rads[i] == 1:
            for j in range(i, lim+1, i):
                rads[j] *= i
    s = 0

    for a in range(1, lim):
        for b in range(a+1, lim-a):
            c = a + b
            if rads[a]*rads[b]*rads[c] < c and gcd(a, b) == 1:
                s += c
    return s


if __name__ == "__main__":
    print(main())
