from game import new_game, move_player, collect_item, is_win, is_lost, ISLAND_MAP
print("=========================")

print("MYSTERY ISLAND")
print("The Lost Lighthouse")

print("=========================")

print("You wake up on a mysterious island after a terrible storm.")
print("The lighthouse is dark, and you must find a way to escape.")

print("Good luck, explorer!🤠")

player_name = input("What is your name?: ")

print(f"Welcome to Mystery Island, {player_name}!")
print("Your adventure begins now.")

# Outer loop: replay the game
while True:
    game = new_game(player_name)
    energy = game["energy"]
    location = game["location"]
    inventory = game["inventory"]
    jungle_decision_made = game["jungle_decision_made"]
    cave_decision_made = game["cave_decision_made"]
    bridge_decision_made = False

    print(f"{player_name}, your starting energy is {energy}.")
    print(f"Current location: {location}")
    print(f"Energy: {energy}")
    print(f"Empty Inventory: {inventory}")

    # Inner loop: player movement
    while True:
        print(f"\nEnergy remaining: {energy}")
        print(f"Inventory: {inventory}")

        print(f"\nYou are currently at: {location}")
        print("Available locations:")

        for place in ISLAND_MAP[location]:
            print(f"- {place}")

        print("- Quit")

        direction = input("\nWhere would you like to go? ")

        direction = direction.strip().title()

        print(f"You chose: {direction}")

        if direction == "Quit":
            print("You have left the island.")
            break

        elif direction == "Beach":
            game["location"] = location
            game["energy"] = energy

            if move_player(game, "Beach"):
                location = game["location"]
                energy = game["energy"]
            else:
                print("You cannot travel there directly!")
                continue

        elif direction == "Jungle":
            game["location"] = location
            game["energy"] = energy

            if move_player(game, "Jungle"):
                location = game["location"]
                energy = game["energy"]
            else:
                print("You cannot travel there directly!")
                continue

        elif direction == "Cave":
            game["location"] = location
            game["energy"] = energy

            if move_player(game, "Cave"):
                location = game["location"]
                energy = game["energy"]
            else:
                print("You cannot travel there directly!")
                continue

        elif direction == "Old Bridge":
            game["location"] = location
            game["energy"] = energy
            game["inventory"] = inventory

            if move_player(game, "Old Bridge"):
                location = game["location"]
                energy = game["energy"]
            elif direction not in ISLAND_MAP[location]:
                print("You cannot travel there directly!")
                continue
            else:
                print("You need a Rope to cross the Old Bridge!")

        elif direction == "Lighthouse":
            game["location"] = location
            game["energy"] = energy
            game["inventory"] = inventory

            if move_player(game, "Lighthouse"):
                location = game["location"]
                energy = game["energy"]
            elif direction not in ISLAND_MAP[location]:
                print("You cannot travel there directly!")
                continue
            else:
                print("You need a Lantern to enter the Lighthouse!")

        else:
            print("That location is not available!")
            continue

    # Item collection
        game["location"] = location
        game["inventory"] = inventory

        item = collect_item(game)

        if item == "Rope":
            print("You found a Rope!")

        elif item == "Lantern":
            print("You found a Lantern!")

        inventory = game["inventory"]
        # Jungle decision
        if location == "Jungle" and jungle_decision_made == False:
            print("\nYou have discovered two paths in the Jungle!")
            print("1. Take the dangerous shortcut (lose 1 extra energy).")
            print("2. Take the safe route (no extra energy loss).")

            while True:
                choice = input("Choose 1 or 2: ")

                if choice == "1":
                    energy = max(0, energy - 1)
                    print("You took the dangerous shortcut and lost 1 energy!")
                    break

                elif choice == "2":
                    print("You took the safe route. Good choice!")
                    break

                else:
                    print("Invalid choice. Please enter 1 or 2.")

            jungle_decision_made = True


              # Cave decision
        if location == "Cave" and cave_decision_made == False:
            print("\nYou discovered a narrow tunnel!")
            print("1. Explore the tunnel (lose 1 extra energy).")
            print("2. Avoid the tunnel (no extra energy loss).")

            while True:
                choice = input("Choose 1 or 2: ")

                if choice == "1":
                    energy = max(0, energy - 1)
                    print("You explored the tunnel and lost 1 energy!")
                    break

                elif choice == "2":
                    print("You avoided the tunnel. Good choice!")
                    break

                else:
                    print("Invalid choice. Please enter 1 or 2.")

            cave_decision_made = True

        # Old Bridge decision
        if location == "Old Bridge" and bridge_decision_made == False:
            print("\nYou have reached the Old Bridge!")
            print("1. Cross carefully (lose 1 extra energy).")
            print("2. Take the longer route (no extra energy loss).")

            while True:
                choice = input("Choose 1 or 2: ")

                if choice == "1":
                    energy = max(0, energy - 1)
                    print("You crossed carefully and lost 1 energy!")
                    break

                elif choice == "2":
                    print("You took the longer route. No extra energy lost!")
                    break

                else:
                    print("Invalid choice. Please enter 1 or 2.")

            bridge_decision_made = True


        print(f"Your inventory: {inventory}")

        print(f"Current location: {location}")
        print(f"Energy remaining: {energy}")

        game["location"] = location
        game["energy"] = energy
        game["inventory"] = inventory

        if is_lost(game):
            print("You have run out of energy!")
            print("GAME OVER!😓")
            break

        elif is_win(game):
            print("Congratulations! You have escaped Mystery Island!🥳")
            print("YOU WIN!")
            print("✅🎉")
            break

    while True:
        replay = input("Would you like to play again? (yes/no): ").strip().lower()

        if replay == "no":
            print("Thanks for playing Mystery Island!")
            break

        elif replay == "yes":
            print("Starting a new adventure!")
            break

        else:
            print("Invalid choice. Please enter yes or no.")

    if replay == "no":
        break
