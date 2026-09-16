from Player import Player
from enemies import Enemies
import random
class Fight():
    def __init__(self, player, enemy_1, enemy_2,enemy_3):
        self.enemy_1=enemy_1
        self.enemy_2=enemy_2
        self.enemy_3=enemy_3
        self.player=player

    # def fight(self):
    #     print(self.player.health)
    #     enemies=[self.enemy_1, self.enemy_2, self.enemy_3]
    #     print(self.enemy_1.health)

    #     while self.player.health >= 0 and self.enemy_1.health+self.enemy_2.health+self.enemy_3.health>0:
    #         for enemy in enemies:
    #             print(enemy.health)
    #             if self.player.speed < enemy.speed:
    #                 self.player.health=self.player.health-(self.player.defence-enemy.attack)
    #                 print(self.player.health)
    #                 print("XXX")
    #             elif self.player.speed >= enemy.speed:
    #                 choice=int(input("Choose comand: \n1. Attack\n2.Increase your defence \n"))
    #                 if choice ==1:
    #                     enemy.health-=self.player.attack
    #                     print("Enemy health: " + str(enemy.health))
    #                 if choice ==2:
    #                     self.player.defence+=1

    def enemy_1_attack(self,enemy):
        self.player.health-=self.enemy_1.attack
        print(f"{self.enemy_1.name} hit u with {self.enemy_1.attack} damage. \nYour HP: {self.player.health}")

    def fight_start(self):
        print("You encoutered enemies!")
        self.enemies_status()

    def enemies_status(self):
        print ("\nEnemy: ".ljust(15)+self.enemy_1.name.ljust(15)  +  self.enemy_2.name.ljust(15)  + self.enemy_3.name.ljust(15)  +
              "\nHP: ".ljust(15) + str(round(self.enemy_1.health,1)).ljust(15)   + str(round(self.enemy_2.health,1)).ljust(15)  + str(round(self.enemy_3.health,1)).ljust(15) +
               "\n\nAttack: ".ljust(16)   +str(self.enemy_1.attack).ljust(15)  + str(self.enemy_2.attack).ljust(15) + str(self.enemy_3.attack).ljust(15)+
               "\nDefence: ".ljust(15)  +str(self.enemy_1.defence).ljust(15) + str(self.enemy_2.defence).ljust(15) + str(self.enemy_3.defence).ljust(15)+
               "\nAvoidance: ".ljust(15) +str(self.enemy_1.avoidance).ljust(15)  + str(self.enemy_2.avoidance).ljust(15) + str(self.enemy_3.avoidance).ljust(15)+
                "\nSpedd : ".ljust(15)  +str(self.enemy_1.speed).ljust(15)  + str(self.enemy_2.speed).ljust(15) + str(self.enemy_3.speed).ljust(15) )

        
    def opponent_choice(self):
        status=False
        enemies=[self.enemy_1,self.enemy_2,self.enemy_3]
        while status==False:
          try:
            opponent_choice=int(input("\nChoose the opponennt u want to attack: "+
                                "\n 1:"+ self.enemy_1.name+
                                "\n 2:" + self.enemy_2.name+
                                "\n 3:" + self.enemy_3.name+
                                "\n"))
          
            for index, enemy in enumerate(enemies):
                if opponent_choice==index+1:
                    if enemy.health>0:
                        if random.random() > enemy.avoidance:
                            print("XXX")
                            if enemy.health >0:
                             if enemy.defence < self.player.temp_attack:
                                enemy.health=enemy.health-(self.player.temp_attack-enemy.defence)
                                print("\nYou damaged: "+ enemy.name+
                                    "\nDamage: " +  str(self.player.attack-enemy.defence))
                                if enemy.health <0:
                                    enemy.health= 0
                                status=True
                             else:
                                 enemy.health-=1
                                 print("\nYou damaged: "+ enemy.name+
                                        "\nDamage: " +  str(1))
                                 status=True
                            else:
                                print("This is a corpse already!")
                        else:
                                print("You missed!")
                                status=True
                    else:
                        print("\nThis is a corpse already!"+
                              "\nAttack living opponents!")
          except ValueError:
              print("U need to enter a number")

    def focus(self):
        command=int(input("Choose the attribute u want to increase for the fight: "+
                          "\n1: Attack"+
                          "\n2: Defence"+
                          "\n3: Avoidance"+
                          "\n4: Speed"+
                          "\n"))
        if command==1:
            player.temp_attack*=1.1
            player.temp_attack=round(player.temp_attack,1)
            print("Your Attack increased to: " + str(player.temp_attack))
        elif command==2:
            player.temp_defence*=1.1
            player.temp_defence=round(player.temp_defence,1)
            print("Your Defence increased to: " + str(player.temp_defence))
        elif command==3:
            player.temp_avoidance+=0.1
            player.temp_avoidance=round(player.temp_avoidance,3)
            print("Your Avoidance increased to: " + str(player.temp_avoidance))
        elif command==4:
            player.temp_speed*=2
            player.temp_speed=round(player.temp_speed,1)
            print("Your Speed increased to: " + str(player.temp_speed))

        else:
            print("XXX")         
    # def focus(self):
    #     stats=[self.player.attack,self.player.defence, self.player.avoidance, self.player.speed]
    #     stats_focus=stats[:]
    #     try:
    #         choice_focus=int(input(("Choose the stat u want to increase for the fight: ")))
    #         for index, stat in enumerate(stats):
    #             print("FFF")
    #             if choice_focus==index:
    #                 stats_focus[choice_focus]*=1.1
    #                 print(stats_focus[choice_focus])
    #                 print(stats_focus)
                   
            
                    
    #     except ValueError:
    #         print("Enter a number!")


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
            # else:
            #     print("\nPress number between 1 and 3")
            #     status=False
           
    def enemy_attack(self, enemy):
        if self.player.temp_avoidance < random.random():
            if self.player.temp_defence>=enemy.attack:
                self.player.health-=1
                print("\n"+enemy.name + " attacked you!"+
                    "\nDamage: "+ str(1)+
                    "\nYour Health: " + str(round(self.player.health,1))+
                    "\n")
            else:
                self.player.health=self.player.health-(enemy.attack-self.player.temp_defence)
                if self.player.health>0:
                    print("\n"+enemy.name + " attacked you!"+
                        "\nDamage: "+ str(round(enemy.attack - self.player.temp_defence,1))+
                        "\nYour Health: " + str(round(self.player.health,1))+
                            "\n")
                else:
                    print("\n"+self.enemy_1.name + " attacked you!"+
                            "\nDamage: "+ str(round(enemy.attack - self.player.temp_defence,1)))
                    print("You are Dead!")
        else:
            print("\nYou avoided the enemy's attack")


    def speed_check(self):
        battlefield={"Player": [self.player.health, self.player.attack, self.player.defence ,self.player.avoidance, self.player.speed],
                    "Enemy 1" : [round(self.enemy_1.health,1), self.enemy_1.attack, self.enemy_1.defence ,self.enemy_1.avoidance,self.enemy_1.speed],
                    "Enemy 2" : [round(self.enemy_2.health,1), self.enemy_2.attack, self.enemy_2.defence ,self.enemy_2.avoidance,self.enemy_2.speed],
                    "Enemy 3" : [round(self.enemy_3.health,1), self.enemy_3.attack, self.enemy_3.defence ,self.enemy_3.avoidance,self.enemy_3.speed]}
        move_order=sorted(battlefield.items(), key=lambda item: item[1][4], reverse=True)
        while self.player.health >0 and (self.enemy_1.health + self.enemy_2.health + self.enemy_3.health) >0: 
            for move, speed in move_order:
            # print(str(move))
                if move=="Player":
                 while True:
                  try:
                    command=int(input("Enter your command: "+
                                      "\n1.Attack Enemy"+
                                      "\n2.Focus: Increase one stat by 1"
                                      "\n3. Use an Item"
                                      "\n"))
                    if command==1:
                        self.opponent_choice()
                        self.enemies_status()
                        break
                    elif command==2:
                        print("LRÁ")
                        self.focus()
                        break
                    else:
                        print("Enter number between 1-3!")
                #elif move in battlefield  --> Idea to make the code smaller 
                 #   print("JAAAA")    
                  except ValueError:
                     print("You neeed to enter a number!")
                elif move=="Enemy 1" and self.enemy_1.health >0:
                    self.enemy_attack(self.enemy_1)
                    if self.player.health<0:
                        break
                    # if self.player.temp_avoidance < random.random():
                    #     if self.player.temp_defence>=self.enemy_1.attack:
                    #         self.player.health-=1
                    #         print("\n"+self.enemy_1.name + " attacked you!"+
                    #             "\nDamage: "+ str(1)+
                    #             "\nYour Health: " + str(round(self.player.health,1))+
                    #             "\n")
                    #     else:
                    #         self.player.health=self.player.health-(self.enemy_1.attack-self.player.temp_defence)
                    #         if self.player.health>0:
                    #             print("\n"+self.enemy_1.name + " attacked you!"+
                    #                 "\nDamage: "+ str(round(self.enemy_1.attack - self.player.temp_defence,1))+
                    #                 "\nYour Health: " + str(round(self.player.health,1))+
                    #                     "\n")
                    #         else:
                    #             print("\n"+self.enemy_1.name + " attacked you!"+
                    #                     "\nDamage: "+ str(round(self.enemy_1.attack - self.player.temp_defence,1)))
                    #             print("You are Dead!")
                    #             break
                    # else:
                    #     print("\nYou avoided the enemy's attack")
                elif move=="Enemy 2" and self.enemy_2.health >0:
                    self.enemy_attack(self.enemy_2)
                    if self.player.health<0:
                        break
                    # if self.player.temp_avoidance < random.random():
                    #     if self.player.temp_defence>=self.enemy_2.attack:
                    #         self.player.health-=1
                    #         print("\n"+self.enemy_2.name + " attacked you!"+
                    #             "\nDamage: "+ str(1)+
                    #             "\nYour Health: " + str(round(self.player.health,1))+
                    #             "\n")
                    #     else:
                    #         self.player.health=self.player.health-(self.enemy_2.attack-self.player.temp_defence)
                    #         print("\n"+self.enemy_2.name + " attacked you!"+
                    #             "\nDamage: "+ str(round(self.enemy_2.attack - self.player.temp_defence,1))+
                    #             "\nYour Health: " + str(round(self.player.health,1))+
                    #             "\n")
                    # else:
                    #     print("\nYou avoided the enemy's attack")
                elif move=="Enemy 3" and self.enemy_3.health >0:
                    self.enemy_attack(self.enemy_3)
                    if self.player.health<0:
                        break
                    # if self.player.temp_avoidance < random.random():
                    #     if self.player.temp_defence>=self.enemy_3.attack:
                    #         self.player.health-=1
                    #         print("\n"+self.enemy_3.name + " attacked you!"+
                    #             "\nDamage: "+ str(1)+
                    #             "\nYour Health: " + str(round(self.player.health,1))+
                    #             "\n")
                    #     else:
                    #         self.player.health=self.player.health-(self.enemy_3.attack-self.player.temp_defence)
                    #         print("\n" + self.enemy_3.name + " attacked you!"+
                    #             "\nDamage: "+ str(round(self.enemy_3.attack - self.player.temp_defence,1))+
                    #             "\nYour Health: " + str(round(self.player.health - self.player.temp_defence,1))+
                    #             "\n")
                    # else:
                    #     print("\nYou avoided the enemy's attack")
                
                    
      


                                
    
player=Player()
#player.intro_get_information_player()
guard=Enemies('Guard',4,3,0,0,1)
fast_knight=Enemies('Fast Knight',8,3,3,0.2,10)
guard_big_1=Enemies('Big Guard',10,4,7,0,1)


fight=Fight(player,fast_knight, guard_big_1, guard)
# fight.fight()

#enemies=[guard,guard]

#fight.enemy_1_attack()
fight.fight_start()
fight.speed_check()
