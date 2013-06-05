#!/usr/bin/python2

def main():
    e = 1

    while True:
        # the number has to start with 1, or it will end up with more digits
        # must be divisible by 3
        for i in xrange(10**e + 2, 10**e * 2, 3):
            s = sorted(str(i))

            if all(sorted(str(i*k)) == s for k in xrange(2, 7)):
                return i
        e += 1

if __name__ == "__main__":
    print main()
