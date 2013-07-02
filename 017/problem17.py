#!/usr/bin/python2

"""Problem 17: Number letter counts"""

def main():
    units = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    tens = ("ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")
    teens = ("eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")

    def count_letters(n):
        words = []

        if n >= 1000:
            words.extend((units[n/1000-1], "thousand"))
            n = n % 1000

        if n >= 100:
            words.extend((units[n/1000-1], "hundred"))
            n = n % 100
            if n:
                words.append("and")

        if 11 <= n <= 19:
            words.append(teens[n-10-1])
        else:
            if n >= 10:
                words.append(tens[n/10-1])
                n = n % 10
            if n >= 1:
                words.append(units[n-1])

        #print words
        return sum(map(len, words))

    return sum(count_letters(i) for i in xrange(1, 1001))

if __name__ == "__main__":
    print main()
