import random

def roll():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return sorted([dice1, dice2], reverse=True)