#!/usr/bin/python

"""Problem 106: Special subset sums: meta-testing"""

from itertools import combinations


def main():
    s = set(range(1, 13))
    pairs = 0

    for i in range(2, len(s)//2+1):
        for a in combinations(s, i):
            for b in combinations(s - set(a), i):
                if a < b and any(x > y for x, y in zip(a, b)):
                    pairs += 1
    return pairs

if __name__ == "__main__":
    print(main())
