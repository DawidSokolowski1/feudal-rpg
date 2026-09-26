class Items():
    def __init__(self):

        self.weapons={"Pitchfork":{"Attack":1, "Bonus": "No Bonus"},
        "Sickle":{"Attack":2, "Bonus": "Chance for bleeding effect"},
        "Fang-Studded Pike":{"Attack":2, "Bonus":""} #Bonus should be Wutanfall, Backstory: Farmer's dogs died due to famine so he made weapon out of their teeths
        }   
        self.armors={"Tunic":{"Defence":1},
                "Buff Coat":{"Defence":2},
                "Jack of Plate":{"Defence":3}}
        self.accessory={"Rune-Etched Ring":{"Avoidance":0.1},
                "Piece of Stem":{"Speed":1},
                "Shield-Formed Broche":{"Defence":1}}
        self.items={"Poison":{"Effect":-1},
                    "Bread":{"HP":5},
                    "Wine":{"Defence":1},
                    "Lavendel":{"Effect":""}}
        
class Inventory(Items):
    def __init__(self):
        super().__init__()
        self.inventory= {
            "Weapons": {},
            "Armor": {},
            "Accessories": {},
            "Items": {}
        }

        self.equiped={"Armor":None,
                "Weapon":None,
                "Accessory":None}
   
    def open_inventory(self):
            for index,(category, objects) in enumerate(self.inventory.items()):
                print(str(index+1) + " " + category+":")
                for item, stats in objects.items():
                    print("\n\t" + item +":")
                    for stat_desc, stat_value in stats.items():
                        print("\t\t"+ stat_desc + ": " + str(stat_value))
            inventory_choice=input("Press E to choose new equimpent: ").title()
            if inventory_choice=="E":
                 category_choice=int(input("Press a number assigned to the category: "))
                 for index,(category, objects) in enumerate(self.inventory.items()):
                     if category_choice==index+1:
                        for index_1,(item, stats) in enumerate(objects.items()):
                            print("\n\t" + str(index_1+1)+" " + item +":")  
                            for stat_desc, stat_value in stats.items():
                                print("\t\t"+ stat_desc + ": " + str(stat_value)) 
                        object_choice=int(input("Choose item you want to equip"))
                        for index,(item, stats) in enumerate(objects.items()):
                            if object_choice==index+1:
                                print("You equiped: " + item)
                                
                                    


        
   



inv=Inventory()
inv.inventory["Weapons"]["Pitchfork"]=inv.weapons["Pitchfork"]
inv.inventory["Weapons"]["Sickle"]=inv.weapons["Sickle"]
#print(inv.inventory)
inv.open_inventory()
# for category, items in inv.inventory.items():
#     print(category+":")
#     for item, stats in items.items():
#         print("\n\t" + item +":")
#         for stat_desc, stat_value in stats.items():
#             print("\t\t"+ stat_desc + ": " + str(stat_value))