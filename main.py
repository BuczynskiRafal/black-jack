from models.game import Game
from exceptions import GameOverException, GameOverUserException, GameOverCroupierException
try:
    game = Game()
    game.play()
except GameOverCroupierException:
    print("You Win!!!")
except GameOverException:
    print("You Lose.")

