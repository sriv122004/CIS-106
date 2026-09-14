ticker = input("Enter stock ticker symbol: ")
shares = int(input("Enter number of shares: "))
cost_per_share = float(input("Enter costs per share: "))

amount_invested = shares * cost_per_share

print("Amount invested in {}: ${:.2f}".format(ticker, amount_invested))