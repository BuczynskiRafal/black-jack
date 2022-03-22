"""This module contains a simple card class"""

# from collections import namedtuple
#
# Card = namedtuple("Card", ["rank", "suit"])

####################################################


class InvalidColor(Exception):
    """Exception color is valid."""


class InvalidValue(Exception):
    """Exception value is valid."""


class Card:
    """Card abstraction"""
    possible_colors = {
        'spades': '\u2664',
        'diamonds': '\u2662',
        'hearts': '\u2661',
        'clubs': '\u2667'
    }
    possible_values = list(range(2, 11)) + ['Ace', 'Jack', 'Queen', 'King']

    def __init__(self, color, value):
        if color not in self.possible_colors:
            raise InvalidColor('Invalid card color.')
        self.color = self.possible_colors[color]

        if value not in self.possible_values:
            raise InvalidValue('Invalid card value.')
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value}, {self.color}'

