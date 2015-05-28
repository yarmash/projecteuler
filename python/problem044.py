#!/usr/bin/python

"""Problem 44: Pentagon numbers"""

from itertools import count
from utils import is_pentagonal, nth_pentagonal as P


def main():
    # P(n+k)-P(n) = 3kn + P(k), P(n+k)-P(n) = P(m)
    for m in count(1):
        for k in range(1, m):
            n, mod = divmod(P(m) - P(k), 3*k)
            if not mod and is_pentagonal(P(n+k) + P(n)):
                return P(m)

if __name__ == "__main__":
    print(main())
