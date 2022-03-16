import time

from models.deck import deck
from models.player import human, croupier
from models.game import Game

game = Game()

counter = 0
desc = True
while desc:
    if counter == 0:
        game.game_beginning()

    if human.check_black_jack():
        print("Black jack, you win.")
        desc = False
        break

    if human.check_game_over():
        print('You lose')
        break

    print("Click 1 to chose pass game.")
    print("Click 2 to chose take card.")

    number = input("Choose what to do next.\n")
    if number == '1':
        if human._score > croupier._score:
            print('Player Win!!!')
            break
        else:
            print('You Lose.')
            break
    elif number == '2':
        human.take_card()
        human.score()
        print(f"Your points: {human._score} and your cards: {human.cards}.\n...")
