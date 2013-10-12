#!/usr/bin/python2

"""Counting summations"""

from projecteuler import memoize

def main():

    @memoize
    def count(k, n):

        if k == n or n == 0: return 1
        if k > n: return 0

        cnt = 0

        while n >= 0:
            cnt += count(k+1, n)
            n -= k

        return cnt

    return count(1, 100) - 1


if __name__ == "__main__":
    print main()
