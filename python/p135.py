#!/usr/bin/env python3

"""Problem 135: Same Differences"""


def main():
    limit = 1_000_000
    target = 10
    solutions = [0]*limit

    for a in range(1, limit):
        for b in range(1, (limit - 1) // a + 1):
            n = a*b

            if (a+b) % 4 == 0 and a < 3*b:
                solutions[n] += 1

    return solutions.count(target)


if __name__ == "__main__":
    print(main())
