#!/usr/bin/python2

"""Totient maximum"""

from projecteuler import prime_sieve_lazy

def main():
    lim = 1000000
    res = 1

    for prime in prime_sieve_lazy():
        if res*prime > lim:
            break
        res *= prime

    return res

if __name__ == "__main__":
    print main()
