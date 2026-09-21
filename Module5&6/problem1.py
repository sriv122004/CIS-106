quantity = float(input("Enter quantity: "))

if quantity >= 1000:
    unitprice = 3.00
else:
    unitprice = 5.00

extendedprice = quantity * unitprice
tax = extendedprice * 0.07
total = extendedprice + tax

print("Quantity: {:10.2f}".format(quantity))
print("Unit Price: $ {:10.2f}".format(unitprice))
print("Extended Price: $ {:10.2f}".format(extendedprice))
print("Tax: $ {:10.2f}".format(tax))
print("Total: $ {:10.2f}".format(total))