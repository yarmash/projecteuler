#!/usr/bin/python2

from projecteuler import prime_sieve

def main():
    lim = 2000000
    return sum(prime_sieve(lim))

if __name__ == "__main__":
    print main()
