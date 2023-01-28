def input_name():
    while True:
        try:
            bidder_name = input("What is your name?: ")
            if bidder_name.isalpha():
                return bidder_name
                break
            else:
                print("Please enter a name (not numbers or symbols).")
        except ValueError:
            print("Please enter a name.")

def input_bid():
    while True:
        try:
            bid = int(input("What's your bid?: $"))
            if bid > 0:
                return bid
                break
            else:
                print("Please enter a number (not letters or symbols) greater than 0.")
        except ValueError:
            print("Please enter a number greater than 0.") 

def input_bidders():
    while True:
        try:
            more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
            if more_bidders == 'yes' or more_bidders == 'no':
                return more_bidders
                break
            else:
                print("Please enter 'yes' or 'no'.")
        except ValueError:
            print("Please enter 'yes' or 'no'.")


# export the functions to be used in other files
__all__ = ['input_name', 'input_bid', 'input_bidders']
