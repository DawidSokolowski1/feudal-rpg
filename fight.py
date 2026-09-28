from Player import Player
from enemies import Enemies
from Inventory import Inventory
import random
import time
from text_tempo import fight_print
from text_tempo import enemy_stats_print

class Fight():
    def __init__(self, player, enemy_1, enemy_2,enemy_3):
        self.enemy_1=enemy_1
        self.enemy_2=enemy_2
        self.enemy_3=enemy_3
        self.player=player


   

    def enemy_1_attack(self,enemy):
        self.player.health-=self.enemy_1.attack
        fight_print(f"{self.enemy_1.name} hit u with {self.enemy_1.attack} damage. \nYour HP: {self.player.health}")

    def fight_start(self):
        fight_print("You encoutered enemies!")
        fight_print(player.inv.equiped, player.inv.get_bonus("Attack"))
        self.player.reset_temp_stats()
        self.enemies_status()

    def enemies_status(self):
        enemy_stats_print ("\nEnemy: ".ljust(15)+self.enemy_1.name.ljust(15)  +  self.enemy_2.name.ljust(15)  + self.enemy_3.name.ljust(15)  +
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
                            if enemy.health >0:
                             self.apply_weapon_status(enemy)
                             if enemy.defence < self.player.temp_attack:
                                enemy.health=enemy.health-(self.player.temp_attack-enemy.defence)
                                fight_print("\nYou damaged: "+ enemy.name+
                                    "\nDamage: " +  str(round(self.player.temp_attack-enemy.defence, 1)))
                                if enemy.health <0:
                                    enemy.health= 0
                                status=True
                             else:
                                 enemy.health-=1
                                 fight_print("\nYou damaged: "+ enemy.name+
                                        "\nDamage: " +  str(1))
                                 status=True
                            else:
                               fight_print("This is a corpse already!")
                        else:
                                fight_print("You missed!")
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
            self.player.temp_attack*=1.1
            self.player.temp_attack=round(player.temp_attack,1)
            fight_print("Your Attack increased to: " + str(player.temp_attack))
        elif command==2:
            self.player.temp_defence*=1.1
            self.player.temp_defence=round(player.temp_defence,1)
            fight_print("Your Defence increased to: " + str(player.temp_defence))
        elif command==3:
            self.player.temp_avoidance+=0.1
            self.player.temp_avoidance=round(player.temp_avoidance,3)
            fight_print("Your Avoidance increased to: " + str(player.temp_avoidance))
        elif command==4:
            self.player.temp_speed*=2
            self.player.temp_speed=round(player.temp_speed,1)
            fight_print("Your Speed increased to: " + str(player.temp_speed))

        else:
            print("")

    #for items against enemies
    def choose_enemy(self):
        enemies = [self.enemy_1, self.enemy_2, self.enemy_3]
        while True:
            choice = input("Target (1-3): ")
            if choice.isdigit() and 1 <= int(choice) <= 3 and enemies[int(choice) - 1].health > 0:
                return enemies[int(choice) - 1]
            fight_print("Pick a living enemy.")

    def apply_weapon_status(self, enemy):
        status, chance, duration = self.player.inv.weapon_status()
        if status and random.random() < chance:
            enemy.effects[status] = duration
            fight_print(f"{enemy.name} is now under the influence of {status}!")

    def use_item_menu(self):
            inv = self.player.inv
            names = list(inv.inventory["Items"])
            if not names:
                print("\nYou have no items.")
                return False
            for i, name in enumerate(names, 1):
                print(f"{i}. {name} x{inv.inventory['Items'][name]['Amount']}")
            choice = input("Number (anything else cancels): ")
            if not choice.isdigit() or not 1 <= int(choice) <= len(names):
                return False
            name = names[int(choice) - 1]
            enemy = None
            if inv.inventory["Items"][name]["Target"] == "enemy":
                enemy = self.choose_enemy()
            return inv.use_item(name, self.player, enemy)     
        

                   
            
           
    def enemy_attack(self, enemy):
        stunned = enemy.is_stunned()   # read BEFORE tick_effects
        enemy.tick_effects()
        if enemy.health <= 0:
            enemy.health = 0
            fight_print(f"\n{enemy.name} died from its wounds.")
            return
        if stunned:
            fight_print(f"\n{enemy.name} can't move.")
            return
        
        if enemy.heal > 0:
            others = [e for e in (self.enemy_1, self.enemy_2, self.enemy_3)
                  if e is not enemy and e.health > 0]
            if others:
                target = min(others, key=lambda e: e.health)
                before = target.health
                target.health = min(target.health + enemy.heal, target.max_health)
                healed = round(target.health - before, 1)
                fight_print(f"\n{enemy.name} heals {target.name} for {healed} HP!"
                    f"\n{target.name} HP: {round(target.health, 1)}")
                return
          
        if self.player.temp_avoidance < random.random():
            if self.player.temp_defence>=enemy.attack:
                self.player.health-=1
                fight_print("\n"+enemy.name + " attacked you!"+
                    "\nDamage: "+ str(1)+
                    "\nYour Health: " + str(round(self.player.health,1))+
                    "\n")
            else:
                self.player.health=self.player.health-(enemy.attack-self.player.temp_defence)
                if self.player.health>0:
                    fight_print("\n"+enemy.name + " attacked you!"+
                        "\nDamage: "+ str(round(enemy.attack - self.player.temp_defence,1))+
                        "\nYour Health: " + str(round(self.player.health,1))+
                            "\n")
                else:
                    fight_print("\n"+enemy.name + " attacked you!"+
                            "\nDamage: "+ str(round(enemy.attack - self.player.temp_defence,1)))
                    fight_print("You are Dead!")
        else:
            fight_print("\nYou avoided the enemy's attack")


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
                    elif command == 3:
                        if self.use_item_menu():
                            self.enemies_status()
                            break
                    else:
                        print("Enter number between 1-3!")
                #elif move in battlefield  --> Idea to make the code smaller 
                 #   print("JAAAA")    
                  except ValueError:
                     print("You neeed to enter a number!")
                elif move=="Enemy 1" and self.enemy_1.health >0:
                    self.enemy_attack(self.enemy_1)
                    if self.player.health<=0:
                        break
                   
                elif move=="Enemy 2" and self.enemy_2.health >0:
                    self.enemy_attack(self.enemy_2)
                    if self.player.health<=0:
                        break
                  
                elif move=="Enemy 3" and self.enemy_3.health >0:
                    self.enemy_attack(self.enemy_3)
                    if self.player.health<=0:
                        break
                   
                
    def resolve_fight(self, exp_reward):
        if self.player.health <= 0:
            return "dead"
        self.player.reset_temp_stats()
        self.player.gain_exp(exp_reward)
        return "alive"                    
      


                                
    
player=Player()
#player.intro_get_information_player()
guard=Enemies('Guard',4,3,0,0,1)
fast_knight=Enemies('Fast Knight',8,3,3,0.2,10)
guard_big_1=Enemies('Big Guard',10,4,7,0,1)


fight=Fight(player,fast_knight, guard_big_1, guard)
# fight.fight()

#enemies=[guard,guard]

#fight.enemy_1_attack()

player.inv.pick_up("Items", "Bread")
player.inv.pick_up("Items", "Poison")
#test
#fight.fight_start()

#test
#fight.speed_check()
