hands = [tuple(line.strip().split(' ')) for line in open('input').readlines()]

CARDS = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

FIVEKIND = 7000000
FOURKIND = 6000000
FULLHOUSE = 5000000
THREEKIND = 4000000
TWOPAIR = 3000000
ONEPAIR = 2000000
HIGHCARD = 1000000

def possibleHands(hand):
    if 'J' not in hand or hand.count('J') == 5:
        return [hand]

    result = []
    for i, card in enumerate(hand):
        if card == 'J':
            for opt in set(hand):
                if opt != 'J':
                    result += possibleHands(hand[:i] + opt + hand[i + 1:])
    return result


def scoreHand(hand):
    return CARDS.index(hand[0]) * 13 ** 4 + CARDS.index(hand[1]) * 13 ** 3 + \
        CARDS.index(hand[2]) * 13 ** 2 + CARDS.index(hand[3]) * 13 + CARDS.index(hand[4])


def evalHand(hand):
    count = [hand.count(card) for card in set(hand)]
        
    if count[0] == 5:
        return FIVEKIND
    if 4 in count:
        return FOURKIND
    if 3 in count and 2 in count:
        return FULLHOUSE
    if 3 in count:
        return THREEKIND
    if count.count(2) == 2:
        return TWOPAIR
    if 2 in count:
        return ONEPAIR
    return HIGHCARD

def evalHands(hand):
    return max([evalHand(hand) for hand in possibleHands(hand)]) + scoreHand(hand)

hands.sort(key=lambda handBid: evalHands(handBid[0]))

print(sum([int(handBid[1]) * (i + 1) for i, handBid in enumerate(hands)]))
