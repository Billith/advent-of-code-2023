from enum import IntEnum

class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7

CARDS = {
    'J': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'Q': 10,
    'K': 11,
    'A': 12,
}

class Hand():
    def __init__(self, hand: str, bid: int) -> None:
        self.hand = hand
        self.bid = bid
        self.set_hand_type()
    
    def __repr__(self) -> str:
        return f"<Hand hand='{self.hand}', bid={self.bid}, type={self.type}>"
    
    def __lt__(self, other) -> bool:
        if self.type != other.type:
            return self.type < other.type

        for h1, h2 in zip(self.hand, other.hand):
            if h1 == h2:
                continue
            else:
                return CARDS[h1] < CARDS[h2]

        return False
    
    def set_hand_type(self):
        char_freq = {}

        for char in self.hand:
            if char in char_freq:
                continue

            char_freq[char] = self.hand.count(char)

        if 'J' in char_freq.keys():
            joker_val = char_freq['J']
            del char_freq['J']

            if len(char_freq.keys()) > 0:
                char_freq[max(char_freq, key=char_freq.get)] += joker_val
            else:
                char_freq['A'] = joker_val

        if 5 in char_freq.values():
            self.type = HandType.FIVE_OF_A_KIND
        elif 4 in char_freq.values():
            self.type = HandType.FOUR_OF_A_KIND
        elif all([x in char_freq.values() for x in [3,2]]):
            self.type = HandType.FULL_HOUSE
        elif 3 in char_freq.values():
            self.type = HandType.THREE_OF_A_KIND
        elif list(char_freq.values()).count(2) == 2:
            self.type = HandType.TWO_PAIR
        elif 2 in char_freq.values():
            self.type = HandType.ONE_PAIR
        else:
            self.type = HandType.HIGH_CARD
        
def solve(input: str) -> int:
    hands = sorted([Hand(hand, int(bid)) for hand, bid in [line.split() for line in input.strip().splitlines()]])
    winnings = []

    for i, hand in enumerate(hands):
        winnings.append(hand.bid * (i + 1))

    return sum(winnings)

def test() -> None:
    input = '''
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
'''
    result = solve(input)
    assert result == 5905, f'unexpected result -> {result}'

test()
print(solve(open('input.txt').read()))
