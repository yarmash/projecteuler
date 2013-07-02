#!/usr/bin/python2

"""Problem 3: Largest prime factor"""

def main():
    num = 600851475143
    f = 3

    while num > 1:
        if (num % f == 0):
            f2 = f
        while (num % f == 0):
            num /= f
        f += 2

    return f2

if __name__ == "__main__":
    print main()
