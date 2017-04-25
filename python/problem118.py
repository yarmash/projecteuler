#!/usr/bin/python

"""Problem 118: Pandigital prime sets"""

from itertools import permutations, chain, combinations

from utils import prime_sieve


def index_sets(indexes=range(1, 9)):
    """
    Find possible places where we can split a string of digits to numbers.
    """
    return chain.from_iterable(combinations(indexes, r) for r in range(1, 9))


def main():
    primes = frozenset(prime_sieve(100_000_000))
    digits = "123456789"
    prime_sets = set()

    for p in permutations(digits, 9):
        if p[-1] in {"2", "4", "5", "6", "8"}:
            continue

        for index_set in index_sets():
            prev = 0
            parts = []

            for i in chain(index_set, [9]):
                if i-prev > 1:
                    if p[i-1] in {"2", "4", "5", "6", "8"}:
                        break
                elif p[i-1] in {"1", "4", "6", "8", "9"}:
                    break
                x = int("".join(p[prev:i]))
                if x not in primes:
                    break
                parts.append(x)
                prev = i
            else:
                prime_set = frozenset(parts)
                if prime_set not in prime_sets:
                    prime_sets.add(prime_set)
    return len(prime_sets)


if __name__ == "__main__":
    print(main())
