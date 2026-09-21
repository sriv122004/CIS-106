quantity = float(input("Enter quantity of widgets: "))

if quantity > 10000:
    price = 10
elif quantity >= 5000:
    price = 20
else:
    price = 30

extendedprice = price * quantity
tax = extendedprice * 0.07
total = extendedprice + tax

print("Extended Price: $ {:10.2f}".format(extendedprice))
print("Tax: $ {:10.2f}".format(tax))
print("Total: $ {:10.2f}".format(total))