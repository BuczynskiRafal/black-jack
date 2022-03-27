"""This module contains a simple deck class build on a card class."""

import random

from models.card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = [
            Card(color=color, value=value)
            for color in Card.possible_colors
            for value in Card.possible_values
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def hit(self):
        """Take one card from the deck."""
        return self.cards.pop()


deck = Deck()
