tickets = float(input("Enter number of concert tickets: "))

if tickets >= 25:
    price = 50
elif tickets >= 10:
    price = 60
elif tickets >= 5:
    price = 70
else:
    price = 75

totalcost = tickets * price

print("Number of tickets: {:10.2f}".format(tickets))
print("Price per ticket: $ {:10.2f}".format(price))
print("Total cost: {:10.2f}".format(totalcost))