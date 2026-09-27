class Enemies():
    def __init__(self, name, health, attack, defence, avoidance, speed):
        self.name=name 
        self.health=health
        self.max_health = health 
        self.attack=attack
        self.defence=defence
        self.avoidance=avoidance
        self.speed=speed
        self.effects = {}
        self.enemy_stat=[self.health, self.attack, self.defence,self.avoidance,self.speed]



    def spawn(name, count=1):
        stats = ENEMY_TEMPLATES[name]
        if count == 1:
            return Enemies(name, stats["health"], stats["attack"],
                            stats["defence"], stats["avoidance"], stats["speed"])
        return [
            Enemies(f"{name} {i+1}", stats["health"], stats["attack"],
                    stats["defence"], stats["avoidance"], stats["speed"])
            for i in range(count)
        ]

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


ENEMY_TEMPLATES = {
    "Mercenary": {"health": 5, "attack": 3, "defence": 1, "avoidance": 0, "speed": 1},
    "Guard": {"health": 6, "attack": 3, "defence": 1, "avoidance": 0.1, "speed": 2},
    "Fast Knight": {"health": 8, "attack": 3, "defence": 3, "avoidance": 0.2, "speed": 10},
    "Healer": {"health": 5, "attack": 1, "defence": 1, "avoidance": 0.1, "speed": 2, "heal": 2},
}

def spawn(name, count=1):
    stats = ENEMY_TEMPLATES[name]
    if count == 1:
        enemy = Enemies(name, stats["health"], stats["attack"],
                         stats["defence"], stats["avoidance"], stats["speed"])
        enemy.heal = stats.get("heal", 0)
        return enemy
    result = []
    for i in range(count):
        enemy = Enemies(f"{name} {i+1}", stats["health"], stats["attack"],
                         stats["defence"], stats["avoidance"], stats["speed"])
        enemy.heal = stats.get("heal", 0)
        result.append(enemy)
    return result

guard_1 = Enemies("Guard 1", 4, 3, 1, 0, 1)
guard_2 = Enemies("Guard 2", 4, 3, 1, 0, 1)
guard_3 = Enemies("Guard 3", 4, 3, 1, 0, 1)



 #Test
# guard=Enemies('Guard',4,3,1,0,1)
# shooter=Enemies('Bowman',2,1,0,0.2,3)
# print(guard.show_stats())
# print(shooter.health)




