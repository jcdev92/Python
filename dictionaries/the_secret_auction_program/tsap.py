from arts import logo
from time import sleep
from inputs_controllers import input_name, input_bid, input_bidders

def main():
    print(logo)
    bids = {}
    bidder_name = input_name()
    bid = input_bid()
    add_bid(bidder_name, bid, bids)
    more_bidders = input_bidders()
    while more_bidders == 'yes':
        bidder_name = input_name()
        bid = input_bid()
        add_bid(bidder_name, bid, bids)
        more_bidders = input_bidders()
    else:
        print("ok, finding the highest bidder...")
        sleep(2)
        print("The winner is...")
        sleep(2)
        winner_finder(bids)


def add_bid(bidder_name, bid, bids):   
    bids[bidder_name] = bid

def winner_finder(bids):
    highest = 0
    winner = ''
    for key in bids:
        if bids[key] > highest:
            highest = bids[key]
            winner = key

    print(f"{winner}!!! with a bid of ${highest}.")        


if __name__ == '__main__':
    main()