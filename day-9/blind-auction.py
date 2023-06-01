"""
Auction Program
"""

# Imports
import os
from ascii_art import bid_hammer

# Data Structures & variables
bidders = []
max = 0
winner = {}

# Functions
def cls():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name=='nt' else 'clear')

def create_bidder():
    """
    Creates a new bidder and adds them to the bidders list.
    Asks for bidder's name and bid price as input.
    """
    bidder = {}

    bidder_name = input("Please input your name:\n")
    bid_price = int(input("Please input your price:\n"))

    bidder = {
        "Name": bidder_name,
        "Price": bid_price 
    }
    bidders.append(bidder)

# Auction
print(bid_hammer)
print("Welcome to the auction!\n")
print("- - - - - - - - - - - - \n")

if not input("Press Enter to begin the auction"):
    cls()

create_bidder()

while input("Is there another bidder (Y or N)?\n").lower() == 'y':
    cls()
    create_bidder()


for bidder in bidders:
    if bidder["Price"] > max:
        max = bidder["Price"]
        winner["Name"] = bidder["Name"]
        winner["Price"] = bidder["Price"]

print(f'The bidder "{winner["Name"]}" has won the auction with {winner["Price"]}€')
