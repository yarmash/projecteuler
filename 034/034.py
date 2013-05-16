#!/usr/bin/python2

# precompute factorials
f = []
for i in range(10):
    f.append(1 if i < 2 else i*f[i-1])

res = 0

for n in xrange(3, 40586): # For the proper upper bound see http://en.wikipedia.org/wiki/Factorion#Upper_bound
    s = 0
    k = n
    while k > 0:
        s += f[k % 10]
        k /= 10

    if n == s:
        res += n

print res
