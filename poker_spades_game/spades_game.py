import spades_test as test
from numpy import random

CARDS = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')

left_cards = [random.choice(CARDS), random.choice(CARDS), random.choice(CARDS)]
right_cards = [random.choice(CARDS), random.choice(CARDS), random.choice(CARDS)]

def play_cards(left_hand, right_hand):
    scorecard = {'left_3_kind': test.check_3ofakind(*left_hand),
                 'right_3_kind': test.check_3ofakind(*right_hand),
                 'left_straight': test.check_straight(*left_hand),
                 'right_straight': test.check_straight(*right_hand),
                 'left_flush': test.check_royal_flush(*left_hand),
                 'right_flush': test.check_royal_flush(*right_hand)} 

    if scorecard['left_3_kind'] and scorecard['right_3_kind'] > 0:
        if scorecard['left_3_kind'] > scorecard['right_3_kind']:
            return -1
        elif scorecard['right_3_kind'] > scorecard['left_3_kind']:
            return 1
        else:
            return 0
        
    if scorecard['left_flush'] or scorecard['right_flush'] > 0:
        if scorecard['left_flush'] == scorecard['right_flush']:
            return 0
        elif scorecard['left_flush'] > 0:
            return -1
        else:
            return 1
    
    if scorecard['left_straight'] and scorecard['right_straight'] > 0:
        if scorecard['left_straight'] == scorecard['right_straight']:
            return 0
        elif scorecard['left_straight'] > scorecard['right_straight']:
            return -1
        else:
            return 1

    if scorecard['left_straight'] > 0 and scorecard['right_3_kind'] >= 0:
        return -1
    elif scorecard['right_straight'] > 0 and scorecard['left_3_kind'] >= 0:
        return 1
    else:
        return 0
    
if __name__ == '__main__':
    print(f'Left hand: {left_cards} \nRight hand: {right_cards}')
    
    print(play_cards(left_cards, right_cards))
   
    if play_cards(left_cards, right_cards) == -1:
        print('Left won this hand.')
    elif play_cards(left_cards, right_cards) == 1:
        print('Right won this hand.')
    else:
        print('This hand is a draw.')
