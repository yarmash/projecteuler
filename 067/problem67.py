#!/usr/bin/python

"""Problem 67: Maximum path sum II"""

import sys
import os
from projecteuler import open_data_file

# This is a more difficult version of Problem 18 and uses the same function.
try:
    import problem18
except ImportError:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "018"))
    import problem18
    del sys.path[0]


def main():
    nums = [[int(d) for d in line.split()]
        for line in open_data_file("triangle.txt")]

    return problem18.calc_max_total(nums)

if __name__ == "__main__":
    print(main())
