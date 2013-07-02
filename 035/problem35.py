#!/usr/bin/python2

"""Problem 35: Circular primes"""

from projecteuler import prime_sieve

def rotations(n):
    k = 5 if 100000 < n else \
        4 if 10000 < n else \
        3 if 1000 < n else \
        2 if 100 < n else \
        1 if 10 < n else \
        0

    for i in range(k+1):
        n = 10**k*(n % 10) + n/10
        yield n

def main():
    primes = prime_sieve(1000000)
    primes_set = set(primes)

    cnt = 0

    for p in primes:
        for r in rotations(p):
            if not r in primes_set:
                break
        else:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print main()
