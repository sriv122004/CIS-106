f = open("students.txt", "r")

total_tuition = 0.0
count = 0

lastname = f.readline().strip()

while lastname != "":
    district_code = f.readline().strip()
    credits = int(f.readline())

    if district_code == "I":
        cost_per_credit = 250.00
    else:
        cost_per_credit = 500.00

    tuition_owed = credits * cost_per_credit

    total_tuition = total_tuition + tuition_owed
    count = count + 1

    print("Student Last Name: ", lastname)
    print("Credits Taken: ", credits)
    print("Tuition Owed: ", tuition_owed)

    lastname = f.readline().strip()

f.close()

print("Total Tuition Owed: ", total_tuition)
print("Number of Students: ", count)