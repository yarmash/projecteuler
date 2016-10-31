#!/usr/bin/python

"""Problem 114: Counting block combinations I"""

from functools import lru_cache


@lru_cache(maxsize=None)
def count(length, minlen):
    """
    Return the number of ways a row of `length` units in length can be filled.

    :param int length: The row length.
    :param int minlen: The minimum length of a red block.
    """
    if length < minlen:
        return 1

    # Consider these cases:
    # * A red block of the max length
    # * A black square at the beginning
    # * A red block followed by a black square at the beginning
    return (1 + count(length-1, minlen) +
            sum([count(length-m-1, minlen) for m in range(minlen, length)]))


def main():
    length, minlen = 50, 3
    return count(length, minlen)

if __name__ == "__main__":
    print(main())
