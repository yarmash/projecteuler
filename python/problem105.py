#!/usr/bin/python

"""Problem 105: Special subset sums: testing"""

from utils import open_data_file
from problem103 import is_special_sum_set


def main():
    with open_data_file("sets.txt") as data_file:
        sets = [[int(x) for x in line.split(",")] for line in data_file]
        return sum([sum(s) for s in sets if is_special_sum_set(s)])

if __name__ == "__main__":
    print(main())
