#!/usr/bin/python2

def reverse(n):
    r = 0
    while n > 0:
        r = r * 10 + n % 10
        n /= 10
    return r

n = 0

for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        k = x*y
        if k <= n:
            break

        if n < k and k == reverse(k):
            n = k
print(n)
