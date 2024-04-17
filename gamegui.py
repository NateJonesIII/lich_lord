# gamegui.py

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from game import Game

class GameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Lich Lord")
        self.master.geometry("800x600")
        self.game = Game()
        
        # Text area for game output
        self.text_area = ScrolledText(master, height=20, width=100)
        self.text_area.pack(pady=10)
        
        # Entry widget for player name input
        self.name_entry = tk.Entry(master, width=50)
        self.name_entry.pack(pady=5)
        self.name_entry.bind("<Return>", self.get_name)
        
        # Buttons
        self.quit_btn = tk.Button(master, text="Quit", command=master.quit)
        self.quit_btn.pack(side=tk.RIGHT, padx=10)
        
        # Initialize game
        self.init_game()
    
    def init_game(self):
        intro_text = (
            "Welcome to the Dungeon Adventure!\n"
            "Are you brave enough to enter the dungeon?\n"
            "Enter your name to begin.\n"
        )
        self.text_area.insert(tk.END, intro_text)
        
    def get_name(self, event):
        player_name = self.name_entry.get().strip()
        self.name_entry.delete(0, tk.END)  # Clear input
        self.text_area.insert(tk.END, f"Welcome, {player_name}!\n")
        self.text_area.insert(tk.END, "Now, choose your class:\n")
        self.text_area.insert(tk.END, "1) Warlock\n2) Holy Saint\n3) Paladin\n4) Flexor\n")
        self.text_area.see(tk.END)  # Scroll to the bottom
        
        # Entry widget for class selection
        self.input_entry = tk.Entry(self.master, width=80)
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<Return>", lambda event: self.get_class(player_name, event))
        
    def get_class(self, player_name, event):
        player_class = self.input_entry.get().strip().lower()
        self.input_entry.delete(0, tk.END)  # Clear input
        
        if self.game.create_player(player_name, player_class):
            self.text_area.insert(tk.END, f"You have chosen the path of the {player_class.capitalize()}!\n")
            self.text_area.insert(tk.END, "Let the adventure begin!\n")
            self.text_area.see(tk.END)  # Scroll to the bottom
            self.input_entry.bind("<Return>", self.process_input)  # Reset input binding
        else:
            self.text_area.insert(tk.END, "Invalid choice. Choose your class.\n")
            self.text_area.see(tk.END)  # Scroll to the bottom
            
    def process_input(self, event):
        user_input = self.input_entry.get().strip().lower()
        self.input_entry.delete(0, tk.END)  # Clear input
        
        # Process player input using game logic
        if self.game.process_input(user_input):
            # Update text area if game logic signals to update
            self.update_text_area()
    
    def update_text_area(self):
        # Clear text area and display updated game output
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, "Updated game output here...\n")
    
    def show_menu(self):
        self.text_area.insert(tk.END, "Menu:\n")
        self.text_area.insert(tk.END, "1) Door\n2) Stairs\n3) You hear noises...\n4) Pet cat\n5) Chest\n6) Next Floor\n7) Quit Game\n")
        self.text_area.see(tk.END)  # Scroll to the bottom
        
        # Entry widget for player input
        self.input_entry = tk.Entry(self.master, width=80)
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<Return>", self.process_input)

def main():
    root = tk.Tk()
    app = GameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()