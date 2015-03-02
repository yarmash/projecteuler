#!/usr/bin/python

"""Problem 44: Pentagon numbers"""

from utils import is_pentagonal, nth_pentagonal


def main():
    diffs = []

    mindiff, diff, n = 0, 1, 1

    while mindiff < diff:
        n += 1
        diff += 3 # the difference increases by 3

        diffs.append(0)

        for i in range(len(diffs)):
            diffs[i] += diff

            if n != (i+1) and is_pentagonal(diffs[i]):
                if is_pentagonal(nth_pentagonal(i+1) + nth_pentagonal(n)):
                    mindiff = min(mindiff, diffs[i]) if mindiff else diffs[i]
    return mindiff

if __name__ == "__main__":
    print(main())
