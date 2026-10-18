students = {"Smith": [85, 90, 88], "Johnson": [92, 87, 94], "Williams": [78, 82, 80], "Brown": [90, 85, 91], "Jones": [88, 92, 86],
"Garcia": [95, 93, 97], "Miller": [82, 85, 80], "Davis": [76, 81, 79], "Rodriguez": [91, 89, 94], "Wilson": [87, 90, 85]}

def calculate_averages(students):
    student_averages = {}
    class_totals = [0, 0, 0]
    count = 0

    for name, grades in students.items():
        total = 0

        for i in range(3):
            total = total + grades[i]
            class_totals[i] = class_totals[i] + grades[i]

        student_averages[name] = total / 3
        count = count + 1

    class_averages = []

    for i in range(3):
        class_averages.append(class_totals[i] / count)

    return student_averages, class_averages

student_averages, class_averages = calculate_averages(students)

print("Student Name\tAverage Grade")
print("--------------------------------")

for name, average in student_averages.items():
    print(f"{name:<16}{average:.2f}")

print("\nClass Average for Each Exam")
print("--------------------------------")

for i in range(3):
    print(f"Exam {i + 1}: {class_averages[i]:.2f}")
