#!/usr/bin/python

"""Problem 86: Cuboid route"""

from math import sqrt
from itertools import count


def main():
    cnt = 0
    for a in count(1):
        for s in range(2, 2*a+1):
            if sqrt(a*a + s*s).is_integer():
                cnt += min(s, a+1) - (s+1)//2

        if cnt > 1000000:
            return a


if __name__ == "__main__":
    print(main())
