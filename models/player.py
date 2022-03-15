from models.deck import FrenchDeck
from models.deck import deck


class Player:
    def __init__(self, name):
        self._name = name
        self.cards = []
        self._score = 0

    def take_card(self):
        self.cards.append(deck.get_random_card())

    def take_two_cards(self):
        self.cards.append(deck.get_random_card())
        self.cards.append(deck.get_random_card())

    def sort_cards(self):
        return sorted(self.cards, key=lambda x: x[0])

    def check_black_jack(self):
        if self.cards[0][0] and self.cards[1][0] == "A" and len(self.cards) == 2:
            return True

    def score(self):
        if Player.check_black_jack(self):
            self._score = 21
        elif Player.sort_cards(self)[0][0] == "A" and Player.sort_cards(self)[1][0] in "JQK" and len(self.cards) == 2:
            self._score = 21
        else:
            try:
                for rank, _ in self.cards:
                    self._score += int(rank)
            except (TypeError, ValueError):
                self._score += 10

    def check_game_over(self):
        return True if self._score > 21 else False




