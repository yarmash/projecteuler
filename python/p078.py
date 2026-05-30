#!/usr/bin/env python3

"""Problem 78: Coin Partitions"""

from itertools import count

MOD = 1_000_000


# Euler's pentagonal-number recurrence for the partition function:
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)#Recurrence_relations
def main():
    partitions = [1]

    for n in count(1):
        total = 0

        for k in count(1):
            sign = 1 if k % 2 else -1

            p1 = k * (3*k - 1) // 2
            if p1 > n:
                break
            total += sign * partitions[n - p1]

            p2 = k * (3*k + 1) // 2
            if p2 <= n:
                total += sign * partitions[n - p2]

        # Only divisibility by MOD matters, so keep every partition value modulo MOD
        total %= MOD

        if not total:
            return n

        partitions.append(total)


if __name__ == "__main__":
    print(main())
