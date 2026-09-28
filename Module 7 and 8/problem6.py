response = input("Do you want to do this program? Enter Yes to continue: ")

count = 0

while response == "Yes":
    lastname = input("Enter student last name: ")
    exam1 = float(input("Enter first exam score: "))
    exam2 = float(input("Enter second exam score: "))

    average = (exam1 + exam2) / 2

    print ("Student Last Name: ", lastname)
    print("Average Exam Score: ", average)

    count = count + 1

    response = input("Do you want to continue? Enter Yes to continue: ")

print("Number of Students: ", count)