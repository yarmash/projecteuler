#!/usr/bin/python

"""Problem 120: Square remainders"""


def main():
    rmax_sum = 0

    for a in range(3, 1001):
        seen = set()
        n = 1
        rmax = 0
        x, y = pow(a-1, n, a*a), pow(a+1, n, a*a)

        while (x, y) not in seen:
            seen.add((x, y))
            r = (x + y) % (a * a)

            if r > rmax:
                rmax = r
            n += 1
            x, y = pow(a-1, n, a*a), pow(a+1, n, a*a)
        rmax_sum += rmax
    return rmax_sum


if __name__ == "__main__":
    print(main())
