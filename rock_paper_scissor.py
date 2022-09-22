import random


computer_choice = random.choice(['scissors', 'paper', 'rock'])

user_choice = input('Choose: scissors, paper or rock\n')

if computer_choice == user_choice:
    print("That's a tie \o/")
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('You win =D \nthe computer had ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('You win =D \nthe computer had ' + computer_choice)
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('You win =D \nthe computer had ' + computer_choice)
else:
    print('You lost =( Try again\nThe computer had ' + computer_choice)