def display_names(names, scores):
    for i in range(len(names)):
        print(names[i], "-", scores[i])

def reverse_names(names, scores):
    for i in range(len(names) - 1, -1, -1):
        print(names[i], "-", scores[i])

def high_low_scores(names, scores):
    high_var = 0
    low_var = 999
    high_index = 0
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i

        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print("\nHighest Score:", names[high_index], "-", high_var)
    print("Lowest Score:", names[low_index], "-", low_var)

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Wilson"]

exam_scores = [85, 92, 78, 90, 88, 95, 82, 76, 91, 87]

print("Last Names and Exam Scores in Original Order:")
display_names(last_names, exam_scores)

print("\nLast Names and Exam Scores in Reverse Order:")
reverse_names(last_names, exam_scores)

high_low_scores(last_names, exam_scores)
