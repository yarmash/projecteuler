#!/usr/bin/python

"""Problem 1: Multiples of 3 and 5"""

def sum_divisible_by(d, lim=999):
    """Return the sum of the numbers <= lim that are divisible by d"""
    n = lim // d
    return (d + n*d)*n >> 1

def main():
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)


if __name__ == "__main__":
    print(main())
