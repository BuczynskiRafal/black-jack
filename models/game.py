from models.deck import deck
from models.player import Player
from exceptions import GameOverException, GameOverUserException, GameOverCroupierException


class Game:
    def __init__(self):
        self.deck = deck
        self.deck.shuffle()

    @staticmethod
    def _print_menu():
        print("Chose what next.")
        print("Type 1 to take card.")
        print("Type 2 to pass.")

    def _croupier_plays(self, user_points):
        croupier = Player()
        croupier_points = croupier.calculate_points()
        for _ in range(2):
            card = self.deck.hit()
            croupier.take_card(card)
        while croupier_points < user_points:

            return croupier_points

    def _user_plays(self):
        user = Player()
        for _ in range(2):
            card = self.deck.hit()
            user.take_card(card)
        while True:
            print(f"Your cards: {user.cards} and points: {user.calculate_points()}")
            print(user.calculate_points())
            self._print_menu()
            choice = input('Type 1 or 2\n')
            if choice == '1':
                user.take_card(self.deck.hit())
            elif choice == '2':
                return user.calculate_points()
            else:
                print('Wrong choice.')

    def play(self):
        try:
            user_points = self._user_plays()
        except GameOverException as error:
            raise GameOverUserException from error

        try:
            croupier_points = self._croupier_plays(user_points)
        except GameOverException as error:
            raise GameOverCroupierException from error
        print("You lose, croupier win.")