#!/usr/bin/python2

def main():
    return len(set(a**b for a in xrange(2, 101) for b in xrange(2, 101)))

if __name__ == "__main__":
    print main()
