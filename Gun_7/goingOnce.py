
maxBid = int(input("Please enter maximum bid : "))

while True:
    current_bid = int(input("Bid : "))

    if current_bid >= maxBid:
        print(f"Sold: {current_bid}")
        break 