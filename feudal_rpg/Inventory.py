"""Inventory and Items.

Items is the catalog of every item that exists in the game and its stats.
Inventory builds on it and stores what the player actually owns and has
equipped, plus the functions to pick up, equip and use items.
"""
import pandas as pd


class Items():
    """The catalog of all items in the game, sorted by category.

    Every item is a dict of its stats. Weapons can also carry a status
    effect ("Status") that is applied with a "Chance" for "Duration" turns.
    Items with a "Target" can be used: "enemy" items are thrown at an
    enemy in a fight, "self" items are used on the player.
    """

    def __init__(self):

        self.weapons = {
            "Pitchfork": {"Attack": 1},
            "Sickle": {"Attack": 2, "Status": "Bleeding", "Chance": 0.3,
                       "Duration": 2},
            "Fang-Studded Pike": {
                "Attack": 2, "Status": "Wutanfall", "Chance": 0.3,
                "Duration": 2,
            },
        }

        self.armors = {
            "Tunic": {"Defence": 1},
            "Buff Coat": {"Defence": 2},
            "Jack of Plate": {"Defence": 3},
        }

        self.accessory = {
            "Rune-Etched Ring": {"Avoidance": 0.1},
            "Piece of Stem": {"Speed": 1},
            "Shield-Formed Broche": {"Defence": 1},
            "Pagan Pendant": {"Avoidance": 0.1},
        }

        self.items = {
            "Poison": {"Status": "Poison", "Duration": 3, "Target": "enemy"},
            "Bread": {"HP": 5, "Target": "self"},
            "Wine": {"Defence": 1, "Target": "self"},
            "Lavendel": {"Status": "Stun", "Duration": 4, "Target": "enemy"},
            "East Villa Key": {},
            "West Villa Key": {},
        }

        # catalog groups all categories, so pick_up() can look up any item by
        # its category name, e.g. self.catalog["Weapons"]["Sickle"]
        self.catalog = {"Weapons": self.weapons, "Armor": self.armors,
                        "Accessories": self.accessory, "Items": self.items}


