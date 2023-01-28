#two ways to sum even numbers

# one
even_sum = 0
for number in range(2, 101, 2):
    even_sum += number

print(even_sum)

# two
acc_even = 0
for number in range(1,101):
    if number % 2 == 0:
        acc_even += number

print(acc_even)