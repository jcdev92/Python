age = int(input("What is your current age? "))

top_age = 90
years_remaining = top_age - age

days_remainig = years_remaining * 365
weeks_remainig = years_remaining * 52
months_remainig = years_remaining * 12


print(f"You have {days_remainig} days, {weeks_remainig} weeks, and {months_remainig} months left.")