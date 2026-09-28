#Inventory and Items
import pandas as pd
class Items():
    def __init__(self):

        self.weapons = {
            "Pitchfork": {"Attack": 1},
            "Sickle": {"Attack": 2, "Status": "Bleeding", "Chance": 0.3, "Duration": 2},
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
            "Shield-Formed Broche":{"Defence":1},
            "Pagan Pendant":{"Avoidance":0.1},
            }
        

        self.items = {
            "Poison":   {"Status": "Poison", "Duration": 3, "Target": "enemy"},
            "Bread":    {"HP": 5, "Target": "self"},
            "Wine":     {"Defence": 1, "Target": "self"},
            "Lavendel": {"Status": "Stun", "Duration": 3, "Target": "enemy"},
            "East Villa Key": {},
            "West Villa Key": {},
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

    def pick_up(self, category, name, amount=1):
        if name in self.inventory[category]:
            if category == "Items":
                self.inventory[category][name]["Amount"] += amount
            return
        item = dict(self.catalog[category][name])
        if category == "Items":
            item["Amount"] = amount
        self.inventory[category][name] = item
        

    def open_inventory(self):
        rows = []
        for category, items in self.inventory.items():
            for item, stats in items.items():
                stat_str = ", ".join(f"{k}: {v}" for k, v in stats.items())
                rows.append({"Category": category, "Item": item, "Stats": stat_str})
    
        if not rows:
            print("\nYour inventory is empty.")
            return
    
        df = pd.DataFrame(rows)
        headers = list(df.columns)
        widths = [max(df[h].astype(str).map(len).max(), len(h)) for h in headers]
    
        print()
        print("  ".join(h.ljust(w) for h, w in zip(headers, widths)))
        print("-" * (sum(widths) + 2 * (len(headers) - 1)))
        for _, row in df.iterrows():
            print("  ".join(str(row[h]).ljust(w) for h, w in zip(headers, widths)))
    # def open_inventory(self):
    #         for category, items in self.inventory.items():
    #             print("\n"+category+":")
    #             for item, stats in items.items():
    #                 print("\n" + item +":")
    #                 for stat_desc, stat_value in stats.items():
    #                     print(" " +stat_desc + ": " + str(stat_value))

    def show_equipped(self):
        print("\nEquipped:")
        for slot, name in self.equiped.items():
            print(f"  {slot}: {name if name else '(none)'}")
            
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

    def has_amount(self, category, name, amount):
        item = self.inventory[category].get(name)
        return item is not None and item.get("Amount", 0) >= amount

    def remove_amount(self, category, name, amount):
        self.inventory[category][name]["Amount"] -= amount
        if self.inventory[category][name]["Amount"] <= 0:
            del self.inventory[category][name]

   



inv=Inventory()
inv.inventory["Weapons"]["Pitchfork"]=inv.weapons["Pitchfork"]
inv.inventory["Weapons"]["Sickle"]=inv.weapons["Sickle"]