class Inventory(Items):
    """The player's own items and the gear they have equipped.

    Inherits from Items, so it has access to the whole catalog, and adds the
    player's inventory, the equipped slots and all item functions.
    """

    def __init__(self):
        # super().__init__() runs Items.__init__, which creates the catalog
        super().__init__()
        # What the player owns, sorted like the catalog. Each entry is a copy
        # of the item's stats; usable items also get an "Amount" counter.
        self.inventory = {
            "Weapons": {},
            "Armor": {},
            "Accessories": {},
            "Items": {}
        }

        # One slot per gear type; None means nothing is equipped there.
        # It stores only the item's name, the stats are read from inventory.
        self.equiped = {"Armor": None,
                        "Weapon": None,
                        "Accessory": None}
        # Links each inventory category to its equipment slot
        self.slots = {"Weapons": "Weapon", "Armor": "Armor",
                      "Accessories": "Accessory"}

    def pick_up(self, category, name, amount=1):
        """Add an item from the catalog to the player's inventory.

        Usable items ("Items") are stacked: picking one up again only raises
        its "Amount". Gear (weapons, armor, accessories) is only stored once.
        dict(...) makes a copy, so changing the player's item never changes
        the catalog entry.
        """
        if name in self.inventory[category]:
            if category == "Items":
                self.inventory[category][name]["Amount"] += amount
            return
        item = dict(self.catalog[category][name])
        if category == "Items":
            item["Amount"] = amount
        self.inventory[category][name] = item

    def open_inventory(self):
        """Print everything the player owns as a table.

        Each item becomes one row (category, name, stats). pandas builds a
        DataFrame from the rows, which is only used to find how wide each
        column has to be; ljust() then pads every value to that width so the
        columns line up.
        """
        rows = []
        for category, items in self.inventory.items():
            for item, stats in items.items():
                stat_str = ", ".join(f"{k}: {v}" for k, v in stats.items())
                rows.append({"Category": category, "Item": item,
                             "Stats": stat_str})

        if not rows:
            print("\nYour inventory is empty.")
            return

        # Width of each column = its longest value or its header,
        # whichever is longer
        df = pd.DataFrame(rows)
        headers = list(df.columns)
        widths = [max(df[h].astype(str).map(len).max(), len(h))
                  for h in headers]

        print()
        print("  ".join(h.ljust(w) for h, w in zip(headers, widths)))
        print("-" * (sum(widths) + 2 * (len(headers) - 1)))
        for _, row in df.iterrows():
            print("  ".join(str(row[h]).ljust(w)
                            for h, w in zip(headers, widths)))
    # def open_inventory(self):
    #         for category, items in self.inventory.items():
    #             print("\n"+category+":")
    #             for item, stats in items.items():
    #                 print("\n" + item +":")
    #                 for stat_desc, stat_value in stats.items():
    #                     print(" " +stat_desc + ": " + str(stat_value))

    def show_equipped(self):
        """Print which item is in each equipment slot, or "(none)"."""
        print("\nEquipped:")
        for slot, name in self.equiped.items():
            print(f"  {slot}: {name if name else '(none)'}")

    def equip(self):
        """Let the player equip an item they own, through two menus.

        First the player picks a category, then an item from that category.
        isdigit() and the range check reject invalid input; the chosen item's
        name is then written into the matching equipment slot.
        """
        # ["Weapons", "Armor", "Accessories"]
        categories = list(self.slots)
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
        """Return the equipped weapon's status effect, its chance and duration.

        Returns (None, 0, 0) if no weapon is equipped or the weapon has no
        status. .get() gives a default value when a key is missing.
        """
        name = self.equiped["Weapon"]
        if not name:
            return None, 0, 0
        w = self.inventory["Weapons"][name]
        return w.get("Status"), w.get("Chance", 0), w.get("Duration", 0)

    def use_item(self, name, player, enemy=None):
        """Use one piece of a usable item and return True if it worked.

        "enemy" items put their status effect (e.g. Stun) on the given enemy.
        "self" items heal the player (never above max_health) and/or raise
        temp_defence for the current fight. One piece is used up, and the item
        is removed from the inventory when none are left.
        """
        item = self.inventory["Items"].get(name)
        if item is None:
            return False
        if item["Target"] == "enemy":
            enemy.effects[item["Status"]] = item["Duration"]
            print(f"{enemy.name} is now {item['Status']}!")
        else:
            player.health = min(player.health + item.get("HP", 0),
                                player.max_health)
            # lasts for the fight
            player.temp_defence += item.get("Defence", 0)
        item["Amount"] -= 1
        if item["Amount"] == 0:
            del self.inventory["Items"][name]
        return True

    def get_bonus(self, stat):
        """Return the total bonus all equipped gear gives to one stat.

        Goes through every equipment slot, and for each equipped item adds its
        value for that stat (0 if the item doesn't have that stat). Used by
        Player.reset_temp_stats() to add gear bonuses to the base stats.
        """
        total = 0
        for category, slot in self.slots.items():
            name = self.equiped[slot]
            if name:
                total += self.inventory[category][name].get(stat, 0)
        return total

    def has_amount(self, category, name, amount):
        """Return True if the player owns at least `amount` of an item."""
        item = self.inventory[category].get(name)
        return item is not None and item.get("Amount", 0) >= amount

    def remove_amount(self, category, name, amount):
        """Take `amount` of an item away, removing it when none are left."""
        self.inventory[category][name]["Amount"] -= amount
        if self.inventory[category][name]["Amount"] <= 0:
            del self.inventory[category][name]

    def use_item_menu(self, player):
        """Menu to use a "self" item (like Bread) outside of a fight.

        Lists only items the player can use on themselves, then calls
        use_item() with the one they pick.
        """
        usable = [name for name, stats in self.inventory["Items"].items()
                  if stats.get("Target") == "self"]
        if not usable:
            print("Nothing usable right now.")
            return
        for i, name in enumerate(usable, 1):
            print(f"{i}. {name}")
        choice = input("Item (number): ")
        if not choice.isdigit() or not 1 <= int(choice) <= len(usable):
            print("Invalid choice.")
            return
        name = usable[int(choice) - 1]
        self.use_item(name, player)
