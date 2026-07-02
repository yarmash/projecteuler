#!/usr/bin/env python3

"""Problem 65: Convergents of e"""

from itertools import repeat

from utils import convergent_fractions, sum_digits


def main():
    # e = [2; 1,2,1, 1,4,1, 1,6,1, ...]
    def quotients():
        k = 2
        yield k

        while True:
            yield from [1, k, 1]
            k += 2

    convergents = convergent_fractions(quotients())

    for _ in repeat(None, 100):
        num = next(convergents)[0]

    return sum_digits(num)


if __name__ == "__main__":
    print(main())
