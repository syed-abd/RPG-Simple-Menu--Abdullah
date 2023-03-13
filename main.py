def display_menu():
    # display the available options to the player
    print("\nWelcome to the Game Menu!")
    print("1. Start Game")
    print("2. View Inventory")
    print("3. View Map")
    print("4. Save Game")
    print("5. Quit")

def start_game():
    # start the game logic
    print("\nGame started! Good luck!")
    # add game logic here

def view_inventory():
    # define a list of items in the player's inventory
    inventory = ["sword", "shield", "potion", "key"]
    # display the inventory to the player
    print("\nInventory:")
    for item in inventory:
        print("- " + item)

def view_map():
    # define a dictionary with map data
    map_data = {"start": "You are here", "end": "The final boss is here", "path": "The path to victory"}
    # display the map to the player
    print("\nMap:")
    for key, value in map_data.items():
        print(key + ": " + value)

def save_game():
    # save the game data to a file
    print("\nGame saved!")

# main loop
while True:
    # display the menu options to the player
    display_menu()

    # get the player's choice from the input
    choice = input("Enter your choice: ")

    # handle the player's choice
    if choice == "1":
        start_game()
    elif choice == "2":
        view_inventory()
    elif choice == "3":
        view_map()
    elif choice == "4":
        save_game()
    elif choice == "5":
        # exit the game loop
        print("Thanks for playing! Goodbye.")
        break
    else:
        # handle invalid input from the player
        print("Invalid choice. Please try again.")
