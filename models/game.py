from models.deck import deck, FrenchDeck
from models.player import human, croupier, Player


class Game:

    def __init__(self):
        self.deck = FrenchDeck()
        self.human = Player(name='human')
        self.croupier = Player(name='croupier')

    def game_beginning(self):
        print("Starting game.\nCroupier shuffle the cards.")
        self.deck.shuffle_cards()
        print("Done.\n...\nTwo cards for human.")
        self.human.take_two_cards()
        self.human.score()
        print(f"Your points: {self.human._score} and your cards: {self.human.cards}.\n...\nTwo cards for croupier.\n...")
        self.croupier.take_two_cards()
        self.croupier.score()

    def advance_game(self):
        desc = True
        while desc:
            if self.human.check_black_jack():
                print("Black jack, you win.")
                desc = False
                break
            if self.human.check_game_over():
                print('You lose')
                break

            print("Click 1 to chose pass game.")
            print("Click 2 to chose take card.")

            number = input("Choose what to do next.\n")
            if number == '1':
                if self.human._score > self.croupier._score:
                    print(f"Your points: {self.human._score} and your cards: {self.human.cards}.")
                    print(f"Croupier points: {self.croupier._score} and his cards: {self.croupier.cards}.")
                    print('Player Win!!!')
                    break
                else:
                    print(f"Your points: {self.human._score} and your cards: {self.human.cards}.")
                    print(f"Croupier points: {self.croupier._score} and his cards: {self.croupier.cards}.")
                    print('You Lose.')
                    break
            elif number == '2':
                self.human.take_card()
                self.human.score()
                print(f"Your points: {self.human._score} and your cards: {self.human.cards}.")
                print(f"Croupier points: {self.croupier._score} and his cards: {self.croupier.cards}.")

