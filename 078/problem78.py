#!/usr/bin/python

"""Problem 78: Coin partitions"""

from itertools import count

def main():

    def pentagonal_numbers():
        #yield 0
        for n in count(1):
            yield n*(3*n-1) >> 1
            yield (-n)*(3*(-n)-1) >> 1


    memo = { 0: 1, 1: 1 }

    def p(n):
        if n in memo:
            return memo[n]

        partition = 0

        for i, pent in enumerate(pentagonal_numbers()):

            if pent > n:
                break

            sign = 1 if ((i+2) >> 1) & 1 else -1

            partition += sign*p(n-pent)

        memo[n] = partition
        return partition

    for i in count():
        if not p(i) % 1000000:
            return i


if __name__ == "__main__":
    print(main())
