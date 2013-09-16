#!/usr/bin/python2

"""Problem 53: Combinatoric selections"""

def main():
    cnt = 0
    # the C(n, r) numbers resemble the Pascal's Triangle
    triangle = [1]*101
    for n in xrange(2, 101):
        triangle[n-1] = 1
        for r in xrange(n-1, 0, -1):
            triangle[r] += triangle[r-1]
            if triangle[r] > 1000000:
                cnt += 1
    return cnt


if __name__ == "__main__":
    print main()
