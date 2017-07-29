#!/usr/bin/env python

"""Problem 121: Disc game prize fund"""

from fractions import Fraction
from itertools import chain, combinations
from operator import mul
from functools import reduce


def main():
    TURNS = 23

    probs = [(Fraction(x - 1, x), Fraction(1, x)) for x in range(2, TURNS + 2)]
    prob = 0

    for c in chain.from_iterable(combinations(range(TURNS), n)
                                 for n in range(TURNS//2 + 1, TURNS+1)):

        prob += reduce(mul, (probs[i][i in c] for i in range(TURNS)))

    return prob.denominator//prob.numerator


if __name__ == "__main__":
    print(main())
