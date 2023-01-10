print("welcome to the roller coaster!")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
    print("you can ride the roller coaster!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print("child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("youth tickets are $7.")
    else:
        bill = 12
        print("adult tickets are $12.")
    wants_photo = input("do you want a photo taken? Y or N. ")
    wants_photo = wants_photo.upper()
    if wants_photo == "Y":
        bill += 3
    print(f"your final bill is ${bill}")
else:
    print("sorry, you have to grow taller before you can ride.")
