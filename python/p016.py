#!/usr/bin/env python3

"""Problem 16: Power Digit Sum"""


def main():
    return sum(map(int, str(2**1000)))


if __name__ == "__main__":
    print(main())
