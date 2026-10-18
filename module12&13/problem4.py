students = {"Smith": 85, "Johnson": 92, "Williams": 78, "Brown": 90, "Jones": 88,
    "Garcia": 95, "Miller": 82, "Davis": 76, "Rodriguez": 91, "Wilson": 87}

total = 0
count = 0

print("Student Name\tGrade")
print("---------------------------")

for name, grade in students.items():
    print(name, "\t\t", grade)
    total = total + grade
    count = count + 1

average = total / count

print("---------------------------")
print("Class Average:", round(average, 2))
