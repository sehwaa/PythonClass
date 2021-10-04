from random import randrange

winning = randrange(1, 11) # 1 ~ 10

def pirate_roulette_game(hole):
    if hole == winning:
        return True
    return False

print(pirate_roulette_game(3))