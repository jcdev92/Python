row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

if len(position) < 2:
    print('too short... yo can only enter a number of 2 digits')
elif len(position) > 2:
    print('too long...yo can only enter a number of 2 digits')
else:
    horizontal = int(position[0])
    vertical = int(position[1])
    if horizontal > 3 or vertical > 3:
        print("Invalid position, try betwen 1 and 3")
    else:
        selected_row = map[vertical - 1][horizontal - 1] = "X"
        print(f"{row1}\n{row2}\n{row3}")