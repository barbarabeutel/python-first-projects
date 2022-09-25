import random

def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

def main():
    player1 = input("What's the first player's name?")
    player2 = input("What's the second player's name?")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print (player1, "rolled", roll1)
    print (player2, "rolled", roll2)

    if roll1>roll2:
        print(player1, "wins!")
    elif roll2>roll1:
        print(player2, "wins!")
    else:
        print("You tie!")

main()