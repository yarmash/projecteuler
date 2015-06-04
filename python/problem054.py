#!/usr/bin/python

"""Problem 54: Poker hands"""

from utils import open_data_file


class Card(object):
    values = {kind: val for val, kind in enumerate("23456789TJQKA", 2)}
    __slots__ = ("kind", "value", "suit")

    def __init__(self, kind, suit):
        self.kind = kind
        self.suit = suit
        self.value = Card.values[kind]

    def __repr__(self):
        return self.kind + self.suit


class Hand(object):
    __slots__ = ("values", "same_suit", "consecutive_values")

    def __init__(self, cards):
        self.same_suit = cards[0].suit == cards[1].suit == cards[2].suit == \
            cards[3].suit == cards[4].suit

        values = [card.value for card in cards]
        values.sort(reverse=True)

        self.consecutive_values = values[0] == values[1] + 1 == \
            values[2] + 2 == values[3] + 3 == values[4] + 4

        self.values = values

    def __lt__(self, other):
        """Make instances of the class comparable"""
        for ours, theirs in zip(self.terms(), other.terms()):
            if ours != theirs:
                return ours < theirs

    def terms(self):
        """Generate terms for comparison"""

        values = self.values

        # save the number of occurrences for each value
        occurrences = [0]*15
        for val in values:
            occurrences[val] += 1

        # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        # Is a case of the straight flush.

        # Straight Flush: All cards are consecutive values of same suit.
        if self.consecutive_values and self.same_suit:
            yield values[0]
        else:
            yield 0

        # Four of a Kind: Four cards of the same value.
        if 4 in occurrences:
            yield occurrences.index(4)
        else:
            yield 0

        # Full House: Three of a kind and a pair.
        if 3 in occurrences and 2 in occurrences:
            yield occurrences.index(3)
        else:
            yield 0

        # Flush: All cards of the same suit.
        if self.same_suit:
            yield values[0]
        else:
            yield 0

        # Straight: All cards are consecutive values.
        if self.consecutive_values:
            yield values[0]
        else:
            yield 0

        # Three of a Kind: Three cards of the same value.
        if 3 in occurrences:
            yield occurrences.index(3)
            for val in values:
                if occurrences[val] != 3:
                    yield val
        else:
            yield 0

        # Two Pairs: Two different pairs.
        if occurrences.count(2) == 2:
            for val in values:
                if occurrences[val] == 2:
                    yield val
                else:
                    unpaired = val
            yield unpaired
        else:
            yield 0

        # One Pair: Two cards of the same value.
        if 2 in occurrences:
            yield occurrences.index(2)
            for val in values:
                if occurrences[val] != 2:
                    yield val
        else:
            yield 0

        # High Card: Highest value card.
        yield values[0]


def main():
    cnt = 0

    deck = {kind+suit: Card(kind, suit) for kind in "23456789TJQKA"
            for suit in "CDHS"}

    with open_data_file("poker.txt") as data_file:
        for line in data_file:
            cards = [deck[card] for card in line.split()]  # example: 9C JD

            if Hand(cards[:5]) > Hand(cards[5:]):
                cnt += 1

    return cnt

if __name__ == "__main__":
    print(main())
