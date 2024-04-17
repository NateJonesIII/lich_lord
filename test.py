from lichlord_game.player import Player
from monster import Monster, Pidgeonpig, Demon, Ghoul, Lich
# objects
player = Player()
pp = Pidgeonpig()

player.add_to_pouch("potion")
# reveal pouch items
player.show_pouch()
# Test monster status method
pp.get_status()

# Test attacking enemy
pp.attack_player(player)
player.status()
# Test attacking player
player.attack_enemy(pp)