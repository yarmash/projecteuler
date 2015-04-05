#!/usr/bin/python

"""Problem 1: Multiples of 3 and 5"""


def arithmetic_series(first, last, terms):
    """Return the sum of the members of a finite arithmetic progression"""
    return terms * (first + last) // 2


def main():
    lim = 999
    return (arithmetic_series(3, lim-lim%3, lim//3) +
            arithmetic_series(5, lim-lim%5, lim//5) -
            arithmetic_series(15, lim-lim%15, lim//15))

if __name__ == "__main__":
    print(main())
