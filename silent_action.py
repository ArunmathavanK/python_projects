import os
a=input("***Welcome to the Silent Auction Program***")
def winner(bids):  #{arun:100,maddy:50,tamil:200}
    win=""
    max=0
    for i in bids: #i=arun
        bid_amount=bids[i]  #bid_amount=100
        if bid_amount>max:
           max=bid_amount
           win=i
    # print(bids)
    print(f"The winner is {win} with a bid of {max}")
bidding={}
try_again=False
while not try_again:
    name=input("What is your name?: ")
    price=int(input("What is your bid?: "))
    bidding[name]=price
    again=input("Are there any other bidders? Type 'Yes' or 'No'? ").lower()
    if again=='no':
        try_again=True
        winner(bidding)
    elif again=='yes':
        os.system('cls')
        # print("\033[H\033[J")  # This clears the terminal by moving the cursor to the top and clearing everything.
