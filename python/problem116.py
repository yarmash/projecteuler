#!/usr/bin/python

"""Problem 116: Red, green or blue tiles"""

from utils import n_choose_k


def count(row_len, tile_len):
    ways = 0

    for ntiles in range(1, row_len//tile_len + 1):
        total_tiles = ntiles + (row_len - ntiles*tile_len)
        ways += n_choose_k(total_tiles, ntiles)
    return ways


def main():
    row_len = 50

    return sum([count(row_len, tile_len) for tile_len in (2, 3, 4)])


if __name__ == "__main__":
    print(main())
