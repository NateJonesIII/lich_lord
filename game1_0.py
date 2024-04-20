import sys, os, re, random
from player import *
from monster import *

# monster instances
pigmon = Pidgeonpig()
demon = Demon()
zombiemon = Zombie()
lichmon = Lich()
ghoulmon = Ghoul()

def print_intro():
    # Clearing the Screen
    os.system('cls')
    print("\nWelcome to \033[1;35;40mLich Lord\033[m!")
    print("You are about to embark on a perilous journey through dungeons filled with monsters.")
    print("Your ultimate goal is to defeat the Lich Lord and restore peace to the realm.\n")

def show_menu():
    print("\nMain Menu:")
    print("1. Start Game")
    print("2. How to Play")
    print("3. Show Class Stats")
    print("4. Quit\n")
    
def battle(player, monster):
    print("A battle begins!")
    while player.health > 0 and monster.health > 0:
        # Player attacks monster
        player.attack_enemy(monster)
        print(f"{monster.get_name()}'s health: {monster.get_health()}")
        if monster.health <= 0:
            print(f"{monster.name} has been defeated!")
            return True  # Player wins the battle

        # Monster attacks player
        monster.attack_enemy(player)
        print(f"{player.get_name()}'s health: {player.get_health()}")
        if player.get_health() <= 0:
            print("You have been defeated!")
            return False  # Player loses the battle

    # If neither health reaches 0, the battle continues
    return None

def dungeon_1(player):
    print("\nWelcome to Dungeon 1!")
    print("You feel a chill in the air as you step into the dark corridor.")
    while True:
        print(f"\nWhat is your choice? {player.get_name()}")
        print("1. Open the rusty door")
        print("2. Search for hidden treasure")
        print("3. Proceed cautiously down the hallway")
        print("4. Turn back and exit the dungeon")
        choice = input("Enter an option: ")
        if choice == "1":
            print("You open the door...\n")
            # Logic for bonus stats
            player.health_alter(10)
            print(f"{player.get_name()} found a blessed turtle you get {10} pts of life")
            print(f"Player health: {player.get_health()}")
            break
        elif choice == "2":
            stink = -10
            player.health_alter(stink)
            print("You search around and find a stinky chest!")
            print(f"You lost {stink} health! player health: {player.get_health()}")
            # Logic for finding an item or encountering a monster
            break
        elif choice == "3":
            print("You cautiously proceed down the hallway...")
            # Logic for encountering a monster or finding an exit
            print(f"Oh no!\nYou've encountered {pigmon.get_name()}")
            battle(player, pigmon)
            if player.health > 0:
                dungeon_2(player)
            break
        elif choice == "4":
            print("You decide to turn back and exit the dungeon.")
            # Logic for exiting the dungeon
            main()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    
def dungeon_2(player):
    print("\nWelcome to Dungeon 2!")
    print("You find yourself in a damp cave filled with the sound of dripping water.")
    while True:
        print(f"\nWhat is your choice? {player.get_name()}")
        print("1. Explore deeper into the cave")
        print("2. Check behind the waterfall")
        print("3. Investigate the mysterious altar")
        print("4. Retreat back to the entrance")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You venture deeper into the cave...")
            # Logic for encountering a monster or finding venturing onward
            dungeon_3(player)
            break
        elif choice == "2":
            print("You find a hidden passage behind the waterfall!")
            # Logic for encountering a monster
            print(f"{demon.roar()}")
            battle(player, demon)
            break
        elif choice == "3":
            print("You approach the mysterious altar...")
            # Logic for encountering a monster or finding an exit
            player.attack_alter(20)
            print("Player was granted an attack buff!")
            print(f"Player attack boosted to {player.get_attack()}!")
            break
        elif choice == "4":
            print("You get Lost... decide to retreat back to the entrance of Dungeon 2....\n")
            # Logic for traversing 
            dungeon_2(player)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

def dungeon_3(player):
    print("\nWelcome to Dungeon 3!")
    print("You step into a dark, musty old library, books lining the shelves.\nYou hear a strange hummm...")
    while True:
        print("\nWhat do you want to do?")
        print("1. Examine the books on the shelves")
        print("2. Search for a hidden passage")
        print("3. Investigate the dusty tome on the pedestal")
        print("4. Leave the library")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You examine the books on the shelves...")
            # Logic for finding an item 
            print("You find a clue to helping you defeat the Lich!")
            print(f"{player.get_name()} learned skill synergy!")
            player.health_alter(player.get_defense())
            player.attack_alter(player.get_defense())
            print("Player has evolved!")
            player.status()
            break
        elif choice == "2":
            print("You search for a hidden passage...")
            # Logic for encountering a monster
            print(f"{ghoulmon.roar()}")
            battle(player, ghoulmon)
            break
        elif choice == "3":
            print("You investigate the dusty tome on the pedestal...")
            # Logic for finding an item 
            print("You find a necronominon o' ebon")
            player.health_alter(-50)
            print(f"{player.get_name()} has been cursed! \nplayer health: {player.get_health()}")
            break
        elif choice == "4":
            print("You decide to leave the library....\n")
            # Logic for exiting the dungeon
            print(f"You got jumped dastardly by a {zombiemon.get_name()}! \n{zombiemon.roar()}")
            if player.get_health > 0:
                dungeon_4(player)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")
            
