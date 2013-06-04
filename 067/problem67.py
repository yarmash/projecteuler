#!/usr/bin/python2

import os
from projecteuler import calc_max_total

def main():
    datafile = os.path.join(os.path.dirname(__file__), "triangle.txt")
    nums = map(int, open(datafile).read().split())

    return calc_max_total(nums)

if __name__ == "__main__":
    print main()
