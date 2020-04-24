from deck import draw_cards
from itertools import cycle

exercises = {
        '♠️' : cycle(('(Inclined) Push-Up',
                     'Pike/Vertical Push-Up',
                     'Standing Dumbbell Press',
                     'Lateral Raises (jug/doorway/band)')),
        '♣️' : cycle(('Pull-Up',
                     'Inverted Row',
                     'Rear Delt Fly',
                     'Upright Row')),
        '♥️' : cycle(('Walking Lunges',
                     'Bulgarian Split Squat',
                     'Single Leg Hip Thrust',
                     'Nordic Hamstrings Curl')),
        '♦️' : cycle(('Bicep Curls',
                     'Skullcrushers w/ table -or- Close grip Push-Ups',
                     'Bycycle/Reverse Crunch',
                     'Standing Calf Raise')),
    }

def calculate_set(suit, number):
    if type(number) is int:
        reps = number+10
    elif number != 'A':
        reps = 20
    else:
        return "2' Rest"
    return (reps, next(exercises[suit]))

workout = lambda n: ((s, calculate_set(*s)) for s in draw_cards(n))
