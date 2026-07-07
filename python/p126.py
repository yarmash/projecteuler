#!/usr/bin/env python3

"""Problem 126: Cuboid Layers"""


def main():
    # guessed search ceiling: counts are exact for all layer sizes <= lim,
    # so this only assumes the answer lies below it
    lim = 20000
    cn = [0]*(lim+1)

    for x in range(1, lim):
        if 6*x*x > lim:  # smallest first layer for this x (y = z = x)
            break
        for y in range(x, lim):
            if 2*(2*x*y + y*y) > lim:  # smallest first layer (z = y)
                break
            for z in range(y, lim):
                c = 2*(x*y + x*z + y*z)  # first layer
                if c > lim:
                    break

                # layer n adds 4*(x+y+z) + 8*(n-2) cubes over layer n-1
                d = 4*(x + y + z)
                while c <= lim:
                    cn[c] += 1
                    c += d
                    d += 8

    return cn.index(1000)


if __name__ == "__main__":
    print(main())
