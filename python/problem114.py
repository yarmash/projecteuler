#!/usr/bin/python

"""Problem 114: Counting block combinations I"""

from functools import lru_cache


def main():
    length = 50

    @lru_cache(maxsize=None)
    def count(length):
        if length < 3:
            return 1

        # Consider these cases:
        # * a red block of the max length
        # * a black square at the beginning
        # * a red block followed by a black square at the beginning
        return 1 + count(length-1) + sum([count(length-n-1)
                                          for n in range(3, length)])

    return count(length)


if __name__ == "__main__":
    print(main())
