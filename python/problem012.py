#!/usr/bin/python

"""Problem 12: Highly divisible triangular number"""

from utils import prime_sieve, triangular_numbers


def main():
    primes = prime_sieve(65500)

    for t in triangular_numbers():
        cnt = 1
        tt = t

        for p in primes:
            if p*p > tt:
                cnt *= 2
                break
            exponent = 1
            while tt % p == 0:
                exponent += 1
                tt //= p
            cnt *= exponent

            if tt == 1:
                break

        if cnt >= 500:
            return t

if __name__ == "__main__":
    print(main())
