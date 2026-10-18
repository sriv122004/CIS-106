class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def calculate_bonus(self, bonus_rate):
        bonus = self.pay * bonus_rate
        return bonus

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

emp_1.fullname()
print(Employee.fullname(emp_1))

bonus_rate = float(input("Enter bonus rate (decimal): "))

bonus = emp_1.calculate_bonus(bonus_rate)

print("Employee Bonus: $", format(bonus, ".2f"))
