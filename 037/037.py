#!/usr/bin/python2

from projecteuler import is_prime

def is_truncatable(p): # check if the prime is right-/left-truncatable
    t = p
    k = -1
    while t > 0:
        t /= 10
        if not is_prime(t):
            return False
        k += 1

    while p > 0:
        p %= 10**k
        if not is_prime(p):
            return False
        k -= 1

    return True


n = 23
s = 0
cnt = 0

while cnt < 11:
    if is_prime(n) and is_truncatable(n):
        s += n
        cnt += 1
    n += 2

print s
