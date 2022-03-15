from models.deck import FrenchDeck
from models.player import Player


class Game:

    def __init__(self):
        pass

    @staticmethod
    def get_two_cards():
        FrenchDeck.get_random_card()
        FrenchDeck.get_random_card()

    #     print('Starting game.')
    #     self.deck = FrenchDeck()
    #     self.human = Player(name="Human")
    #     self.croupier = Player(name="Croupier")

    # def play_game(self):
    #     pass
    #
    # def take_two_cards(self):
    #     print('Take two cards.')
    #
    #
    # def show_points(self):
    #     pass
    #
    # def check_game_over(self):
    #     pass
        # if Player.

    # @staticmethod
    # def player_chose(number=input()):
    #     print("Choose what to do next.")
    #     print("Click 1 to chose pass game.")
    #     print("Click 2 to chose take card.")
    #     return number
