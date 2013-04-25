#!/usr/bin/python2

# TODO: use the 'number of divisors' formula
step = 0
triangle = 0

while True:
    step += 1
    triangle += step

    cnt = 0

    lim = int(triangle**0.5)
    if triangle == lim*lim:
        cnt -= 1

    for i in xrange(1, lim + 1):
        if triangle % i == 0:
            cnt += 2
            if cnt > 500:
                print triangle
                exit()
