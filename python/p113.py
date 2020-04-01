#!/usr/bin/env python3

"""Problem 113: Non-bouncy numbers"""

from math import comb


def main():
    ndigits = 100
    # numbers of combinations w/ replacement = (n + k - 1)! / k!(n - 1)!
    return sum([comb(9+k, k) + comb(8+k, k)
                for k in range(1, ndigits+1)]) - 10*ndigits


if __name__ == '__main__':
    print(main())
