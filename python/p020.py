#!/usr/bin/env python3

"""Problem 20: Factorial Digit Sum"""

from math import factorial

from utils import sum_digits


def main():
    return sum_digits(factorial(100))


if __name__ == "__main__":
    print(main())
