#Inventory and Items
class Items():
    def __init__(self):

        self.weapons = {
            "Pitchfork": {"Attack": 1},
            "Sickle": {"Attack": 2, "Status": "Bleeding", "Chance": 0.7, "Duration": 2},
            "Fang-Studded Pike": {
                "Attack": 2, "Status": "Wutanfall", "Chance": 0.3, "Duration": 2,
            },
        }   

        self.armors={
            "Tunic":{"Defence":1},
            "Buff Coat":{"Defence":2},
            "Jack of Plate":{"Defence":3
            },
        }

        self.accessory={
            "Rune-Etched Ring":{"Avoidance":0.1},
            "Piece of Stem":{"Speed":1},
            "Shield-Formed Broche":{"Defence":1
            },
        }

        self.items = {
            "Poison":   {"Status": "Poison", "Duration": 3, "Target": "enemy"},
            "Bread":    {"HP": 5, "Target": "self"},
            "Wine":     {"Defence": 1, "Target": "self"},
            "Lavendel": {"Status": "Stun", "Duration": 3, "Target": "enemy"
            },
        }


        self.catalog = {"Weapons": self.weapons, "Armor": self.armors,
                "Accessories": self.accessory, "Items": self.items}
        
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
        self.slots = {"Weapons": "Weapon", "Armor": "Armor", "Accessories": "Accessory"}

    def pick_up(self, category, name):
        if name in self.inventory[category]:
            if category == "Items":
                self.inventory[category][name]["Amount"] += 1
            return
        item = dict(self.catalog[category][name])
        if category == "Items":
            item["Amount"] = 1
        self.inventory[category][name] = item
        

    def open_inventory(self):
            for category, items in self.inventory.items():
                print(category+":")
                for item, stats in items.items():
                    print("\n\t" + item +":")
                    for stat_desc, stat_value in stats.items():
                        print("\t\t"+ stat_desc + ": " + str(stat_value))

    def equip(self):
        categories = list(self.slots)          # ["Weapons", "Armor", "Accessories"]
        for i, cat in enumerate(categories, 1):
            print(f"{i}. {cat}")
        choice = input("Category (number): ")
        if not choice.isdigit() or not 1 <= int(choice) <= len(categories):
            print("Invalid choice.")
            return
        category = categories[int(choice) - 1]

        names = list(self.inventory[category])
        if not names:
            print("Nothing to equip there.")
            return
        for i, name in enumerate(names, 1):
            print(f"{i}. {name}")
        choice = input("Item (number): ")
        if not choice.isdigit() or not 1 <= int(choice) <= len(names):
            print("Invalid choice.")
            return
        self.equiped[self.slots[category]] = names[int(choice) - 1]
        print(f"Equipped {names[int(choice) - 1]}.")

    def weapon_status(self):
        name = self.equiped["Weapon"]
        if not name:
            return None, 0, 0
        w = self.inventory["Weapons"][name]
        return w.get("Status"), w.get("Chance", 0), w.get("Duration", 0)

    def use_item(self, name, player, enemy=None):
        item = self.inventory["Items"].get(name)
        if item is None:
            return False
        if item["Target"] == "enemy":
            enemy.effects[item["Status"]] = item["Duration"]
            print(f"{enemy.name} is now {item['Status']}!")
        else:
            player.health += item.get("HP", 0)
            player.temp_defence += item.get("Defence", 0)   # lasts for the fight
        item["Amount"] -= 1
        if item["Amount"] == 0:
            del self.inventory["Items"][name]
        return True

    def get_bonus(self, stat):
        total = 0
        for category, slot in self.slots.items():
            name = self.equiped[slot]
            if name:
                total += self.inventory[category][name].get(stat, 0)
        return total
   



inv=Inventory()
inv.inventory["Weapons"]["Pitchfork"]=inv.weapons["Pitchfork"]
inv.inventory["Weapons"]["Sickle"]=inv.weapons["Sickle"]


