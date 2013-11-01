#!/usr/bin/python

"""Problem 55: Lychrel numbers"""

from projecteuler import memoize

@memoize
def reverse(num):
    r = 0
    while num > 0:
        r = r * 10 + num % 10
        num //= 10
    return r

def main():
    cnt = 0

    for i in range(1, 10000):
        for _ in range(1, 50):
            i += reverse(i)

            if i == reverse(i):
                break
        else:
            cnt += 1

    return cnt

if __name__ == "__main__":
    print(main())
