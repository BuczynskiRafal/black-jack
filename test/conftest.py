from pytest import fixture

from models.card import Card
from models.player import Player
from models.deck import FrenchDeck


@fixture
def t_card():
    return Card()


@fixture
def t_player():
    return Player()


@fixture
def t_deck():
    return FrenchDeck()


