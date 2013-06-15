#!/usr/bin/python2

from projecteuler import is_prime, prime_sieve, memoize

def main():
    lim = 9000

    primes = prime_sieve(lim)

    @memoize
    def chk(i, j):
        p1, p2 = primes[i], primes[j]
        return is_prime(int(str(p1)+str(p2))) and is_prime(int(str(p2)+str(p1)))

    candidates = []

    def find_candidates(p):
        if len(p) == 5:
            candidates.append(sum(primes[i] for i in p))
        else:
            for i in xrange(p[-1], len(primes)):
                for j in p:
                    if not chk(j, i):
                        break
                else:
                    find_candidates(p+[i])

    for i in xrange(1, len(primes)-4):
        find_candidates([i])

    return min(candidates)

if __name__ == "__main__":
    print main()
