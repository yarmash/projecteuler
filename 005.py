#!/usr/bin/python2

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10
# without any remainder.  What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

# Answer: 232792560


from math import log, sqrt

def get_primes(limit):

    def is_prime(n):
        limit = int(sqrt(n))
        for k in range(2, limit+1):
            if n % k == 0:
                return False
        return True

    primes = []

    for n in range(2, limit+1):
        if is_prime(n):
            primes.append(n)

    return primes


n = 20

primes = get_primes(n) # prime numbers <= N. TODO: use a sieve of Eratosthenes

limit = sqrt(n)
result = 1

for p in primes:
    exponent = 1 if p > limit else int(log(n)/log(p))
    result *= p ** exponent

print result
