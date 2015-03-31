#!/usr/bin/python

"""Problem 3: Largest prime factor"""


def main():
    num = 600851475143
    max_factor = int(num**.5)
    factor = last_factor = 3

    while num > 1 and factor <= max_factor:
        if num % factor == 0:
            last_factor = factor
            while num % factor == 0:
                num //= factor
            max_factor = int(num**.5)
        factor += 2

    return last_factor if num == 1 else num

if __name__ == "__main__":
    print(main())
