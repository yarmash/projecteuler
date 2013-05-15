#!/usr/bin/python2

def is_pandigital(n):
    res = 0

    while n > 0:
        k = n % 10
        if k == 0:
            return False
        res |= (1 << k-1)
        n /= 10

    return res == 511

digits = "123456789"
products = set()

def check(x, y):
    for a in range(1, 10**x):
        for b in range(1, 10**y):
            p = a*b
            if p > 9876: break

            s = str(a)+str(b)+str(p)

            if is_pandigital(int(s)):
                products.add(p)

# the solutions must either be 1x4 or 2x3 digits
check(1, 4)
check(2, 3)

print sum(products)
