#!/usr/bin/python2

from projecteuler import is_palindrome

def main():
    n = 0

    for x in xrange(999, 99, -1):
        for y in xrange(x, 99, -1):
            k = x*y
            if k <= n:
                break
            if is_palindrome(k, 10):
                n = k
    return n

if __name__ == "__main__":
    print main()
