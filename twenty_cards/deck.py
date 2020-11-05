from itertools import product
from pprint import pprint
from random import sample

cards = [
    ['🂡', '🂢', '🂣', '🂤', '🂥', '🂦', '🂧', '🂨', '🂩', '🂪', '🂫', '🂬', '🂭', '🂮'],
    ['🂱', '🂲', '🂳', '🂴', '🂵', '🂶', '🂷', '🂸', '🂹', '🂺', '🂻', '🂼', '🂽', '🂾'],
    ['🃁', '🃂', '🃃', '🃄', '🃅', '🃆', '🃇', '🃈', '🃉', '🃊', '🃋', '🃌', '🃍', '🃎'],
    ['🃑', '🃒', '🃓', '🃔', '🃕', '🃖', '🃗', '🃘', '🃙', '🃚', '🃛', '🃜', '🃝', '🃞']
]

def draw_cards(n=20):
    suits = {'♠️', '♥️', '♦️', '♣️'}
    numbers = set(range(2, 11)).union({'J', 'Q', 'K', 'A'})

    deck = set(product(suits, numbers))

    hand = sample(deck, k=n)
    for c in hand:
        yield c

def card_char(identifier):
    suits = {'♠️':0, '♥️':1, '♦️':2, '♣️':3}
    numbers = { number: idx for idx, number in enumerate(['A'] + list(range(2, 11)) + ['J', 'Q', 'K']) }

    suit, number = identifier

    suit_id, number_id = suits.get(suit), numbers.get(number)

    return cards[suit_id][number_id]