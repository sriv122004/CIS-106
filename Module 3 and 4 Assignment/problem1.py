exam1 = float(input("Enter first exam score: "))
exam2 = float(input("Enter second exam score: "))

total = (exam1 * .60) + (exam2 * .40)

print("Total score: {:.2f}".format(total))