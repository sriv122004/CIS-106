principle = float(input("Enter principle amount: "))
years = float(input("Enter years to maturity: "))

if principle > 100000 and years == 5:
    rate = 0.06
elif principle >= 50000 and years == 10:
    rate = 0.05
elif principle >= 50000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

interest = principle * rate

print("Principle: $ {:10.2f}".format(principle))
print("Interest Rate: {:10.2f}%".format(rate * 100))
print("Interest: $ {:10.2f}".format(interest))