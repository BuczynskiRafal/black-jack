"""This module contain a set of test deck module."""

import random

class TestFrenchDeck:
    """Class contain test to FrenchDeck class."""
    def test_deck_contain_all_ranks(self, t_deck):
        expected_elements = [str(n) for n in range(2, 11)] + list("JPQKA")
        assert len(t_deck.ranks) == 14
        assert expected_elements == t_deck.ranks

    def test_deck_contain_all_suits(self, t_deck):
        expected_elements = "spades diamonds clubs hearts".split()
        assert len(t_deck.suits) == 4
        assert expected_elements == t_deck.suits

    def test_deck_attributes_is_string_type(self, t_deck):
        for attr in t_deck.ranks:
            assert isinstance(attr, str)
        for attr in t_deck.suits:
            assert isinstance(attr, str)

    def test_get_random_card(self, t_deck, mocker):
        mocker.patch('random.randint')
        assert t_deck.get_random_card()


