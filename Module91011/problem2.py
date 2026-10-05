def compute_average(hits, atbats):
    average = hits / atbats
    return average

count = 0
response = input("Do you want to enter a player? Yes or No: ")

while response == "Yes":
    lastname = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    atbats = int(input("Enter number of at bats: "))

    average = compute_average(hits, atbats)

    print(f"Last name: {lastname}")
    print(f"Batting average: {average:.3f}")

    count = count + 1

    response = input("Do you want to enter another player? Yes or No: ")

print(f"Number of players entered: {count}")