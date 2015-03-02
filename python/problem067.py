#!/usr/bin/python

"""Problem 67: Maximum path sum II"""

from utils import open_data_file

# This is a more difficult version of Problem 18 and uses the same function.
from problem018 import calc_max_total


def main():
    with open_data_file("triangle.txt") as data_file:
        nums = [[int(d) for d in line.split()] for line in data_file]

    return calc_max_total(nums)

if __name__ == "__main__":
    print(main())
