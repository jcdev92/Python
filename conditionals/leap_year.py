year = int(input('enter a year and check if it is a leap year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('leap year')
        else:
            print('not a leap year')
    else: 
        print('leap year')
else:
    print('not a leap year')