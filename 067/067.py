#!/usr/bin/python2

import os
from projecteuler import calc_max_total

datafile = os.path.join(os.path.dirname(__file__), "triangle.txt")
nums = map(int, open(datafile).read().split())

print calc_max_total(nums)
