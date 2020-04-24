from itertools import product
from pprint import pprint
from random import sample

def draw_cards(n=20):
    suits = {'♠️', '♥️', '♣️', '♦️'}
    numbers = set(range(2, 11)).union({'J', 'Q', 'K', 'A'})

    deck = set(product(suits, numbers))

    hand = sample(deck, k=n)
    for c in hand:
        yield c
