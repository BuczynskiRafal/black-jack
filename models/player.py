class Player:

    def __init__(self, name):
        self._name = name
        self.cards = []
        self._score = 0

    def score(self):
        if self.cards[0][0] and self.cards[1][0] == 'A':
            self._score = 21
        else:
            for rank, _ in self.cards:
                if rank not in 'JPQKA':
                    self._score += int(rank)
                else:
                    self._score += 10
