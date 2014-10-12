#!/usr/bin/python

"""Problem 91: Right triangles with integer coordinates"""

from collections import namedtuple
from itertools import combinations


def main():
    N = 50
    Point = namedtuple('Point', ['x', 'y'])
    points = [Point(x, y) for x in range(N+1) for y in range(N+1) if x or y]
    cnt = 0

    for p, q in combinations(points, 2):
        a = p.x * p.x + p.y * p.y
        b = q.x * q.x + q.y * q.y
        c = (p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y)

        if a + b == c or a + c == b or b + c == a:
            cnt += 1

    return cnt

if __name__ == "__main__":
    print(main())
