from pytest import fixture

from models.card import Card
from models.deck import Deck


@fixture
def t_card():
    return Card('hearts', 'Ace')


@fixture
def t_deck():
    return Deck()


# @fixture
# def t_player():
#     return Player(name='test_player')
#
#
