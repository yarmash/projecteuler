#!/usr/bin/env python3

"""Problem 54: Poker Hands"""

from utils import get_path


class Card:
    __slots__ = ("kind", "suit", "value")

    # values are powers of 2
    values = {v: 1 << i for i, v in enumerate("23456789TJQKA")}

    def __init__(self, kind, suit):
        self.kind = kind
        self.suit = suit
        self.value = Card.values[kind]

    def __repr__(self):
        return self.kind + self.suit


class Hand:
    __slots__ = ("values", "same_suit", "straight", "quad", "trip", "pairs")

    # bitmasks of consecutive values, mapped to the straight's rank;
    # in the wheel (A-2-3-4-5) the ace plays low, so it ranks lowest
    straights = {0b1000000001111: 1, **{0b11111 << i: i + 2 for i in range(9)}}

    def __init__(self, cards):
        self.same_suit = cards[0].suit == cards[1].suit == cards[2].suit == \
            cards[3].suit == cards[4].suit

        values = quad = trip = pairs = 0

        for card in cards:
            value = card.value

            if value & values:
                if value & pairs:
                    if value & trip:
                        quad |= value
                    else:
                        trip |= value
                else:
                    pairs |= value
            else:
                values |= value

        pairs ^= trip
        trip ^= quad

        self.values = values
        self.quad = quad
        self.trip = trip
        self.pairs = pairs

        # 0 if not a straight, otherwise the straight's rank
        self.straight = Hand.straights.get(values, 0)

    def __lt__(self, other):
        """Make instances of the class comparable"""
        for ours, theirs in zip(self.terms(), other.terms()):
            if ours != theirs:
                return ours < theirs

    def terms(self):
        """Generate terms for comparison"""

        # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        # Is a case of Straight Flush.

        # Straight Flush: All cards are consecutive values of same suit.
        if self.straight and self.same_suit:
            yield self.straight
        else:
            yield 0

        # Four of a Kind: Four cards of the same value.
        yield self.quad

        # Full House: Three of a kind and a pair.
        if self.trip and self.pairs:
            yield self.trip
        else:
            yield 0

        # Flush: All cards of the same suit.
        if self.same_suit:
            yield self.values
        else:
            yield 0

        # Straight: All cards are consecutive values.
        yield self.straight

        # Three of a Kind: Three cards of the same value.
        if self.trip:
            yield self.trip
            yield self.trip ^ self.values
        else:
            yield 0

        # Two Pairs: Two different pairs.
        if self.pairs and (self.pairs & (self.pairs-1)):
            yield self.pairs
            yield self.pairs ^ self.values
        else:
            yield 0

        # One Pair: Two cards of the same value.
        if self.pairs:
            yield self.pairs
            yield self.pairs ^ self.values
        else:
            yield 0

        # High Card: Highest value card.
        yield self.values


def main():
    cnt = 0

    deck = {kind+suit: Card(kind, suit) for kind in "23456789TJQKA"
            for suit in "CDHS"}

    with get_path("data", "poker.txt").open() as data_file:
        for line in data_file:
            cards = [deck[card] for card in line.split()]  # example: 9C JD

            if Hand(cards[:5]) > Hand(cards[5:]):
                cnt += 1

    return cnt


if __name__ == "__main__":
    print(main())
