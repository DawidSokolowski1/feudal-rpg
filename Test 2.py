from intro import Intro

class Player(Intro):
    def __init__(self):
        self.health=30
        self.attack=5
        self.defence=3
        self.avoidance=0.05
        self.speed=1.01
        self.player_stats=[self.health, self.attack, self.defence, self.avoidance, self.speed]

        self.temp_attack=self.attack
        self.temp_defence=self.defence


    def print_health(self):
        print(self.health)

    def focus(self):
        command=int(input("Choose the attribute u want to increase for the fight: "))
        if command==1:
            self.temp_attack*=1.1
        elif command==2:
            self.temp_defence*=1.1
        else:
            print("XXX")

    def player_temp_stats(self):
        temp_stats=[]
        for stat in self.player_stats:
            stat*=2
            temp_stats.append(stat)
        print(temp_stats)
        return temp_stats

player=Player()
player.player_temp_stats()
player.focus()
print(player.temp_attack)
player.focus()
print(player.temp_attack)