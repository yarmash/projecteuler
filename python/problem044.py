#!/usr/bin/python

"""Problem 44: Pentagon numbers"""

from itertools import count
from utils import is_pentagonal, nth_pentagonal as P


def main():
    # P(n+k)-P(n) = 3kn + P(k), P(n+k)-P(n) = P(m)
    for m in count(1):
        pm = P(m)
        for k in range(1, m):
            n, mod = divmod(pm - P(k), 3*k)
            if not mod and is_pentagonal(pm + 2*P(n)):
                return pm

if __name__ == "__main__":
    print(main())
