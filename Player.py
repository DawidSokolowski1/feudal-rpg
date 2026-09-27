from intro import Intro
from Inventory import Inventory
from enemies import Enemies

class Player(Intro):
    def __init__(self):
        self.health=30
        self.attack=5
        self.defence=1
        self.avoidance=0.1
        self.speed=1.01
        self.player_stats=[self.health, self.attack, self.defence, self.avoidance, self.speed]
        self.inv = Inventory()
# Temp stats, that increase only during the battle 
        self.temp_attack=self.attack
        self.temp_defence=self.defence
        self.temp_avoidance=self.avoidance
        self.temp_speed=self.speed

    def player_stats_intro(self):
        self.health=25
        self.attack=2
        self.defence=0
        self.avoidance=0.0
        self.speed=0.5

    def player_stats_normal(self):
        self.health = 30
        self.attack = 5
        self.defence = 1
        self.avoidance = 0.1
        self.speed = 1.01

    def print_health(self):
        print(self.health)

    def intro_get_information_player(self):
        self.name=self.get_name()
        self.age=self.get_age()
        self.zodiac=self.get_zodiac()
        return self.name, self.age, self.zodiac

    def player_status(self):
        print("\nName: ".ljust(15) + #self.name+
              "\nHP: ".ljust(15) + str(self.health)+
              "\nAttack: ".ljust(15) + str(self.attack)+
              "\nDefence: ".ljust(15) + str(self.attack)+
              "\nAvoidacne: ".ljust(15) + str(self.avoidance)+
              "\nSpeed: ".ljust(15) + str(self.speed))

# calculates player stats + equiped inventory 
    def reset_temp_stats(self):
        self.temp_attack = self.attack + self.inv.get_bonus("Attack")
        self.temp_defence = self.defence + self.inv.get_bonus("Defence")
        self.temp_avoidance = self.avoidance + self.inv.get_bonus("Avoidance")
        self.temp_speed = self.speed + self.inv.get_bonus("Speed")

player=Player()
# player.intro_get_information_player()
# print(player.name)
# player.player_status()
# player=Player()
# player.intro_get_information_player()
# print(player.name)
# Test
#player=Player()
# player.print_health()
# print(player.player_stats)
        
player = Player()
guard = Enemies("Guard", 4, 3, 1, 0, 1)

