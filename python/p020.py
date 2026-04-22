#!/usr/bin/env python3

"""Problem 20: Factorial Digit Sum"""

from math import factorial


def main():
    return sum(int(d) for d in str(factorial(100)))

if __name__ == "__main__":
    print(main())
