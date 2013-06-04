#!/usr/bin/python2

from math import factorial
from projecteuler import factorials_table

def main():
    cnt = 0
    f = factorials_table(100)

    for n in xrange(23, 101):
        for r in xrange(1, n+1):
            if f[n]/(f[r]*f[n-r]) > 1000000:
                cnt += 1
    return cnt

if __name__ == "__main__":
    print main()