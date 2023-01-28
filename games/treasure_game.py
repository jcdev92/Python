print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')


print('Welcome to Treasure Island. \nYour mission is to find the treasure')
print('Next step find the beach to go to the island')
way=input('you have two ways to chooise, left or right, choose one to keep finding the trasure or fall into a hole: \n')
if way == 'left':
    action=input(
        'now you are in the beach, what do you want to do, wait for a boat or swim?: \n')
    if action == 'wait':
        print('the boat came and took you to the treasure island...')
        print('Excellent now you are infront of the treasure room')
        door=input('wait... there is three doors.. one red, other blue and the other one is yellow, choose wise and you will be rich or else you will die: \n')
        if door == 'yellow':
            print('OMFG!!! THE CHEST IS THERE!!!! OPEN IT NOW!!!')
            print('OPENING... AND... 600KG OF GOLD!! 100KG OF PEARL!!! CONGRATSS!!')
        elif door == 'red':
            print('there is a room full of fire, you burned, GAME OVER!')
        else:
            print('Attacked by trout. Game Over')
    else:
        print('Eaten by beasts. Game Over.')
else:
    print('Fall into a hole. Game Over.')
