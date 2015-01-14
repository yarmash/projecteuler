#!/usr/bin/python

"""Problem 60: Prime pair sets"""

from projecteuler import prime_sieve, memoize, is_prime

def main():
    primes = prime_sieve(8500)

    @memoize
    def check(p1, p2):
        return is_prime(int(str(p1)+str(p2))) and is_prime(int(str(p2)+str(p1)))

    def candidates(p):
        for i in range(p[-1]+1, len(primes)):
            if all(check(primes[i], primes[j]) for j in p):
                if len(p) == 4:
                    yield p+[i]
                else:
                    yield from candidates(p+[i])

    for i in range(len(primes)):
        try:
            quint = next(candidates([i]))
            return sum(primes[x] for x in quint)
        except StopIteration:
            pass


if __name__ == "__main__":
    print(main())
