#!/usr/bin/python2

from projecteuler import prime_sieve

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

def main():
    primes = [ x for x in prime_sieve(10000) if x > 1000 and x != 1487 and x != 4817 and x != 8147 ]
    primes_set = frozenset(primes)

    for i, p in enumerate(primes):

        for q in primes[i+1:]:
            r = 2*q-p

            if r > primes[-1]:
                break

            if r in primes_set and is_permutation(p, q) and is_permutation(q, r):
                return "%d%d%d" % (p, q, r)

if __name__ == "__main__":
    print main()
