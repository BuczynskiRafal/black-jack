import time

from models.deck import FrenchDeck
from models.player import Player
from models.game import Game

deck = FrenchDeck()
human = Player(name="Human")
croupier = Player(name="Croupier")


desc = True
while desc:
    print("Starting game.\nCroupier shuffle the cards.")
    deck.shuffle_cards()
    time.sleep(1)
    print("Done.\n...\nTwo cards for human.")
    human.cards.append(deck.get_random_card())
    human.cards.append(deck.get_random_card())
    human.score()
    time.sleep(1)
    print(f"Your points: {human._score} and your cards: {human.cards}.\n...\nTwo cards for croupier.")

    if human.check_black_jack():
        print("Black jack, you win.")
        desc = False
        break

    if human.check_game_over():
        print('You lose')
        break

    croupier.cards.append(deck.get_random_card())
    croupier.cards.append(deck.get_random_card())
    print("...")
    print("Choose what to do next.")
    print("Click 1 to chose pass game.")
    print("Click 2 to chose take card.")
    break
