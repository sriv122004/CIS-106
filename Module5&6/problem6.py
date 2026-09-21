lastname = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
joblevel = float(input("Enter job level: "))

if joblevel >= 10:
    bonusrate = 0.25
elif joblevel >= 5:
    bonusrate = 0.20
else:
    bonusrate = 0.10

bonus = salary * bonusrate

print("Employee last name: ", lastname)
print("Bonus: $ {:10.2f}".format(bonus))