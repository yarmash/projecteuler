#!/usr/bin/env python

"""Problem 133: Repunit nonfactors"""


from utils import prime_sieve


def A(n):
    r = k = 1

    while r:
        r = (r*10 + 1) % n
        k += 1
    return k


def check(n):
    while n % 2 == 0:
        n //= 2
    while n % 5 == 0:
        n //= 5
    return n == 1


def main():
    primes = prime_sieve(100_000)
    factors = []

    for prime in primes:
        if prime > 5 and check(A(prime)):
            factors.append(prime)

    return sum(primes) - sum(factors)


if __name__ == "__main__":
    print(main())
