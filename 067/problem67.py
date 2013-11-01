#!/usr/bin/python

"""Problem 67: Maximum path sum II"""

import sys
from os.path import join, dirname

# This is a more difficult version of Problem 18 and uses the same function.
try:
    import problem18
except ImportError:
    sys.path.insert(0, join(dirname(__file__), "..", "018"))
    import problem18
    sys.path.pop(0)


def main():
    datafile = join(dirname(__file__), "triangle.txt")
    nums = [ int(d) for d in open(datafile).read().split() ]

    return problem18.calc_max_total(nums)

if __name__ == "__main__":
    print(main())
