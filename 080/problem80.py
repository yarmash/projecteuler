#!/usr/bin/python

"""Problem 80: Square root digital expansion"""

from math import sqrt

def main():
    # http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Babylonian_method

    squares = {x*x for x in range(1, 11)}
    res = 0

    for num in (x for x in range(1, 101) if not x in squares):
        num *= 10**200
        root = int(sqrt(num))

        while True:
            new = (root + num//root) >> 1
            if new == root:
                break
            root = new

        res += sum(int(x) for x in ("%i" % root)[:100])
    return res


if __name__ == "__main__":
    print(main())
