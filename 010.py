#!/usr/bin/python2

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Answer: 142913828922

n = 2000000
a = [True]*n

limit = int(n**0.5)

for i in range(4, limit, 2): # cross out even numbers
    a[i] = False

for i in range(3, limit, 2):
    if a[i] == True:
        for j in range(i**2, n, 2*i):
            a[j] = False

s = 2
for i in xrange(3, n, 2):
    if a[i] == True:
        s += i

print s
