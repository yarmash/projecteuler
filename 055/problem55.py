#!/usr/bin/python2

from projecteuler import memoize

@memoize
def reverse(num):
    r = 0
    while num > 0:
        r = r * 10 + num % 10
        num /= 10
    return r

def main():
    cnt = 0

    for i in xrange(1, 10000):
        for _ in xrange(1, 50):
            i += reverse(i)

            if i == reverse(i):
                break
        else:
            cnt += 1

    return cnt

if __name__ == "__main__":
    print main()
