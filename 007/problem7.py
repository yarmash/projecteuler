#!/usr/bin/python2

from projecteuler import prime_sieve_lazy

def main():
    count = 0
    for prime in prime_sieve_lazy():
        count += 1
        if count == 10001:
            return prime

if __name__ == "__main__":
    print main()
