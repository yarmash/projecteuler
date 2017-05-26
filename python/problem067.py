#!/usr/bin/python

"""Problem 67: Maximum path sum II"""

from utils import get_path

# This is a more difficult version of Problem 18.
import problem018


def main():
    with get_path("data", "triangle.txt").open() as data_file:
        triangle = [[int(d) for d in line.split()] for line in data_file]

    return problem018.main(triangle)


if __name__ == "__main__":
    print(main())
