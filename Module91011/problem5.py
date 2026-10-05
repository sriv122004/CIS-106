def compute_discount(qty, price, rate):
    total = qty * price
    discount = total * rate
    discountprice = total - discount

    return discount, discountprice

qty = int(input("Enter quantity: "))
price = float(input("Enter price: "))
rate = float(input("Enter discount rate: "))

discount, discountprice = compute_discount(qty, price, rate)

print(f"Quantity: {qty}")
print(f"Price: ${price:.2f}")
print(f"Discount amount: ${discount:.2f}")
print(f"Discounted price: ${discountprice:.2f}")