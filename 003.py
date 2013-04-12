#!/usr/bin/python2

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Answer: 6857


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
