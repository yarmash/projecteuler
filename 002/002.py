#!/usr/bin/python2

x, y = 1, 2
limit = 4000000
s = 0

while 1:
    if y % 2 == 0:
        s += y

    x, y = y, x + y

    if y > limit:
        break

print(s)
