#!/usr/bin/python2

from projecteuler import is_prime

def main():
    num = 3
    count = 2

    while count < 10001:
        num += 2 # loop through odd numbers
        if is_prime(num):
            count += 1

    return num

if __name__ == "__main__":
    print main()
