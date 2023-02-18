import random

print('Welcome to the Dice Roller App')
print('--------------------------------')

# Validate Input
while True:
    try:
        numberPicked = int(input('Pick a number between 1 and 10: '))
        if numberPicked > 0 and numberPicked <= 10:
            break
        else:
            print('Invalid input. Try again.')
    except:
        print('Please provide a number')
        
# Roll the dice
def RollDice(amountOfDice):
    possibleFaces = [1, 2, 3, 4, 5, 6]
    for die in range(amountOfDice):
        roll = random.choice(possibleFaces)
        print('Die ', die + 1, ' rolled a ', roll, sep='')
        
RollDice(numberPicked)
