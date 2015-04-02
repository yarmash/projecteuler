#!/usr/bin/python

"""Problem 94: Almost equilateral triangles"""

from utils import isqrt


def main():
    max_perimeter = 1000000000
    psum = 0

    for a in range(5, max_perimeter//3+2, 2):
        tmp = a*a - (a-1)*(a-1)//4
        if isqrt(tmp)**2 == tmp:
            psum += a+a+a-1

        tmp = a*a - (a+1)*(a+1)//4
        if isqrt(tmp)**2 == tmp:
            psum += a+a+a+1

    return psum

if __name__ == "__main__":
    print(main())
