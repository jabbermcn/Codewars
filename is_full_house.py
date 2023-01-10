# def is_one_pair(hand):
#     """returns True for one pair, else False."""
#     hand_values = [card for card in hand]
#     val_count = {card: hand_values.count(card) for card in hand_values}
#     pair_val = [card for card in hand_values if hand_values.count(card) == 2]
#     pair_count = sum(1 for val in val_count.values() if val == 2)
#     if pair_count == 1:
#         return True, pair_val[0]
#     return False
#
#
# def is_three_of_a_kind(hand):
#     """returns True for three of a kind, else False."""
#     hand_values = [card for card in hand]
#     val_count = {card: hand_values.count(card) for card in hand_values}
#     if 3 in val_count.values():
#         return True
#     return False
#
#
# def is_full_house(hand):
#     """returns True for a full house, False otherwise."""
#     if is_one_pair(hand) and is_three_of_a_kind(hand):
#         return True
#     return False
#
#
# print(is_full_house(["A", "A", "A", "K", "K"]))


def is_full_house(hand):
    return all([hand.count(i) >= 2 for i in hand])
