from art import logo
import os

#Print starting logo
print(logo)

#Create dictionary to store the bids
bid_dictionary = {}

#Create function to find highest bidder
def find_highest_bidder(bidding_record):
  highest_bid = 0
  highest_bidder = ''
  for bidder_name in bidding_record:
    bid_amount = bidding_record[bidder_name]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      highest_bidder = bidder_name
  print(f"The winner is {highest_bidder} with bid of ${highest_bid}")

#Create loop to ask for bid price if there are other bidders
continue_bidding = True

while continue_bidding:
    name = input("What is your name?")
    bid = int(input("What is your bid price? $"))
    bid_dictionary[name] = bid

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if other_bidders == "no":
        continue_bidding = False
        find_highest_bidder(bid_dictionary)
    elif other_bidders == "yes":
        os.system("clear")

