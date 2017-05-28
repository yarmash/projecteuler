#!/usr/bin/python

"""Problem 119: Digit power sum"""

from itertools import count


def main():

    def sum_digits(n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r

    cnt = 0

    for num_digits in count(2):
        max_num = 10**num_digits
        min_num = max_num//10

        for digit_sum in range(2, num_digits*9 + 1):
            num = digit_sum * digit_sum
            p = 2

            while num < max_num:
                if min_num <= num < max_num and num == sum_digits(num)**p:
                    cnt += 1
                    if cnt == 30:
                        return num
                num *= digit_sum
                p += 1


if __name__ == "__main__":
    print(main())
