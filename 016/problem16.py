#!/usr/bin/python2

def main():
    return sum(int(digit) for digit in str(2**1000))

if __name__ == "__main__":
    print main()
