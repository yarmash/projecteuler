#!/usr/bin/python

"""Problem 88: Product-sum numbers"""

from functools import reduce
from operator import mul
from itertools import product
from projecteuler import prime_factors


def generate_factorizations(exponents, start):
    if sum(exponents) == 0:
        yield []
    else:
        for p in product(*(range(e+1) for e in exponents)):
            if p >= start:
                remainder = [x - y for x, y in zip(exponents, p)]
                for f in generate_factorizations(remainder, p):
                    yield [p] + f


def factorizations(n):
    factors = prime_factors(n)
    primes = [x[0] for x in factors]
    exponents = [x[1] for x in factors]

    for f in generate_factorizations(exponents, (0,)*(len(exponents)-1) + (1,)):
        yield [reduce(mul, [p**e for p, e in zip(primes, x)]) for x in f]


def main():
    K = [float("inf")]*12001
    K[0:2] = 0, 0

    # the minimal product-sum for some k is between k and 2k
    for n in range(4, 24001):
        for f in factorizations(n):
            k = (n-sum(f)) + len(f)
            if k < 12001 and K[k] > n:
                K[k] = n

    return sum(set(K))


if __name__ == "__main__":
    print(main())
