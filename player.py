# player.py
# divider variable
divider = "======================"

class Player:
    def __init__(self, name="", health=100, attack=50, defense=20, pouch=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.pouch = pouch if pouch is not None else []
        
    def status(self):
        print(divider)
        print(f"{self.name}'s Status:")
        print(divider)
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(divider)

    def last_resort_attack(self):
        # player last resort attack; life must be below 40 to activate
        if self.health < 40:
            print("Blessed hands of Heavanaught!")
            return 250
        else:
            print("There is no dire need of this ability to be used fight onward!")
            return 0
        
    def add_to_pouch(self, item):
        if len(self.pouch) < 7:
            self.pouch.append(item)
        else:
            print("Pouch is full. Swapping out items.")
            self.swap_and_add(item)

    def remove_from_pouch(self, item):
        if item in self.pouch:
            self.pouch.remove(item)
        else:
            print(f"{item} not found in pouch.")

    def swap_and_add(self, item):
        print(f"Swapping out {self.pouch[0]} with {item}")
        self.pouch.pop(0)
        self.pouch.append(item)
        
    def attack_enemy(self, enemy):
        enemy.health -= self.attack
        print(f"Player attacks {enemy.name} for {self.attack} damage!")

    def show_pouch(self):
        print("Items in pouch:")
        print(divider)
        for item in self.pouch:
            print(item)
        print(divider)
            
    def heal(self):
        if "potion" in self.pouch:
            print("You use a healing potion to heal back to full health!")
            self.health = 100
            self.pouch.remove("potion")
        else:
            print("No healing potion found in pouch.")
    
    def attack_alter(self, pts):
        self.attack += pts
    
    def health_alter(self, pts):
        self.health += pts
    
    def get_health(self):
        return self.health
    
    def get_name(self):
        return self.name
    
    def get_attack(self):
        return self.attack
    
    def get_defense(self):
        return self.defense
class Flexor(Player):
    def __init__(self, name="", health=160, attack=70, defense=25, pouch=["potion","chain"]):
        super().__init__(name, health, attack, defense, pouch)
    def status(self):
        print(divider)
        print(f"Flexer {self.name}'s Status:")
        print(divider)
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(divider)

class Warlock(Player):
    def __init__(self, name="", health=120, attack=70, defense=15, pouch=["potion","staff"]):
        super().__init__(name, health, attack, defense, pouch)
    
    def status(self):
        print(divider)
        print(f"Warlock {self.name}'s Status:")
        print(divider)
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(divider)
        
class HolySaint(Player):
    def __init__(self, name="", health=115, attack=65, defense=20, pouch=["potion","Blessed Bible"]):
        super().__init__(name, health, attack, defense, pouch)
    
    def status(self):
        print(divider)
        print(f"Holy Saint {self.name}'s Status:")
        print(divider)
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(divider)
        
        
class Paladin(Player):
    def __init__(self, name="", health=145, attack=75, defense=35, pouch=["potion","Holy Saber"]):
        super().__init__(name, health, attack, defense, pouch)
        
    def status(self):
        print(divider)
        print(f"Paladin{self.name}'s Status:")
        print(divider)
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(divider)