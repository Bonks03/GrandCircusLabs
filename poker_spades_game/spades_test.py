CARDS = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')

def check_3ofakind(card1, card2, card3):
    if card1 == card2 == card3:
        return (CARDS.index(card1) + 2)
    else:
        return 0


def check_straight(card1, card2, card3):
    hand = [card1, card2, card3]
    tuple_index = []
    # Checks for duplicates in list
    if len(set(hand)) < len(hand):
        return 0
    else:
        # Adds the index to the list instead of the card. Simplifies the sequence check
        for card in hand:    
            tuple_index.append(CARDS.index(card))
        sorted_hand = sorted(tuple_index)
        low_card, mid_card, high_card = sorted_hand[0], sorted_hand[1], sorted_hand[2]
        # Checks if cards are in order by checking if the indexes are only 1 apart
        if (mid_card + 1) == high_card and (mid_card - 1) == low_card:
            return (high_card + 2)   
        # Returns 0 if cards are different but not sequential
        else:
            return 0


def check_royal_flush(card1, card2, card3):
    straight = check_straight(card1, card2, card3)
    if straight >= 12:
        return straight
    else:
        return 0