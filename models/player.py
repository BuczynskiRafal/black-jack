from models.deck import FrenchDeck


class Player:
    def __init__(self, name):
        self._name = name
        self.cards = []
        self._score = 0

    def sort_cards(self):
        return sorted(self.cards, key=lambda x: x[0])

    def check_black_jack(self):
        if self.cards[0][0] and self.cards[1][0] == "A" and len(self.cards) == 2:
            return True

    def score(self):
        if Player.check_black_jack(self):
            self._score = 21
        elif Player.sort_cards(self)[0][0] == "A" and Player.sort_cards(self)[1][0] in "JPQK" and len(self.cards) == 2:
            self._score = 21
        else:
            for rank, _ in self.cards:
                if rank not in "JPQKA":
                    self._score += int(rank)
                else:
                    self._score += 10

