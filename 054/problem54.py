#!/usr/bin/python2

"""Problem 54: Poker hands"""

import os

def hands():
    datafile = os.path.join(os.path.dirname(__file__), "poker.txt")

    for line in open(datafile):
        cards = map(Card, line.split())
        yield Hand(cards[:5]).evaluate(), Hand(cards[5:]).evaluate()


class Card():
    values = dict(zip(("23456789TJQKA"), range(2, 15)))
    suits = { s[0] : s for s in ("Clubs", "Diamonds", "Hearts", "Spades") }

    def __init__(self, data):
        self.kind = data[0]
        self.suit = data[1]
        self.value = Card.values[data[0]]

    def __repr__(self):
         return "%s%s" % (self.kind, Card.suits[self.suit])


class Hand():
    def __init__(self, cards):
        cards.sort(key=lambda card: card.value, reverse=True)

        self.cards = cards
        self.same_suit = all(card.suit == cards[0].suit for card in cards[1:])
        self.consecutive_values = all(cards[i].value - cards[i+1].value == 1 for i in range(4))

    def evaluate(self):
        cards = self.cards

        # save the number of occurrences for each value
        occurrences = [0]*15
        for card in cards:
            occurrences[card.value] += 1

        # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        # Is a case of the straight flush.

        # Straight Flush: All cards are consecutive values of same suit.
        if self.consecutive_values and self.same_suit:
            yield 1
            yield cards[0].value
        else:
            yield 0

        # Four of a Kind: Four cards of the same value.
        if 4 in occurrences:
            yield 1
            yield occurrences.index(4)
        else:
            yield 0

        # Full House: Three of a kind and a pair.
        if 3 in occurrences and 2 in occurrences:
            yield 1
            yield occurrences.index(3)
        else:
            yield 0

        # Flush: All cards of the same suit.
        if self.same_suit:
            yield 1
            yield cards[0].value
        else:
            yield 0

        # Straight: All cards are consecutive values.
        if self.consecutive_values:
            yield 1
            yield cards[0].value
        else:
            yield 0

        # Three of a Kind: Three cards of the same value.
        if 3 in occurrences:
            yield 1
            yield occurrences.index(3)
            for card in cards:
                if occurencies[card.value] != 3:
                    yield card.value
        else:
            yield 0

        # Two Pairs: Two different pairs.
        if occurrences.count(2) == 2:
            yield 1
            for card in cards:
                if occurrences[card.value] == 2:
                    yield card.value
            for card in cards:
                if occurrences[card.value] != 2:
                    yield card.value
        else:
            yield 0

        # One Pair: Two cards of the same value.
        if 2 in occurrences:
            yield 1
            yield occurrences.index(2)
            for card in cards:
                if occurrences[card.value] != 2:
                    yield card.value
        else:
            yield 0

        # High Card: Highest value card.
        yield cards[0].value


def main():
    cnt = 0

    for it1, it2 in hands():
        v1 = v2 = 0

        while v1 == v2:
            v1 = it1.next()
            v2 = it2.next()

        if v1 > v2:
            cnt += 1
    return cnt


if __name__ == "__main__":
    print main()
