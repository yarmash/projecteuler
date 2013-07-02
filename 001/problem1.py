#!/usr/bin/python2

"""Problem 1: Multiples of 3 and 5"""

def sum_divisible_by(n, limit=1000):
    k = (limit - 1) / n
    s = (n*(1+k)*k)/2
    return s

def main():
    return sum_divisible_by(5) + sum_divisible_by(3) - sum_divisible_by(15)


if __name__ == "__main__":
    print main()
