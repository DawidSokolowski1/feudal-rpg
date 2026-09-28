from intro import Intro
from Inventory import Inventory
from enemies import Enemies

class Player(Intro):
    def __init__(self):
        self.health=35
        self.max_health = self.health
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

        self.exp = 0
        self.level = 1
        self.exp_to_level = 10

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

    def gain_exp(self, amount):
        print(f"\nYou gained {amount} EXP.")
        self.exp += amount
        while self.exp >= self.exp_to_level:
            self.exp -= self.exp_to_level
            self.level += 1
            self.exp_to_level += 10
            print(f"\nLevel up! You are now level {self.level}.")
            self.choose_stat_upgrade()


    def choose_stat_upgrade(self):
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
                self.avoidance = min(round(self.avoidance + 0.05, 2), 0.5)
                print(f"Avoidance increased to {self.avoidance}")
                break
            elif choice == "4":
                self.speed += 1
                print(f"Speed increased to {self.speed}")
                break
            else:
                print("Enter a number between 1-4")

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

