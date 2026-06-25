#!/usr/bin/env python3

"""Problem 135: Same Differences"""


def main():
    limit = 1_000_000
    target = 10
    solutions = [0] * limit

    # n = (y + d)^2 - y^2 - (y - d)^2 = y * (4d - y)
    for y in range(1, limit):
        stop = min(3 * y, (limit - 1) // y + 1)
        start = -y % 4 or 4

        for factor in range(start, stop, 4):
            solutions[y * factor] += 1

    return solutions.count(target)


if __name__ == "__main__":
    print(main())
