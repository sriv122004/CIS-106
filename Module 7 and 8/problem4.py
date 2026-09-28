f = open("foods.txt", "r")

total_extended_price = 0.0
count = 0

item = f.readline().strip()

while item != "":
    quantity = float(f.readline())
    price = float(f.readline())

    extended_price = quantity * price

    total_extended_price = total_extended_price + extended_price
    count = count + 1

    print("Item: ", item)
    print("Quantity: ", quantity)
    print("Price: ", price)
    print("Extended Price: ", extended_price)

    item = f.readline().strip()

f.close()

average_order = total_extended_price / count

print("Sum of Extended Prices: ", total_extended_price)
print("Number of Orders: ", count)
print("Average Order: ", average_order)