import random

def RollDice(amountOfDice):
    possibleFaces = [1, 2, 3, 4, 5, 6]
    results = []
    for die in range(amountOfDice):
        roll = random.choice(possibleFaces)
        results.append(roll)
    return results
