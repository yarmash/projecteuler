#!/usr/bin/env python

"""Problem 129: Repunit divisibility"""

from itertools import count
from math import gcd


def main():
    lim = 10

    def R(k):  # R(6) = 111111
        return (10**k-1)//9

    for n in count(3):
        if not gcd(n, 10) == 1:
            continue

        for k in count(2):
            r = R(k)

            print(n, k, r)

            if not r % n:
                if k > lim:
                    return n
                break

if __name__ == "__main__":
    print(main())
