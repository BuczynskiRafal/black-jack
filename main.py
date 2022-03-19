import time

from models.deck import deck
from models.player import human, croupier
from models.game import Game

game = Game()
game.game_beginning()
game.advance_game()
