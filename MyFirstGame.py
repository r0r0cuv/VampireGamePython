import time

# Game Intro
print("A vampire attacks the mansion just before the guests arrive!")
time.sleep(1)
print("You must collect a few essential items to defeat him.")
time.sleep(1)
print("Find holy water, a stake, garlic, a cross, and a protein bar before time runs out.\n")

# Initialize game state
inventory = []
vampire_defeated = False
rooms = {
    'Library': 'holy water',
    'Cellar': 'stake',
    'Kitchen': 'garlic',
    'Gallery': 'cross',
    'Bedroom': 'protein bar'
}
visited_rooms = set()

def display_status():
    print("\nInventory:", inventory)
    print("Visited rooms:", list(visited_rooms))
    print("Rooms to explore:", [room for room in rooms if room not in visited_rooms])

# Main Game Loop
while not vampire_defeated:
    display_status()
    choice = input("\nWhere would you like to go? (Type room name or 'fight' to face the vampire): ").title()

    if choice == 'Fight':
        required_items = ['holy water', 'stake', 'garlic', 'cross', 'protein bar']
        if all(item in inventory for item in required_items):
            print("\nYou splash the vampire with holy water, stab him with the stake, and wave the garlic and cross!")
            time.sleep(1)
            print("You eat the protein bar to regain strength for the final blow...")
            time.sleep(1)
            print("The vampire screams and vanishes into dust! You saved the guests!")
            vampire_defeated = True
        else:
            print("\nYou don’t have everything you need. The vampire overpowers you. Game Over!")
            break

    elif choice in rooms:
        if choice in visited_rooms:
            print("\nYou've already searched that room.")
        else:
            item = rooms[choice]
            print(f"\nYou search the {choice} and find a {item}!")
            inventory.append(item)
            visited_rooms.add(choice)
    else:
        print("\nInvalid room. Try again.")

if vampire_defeated:
    print("\n*** Congratulations, hero! ***")
