#!/usr/bin/env python3

"""Problem 108: Diophantine Reciprocals I"""

from math import prod


def num_of_divisors(factors):
    """Get the number of divisors of n^2 from prime factors of n"""
    return prod(2*f[1] + 1 for f in factors)


def num(factors):
    """Get the number from its prime factors"""
    return prod(f[0]**f[1] for f in factors)


def main(lim=1000,
         # the number of primes to be considered is ceil(log3(lim*2))
         primes=(2, 3, 5, 7, 11, 13, 17)):

    min_n = float("inf")
    lim = lim*2 - 1

    factors = [[[x, 1] for x in primes[:i]] for i in range(1, len(primes)+1)]
    solutions = 1 << len(primes)+1

    while factors:
        f = factors.pop()
        # if a bigger number of distinct primes produced no solutions, then
        # we're done.
        if not solutions & (1 << len(f)+1):
            break

        if num_of_divisors(f) > lim and num(f) < min_n:
            min_n = num(f)
            solutions |= 1 << len(f)

        new = f

        for i in range(len(f)):
            new = [x[:] for x in new]
            new[i][1] += 1
            if num(new) >= min_n:
                break
            factors.append(new)
    return min_n


if __name__ == "__main__":
    print(main())
