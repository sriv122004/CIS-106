def compute_extprice(qty, price):
    extprice = qty * price

    if extprice > 10000:
        extprice = extprice * 0.90

    return extprice

totalextprice = 0
response = input("Do you want to enter an item? Yes or No: ")

while response == "Yes":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    extprice = compute_extprice(qty, price)

    print(f"Quantity: {qty}")
    print(f"Price: ${price:.2f}")
    print(f"Extended price: ${extprice:.2f}")

    totalextprice = totalextprice + extprice

    response = input("Do you want to enter another item? Yes or No: ")

print(f"Total extended price: ${totalextprice:.2f}")