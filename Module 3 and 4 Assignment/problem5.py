purchase_price = float(input("Enter purchase price per share: "))
current_price = float(input("Enter current stock price: "))
quantity = int(input("Enter quantity of stock: "))

value_change = (current_price - purchase_price) * quantity

print("Increase or decrease in stock value: ${:.2f}".format(value_change))