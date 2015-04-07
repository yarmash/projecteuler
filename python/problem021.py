#!/usr/bin/python

"""Problem 21: Amicable numbers"""

from utils import pdsums_sieve


def main():
    limit = 10000
    dsums = pdsums_sieve(limit)
    asum = 0

    for i in range(2, limit):
        if dsums[i] < limit and i != dsums[i] and i == dsums[dsums[i]]:
            asum += i + dsums[i]

            dsums[dsums[i]] = 0
    return asum

if __name__ == "__main__":
    print(main())
