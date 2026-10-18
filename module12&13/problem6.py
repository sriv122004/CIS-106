def display_players(players):
    print("Player Name\tBatting Average")
    print("--------------------------------")

    for name, average in players.items():
        print(f"{name:<16}{average:.3f}")

players = {}

file = open("players.txt", "r")

for line in file:
    data = line.strip().split(",")
    name = data[0]
    average = float(data[1])
    players[name] = average

file.close()

display_players(players)