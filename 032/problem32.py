#!/usr/bin/python2

"""Problem 32: Pandigital products"""

from projecteuler import is_pandigital

def main():
    products = set()

    # the solutions must either be 1x4 or 2x3 digits
    for r in (((2, 10), (1234, 9877)), ((12, 82), (123, 988))):
        for a in xrange(*r[0]):
            if not a % 5: continue
            for b in xrange(*r[1]):
                if not b % 5: continue
                p = a*b
                if p > 9876: break
                if is_pandigital(int(str(a)+str(b)+str(p))):
                    products.add(p)

    return sum(products)

if __name__ == "__main__":
    print main()
