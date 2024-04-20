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
        player.health -= self.get_attack()
        print(f"{self.get_name()} attacks the player with {self.get_attack()} damage!")
        
    def get_name(self):
        return self.name
    
    def get_health(self):
        if self.health < 0:
            return 0
        return self.health
    
    def get_attack(self):
        return self.attack
    
    def health_alter(self, pts):
        self.health += pts
    
class Lich(Monster):
    def __init__(self):
        super().__init__("LICH LORD", 500, 30)

    def roar(self):
        print("The dark incantations of the SLIME LORD fill the air...\n")
        return "The dark incantations of the SLIME LORD fill the air...\n"

    def attack_enemy(self, player):
        player.health -= self.attack
        print(f"The Lich liches forward, blasting bile, dealing {self.attack} damage!\n The Lich is chanting some kind of filth!")
        
class Demon(Monster):
    def __init__(self):
        super().__init__("Demon", 200, 29, 35)

    def roar(self):
        return "The terrifying roar of the Demon echoes in the darkness...\n"
    
    def attack_enemy(self, player):
        player.health -= self.attack
        print(f"The Demon lunges forward, claws slashing, dealing {self.attack} damage!\nThe demons calls you filth!")


class Ghoul(Monster):
    def __init__(self):
        super().__init__("Ghoul", 150, 25)

    def roar(self):
        return "The chilling moans of the Ghoul send shivers down your spine...\n"

    def attack_enemy(self, player):
        player.health -= self.attack
        print(f"The Ghoul's decaying hands reach out, dealing {self.attack} damage!")
        
class Pidgeonpig(Monster):
    def __init__(self):
        super().__init__("Pidgeonpig", 85, 15, 10)

    def roar(self):
        print("The unsettling cooing of the Pidgeonpig fills the area...\n")
        return "The unsettling cooing of the Pidgeonpig fills the area...\n"
    
    def attack_enemy(self, player):
        bonus = 5
        
        player.health -= self.get_attack()
        print(f"The Pidgeonpig pecks viciously, inflicting {self.get_attack()} damage!")
        player.health -= bonus
        print(f"Oh no! The Pidgeonpig flapped mud at player for additional {bonus} damage!")
       
 

class Zombie(Monster):
    def __init__(self):
        super().__init__("Pickle the Zombie", 75, 28)

    def roar(self):
        return "The guttural groans of the Zombie resonate in the silence...\n"
    
    def attack_enemy(self, player):
        player.health -= self.get_attack()
        self.health_alter(5) # Regenerative attack
        print(f"The Zombie's decomposing claws swipe, dealing {self.get_attack()} damage and regenerating 5 HP!")
        
class Leecher(Monster):
    def __init__(self):
        super().__init__("Leecher", 150, 25)

    def roar(self):
        return "The gargling nosie of the Leecher causes you to turn pale in fear...\n"

    def attack_enemy(self, player):
        player.health -= self.get_attack()
        print(f"The Leech's tentacles reach out, dealing {self.attack} damage!")