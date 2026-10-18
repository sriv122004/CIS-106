class Student:

    def __init__(self, first, last, district, credits):
        self.first = first
        self.last = last
        self.district = district
        self.credits = credits

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def calculate_tuition(self):
        if self.district == 'I':
            tuition = self.credits * 250.00
        else:
            tuition = self.credits * 500.00

        return tuition

student1 = Student('Steven', 'Rivera', 'I', 12)
student2 = Student('Roselyn', 'Saavedra', 'O', 15)

print("Student Name:", student1.fullname())
print("District Code:", student1.district)
print("Enrolled Credits:", student1.credits)
print("Tuition Owed: $", format(student1.calculate_tuition(), ".2f"))

print()

print("Student Name:", student2.fullname())
print("District Code:", student2.district)
print("Enrolled Credits:", student2.credits)
print("Tuition Owed: $", format(student2.calculate_tuition(), ".2f"))
