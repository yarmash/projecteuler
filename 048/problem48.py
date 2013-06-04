#!/usr/bin/python2

def main():
    return sum(i**i for i in xrange(1, 1001)) % 10**10

if __name__ == "__main__":
    print main()
