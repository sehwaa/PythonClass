from random import randrange

winning = randrange(1, 11)

def pirate_roulette_game(hole=7):
    if hole == winning:
        return True
    return False

print(pirate_roulette_game())