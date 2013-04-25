#!/usr/bin/python2

s = 1000

for n in xrange(1, 1000):
    for m in xrange(n+1, 1000):
        k = 1
        while True:
            a = k*(m**2 - n**2)
            b = k*(2*m*n)
            c = k*(m**2 + n**2)

            if a+b+c > s:
                break

            if a+b+c == s:
                print a*b*c
                exit()

            k += 1
