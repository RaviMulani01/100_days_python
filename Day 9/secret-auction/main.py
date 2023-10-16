from art import logo
import os

print(logo)
print("Welcome to the secret auction program.")

# create empty dictionary for store all bidder info.
secret_action = {}

bidding_finished = False

while not bidding_finished:
    name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))

    # add bidder info in dictionary
    secret_action[name] = bid_amount

    new_bidder = input("Are there any other bidder? Type 'yes' or 'no'.\n").lower()
    
    # clear the screen
    os.system('clear')

    if new_bidder == "yes":
        bidding_finished = False
    
    else:
         bidding_finished = True

# create a variable to select final bidder
bid_winner = ""
highest_bid = 0

# create loop for select highest amount bidder
for bidder in secret_action:
    if secret_action[bidder] > highest_bid:
        highest_bid = secret_action[bidder]
        bid_winner = bidder

# print the bid winner
print(logo)
print(f"The winner is {bid_winner} with bid of ${highest_bid}.")
