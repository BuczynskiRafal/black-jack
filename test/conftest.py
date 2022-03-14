from pytest import fixture

from models.card import Card
from models.player import Player
from models.deck import FrenchDeck


@fixture
def t_card():
    return Card(rank='4', suit='clubs')


@fixture
def t_player():
    return Player(name='test_player')


@fixture
def t_deck():
    return FrenchDeck()


