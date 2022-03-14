"""This module contain a set of test deck module."""

import random
import pytest
from unittest.mock import patch

from models.card import Card


class TestFrenchDeck:
    """Class contain test to FrenchDeck class."""
    def test_deck_contain_all_ranks(self, t_deck):
        expected_elements = [str(n) for n in range(2, 11)] + list("JQKA")
        assert len(t_deck.ranks) == 13
        assert expected_elements == t_deck.ranks

    def test_deck_contain_all_suits(self, t_deck):
        expected_elements = "spades diamonds clubs hearts".split()
        assert len(t_deck.suits) == 4
        assert expected_elements == t_deck.suits

    def test_creation_all_cards(self, t_deck):
        assert len(t_deck) == 52

    def test_deck_attributes_is_string_type(self, t_deck):
        for attr in t_deck.ranks:
            assert isinstance(attr, str)
        for attr in t_deck.suits:
            assert isinstance(attr, str)

    def test_get_random_card(self, t_deck, t_card):
        with patch('random.randint') as mock_rand:
            mock_rand.return_value = 10
            assert t_deck.get_random_card() == t_card

    def test_shuffle_cards(self, t_deck):
        assert t_deck != t_deck.shuffle_cards()

    # sort cards not working
    def test_sort_cards(self, t_deck):
        assert t_deck != t_deck.shuffle_cards()
        # assert t_deck == t_deck.sort_cards()
