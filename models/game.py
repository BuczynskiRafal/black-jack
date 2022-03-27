from models.deck import Deck
from models.player import Player, GameOverException, GameOverUserException


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    @staticmethod
    def _print_menu():
        print("Chose what next.")
        print("Type 1 to take card.")
        print("Type 2 to pass.")

    def _user_plays(self):
        user = Player()
        print(self.deck.__dict__)
        for _ in range(2):
            print(self.deck.hit())
            card = self.deck.hit()
            print(card)
            user.take_card(card)
        while True:
            print(f"Your cards: {user.cards} and points: {user.calculate_points()}")
            self._print_menu()
            choice = input('Type 1 or 2\n')
            if choice == '1':
                user.take_card(self.deck.hit())
            elif choice == '2':
                break
            else:
                print('Wrong choice.')

    def play(self):
        try:
            self._user_plays()
        except GameOverException as error:
            raise GameOverUserException from error
