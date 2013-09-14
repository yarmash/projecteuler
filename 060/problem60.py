#!/usr/bin/python2

"""Problem 60: Prime pair sets"""

from projecteuler import prime_sieve, memoize
from euler import is_prime

def main():
    primes = prime_sieve(8500)

    @memoize
    def check(p1, p2):
        return is_prime(int(str(p1)+str(p2))) and is_prime(int(str(p2)+str(p1)))

    def candidates(p):
        for i in xrange(p[-1]+1, len(primes)):
            if all(check(primes[i], primes[j]) for j in p):
                if len(p) == 4:
                    yield p+[i]
                else:
                    for c in candidates(p+[i]):
                        yield c

    for i in xrange(len(primes)):
        try:
            quint = candidates([i]).next()
            return sum(primes[x] for x in quint)
        except StopIteration:
            pass


if __name__ == "__main__":
    print main()
