#!/usr/bin/python

"""Problem 54: Poker hands"""

from utils import open_data_file
from operator import attrgetter


class Card(object):
    values = dict(zip("23456789TJQKA", range(2, 15)))
    suits = {s[0]: s for s in ("Clubs", "Diamonds", "Hearts", "Spades")}
    __slots__ = ("kind", "value", "suit")

    def __init__(self, data):
        self.kind, self.suit = data  # example: 9C JD
        self.value = Card.values[self.kind]

    def __repr__(self):
        return "%s%s" % (self.kind, Card.suits[self.suit])


class Hand(object):
    __slots__ = ("cards", "same_suit", "consecutive_values")

    def __init__(self, cards):
        cards.sort(key=attrgetter("value"), reverse=True)

        self.cards = cards

        self.same_suit = cards[0].suit == cards[1].suit == cards[2].suit == \
            cards[3].suit == cards[4].suit

        self.consecutive_values = cards[0].value == cards[1].value + 1 == \
            cards[2].value + 2 == cards[3].value + 3 == cards[4].value + 4


class Evaluator(object):
    @staticmethod
    def terms(hand):
        """Generate terms for hands' comparison"""

        cards = hand.cards

        # save the number of occurrences for each value
        occurrences = [0]*15
        for card in cards:
            occurrences[card.value] += 1

        # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        # Is a case of the straight flush.

        # Straight Flush: All cards are consecutive values of same suit.
        if hand.consecutive_values and hand.same_suit:
            yield cards[0].value
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
        if hand.same_suit:
            yield cards[0].value
        else:
            yield 0

        # Straight: All cards are consecutive values.
        if hand.consecutive_values:
            yield cards[0].value
        else:
            yield 0

        # Three of a Kind: Three cards of the same value.
        if 3 in occurrences:
            yield occurrences.index(3)
            for card in cards:
                if occurrences[card.value] != 3:
                    yield card.value
        else:
            yield 0

        # Two Pairs: Two different pairs.
        if occurrences.count(2) == 2:
            for card in cards:
                if occurrences[card.value] == 2:
                    yield card.value
                else:
                    unpaired = card.value
            yield unpaired
        else:
            yield 0

        # One Pair: Two cards of the same value.
        if 2 in occurrences:
            yield occurrences.index(2)
            for card in cards:
                if occurrences[card.value] != 2:
                    yield card.value
        else:
            yield 0

        # High Card: Highest value card.
        yield cards[0].value

    def compare(self, hand1, hand2):
        for term1, term2 in zip(self.terms(hand1), self.terms(hand2)):
            if term1 == term2:
                continue
            if term1 > term2:
                return 1
            return -1


def main():
    cnt = 0
    evaluator = Evaluator()

    with open_data_file("poker.txt") as data_file:
        for line in data_file:
            cards = [Card(c) for c in line.split()]
            if evaluator.compare(Hand(cards[:5]), Hand(cards[5:])) > 0:
                cnt += 1

    return cnt

if __name__ == "__main__":
    print(main())
