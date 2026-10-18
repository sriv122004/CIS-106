def display_names(names):
    for i in range(len(names)):
        print(names[i])

def reverse_names(names):
    for i in range(len(names) - 1, -1, -1):
        print(names[i])

last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
              "Garcia", "Miller", "Davis", "Rodriguez", "Wilson"]

print("Last Names in Original Order:")
display_names(last_names)

print("\nLast Names in Reverse Order:")
reverse_names(last_names)
