from models.card import Card

def test_calculate_player_points(t_player):
    first_card = Card('hearts', 5)
    second_card = Card('spades', 2)

    t_player.take_card(first_card)
    t_player.take_card(second_card)

    assert t_player.calculate_points() == 7


def test_calculate_player_points_hit_two_aces(t_player):
    first_card = Card('hearts', 'Ace')
    second_card = Card('spades', 'Ace')

    t_player.take_card(first_card)
    t_player.take_card(second_card)

    assert t_player.calculate_points() == 21


def test_calculate_player_points_hit_one_ace_two_cards(t_player):
    """[Ace, 5]"""
    first_card = Card('hearts', 'Ace')
    second_card = Card('spades', 5)

    t_player.take_card(first_card)
    t_player.take_card(second_card)

    assert t_player.calculate_points() == 6


def test_calculate_player_points_three_cards(t_player):
    """[Ace, Ace, Ace]"""
    first_card = Card('hearts', 'Ace')
    second_card = Card('spades', 'Ace')
    third_card = Card('diamonds', 'Ace')

    t_player.take_card(first_card)
    t_player.take_card(second_card)
    t_player.take_card(third_card)

    assert t_player.calculate_points() == 3
