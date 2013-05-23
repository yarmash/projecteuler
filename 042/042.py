#!/usr/bin/python2

import os
from math import sqrt

datafile = os.path.join(os.path.dirname(__file__), "words.txt")
words = eval("["+open(datafile).read()+"]")

# if the positive triangular root n of x is an integer, then x is the nth triangular number
def is_triangular_number(n):
    r = (sqrt(8*n +1) - 1)/2
    return r.is_integer()

cnt = 0

for word in words:
    if is_triangular_number(sum([ ord(c)-64 for c in word ])):
        cnt += 1

print cnt
