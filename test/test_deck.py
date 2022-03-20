"""This module contain a set of test deck module."""

from models.card import Card


def test_creation(t_deck):
    """Test all cards will be created."""
    assert len(t_deck.cards) == 52

def test_deck(t_deck):
    """Test deck test contains all values and colors."""
    cards = [(card.value, card.color) for card in t_deck.cards]
    for color in Card.possible_colors:
        heart_cards = [card for card in cards if card[1] == '♡']
        assert len(heart_cards) == 13

def test_shuffle(t_deck):
    """Test if the deck is shuffled correctly."""
    shuffled = t_deck.shuffle()
    assert t_deck.cards != shuffled

def test_take_card(t_deck):
    """Test if the card is correctly drawn from the deck."""
    last_card = t_deck.cards[-1]
    take_card = t_deck.take_card()
    assert last_card == take_card

def test_deck_count_card(t_deck):
    """There is no check or drawn card in the deck."""
    card = t_deck.take_card()
    assert len(t_deck.cards) == 51
    assert card not in t_deck.cards
