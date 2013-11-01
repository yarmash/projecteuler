#!/usr/bin/python

"""Problem 2: Even Fibonacci numbers"""


def main():
    limit = 4000000
    a, b, c, sum_ = 1, 1, 2, 0

    # every third Fibonacci number is even
    while c <= limit:
        sum_ += c
        a = b + c
        b = c + a
        c = a + b

    return sum_


if __name__ == "__main__":
    print(main())
