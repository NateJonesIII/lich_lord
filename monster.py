# monster.py

class Monster:
    def __init__(self, name="", health=0, attack=0, armor=0):
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor

    def get_status(self):
        print(f"{self.name} | Health: {self.health} | Attack: {self.attack} | Armor: {self.armor}")
    
    def roar(self):
        print("\nRoar\n")
        
    def attack(self, player):
        player.health -= self.attack
        print(f"{self.name} attacks the player with {self.attack} damage!")
    
class Lich(Monster):
    def __init__(self):
        super().__init__("SLIME LORD", 500, 30)

    def roar(self):
        print("The dark incantations of the SLIME LORD fill the air...\n")
        return "The dark incantations of the SLIME LORD fill the air...\n"


class Demon(Monster):
    def __init__(self):
        super().__init__("Demon", 200, 40, 25)

    def roar(self):
        return "The terrifying roar of the Demon echoes in the darkness...\n"
    
    def attack(self, player):
        player.health -= self.attack
        print(f"The Demon lunges forward, claws slashing, dealing {self.attack} damage!\n The demons calls you filth!")


class Ghoul(Monster):
    def __init__(self):
        super().__init__("Ghoul", 150, 25)

    def roar(self):
        return "The chilling moans of the Ghoul send shivers down your spine...\n"

    def attack(self, player):
        player.health -= self.attack
        print(f"The Ghoul's decaying hands reach out, dealing {self.attack} damage!")
        
class Pidgeonpig(Monster):
    def __init__(self):
        super().__init__("Pidgeonpig", 51, 10, 10)

    def roar(self):
        print("The unsettling cooing of the Pidgeonpig fills the area...\n")
        return "The unsettling cooing of the Pidgeonpig fills the area...\n"
    
    def attack_player(self, player):
        bonus = int(self.attack / 2)
        player.health -= self.attack
        print(f"The Pidgeonpig pecks viciously, inflicting {self.attack} damage!")
        player.health -= bonus
        print(f"Oh no! The Pidgeonpig flapped mud at player for additional {bonus} damage!")
        return player.health
 

class Zombie(Monster):
    def __init__(self):
        super().__init__("Zombie", 75, 15)

    def roar(self):
        return "The guttural groans of the Zombie resonate in the silence...\n"
    
    def attack(self, player):
        player.health -= self.attack
        self.hp += 5  # Regenerative attack
        print(f"The Zombie's decomposing claws swipe, dealing {self.attack} damage and regenerating 5 HP!")