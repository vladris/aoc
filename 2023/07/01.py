hands = [tuple(line.strip().split(' ')) for line in open('input').readlines()]

CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

FIVEKIND = 7000000
FOURKIND = 6000000
FULLHOUSE = 5000000
THREEKIND = 4000000
TWOPAIR = 3000000
ONEPAIR = 2000000
HIGHCARD = 1000000

def evalHand(hand):
    count = [hand.count(card) for card in set(hand)]
    score = CARDS.index(hand[0]) * 13 ** 4 + CARDS.index(hand[1]) * 13 ** 3 + \
        CARDS.index(hand[2]) * 13 ** 2 + CARDS.index(hand[3]) * 13 + CARDS.index(hand[4])
        
    if count[0] == 5:
        return FIVEKIND + score
    if 4 in count:
        return FOURKIND + score
    if 3 in count and 2 in count:
        return FULLHOUSE + score
    if 3 in count:
        return THREEKIND + score
    if count.count(2) == 2:
        return TWOPAIR + score
    if 2 in count:
        return ONEPAIR + score
    return HIGHCARD + score

hands.sort(key=lambda handBid: evalHand(handBid[0]))

print(sum([int(handBid[1]) * (i + 1) for i, handBid in enumerate(hands)]))
