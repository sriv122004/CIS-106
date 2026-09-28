f = open("employees.txt", "r")

total_bonus = 0.0

lastname = f.readline().strip()

while lastname != "":
    salary = float(f.readline())

    if salary >= 100000:
        bonus_rate = 0.20
    elif salary >= 50000:
        bonus_rate = 0.15
    else:
        bonus_rate = 0.10

    bonus = salary * bonus_rate
    total_bonus = total_bonus + bonus

    print("Employee Last Name: ", lastname)
    print("Salary: ", salary)
    print("Bonus: ", bonus)

    lastname = f.readline().strip()

f.close()

print("Sum of All Bonuses Paid: ", total_bonus)