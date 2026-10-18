def display_names(names, scores):
    for i in range(len(names)):
        print(names[i], "-", scores[i])

def reverse_names(names, scores):
    for i in range(len(names) - 1, -1, -1):
        print(names[i], "-", scores[i])

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Wilson"]

exam_scores = [85, 92, 78, 90, 88, 95, 82, 76, 91, 87]

print("Last Names and Exam Scores in Original Order:")
display_names(last_names, exam_scores)

print("\nLast Names and Exam Scores in Reverse Order:")
reverse_names(last_names, exam_scores)
