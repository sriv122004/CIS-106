partnumber = input("Enter part number: ")
quantity = float(input("Enter quantity: "))

if partnumber == "10" or partnumber == "55":
    unitcost = 1.00
elif partnumber == "99":
    unitcost = 2.00
elif partnumber == "80" or partnumber == "70":
    unitcost = 3.00
else:
    unitcost = 5.00

totalcost = quantity * unitcost

print("Part Number: ", partnumber)
print("Cost Per Unit: $ {:10.2f}".format(unitcost))
print("Total Cost: $ {:10.2f}".format(totalcost))