def dungeon_4(player):
    print("\nWelcome to Dungeon 4!")
    print("You find yourself in an ancient temple, with intricate carvings adorning the walls.")
    while True:
        print("\nWhat do you want to do?")
        print("1. Examine the carvings on the walls")
        print("2. Offer a prayer at the altar")
        print("3. Descend into the dark abyss below")
        print("4. Retreat back to the entrance")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You examine the intricate carvings on the walls...")
            # Logic for finding an item or encountering a monster
            print(zombiemon.roar())
            battle(player, zombiemon)
            break
        elif choice == "2":
            print("You offer a prayer at the ancient altar...")
            print(f"{player.get_name()} is blessed!\n{25} bonus to attack!")
            player.attack_alter(25)
            break
        elif choice == "3":
            print("You descend into the dark abyss below...")
            print(f"You find a lamp... a dijiin pulls your hang nail for {-10} damage!")
            player.alter_health(-10)
            print(f"Health: {player.get_health()}")
            break
        elif choice == "4":
            print("You decide to take a break to plan and recover.")
            player.health_alter(25)
            print(f"{player.get_name()} recovers {25} health!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def dungeon_5(player):
    print("\nWelcome to Dungeon 5!")
    print("You enter a chamber filled with mystical energy, crackling with power.")
    while True:
        print("\nWhat do you want to do?")
        print("1. Channel the mystical energy")
        print("2. Attempt to decipher the ancient runes")
        print("3. Explore the hidden passages")
        print("4. Retreat back to the entrance")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("You attempt to channel the mystical energy...")
            player.attack_alter(20)
            print("Player absorbs the power!")
            break
        elif choice == "2":
            print("You attempt to decipher the ancient runes...")
            print(f"{player.get_name()} can't read the language")
            break
        elif choice == "3":
            print("You explore the hidden passages further...")
            battle(player, lichmon)
            break
        elif choice == "4":
            print("You hear noises...")
            print(zombiemon.roar())
            battle(player, zombiemon)
            print("It was sent by the Lich look out!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

def start_game(player):
    print(f"Welcome {player.name}!\n")
    print("Let the adventure begin!\n")
    dungeon_functions = [dungeon_1, dungeon_2, dungeon_3, dungeon_4, dungeon_5]
    for i, dungeon_func in enumerate(dungeon_functions, start=1):
        print(f"You are now in Dungeon {i}\n")
        dungeon_func(player)
        print("\n")  # Add a newline for clarity
    print("You have reached the final dungeon. Prepare to face the Lich Lord!")
    # Final battle logic here
    battle(player, lichmon)
    if player.get_health() > 0 and lichmon.get_health() < 0:
        print(f"{player.get_name()} has defeated the Lich!!!!")
        print("Thank you for playing!")
        sys.exit()
    else:
        print(f"{player.get_name()} has lost the battle!")
        print("Thank you for playing!")
        print("Play again...?")
        play = input("Yes or No..\n")
        if play.lower() == "no":
            print("Thank you for playing! Goodbye")
            sys.exit()
        else:
            main()
        

def how_to_play():
    print("\nHow to Play:")
    print("1. Enter your name without using spaces when prompted.")
    print("2. Choose your class from the available options.")
    print("3. Explore each dungeon by battling monsters or finding the exit.")
    print("4. Use your attacks strategically to defeat enemies.")
    print("5. Progress through all five dungeons to reach the Lich Lord.")
    print("6. Defeat the Lich Lord to win the game and restore peace to the realm.\n")

def show_class_stats():
    print("\nClass Stats:")
    print(divider)
    print("1. Flexor:")
    print("   - Health: 160")
    print("   - Attack: 70")
    print("   - Defense: 25")
    print("   - Starting Items: Potion, Chain")
    print(divider)
    print("2. Warlock:")
    print("   - Health: 120")
    print("   - Attack: 70")
    print("   - Defense: 15")
    print("   - Starting Items: Potion, Staff")
    print(divider)
    print("3. Holy Saint:")
    print("   - Health: 115")
    print("   - Attack: 65")
    print("   - Defense: 20")
    print("   - Starting Items: Potion, Blessed Bible")
    print(divider)
    print("4. Paladin:")
    print("   - Health: 145")
    print("   - Attack: 75")
    print("   - Defense: 35")
    print("   - Starting Items: Potion, Holy Saber")
    print(divider)

def main():
    print_intro()
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            player_name = input("Enter your name (no spaces allowed): ")
            if not re.match("^\S+$", player_name):
                print("Invalid name. Please enter a name without spaces.")
                continue
            print(f"\nYou chose the name: {player_name}")
            print("\nChoose your class:")
            print("1. Flexor")
            print("2. Warlock")
            print("3. Holy Saint")
            print("4. Paladin")
            class_choice = input("Enter the number corresponding to your class: ")
            player_class = None
            if class_choice == "1":
                player_class = Flexor(player_name)
            elif class_choice == "2":
                player_class = Warlock(player_name)
            elif class_choice == "3":
                player_class = HolySaint(player_name)
            elif class_choice == "4":
                player_class = Paladin(player_name)
            else:
                print("Invalid choice. Please enter a number between 1 and 4.\n")
                continue
            class_name = player_class.__class__.__name__
            print(f"\nYou chose the class: {class_name}")
            start_game(player_class)
        elif choice == "2":
            how_to_play()
        elif choice == "3":
            show_class_stats()
        elif choice == "4":
            print("\nThank you for playing Lich Lord!\n")
            sys.exit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()