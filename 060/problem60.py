#!/usr/bin/python2

from projecteuler import prime_sieve
from miller_rabin import miller_rabin as is_prime

def main():
    lim = 8500
    primes = prime_sieve(lim)

    # store possible pairs for each prime
    candidates = [None]*len(primes)
    for i in xrange(1, len(primes)):
        candidates[i] = set(j for j in xrange(i+1, len(primes)) if is_prime(int(str(primes[i])+str(primes[j]))) and is_prime(int(str(primes[j])+str(primes[i]))))

    quintuplets = []

    def find_quints(p):
        if len(p) == 5:
            quintuplets.append(sum(primes[i] for i in p))
            return

        for i in xrange(p[-1]+1, len(primes)):
            for j in p:
                if not i in candidates[j]:
                    break
            else:
                find_quints(p+[i])

    for i in xrange(1, len(primes)-4):
        find_quints([i])

    return min(quintuplets)

if __name__ == "__main__":
    print main()
