last_name = input("Enter your last name: ")
midterm = float(input("Enter your midterm exam score: "))
final = float(input("Enter final exam score: "))

total_exam_points = (midterm * .40) + (final * .60)

print("Student: {} | Total exam points: {:.2f}".format(last_name, total_exam_points))