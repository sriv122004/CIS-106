class Student:

    def __init__(self, first, last, district, credits):
        self.first = first
        self.last = last
        self.district = district
        self.credits = credits

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def calculate_tuition(self):
        tuition_rates = {'I': 250.00, 'O': 500.00, 'X': 800.00, 'G': 250.00}

        tuition = self.credits * tuition_rates[self.district]
        return tuition

student1 = Student('Steven', 'Rivera', 'I', 12)
student2 = Student('Roselyn', 'Saavedra', 'O', 15)
student3 = Student('Alan', 'Flores', 'X', 10)
student4 = Student('Kevin', 'Salgado', 'G', 9)

print("Student Name:", student1.fullname())
print("District Code:", student1.district)
print("Enrolled Credits:", student1.credits)
print("Tuition Owed: $", format(student1.calculate_tuition(), ".2f"))

print()

print("Student Name:", student2.fullname())
print("District Code:", student2.district)
print("Enrolled Credits:", student2.credits)
print("Tuition Owed: $", format(student2.calculate_tuition(), ".2f"))

print()

print("Student Name:", student3.fullname())
print("District Code:", student3.district)
print("Enrolled Credits:", student3.credits)
print("Tuition Owed: $", format(student3.calculate_tuition(), ".2f"))

print()

print("Student Name:", student4.fullname())
print("District Code:", student4.district)
print("Enrolled Credits:", student4.credits)
print("Tuition Owed: $", format(student4.calculate_tuition(),  ".2f"))