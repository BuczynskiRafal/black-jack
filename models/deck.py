import random

from models.card import Card


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JPQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [
            Card(rank, suit) for rank in self.ranks for suit in self.suits
        ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def get_random_card(self):
        rand_index = random.randint(1, len(self._cards))
        return self._cards.pop(rand_index)

    def shuffle_cards(self):
        return random.shuffle(self._cards)


