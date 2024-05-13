from art import logo
import os

# defining a function that clears the console every time a new user needs to input data
def clear_console():
    # for windows
    if os.name == "nt":
        _ = os.system("cls")

    # for mac and linux (os.name is posix)
    else:
        _ = os.system("clear")


# program start
print(logo)
print("Welcome to the secret auction program.")

# init a dictionary to keep track of the people and their bids
bids = {}

# start a while loop
auction_ended = False
while not auction_ended:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    # adding the input to the dictionary
    bids[name] = bid

    # asking whether we should exit the program or keep taking input
    other_bidders = input("Are there other bidders? Type 'yes' or 'no'. ").lower()
    if other_bidders == "no":
        auction_ended = True

    # clearing the console so that the next user does not see the already inputted bids
    clear_console()

# deciding who won the auction
winner = ""
winning_bid = 0

for bidder in bids:
    if bids[bidder] > winning_bid:
        winner = bidder
        winning_bid = bids[bidder]

# printing the winner
print(f"The winner is {winner} with a bid of ${winning_bid}.") 