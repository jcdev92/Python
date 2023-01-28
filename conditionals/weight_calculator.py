heigth = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / heigth ** 2
bmi = round(bmi)

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
    print('Your BMI is {bmi}, you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')

