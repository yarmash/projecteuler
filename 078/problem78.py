#!/usr/bin/python

"""Problem 78: Coin partitions"""

def gen_p():
    plist = [1]
    yield 1

    n = 1

    while True:
        t = 1
        k = 1
        p = 0

        while t > 0:
            sign = 1 if k & 1 else -1
            t = n - (k*(3*k+1) >> 1)
            if t >= 0:
                p += sign*plist[t]
            t = n - (k*(3*k-1) >> 1)
            if t >= 0:
                p += sign*plist[t]
            k +=1
        n += 1
        plist.append(p)
        yield p

def main():
    for n, p in enumerate(gen_p()):
        if p % 1000000 == 0:
            return n

if __name__ == "__main__":
    print(main())
