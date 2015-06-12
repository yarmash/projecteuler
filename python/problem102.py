#!/usr/bin/python

"""Problem 102: Triangle containment"""

from utils import open_data_file


def main():
    cnt = 0

    with open_data_file("triangles.txt") as data_file:
        for line in data_file:
            x1, y1, x2, y2, x3, y3 = map(int, line.split(","))

            # if z-components of cross products OA x OB, OB x OC, OC x OA are
            # all of the same sign, the origin is within the triangle.

            if (x1*y2 - y1*x2 > 0) is (x2*y3 - y2*x3 > 0) is (x3*y1 - y3*x1 > 0):
                cnt += 1
    return cnt

if __name__ == "__main__":
    print(main())
