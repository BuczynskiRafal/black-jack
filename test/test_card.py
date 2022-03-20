"""This module contains a set of test card class."""

import pytest

from models.card import Card, InvalidColor, InvalidValue


def test_creation():
    """Test in I can create valid card."""
    card = Card('hearts', 'Ace')
    assert card.color == '♡'
    assert card.value == 'Ace'


def test_creation_wrong_value():
    """Test if code raise exception when wrong value."""
    with pytest.raises(InvalidValue) as message:
        Card('hearts', 'A')
        assert message == 'Invalid card value.'


def test_creation_wrong_color():
    """Test if code raise exception when wrong color."""
    with pytest.raises(InvalidColor) as message:
        Card('xxx', 'A')
        assert message == 'Invalid card color.'


def test_card_representation():
    """Test if card has correct card representation."""
    card = Card('hearts', 'Ace')
    assert repr(card) == 'Ace, ♡'
