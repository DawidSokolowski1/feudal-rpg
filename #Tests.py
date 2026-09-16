#Tests
import random
from Player import Player
from enemies import Enemies
# country_pop={"Poland": 38000000, "Germany":80000000, "France": 60000000, "Japan": 150000000}
# for country in country_pop:
#     print(country)

# country_pop=sorted(country_pop.items(), key=lambda item: item[1], reverse=True)
# print("\nsorted:")
# for country in country_pop:
#     print(" "+country[0])

# country_infos={"Poland":[38, 'Szczecin', 'Europe'], "USA":[300, 'Washington D.C.', 'North America'], "Germany": [80,'Berlin', 'Europe']}
# for country, infos in country_infos.items():
#     print (infos[0])

# country_infos_sorted=sorted(country_infos.items(),key=lambda item: item[1][2])
# a,b,c=country_infos_sorted
# print(country_infos_sorted)
# print(a[1][1])

# x="Enemyyyyyyyyyyy"
# print(len(x))
# y=len(x)+10
# print(y)
# print(x +"Alien".rjust(30-len(x)) + "Ninja".rjust(30-len("Enemy"))
#       + "\nHP" + str(10).rjust(30-len("HP"))+ str(10).rjust(30-len("HP"))+
#       "\nAttack"+"30".rjust(30-len("Attack"))+"100".rjust(30-len("Attack")+len("100"))+
#       "\nDefenceeee"+"50".rjust(30-len("Defenceeee"))+ "50".rjust(30-len("Defenceeee")+len("50")))

# print("\nHP".ljust(20) + "20".ljust(20)+ "3000".ljust(20)+
#       "\nAttack".ljust(20) + "10".ljust(20) + "220000000000".ljust(20))


print("\n"+str(random.randint(1,100)))
print(random.randint(1,100)*0.20)
print(random.randint(1,100)*0.80)

print(5*0.95)
print(95*0.05)
print(random.random())
if random.random() < 0.05:
    print("You missed")
else: 
    print("You damaged your enemy")
    


player=Player()
guard=Enemies('Guard',10,10,10,0.1,10)
knight=Enemies('Knight',5,10,3,0,1)
print(guard.name)

battlefield=[player,guard,knight]
battlefield[1]

countries=[['Polska',38],['Germany',50]]
print(sorted(countries, key=lambda x:x[1]))
print(countries[1][1])


class Fight():
 def __init__(self, player, enemy_1, enemy_2,enemy_3):
        self.enemy_1=enemy_1
        self.enemy_2=enemy_2
        self.enemy_3=enemy_3
        self.player=player
        
 def focus(self):
            stats=[self.player.attack, self.player.defence, self.player.avoidance, self.player.speed]
            try:
                choice_focus=int(("Choose the stat u want to increase for the fight: "))
                for index, stat in enumerate(stats):
                    if choice_focus==index:
                        stat*=1.1
                    else:
                        break
            except ValueError:
                print("Enter a number!")
     
 def opponent_choice(self):
        status=False
        enemies=[self.enemy_1, self.enemy_2, self.enemy_3]
        while True:
            opponent_choice=int(input("\nChoose the opponennt u want to attack: "+
                                "\n 1:"+ self.enemy_1.name+
                                "\n 2:" + self.enemy_2.name+
                                "\n 3:" + self.enemy_3.name+
                                "\n"))
            for index, enemy in enumerate(enemies):
                    if opponent_choice==index+1:
                        if random.random() > enemy.avoidance:
                            print(enemy.health)
                            if enemy.health >0:
                                enemy.health-=self.player.attack
                                print("\nYou damaged: "+ enemy.name+
                                    "\nDamage: " + str(self.player.attack)+
                                    "\nEnemys health: " + str(enemy.health))

                                
                                
                            else:
                                print("This is a corpses already!")

                        else:
                            print("You missed!")
                            


            # if opponent_choice==1:
            #     status=True
            #     if random.random() > self.enemy_1.avoidance:
            #         if self.enemy_1.defence>=self.player.attack:
            #             self.enemy_1.health-=1
            #             if self.enemy_1.health<0:
            #                 self.enemy_1.health=0
            #         else:
            #             self.enemy_1.health=self.enemy_1.health-(self.player.attack-self.enemy_1.defence)
            #             if self.enemy_1.health<0:
            #                 self.enemy_1.health=0
            #         print("\nYou damaged opponent: " + self.enemy_1.name + 
            #               "\nDamage: " + str(self.player.attack-self.enemy_1.defence) )
            #     else:
            #         print("You missed!")
            # elif opponent_choice==2:
            #     status=True
            #     if random.random() > self.enemy_2.avoidance:
            #         if self.enemy_2.defence>=self.player.attack:
            #             self.enemy_2.health-=1
            #         else:
            #             self.enemy_2.health=self.enemy_2.health - (self.player.attack-self.enemy_2.defence)
            #             if self.enemy_2.health<0:
            #                 self.enemy_2.health=0
            #             print("\nYou damaged opponent: " + self.enemy_2.name + 
            #                   "\nDamage: " + str(self.player.attack-self.enemy_2.defence))
            # elif opponent_choice==3:
            #     status=True
            #     if random.random() > self.enemy_3.avoidance:
            #         if self.enemy_3.defence>=self.player.attack:
            #             self.enemy_3.health-=1
            #         else:
            #             self.enemy_3.health=self.enemy_3.health - (self.player.attack-self.enemy_3.defence)
            #             if self.enemy_3.health<0:
            #                 self.enemy_3.health=0
            #         print("\nYou damaged opponent: " + self.enemy_3.name +
            #               "\nDamage: " + str(self.player.attack-self.enemy_3.defence))
            else:
                print("\nPress number between 1 and 3")
                status=False




fight=Fight(player,guard,guard,knight)
# fight.opponent_choice()

fight.focus()
