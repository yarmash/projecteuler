#!/usr/bin/python2
# coding=utf-8

from math import sqrt, factorial

def memoize(fn):
    memo = {}
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = fn(*args)
        memo[args] = result
        return result
    return wrapper

def is_prime(n):
    if n <= 1:
        return False
    elif n < 4:
        return True # 2 and 3 are prime
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True # we have already excluded 4, 6 and 8
    elif n % 3 == 0:
        return False
    else:
        limit = int(sqrt(n))
        k = 5
        while k <= limit: # check through all the numbers of the form 6k ± 1
            if n % k == 0 or n % (k+2) == 0:
                return False
            k += 6

        return True


# returns the prime numbers <= limit
# implements The Sieve of Eratosthenes
def prime_sieve(n):
    if n <= 1:
        return []

    bound = (n-1)/2 # last index of the sieve
    sieve = [True]*(bound+1)

    for i in xrange(1, int(sqrt(n)/2)+1):
        if sieve[i]: # 2*i+1 is a prime, mark multiples
            for j in xrange(2*i*(i+1), bound+1, 2*i+1):
                sieve[j] = False
    primes = [2]
    for i in xrange(1, bound+1):
        if sieve[i]:
            primes.append(2*i+1)
    return primes


# http://www.cs.hmc.edu/~oneill/papers/Sieve-JFP.pdf
def prime_sieve_lazy():
    yield 2
    n = 3
    composites = {}

    while True:
        if n not in composites:
            yield n
            composites[n*n] = [n]
        else:
            for prime in composites[n]:
                composites.setdefault(prime*2 + n, []).append(prime)
            del composites[n]
        n += 2


# returns prime factors of an integer
def prime_factors(n):
    primes = prime_sieve(int(sqrt(n)))
    factors = []

    for p in primes:
        if p*p > n:
            break

        e = 0
        while n % p == 0:
            e += 1
            n //= p

        if e > 0:
            factors.append((p, e))

    if n > 1:
        factors.append((n, 1))

    return factors

def sum_of_divisors(n):
    if n == 1:
        return 1
    # http://mathschallenge.net/index.php?section=faq&ref=number/sum_of_divisors
    return reduce(lambda x,y: x * (y[0]**(y[1]+1)-1)/(y[0]-1), prime_factors(n), 1)

def sum_of_proper_divisors(n):
    return sum_of_divisors(n) - n

# returns the Greatest Common Divisor of a and b (Euclidean algorithm)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# checks if a number is palindromic in the given base
def is_palindrome(n, base):
    r = 0
    t = n
    while t > 0:
        r = r * base + t % base
        t /= base
    return r == n

# checks if a number is x to y pandigital
# the function doesn't check for redundant digits
def is_pandigital(n, end=9, start=1):
    res = 0

    while n > 0:
        res |= (1 << n % 10)
        n /= 10

    return res == (2**(end-start+1) - 1) << start

# checks if an integer is a permutation of another
def is_permutation(a, b):
    if (a - b) % 9: # the difference must be a multiple of 9.
        return False
    return sorted(str(a)) == sorted(str(b))


# functions for calculating polygonal numbers
def nth_triangle(n):
    return n*(n+1)/2

def nth_square(n):
    return n*n

def nth_pentagonal(n):
    return n*(3*n - 1)/2

def nth_hexagonal(n):
    return n*(2*n-1)

def nth_heptagonal(n):
    return n*(5*n-3)/2

def nth_octagonal(n):
    return n*(3*n - 2)


def is_pentagonal(n):
    k = (sqrt(24*n+1)+1)/6
    return k.is_integer()

# returns Pythagorean triplets with a+b+c=p using the formula a+b+c = 2*m*(m+n)*d
# p is always even
# http://projecteuler.net/overview=009
def pythagorean_triplets(p):
    p >>= 1

    for m in xrange(2, int(sqrt(p)+1)):
        if p % m == 0:
            pm = p / m
            while not pm&1: # reduce the search space by removing all factors 2
                pm >>= 1
            k = m + 2 if m&1 else m + 1

            while k < 2*m and k <= pm:
                if pm % k == 0 and gcd(k, m) == 1:
                    d = p/(k*m)
                    n = k - m
                    a = d*(m*m - n*n)
                    b = 2*d*m*n
                    c = d*(m*m + n*n)
                    yield (a, b, c)
                k += 2

# returns the number of k-combinations of a set of n elements
def number_of_combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# returns continued fraction expansion of a square root, e.g. sqrt(6) -> [2, 2, 4]
# http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
def sqrt_fraction_expansion(num):
    m = 0
    d = 1
    a0 = a = int(sqrt(num))

    expansion = [a0]

    while a != 2*a0:
        m = d*a - m
        d = (num - m*m)/d
        a = (a0 + m)/d
        expansion.append(a)

    return expansion

# get convergent fractions resulting from the quotients
# http://en.wikipedia.org/wiki/Continued_fraction#Continued_fraction_expansions_of_.CF.80
def convergent_fractions(quotients):
    num, den, prev_num, prev_den = quotients.next(), 1, 1, 0

    while True:
        yield num, den
        q = quotients.next()
        prev_num, num, prev_den, den = num, prev_num + num*q, den, prev_den + den*q
