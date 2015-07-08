#!/usr/bin/python

"""Problem 106: Special subset sums: meta-testing"""

from itertools import chain, combinations


def main():
    s = list(range(1, 13))

    cnt = 0

    for pair in combinations(chain.from_iterable(
            [combinations(s, r) for r in range(2, len(s)//2+1)]), 2):

        if len(pair[0]) != len(pair[1]):
            continue
        if set(pair[0]) & set(pair[1]):
            continue
        if all(pair[0][i] < pair[1][i] for i in range(len(pair[0]))):
            continue

        cnt += 1
    return cnt

if __name__ == "__main__":
    print(main())
