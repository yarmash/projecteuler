#!/usr/bin/python2

"""Problem 21: Amicable numbers"""

from projecteuler import sum_of_proper_divisors

def main():
    s = 0

    for a in xrange(2, 10000):
        b = sum_of_proper_divisors(a)
        if a < b < 9999 and sum_of_proper_divisors(b) == a:
            s += a + b

    return s

if __name__ == "__main__":
    print main()
