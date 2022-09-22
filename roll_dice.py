import random

roll = random.randint(1,6)
guess = int(input('Guess the dice roll:\n'))

if guess==roll:
    print ('Slayed! You got it right! The dice rolled a ' + str(roll))
else:
    print('HA HA you wished but failed, they rolled a '+ str(roll))