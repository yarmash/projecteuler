#!/usr/bin/python2

from projecteuler import prime_sieve
from miller_rabin import miller_rabin as is_prime

def main():
    lim = 8400
    primes = prime_sieve(lim)
    del primes[2] # delete 5 and 2
    del primes[0]

    # store possible pairs for each prime
    candidates = [ set(j for j in xrange(i+1, len(primes)) if is_prime(int(str(primes[i])+str(primes[j]))) and is_prime(int(str(primes[j])+str(primes[i]))))
        for i in xrange(len(primes)) ]

    res = float("Inf")

    for i in xrange(len(primes)-4):
        for j in candidates[i]:
            for k in candidates[i] & candidates[j]:
                for l in candidates[i] & candidates[j] & candidates[k]:
                    for m in candidates[i] & candidates[j] & candidates[k] & candidates[l]:
                        s = sum(primes[x] for x in (i, j, k, l, m))
                        if s < res:
                            res = s
    return res

if __name__ == "__main__":
    print main()
