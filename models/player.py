from models.card import Card


class Player:
    def __init__(self):
        self.cards = []

    def take_card(self, card: Card):
        self.cards.append(card)

    def calculate_points(self):
        points = 0
        number_of_aces = len([card for card in self.cards if card.value == 'Ace'])
        if number_of_aces == 2:
            return 21
        if number_of_aces == 1 and len(self.cards) == 2:
            return 10
        for card in self.cards:
            if card.value in ['Ace', ]:
                points += 1
            if card.value in ['Jack', 'Queen', 'King']:
                points += 10
            else:
                points += card.value
        return points


player = Player()
first_card = Card('hearts', 'Ace')
second_card = Card('spades', 'Ace')
third_card = Card('diamonds', 'Ace')

player.take_card(first_card)
player.take_card(second_card)
player.take_card(third_card)
for card in player.cards:
    print(card.value)
print(player.calculate_points())
