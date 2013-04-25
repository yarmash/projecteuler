#!/usr/bin/python2

n = 600851475143
f = 2
f2 = f

while n > 1:
    if (n % f == 0):
        f2 = f
    while (n % f == 0):
        n /= f
    f += 1

print(f2)
