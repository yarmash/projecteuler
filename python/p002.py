#!/usr/bin/env python3

"""Problem 2: Even Fibonacci Numbers"""


def main():
    limit = 4_000_000
    curr_even, prev_even, Σ = 2, 0, 0

    while curr_even <= limit:
        Σ += curr_even
        prev_even, curr_even = curr_even, 4 * curr_even + prev_even
    return Σ


if __name__ == "__main__":
    print(main())
