class Enemies():
    def __init__(self, name, health, attack, defence, avoidance, speed):
        self.name=name 
        self.health=health
        self.attack=attack
        self.defence=defence
        self.avoidance=avoidance
        self.speed=speed
        self.effects = {}
        self.enemy_stat=[self.health, self.attack, self.defence,self.avoidance,self.speed]

    def show_stats(self):
        print(f"Name: {self.name} \nHealth: {self.health} \nAttack: {self.attack} \nDefence: {self.defence} \nAvoidance: {self.avoidance} \nSpeed: {self.speed}")

    def guard_sword_stats(self):
        self.health=4
        self.attack=3
        self.defence=1
        self.avoidance=0
        self.speed=1
        #self.guard=[self.health, self.attack, self.defence]

    def guard_bow(self):
        self.health=2
        self.attack=1
        self.defence=0
        self.avoidance=0.3
        self.speed=3

    def enemy_stat(self):
        self.enemy_stat=[self.health, self.attack, self.defence,self.avoidance,self.speed]



    def enemy_fight(self):
        stats=[]

    def tick_effects(self):
        if "Poison" in self.effects:
         self.health -= 1
        if "Bleeding" in self.effects:
         self.health -= 1
         self.effects = {e: t - 1 for e, t in self.effects.items() if t > 1}

    def is_stunned(self):
        return "Stun" in self.effects

    #guard_sword=guard_sword_stats()
    
guard = Enemies('Guard', 4, 3, 1, 0, 1)
guard.effects["Poison"] = 3
guard.tick_effects()
print(guard.health, guard.effects)   # 3 {'Poison': 2}
 #Test
# guard=Enemies('Guard',4,3,1,0,1)
# shooter=Enemies('Bowman',2,1,0,0.2,3)
# print(guard.show_stats())
# print(shooter.health)




