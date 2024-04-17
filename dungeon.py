# dungeon.py

import random
from player import Player
from monster import Lich, Demon, Ghoul, Pidgeonpig, Zombie

# Function for the Door scenario
def door(player):
    # Assuming enemy objects are stored in a list
    enemies = [Lich(), Demon(), Ghoul(), Pidgeonpig(), Zombie()]
    # Selecting a random enemy from the list
    enemy = random.choice(enemies)
    print(f"You encounter a {enemy.name} behind the door he wants to spit his stats to scare you!!\nBe Careful!")
    enemy.get_status()  # Print enemy status

# Function for the Stairs scenario
def stairs(player):
    print("You climb the stairs and feel reinvigorated! +15 health.")
    player.health += 15
    print(f"Your health is now {player.health}.")

# Function for the Noises scenario
def noises(player):
    print("You hear noises... It's a battle!")
    # Assuming a battle function exists to handle the battle between player and enemy
    # Example: battle(player, enemy)
    # Implement this function based on your existing battle logic

# Function for the Pet Cat scenario
def pet_cat(player):
    choice = input("You encounter a cute cat! Do you want to pet it? (yes/no)\n").lower()
    if choice == "yes":
        print("Meow! You feel a surge of power! +20 attack.")
        player.attack += 20
    elif choice == "no":
        print("The cat scratches you! -10 health.")
        player.health -= 10
    else:
        print("Invalid choice. The cat stares at you, confused.")

# Function for the Chest scenario
def chest(player):
    choice = input("You found a chest! Do you want to open it? (open/leave)\n").lower()
    if choice == "open":
        print("You open the chest and find treasures!")
        # Add treasure logic here
    elif choice == "leave":
        print("You leave the chest untouched.")
    else:
        print("Invalid choice. The chest remains unopened.")

# Function for the Next Floor scenario
def next_floor(player):
    print("You descend to the next floor of the dungeon.")

# Function for quitting the game
def quit_game(player):
    print("Exiting the game...")
    exit()

# Map choices to functions
dungeon_choices = {
    "Door": door,
    "Stairs": stairs,
    "Noises": noises,
    "Pet cat": pet_cat,
    "Chest": chest,
    "Next floor": next_floor,
    "Quit game": quit_game
}
