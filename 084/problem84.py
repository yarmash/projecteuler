#!/usr/bin/python

"""Problem 84: Monopoly odds"""

from random import randint, shuffle


class Dice(object):
    """Represents a pair of dice"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return [randint(1, self.sides), randint(1, self.sides)]


class Deck(object):
    """Represents a deck of Chance or Community Chest cards"""
    def __init__(self):
        cards = list(range(16))
        shuffle(cards)
        self.cards = cards
        self.index = 0

    def draw(self):
        card = self.cards[self.index]
        self.index = self.index + 1 if self.index < 15 else 0
        return card


def main():
    dice = Dice(sides=4)
    ch_deck = Deck()
    cc_deck = Deck()
    position = 0
    visits = [0]*40
    doubles = 0  # consecutive doubles

    for i in range(1000000):
        roll = dice.roll()

        if roll[0] == roll[1]:
            doubles += 1
            if doubles == 3:
                position = 10
                visits[10] += 1
                doubles = 0
                continue
        else:
            doubles = 0

        score = roll[0] + roll[1]
        position = (position + score) % 40

        if position in (7, 22, 36):  # CH[123]
            card = ch_deck.draw()

            if card == 0:    # "Advance to GO"
                position = 0
            elif card == 1:  # "Go to JAIL"
                position = 10
            elif card == 2:  # "Go to C1"
                position = 11
            elif card == 3:  # "Go to E3"
                position = 24
            elif card == 4:  # "Go to H2"
                position = 39
            elif card == 5:  # "Go to R1"
                position = 5
            elif card == 6 or card == 7:  # "Go to next R" (there are two of these)
                if position == 7:
                    position = 15
                elif position == 22:
                    position = 25
                else:
                    position = 5
            elif card == 8:  # "Go to next U":
                if position == 22:
                    position = 28
                else:
                    position = 12
            elif card == 9:  # "Go back 3 squares":
                position -= 3

        # CC should be checked after CH to allow for moving back 3 from CH3
        if position in (2, 17, 33):  # CC[123]
            card = cc_deck.draw()

            if card == 0:    # "Advance to GO":
                position = 0
            elif card == 1:  # "Go to JAIL":
                position = 10
        elif position == 30:  # G2J
            position = 10

        visits[position] += 1

    return "".join(["{0:02d}".format(i) for i in
        sorted(range(len(visits)), key=lambda x: visits[x], reverse=True)][0:3])

if __name__ == "__main__":
    print(main())
