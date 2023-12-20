from art import logo
import os
clear = lambda: os.system('cls')

is_auction_finished = False
bidders_info = []
highest_bid = 0
winner = ''

print(logo)
print("Welcome to the secret auction program")



def new_bidder(name, bid):
    new_dict = {"name": name, "bid": bid}
    bidders_info.append(new_dict)


while not is_auction_on:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    new_bidder(name, bid)
    next_bidder = input(
        "Are there any other bidders? Type 'yes' or 'no'.").lower()
    if next_bidder == "yes":
        clear()
        continue
    elif next_bidder == 'no':
        clear()
        is_auction_finished = True
    else:
        print("you have to type either 'yes' or 'no'")
        is_auction_finished = True

for bidder in bidders_info:
    if bidder['bid'] > highest_bid:
        highest_bid = bidder['bid']
        winner = bidder['name']

print(f"The winner is {winner} with a bid of ${highest_bid}.")
