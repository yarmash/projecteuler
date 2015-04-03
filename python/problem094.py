#!/usr/bin/python

"""Problem 94: Almost equilateral triangles"""


def main():
    max_perimeter = 1000000000
    psum = 0

    triplets = [(3, 4, 5)]

    while triplets:
        a, b, c = triplets.pop()

        if 2*(c + a) > max_perimeter or 2*(c + b) > max_perimeter:
            continue

        if c - 2*a == 1 or c - 2*a == -1:
            psum += 2*(c + a)

        if c - 2*b == 1 or c - 2*b == -1:
            psum += 2*(c + b)

        triplets.extend([
            (a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c),
            (a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c),
            (-a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c)])

    return psum

if __name__ == "__main__":
    print(main())
