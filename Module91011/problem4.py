def compute_price(msrp, make, model, electric):
    if electric == "Y":
        percent = 0.30
    elif make == "Honda" and model == "Accord":
        percent = 0.10
    elif make == "Toyota" and model == "Rav4":
        percent = 0.15
    else:
        percent = 0.05

    discount = msrp * percent
    newmsrp = msrp - discount
    tax = newmsrp * 0.07
    total = newmsrp + tax

    return total

totalmsrp = 0
totalsales = 0

response = input("Do you want to enter a vehicle? Yes or No: ")

while response == "Yes":
    make = input("Enter vehicle make: ")
    model = input("Enter vehicle model: ")
    electric = input("Is the vehicle electric? Y or N: ")
    msrp = float(input("Enter MSRP: "))

    total = compute_price(msrp, make, model, electric)

    print(f"Make: {make}")
    print(f"Model: {model}")
    print(f"MSRP: ${msrp:.2f}")
    print(f"Out the door price: ${total:.2f}")

    totalmsrp = totalmsrp + msrp
    totalsales = totalsales + total

    response = input("Do you want to enter another vehicle? Yes or No: ")

print(f"Total MSRP: ${totalmsrp:.2f}")
print(f"Total sales price: ${totalsales:.2f}")