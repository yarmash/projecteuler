#!/usr/bin/python2

import os
from projecteuler import memoize

datafile = os.path.join(os.path.dirname(__file__), "triangle.txt")
nums = map(int, open(datafile).read().split())

@memoize
def calc_total(rownum, idx):
    # the index is calculated using the formula for the sum of the members of an arithmetic progression
    n = nums[ ((1 + (rownum-1))*(rownum-1))/2 + idx ]

    return n if rownum == 100 else n + max(calc_total(rownum+1, idx), calc_total(rownum+1, idx+1))

print calc_total(1, 0)
