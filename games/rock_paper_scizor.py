import random

print('''Welcome to rock, paper o scissor game!!.
Choose one option between these tools to play this game. 
Remebrer the rules, rock kills scissors, 
scissors kills paper, and paper kills rock, who 
choose the killer tool win, the other one lose.
are yo ready?!\n''')


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

game_images = [rock, paper, scissors]

person_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors'))

if person_choice >= 3 or person_choice < 0:
    print('You tiped an invalid number of choice, is from 0 to 2, try again\n')

else: 
    print('\nYou choose:\n')
    print(game_images[person_choice], '\n')
    print('Computer choose:\n')
    computer_choice = random.randint( 0 , 2 )
    print(game_images[computer_choice], '\n')

# rules
# 0 rock
# 1 paper
# 2 scissor

    if person_choice == 0 and computer_choice == 2:
        print('you win!')
    elif person_choice == 2 and computer_choice == 0:
        print('you lose!')
    elif computer_choice > person_choice:
        print('You lose!')
    elif person_choice > computer_choice:
        print('You Win!!')
    elif computer_choice == person_choice:
        print('it is a draw!') 