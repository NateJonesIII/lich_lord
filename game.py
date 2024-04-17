# game.py

from player import Player, Warlock, HolySaint, Paladin, Flexor
from dungeon import dungeon_choices

class Game:
    def __init__(self):
        self.player = None
    
    def process_input(self, user_input):
        if not self.player:
            self.create_player(user_input)
            return
        
        if user_input in dungeon_choices:
            dungeon_choices[user_input](self.player)
            return True  # Signal to update GUI
        else:
            return False
    
    def create_player(self, player_name, player_class):
        class_mapping = {
            "1": Warlock,
            "2": HolySaint,
            "3": Paladin,
            "4": Flexor
        }
        
        if player_class in class_mapping:
            player_class = class_mapping[player_class]
            self.player = player_class(name=player_name)
            return True  # Signal to update GUI
        else:
            return False

if __name__ == "__main__":
    game = Game()
    while True:
        user_input = input("Enter your choice: ").lower()
        game.process_input(user_input)
