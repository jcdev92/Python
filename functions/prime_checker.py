def main():
    print("enter a number to check if it is prime or not:\n")
    n = int(input("number: "))
    prime_checker(number=n)

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

if __name__ == '__main__':
    main()