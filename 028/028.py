#!/usr/bin/python2

size = 1001
n = 1
result = 0
cnt = 0
step = 2


while n <= size*size:
    result += n
    cnt += 1
    n += step

    if not cnt % 4:
        step += 2

print result
