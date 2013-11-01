#!/usr/bin/python

"""Problem 42: Coded triangle numbers"""

import os
from math import sqrt

# if the positive triangular root n of x is an integer, then x is the nth triangular number
def is_triangular_number(n):
    r = (sqrt(8*n +1) - 1)/2
    return r.is_integer()

def main():
    datafile = os.path.join(os.path.dirname(__file__), "words.txt")
    words = eval("["+open(datafile).read()+"]")

    cnt = 0

    for word in words:
        if is_triangular_number(sum([ ord(c)-64 for c in word ])):
            cnt += 1

    return cnt

if __name__ == "__main__":
    print(main())
