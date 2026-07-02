#!/usr/bin/env python3

"""Problem 56: Powerful Digit Sum"""

from utils import sum_digits


def main():
    res = 0

    for a in range(90, 100):
        for b in range(90, 100):
            dsum = sum_digits(a**b)
            if dsum > res:
                res = dsum
    return res


if __name__ == "__main__":
    print(main())
