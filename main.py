import time

from models.deck import FrenchDeck
from models.player import Player
# from models.game import Game
from models.deck import deck

human = Player(name="Human")
croupier = Player(name="Croupier")


print("Starting game.\nCroupier shuffle the cards.")
deck.shuffle_cards()
print("Done.\n...\nTwo cards for human.")
human.take_two_cards()
human.score()
print(f"Your points: {human._score} and your cards: {human.cards}.\n...\nTwo cards for croupier.\n...")
croupier.take_two_cards()
croupier.score()

desc = True
while desc:
    if human.check_black_jack():
        print("Black jack, you win.")
        desc = False
        break

    if human.check_game_over():
        print('You lose')
        break

    print("Click 1 to chose pass game.")
    print("Click 2 to chose take card.")

    number = input("Choose what to do next.")
    print(f'number: {number}')
    if number == 1:
        print(f'input == {number}')
        if human._score > croupier._score:
            print('Player Win!!!')
        else:
            print('You Lose.')
    elif number == 2:
        human.take_card()

    desc = False
























