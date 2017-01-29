#!/usr/bin/python

"""Problem 117: Red, green, and blue tiles"""

from functools import lru_cache


@lru_cache(maxsize=None)
def count(row_len):
    if row_len < 0:
        return 0
    if row_len < 2:
        return 1
    return sum([count(row_len - tile_len) for tile_len in (1, 2, 3, 4)])


def main():
    row_len = 50
    return count(row_len)


if __name__ == "__main__":
    print(main())
