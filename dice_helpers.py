import random

RANKED_PAIRS = [
    [3, 1],
    [3, 2],
    [4, 1],
    [4, 2],
    [4, 3],
    [5, 1],
    [5, 2],
    [5, 3],
    [5, 4],
    [6, 1],
    [6, 2],
    [6, 3],
    [6, 4],
    [6, 5],
    [1, 1],
    [2, 2],
    [3, 3],
    [4, 4],
    [5, 5],
    [6, 6],
    [2, 1]
]

def roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return sorted([dice1, dice2], reverse=True)