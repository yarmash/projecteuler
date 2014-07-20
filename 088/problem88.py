#!/usr/bin/python

"""Problem 88: Product-sum numbers"""

from functools import reduce
from operator import mul
from itertools import count
from math import ceil, sqrt


def main():
    # the minimal product-sum for some k is between k and 2k

    min_product_sums = [float("inf")]*12001
    min_product_sums[0:2] = 0, 0

    factors = [[i] for i in range(2, ceil(sqrt(24000)))]

    # generate combinations of factors in nondecreasing order
    while factors:
        f = factors.pop()
        product_sum = reduce(mul, f)
        k = (product_sum-sum(f)) + len(f)
        if k <= 12000 and product_sum < min_product_sums[k]:
            min_product_sums[k] = product_sum

        for i in count(f[-1]):
            if product_sum*i > 24000:
                break
            factors.append(f + [i])

    return sum(set(min_product_sums))


if __name__ == "__main__":
    print(main())
