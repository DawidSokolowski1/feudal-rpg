"""Start of the game: run with `python -m feudal_rpg`.

A new player is created and the world loop starts at the house. If
the player chooses "Restart the whole game" after dying, explore()
returns "restart" and the loop starts over with a fresh player.
"""
from .Player import Player
from .text_tempo import pause
from . import world
from .location import LOCATIONS


while True:
    player = Player()
    player.player_stats_normal()
    result = world.explore(player, LOCATIONS, "house")
    if result != "restart":
        break
