#!/usr/bin/python

"""Problem 7: 10001st prime"""

from utils import prime_sieve_lazy


def main():
    count = 0
    for prime in prime_sieve_lazy():
        count += 1
        if count == 10001:
            return prime

if __name__ == "__main__":
    print(main())
