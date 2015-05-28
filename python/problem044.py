#!/usr/bin/python

"""Problem 44: Pentagon numbers"""

from utils import is_pentagonal


def main():

    pentagonals = []
    pset = set()
    min_diff = float("inf")
    p = diff = 1

    while True:
        diff += 3  # the difference increases by 3
        p += diff

        if not p & 1:  # both numbers must be even
            for i, v in enumerate(reversed(pentagonals)):
                d = p - v
                if d > min_diff:
                    break

                if d in pset and is_pentagonal(p + v):
                    if d < min_diff:
                        min_diff = d
            pentagonals.append(p)
            pset.add(p)

        if diff > min_diff:
            break

    return min_diff

if __name__ == "__main__":
    print(main())
