import time

from models.deck import FrenchDeck
from models.player import Player

deck = FrenchDeck()
human = Player(name='Human')
croupier = Player(name='Croupier')

print('Starting game.')
print('Croupier shuffle the cards.')
deck.shuffle_cards()
time.sleep(1)
print('Done')
print('...')
print('Two cards for human.')
human.cards.append(deck.get_random_card())
human.cards.append(deck.get_random_card())
human.score()
time.sleep(1)
print(f'Your cards: {human.cards} and your points: {human._score}.')
print('...')
print('Two cards for croupier.')
croupier.cards.append(deck.get_random_card())
croupier.cards.append(deck.get_random_card())
print('...')



