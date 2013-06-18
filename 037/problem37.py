#!/usr/bin/python2

from projecteuler import is_prime
from math import log10


def is_truncatable(p): # check if the prime is right-/left-truncatable
    t = p/10

    while t > 0:
        if not is_prime(t):
            return False
        t /= 10


    k = int(log10(p))
    t = p % 10**k

    while t > 0:
        if not is_prime(t):
            return False
        k -= 1
        t %= 10**k

    return True

def main():
    n = 23
    s = 0
    cnt = 0

    while cnt < 11:
        if is_prime(n) and is_truncatable(n):
            s += n
            cnt += 1
        n += 2

    return s

if __name__ == "__main__":
    print main()
