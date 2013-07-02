#!/usr/bin/python2

"""Problem 34: Digit factorials"""

from projecteuler import factorials_table

def main():
    # precalculate factorials
    f = factorials_table(9)
    res = 0

    for n in xrange(3, 40586): # For the proper upper bound see http://en.wikipedia.org/wiki/Factorion#Upper_bound
        s = 0
        k = n
        while k > 0:
            s += f[k % 10]
            k /= 10

        if n == s:
            res += n
    return res

if __name__ == "__main__":
    print main()
