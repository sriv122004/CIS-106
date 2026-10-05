def compute_grades(exam1, exam2, exam3):
    total = exam1 + exam2 + exam3
    average = total / 3

    return total, average

lastname = input("Enter student's last name: ")
exam1 = float(input("Enter exam 1 score: "))
exam2 = float(input("Enter exam 2 score: "))
exam3 = float(input("Enter exam 3 score: "))

total, average = compute_grades(exam1, exam2, exam3)

print(f"Last name: {lastname}")
print(f"Total points: {total:.2f}")
print(f"Average exam score: {average:.2f}")