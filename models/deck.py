"""This module contains a simple deck class build on a card class."""

import random

from models.card import Card


# class FrenchDeck:
#     """
#     FrenchDeck class allow you to create single object contained all
#     cards like real french deck.
#     """
#
#     ranks = [str(n) for n in range(2, 11)] + list("JQKA")
#     suits = "spades diamonds clubs hearts".split()
#
#     def __init__(self):
#         self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]
#
#     def __len__(self):
#         return len(self._cards)
#
#     def __getitem__(self, position):
#         return self._cards[position]

class Deck:
    def __init__(self) -> None:
        self.cards = [
            Card(color=color, value=value)
            for color in Card.possible_colors
            for value in Card.possible_values
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def take_card(self):
        """Take one card from the deck."""
        self.cards.pop()
