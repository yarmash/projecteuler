#!/usr/bin/env python

"""Problem 86: Cuboid route"""

from itertools import count
from math import hypot


def main():
    cnt = 0
    for a in count(1):
        for s in range(2, 2*a+1):
            if hypot(a, s).is_integer():
                cnt += min(s, a+1) - (s+1)//2

        if cnt > 1000000:
            return a


if __name__ == "__main__":
    print(main())
