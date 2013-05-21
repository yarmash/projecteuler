#!/usr/bin/python2
# coding=utf-8

from math import sqrt

def memoize(fn):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = fn(*args)
        cache[args] = result
        return result
    return wrapper

def is_prime(n):
    if n == 1:
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
            if n % k == 0:
                return False
            if n % (k+2) == 0:
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


# returns prime factors of an integer
def prime_factors(n):
    primes = prime_sieve(int(sqrt(n)))
    prime_factors = []

    for p in primes:
        if p*p > n:
            break

        e = 0
        while n % p == 0:
            e += 1
            n //= p

        if e > 0:
            prime_factors.append((p, e))

    if n > 1:
        prime_factors.append((n, 1))

    return prime_factors

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

# checks if a number is 1 to N pandigital
def is_pandigital(n, d=9):
    res = 0

    while n > 0:
        k = n % 10
        if k == 0:
            return False
        res |= (1 << k-1)
        n /= 10

    return res == 2**d - 1

# returns Pythagorean triplets with a+b+c=p using the formula a+b+c = 2*m*(m+n)*d
# http://projecteuler.net/overview=009
def pythagorean_triplets(p):
    p >>= 1

    for m in range(2, int(sqrt(p)+1)):
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

# The function used for the problems 18 & 67
# the number of rows in the triangle and the number's index in the array are calculated using the formulas
# for the sum of the members of an arithmetic progression
def calc_max_total(nums):
    nrows = (-1 + sqrt(1+4*2*len(nums))) / 2

    @memoize
    def calc_total(rownum, idx):
        n = nums[ ((1 + (rownum-1))*(rownum-1))/2 + idx ]
        return n if rownum == nrows else n + max(calc_total(rownum+1, idx), calc_total(rownum+1, idx+1))

    return calc_total(1, 0)
