#!/usr/bin/python2

"""Counting fractions"""

from projecteuler import prime_sieve



def main():
    # http://en.wikipedia.org/wiki/Farey_sequence

    n = 1000000
    primes = prime_sieve(int(n**.5))

    def phi(n):
        res = float(n)

        for p in primes:
            if p*p > n: break

            if n % p == 0:
                res -= res/p
                while n % p == 0:
                    n /= p
        if n > 1:
            res -= res/n
        return res

    return int(sum(phi(m) for m in xrange(2, n+1)))


if __name__ == "__main__":
    print main()
