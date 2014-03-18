#!/usr/bin/python

"""Problem 78: Coin partitions"""

def main():
    partitions = [1]
    n = 1

    while True:
        t = 1
        k = 1
        p = 0
        sign = 1

        while t > 0:
            t = n - (k*(3*k+1) >> 1)
            if t >= 0:
                p += sign*partitions[t]
            t = n - (k*(3*k-1) >> 1)
            if t >= 0:
                p += sign*partitions[t]
            k += 1
            sign = -sign

        if not p % 1000000:
            return n

        n += 1
        partitions.append(p)


if __name__ == "__main__":
    print(main())
