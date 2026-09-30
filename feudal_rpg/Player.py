"""Player class for the feudal RPG: stats, levelling and battle stats."""

from .Inventory import Inventory


class Player:
    """The player character.

    Holds the base stats, the temporary battle stats, the inventory,
    the experience/level system and the death state.
    """

    def __init__(self):
        """Create a new player with starting stats and an empty inventory.

        Runs once when a Player object is created (player = Player()).
        """
        self.health = 30  # current hit points
        # Upper limit for health (e.g. the healer can't heal above it)
        self.max_health = self.health
        self.attack = 5  # base damage the player deals
        self.defence = 1  # reduces the damage the player takes
        self.avoidance = 0.1  # chance to dodge an attack (0.1 = 10%)
        self.speed = 1.01  # decides how fast the player acts in a fight
        # Snapshot of the starting stats. The values are copied at this
        # moment, so the list does not update when the stats change later.
        self.player_stats = [self.health, self.attack, self.defence,
                             self.avoidance, self.speed]
        # The player's own Inventory object (items and equipment)
        self.inv = Inventory()

        # Temp stats, that increase only during the battle.
        # They start as copies of the base stats; reset_temp_stats()
        # recalculates them before a fight, so buffs during a battle
        # don't permanently change the base stats.
        self.temp_attack = self.attack
        self.temp_defence = self.defence
        self.temp_avoidance = self.avoidance
        self.temp_speed = self.speed

        # Levelling system
        self.exp = 0  # experience collected towards the next level
        self.level = 1  # current level of the player
        # EXP needed to reach the next level (grows by 10 each level)
        self.exp_to_level = 10

        # Death tracking
        # True when the player has died (used for the retry system)
        self.has_died = False
        # Where the player died, so the game can restart from there
        self.died_at = None

    def player_stats_intro(self):
        """Set the weaker stats used during the intro part of the story.

        The player starts weak before the "real" game begins.
        """
        self.health = 25
        self.attack = 2
        self.defence = 0
        self.avoidance = 0.0
        self.speed = 0.5

    def player_stats_normal(self):
        """Set the player's stats back to the normal values after the intro."""
        self.health = 30
        self.attack = 5
        self.defence = 1
        self.avoidance = 0.1
        self.speed = 1.01

    def print_health(self):
        """Print only the current health of the player."""
        print(self.health)

    def player_status(self):
        """Print an overview of the player's stats.

        ljust(12) pads each label with spaces so the values line up in
        a column. Gear bonuses from equipped items are shown in
        brackets next to the base stat.
        """
        print("\n--- STATS ---")
        print("Level: ".ljust(12) + str(self.level))
        print("EXP: ".ljust(12) + f"{self.exp}/{self.exp_to_level}")
        print("HP: ".ljust(12) + f"{self.health}/{self.max_health}")
        for stat in ("Attack", "Defence", "Avoidance", "Speed"):
            base = getattr(self, stat.lower())
            bonus = self.inv.get_bonus(stat)
            line = (stat + ": ").ljust(12) + str(base)
            if bonus:
                line += f" (+{bonus} from gear)"
            print(line)

    def gain_exp(self, amount):
        """Add experience to the player and handle levelling up.

        Called e.g. after winning a fight. A while loop is used instead
        of an if, so the player can level up several times in a row
        when they get a lot of EXP at once.
        """
        print(f"\nYou gained {amount} EXP.")
        self.exp += amount
        while self.exp >= self.exp_to_level:
            # Leftover EXP carries over to the next level
            self.exp -= self.exp_to_level
            self.level += 1
            # Each level needs 10 more EXP than the previous one
            self.exp_to_level += 10
            print(f"\nLevel up! You are now level {self.level}." +
                  "\n")
            # Let the player pick which stat to improve
            self.choose_stat_upgrade()

    def choose_stat_upgrade(self):
        """Ask the player which stat to increase after a level up.

        The while True loop keeps asking until a valid choice (1-4) is
        typed; break exits the loop once a stat has been upgraded.
        """
        print("Choose a stat to upgrade:")
        print("1. Attack")
        print("2. Defence")
        print("3. Avoidance")
        print("4. Speed")
        while True:
            choice = input("> ")
            if choice == "1":
                self.attack += 1
                print(f"Attack increased to {self.attack}")
                break
            elif choice == "2":
                self.defence += 1
                print(f"Defence increased to {self.defence}")
                break
            elif choice == "3":
                # +5% dodge chance. round() avoids float errors like
                # 0.15000000002, and min(..., 0.5) caps avoidance at 50%
                # so the player can't become impossible to hit.
                self.avoidance = min(round(self.avoidance + 0.05, 2), 0.5)
                print(f"Avoidance increased to {self.avoidance}")
                break
            elif choice == "4":
                self.speed += 1
                print(f"Speed increased to {self.speed}")
                break
            else:
                # Any other input is invalid, so the loop asks again
                print("Enter a number between 1-4")

    def reset_temp_stats(self):
        """Calculate the battle stats: player stats + equipped inventory.

        inv.get_bonus("<Stat>") returns the total bonus the equipped
        gear gives for that stat. Called before a fight so any temporary
        changes from the last battle are removed.
        """
        self.temp_attack = self.attack + self.inv.get_bonus("Attack")
        self.temp_defence = self.defence + self.inv.get_bonus("Defence")
        self.temp_avoidance = (self.avoidance
                               + self.inv.get_bonus("Avoidance"))
        self.temp_speed = self.speed + self.inv.get_bonus("Speed")
