import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
computer_choice = int(random.randint(0, 2))

#print("Computer's choice: " + str(computer_choice))
#print("Player's choice: " + str(player_choice))
print(f"Player's choice: {player_choice}")
if player_choice == 0:
    print(rock)
elif player_choice == 1:
    print(paper)
elif player_choice == 2:
    print(scissors)
else:
    print("That's not an option!")

print(f"Computer's choice: {computer_choice}")
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
elif computer_choice ==2:
    print(scissors)
else:
    print("Whaaat?! How is this possible!")

scissors > paper
paper > rock
rock > scissors


rock = 0
paper = 1
scissors = 2


if computer_choice > player_choice:
    print("You lose")
elif computer_choice < player_choice:
    print("You win!")
else:
    print("It's a tie...")



#print(computer_choice)
