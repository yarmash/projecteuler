#!/usr/bin/env python

"""Problem 24: Lexicographic permutations"""

from math import factorial


def main():
    def nthPerm(s, n):
        if len(s) < 2:
            return s
        quot, n = divmod(n, factorial(len(s)-1))
        return s[quot] + nthPerm(s[:quot] + s[quot+1:], n)

    return nthPerm('0123456789', 999999)

if __name__ == "__main__":
    print(main())
