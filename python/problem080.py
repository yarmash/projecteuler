#!/usr/bin/python

"""Problem 80: Square root digital expansion"""

from utils import isqrt


def main():

    total = 0

    for num in range(2, 100):
        if num not in {4, 9, 16, 25, 36, 49, 64, 81}:
            root = isqrt(num * (10**2)**99)
            total += sum([int(x) for x in str(root)])
    return total

if __name__ == "__main__":
    print(main())
