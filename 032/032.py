#!/usr/bin/python2

from projecteuler import is_pandigital

products = set()

# the solutions must either be 1x4 or 2x3 digits
for r in (((2, 10), (1234, 9877)), ((12, 82), (123, 988))):
    for a in range(*r[0]):
        if not a % 5: continue
        for b in range(*r[1]):
            if not b % 5: continue
            p = a*b
            if p > 9876: break
            if is_pandigital(int(str(a)+str(b)+str(p))):
                products.add(p)

print sum(products)
