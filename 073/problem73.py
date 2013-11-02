#!/usr/bin/python

"""Problem 73: Counting fractions in a range"""

import sys
sys.setrecursionlimit(10000)

def main():
    def count(n, left, right):
        med = left + right
        if med > n:
            return 0
        return 1 + count(n, left, med) + count(n, med, right)

    return count(12000, 3, 2)


if __name__ == "__main__":
    print(main())
