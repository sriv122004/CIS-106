# Final Project: Pokemon Collection Manager
# This application lets users create and manage their own Pokemon collection. Users can add, view,
# find, and delete Pokemon from their collection. The collection can also be saved to a text file.
# I chose to make my project around Pokemon because I'm a pretty big Pokemon nerd. I originally wanted
# to do a "Guess the Pokemon" type of program but realized it was going to be more complicated, so I
# opted for a collection system instead

# Displays the starting menu with different choices the user can select
def menu():
    print("\nPokemon Collection Manager")
    print("--------------------------")
    print("1. Add Pokemon")
    print("2. View Pokemon")
    print("3. Find Pokemon")
    print("4. Delete Pokemon")
    print("5. Save Collection")
    print("6. Quit")

    choice = input("Select a choice: ")
    return choice

# Adds a Pokemon with its corresponding dex number, typing, and level to the collection
def add_pokemon(pokemon):
    name = input("Enter Pokemon name: ")
    number = int(input("Enter Pokedex number: "))
    pokemon_type = input("Enter Pokemon type: ")
    level = int(input("Enter Pokemon level: "))

    pokemon[name] = [number, pokemon_type, level]

    print("Pokemon added successfully!")

# Displays all Pokemon added in the collection
def view_pokemon(pokemon):
    if len(pokemon) == 0:
        print("No Pokemon in the collection.")

    else:
        print("\nPokemon Collection")
        print("------------------")

        for name in pokemon:
            number = pokemon[name][0]
            pokemon_type = pokemon[name][1]
            level = pokemon[name][2]

            print("Name:", name)
            print("Pokedex Number:", number)
            print("Type:", pokemon_type)
            print("Level:", level)
            print()

# Searches for a Pokemon in the collection via typing its name
def find_pokemon(pokemon):
    name = input("Enter Pokemon name to find: ")

    if name in pokemon:
        number = pokemon[name][0]
        pokemon_type = pokemon[name][1]
        level = pokemon[name][2]

        print("\nPokemon Found!")
        print("Name:", name)
        print("Pokedex Number:", number)
        print("Type:", pokemon_type)
        print("Level:", level)

    else:
        print("Pokemon not found in the collection.")

# Deletes a Pokemon from the collection via typing its name
def delete_pokemon(pokemon):
    name = input("Enter Pokemon name to delete: ")

    if name in pokemon:
        del pokemon[name]
        print("Pokemon deleted successfully!")

    else:
        print("Pokemon not found in the collection.")

# Saves the Pokemon collection to a text file
def save_pokemon(pokemon):
    file = open("pokemon.txt", "w")

    for name in pokemon:
        number = pokemon[name][0]
        pokemon_type = pokemon[name][1]
        level = pokemon[name][2]

        file.write("Name: " + name + "\n")
        file.write("Pokedex Number: " + str(number) + "\n")
        file.write("Type: " + pokemon_type + "\n")
        file.write("Level: " + str(level) + "\n")
        file.write("\n")

    file.close()

    print("Pokemon collection saved successfully!")

# Main function that controls the application based on the user's menu choice
def main():
    pokemon = {}

    choice = ""

    while choice != "6":
        choice = menu()

        if choice == "1":
            add_pokemon(pokemon)

        elif choice == "2":
            view_pokemon(pokemon)

        elif choice == "3":
            find_pokemon(pokemon)

        elif choice == "4":
            delete_pokemon(pokemon)

        elif choice == "5":
            save_pokemon(pokemon)

        elif choice == "6":
            print("Goodbye!")

        else:
            print("Invalid choice. Please try again.")


main()