"""Turn-based fight between the player and three enemies.

A Fight is created with the player and exactly three enemies (story.py
uses empty "filler" enemies with 0 HP when a fight has fewer). The
story calls fight_start(), then speed_check() runs the rounds until
the player or all enemies are dead, and resolve_fight() hands out EXP.
"""
from .Player import Player
from .enemies import Enemies
from .Inventory import Inventory
import random
import time
from .text_tempo import fight_print
from .text_tempo import enemy_stats_print


class Fight():
    """One fight: the player against three enemies."""

    def __init__(self, player, enemy_1, enemy_2, enemy_3):
        """Store the player and the three enemies taking part in this fight."""
        self.enemy_1 = enemy_1
        self.enemy_2 = enemy_2
        self.enemy_3 = enemy_3
        self.player = player

    def enemy_1_attack(self, enemy):
        """Let enemy_1 hit the player for its full attack value.

        Older, simple attack function; the fight now uses enemy_attack().
        """
        self.player.health -= self.enemy_1.attack
        fight_print(f"{self.enemy_1.name} hit u with "
                    f"{self.enemy_1.attack} damage. "
                    f"\nYour HP: {self.player.health}")

    def fight_start(self):
        """Start the fight: announce it, prepare stats, show the enemies.

        reset_temp_stats() sets the player's temp stats to base stats + gear
        bonuses, so Focus boosts from an earlier fight don't carry over.
        """
        fight_print("You encoutered enemies!")
        self.player.reset_temp_stats()
        self.enemies_status()

    def enemies_status(self):
        """Print a table with the name and stats of all three enemies.

        Every value is padded to 15 characters with ljust(15), so the three
        enemies appear as three columns next to each other.
        """
        enemy_stats_print(
            "\nEnemy: ".ljust(15)
            + self.enemy_1.name.ljust(15)
            + self.enemy_2.name.ljust(15)
            + self.enemy_3.name.ljust(15)
            + "\nHP: ".ljust(15)
            + str(round(self.enemy_1.health, 1)).ljust(15)
            + str(round(self.enemy_2.health, 1)).ljust(15)
            + str(round(self.enemy_3.health, 1)).ljust(15)
            + "\n\nAttack: ".ljust(16)
            + str(self.enemy_1.attack).ljust(15)
            + str(self.enemy_2.attack).ljust(15)
            + str(self.enemy_3.attack).ljust(15)
            + "\nDefence: ".ljust(15)
            + str(self.enemy_1.defence).ljust(15)
            + str(self.enemy_2.defence).ljust(15)
            + str(self.enemy_3.defence).ljust(15)
            + "\nAvoidance: ".ljust(15)
            + str(self.enemy_1.avoidance).ljust(15)
            + str(self.enemy_2.avoidance).ljust(15)
            + str(self.enemy_3.avoidance).ljust(15)
            + "\nSpeed : ".ljust(15)
            + str(self.enemy_1.speed).ljust(15)
            + str(self.enemy_2.speed).ljust(15)
            + str(self.enemy_3.speed).ljust(15))

    def opponent_choice(self):
        """Let the player pick an enemy and attack it.

        The loop repeats until the player has used their turn (status = True).
        An attack can:
        - miss, if a random number (0-1) is not above the enemy's avoidance,
        - deal temp_attack - defence damage, if the attack beats the defence,
        - otherwise deal 1 damage, so every hit does at least something.
        Choosing a dead enemy does not use the turn; the player picks again.
        """
        status = False
        enemies = [self.enemy_1, self.enemy_2, self.enemy_3]
        while not status:
            try:
                opponent_choice = int(input(
                    "\nChoose the opponennt u want to attack: "
                    + "\n 1:" + self.enemy_1.name
                    + "\n 2:" + self.enemy_2.name
                    + "\n 3:" + self.enemy_3.name
                    + "\n"))

                # enumerate gives each enemy its position (0, 1, 2);
                # index + 1 matches the menu numbers (1, 2, 3)
                for index, enemy in enumerate(enemies):
                    if opponent_choice == index + 1:
                        if enemy.health > 0:
                            # random.random() is a number from 0 to 1;
                            # above avoidance = hit
                            if random.random() > enemy.avoidance:
                                if enemy.health > 0:
                                    # Hit: weapon status may apply
                                    self.apply_weapon_status(enemy)
                                    if (enemy.defence
                                            < self.player.temp_attack):
                                        enemy.health = (
                                            enemy.health
                                            - (self.player.temp_attack
                                               - enemy.defence))
                                        fight_print(
                                            "\nYou damaged: " + enemy.name
                                            + "\nDamage: "
                                            + str(round(
                                                self.player.temp_attack
                                                - enemy.defence, 1)))
                                        if enemy.health < 0:
                                            enemy.health = 0
                                        status = True
                                    else:
                                        enemy.health -= 1
                                        fight_print("\nYou damaged: "
                                                    + enemy.name
                                                    + "\nDamage: " + str(1))
                                        status = True
                                else:
                                    fight_print("This is a corpse already!")
                            else:
                                fight_print("You missed!")
                                status = True
                        else:
                            print("\nThis is a corpse already!"
                                  + "\nAttack living opponents!")
            except ValueError:
                # int() raised a ValueError because the input was not a number
                print("U need to enter a number")

    def focus(self):
        """Raise one of the player's temp stats for the rest of this fight.

        Only the temp stats change, so the boost ends when the fight ends
        (reset_temp_stats() sets them back). round() removes float errors
        such as 1.1000000001.
        """
        command = int(input(
            "Choose the attribute u want to increase for the fight: "
            + "\n1: Attack"
            + "\n2: Defence"
            + "\n3: Avoidance"
            + "\n4: Speed"
            + "\n"))
        if command == 1:
            self.player.temp_attack += 1
            self.player.temp_attack = round(self.player.temp_attack, 1)
            fight_print("Your Attack increased to: "
                        + str(self.player.temp_attack))
        elif command == 2:
            self.player.temp_defence += 1
            self.player.temp_defence = round(self.player.temp_defence, 1)
            fight_print("Your Defence increased to: "
                        + str(self.player.temp_defence))
        elif command == 3:
            self.player.temp_avoidance += 0.1
            self.player.temp_avoidance = round(self.player.temp_avoidance, 3)
            fight_print("Your Avoidance increased to: "
                        + str(self.player.temp_avoidance))
        elif command == 4:
            self.player.temp_speed += 1
            self.player.temp_speed = round(self.player.temp_speed, 1)
            fight_print("Your Speed increased to: "
                        + str(self.player.temp_speed))

        else:
            print("")

    # for items against enemies
    def choose_enemy(self):
        """Ask which enemy to target with an item; return that enemy.

        Keeps asking until the input is a number from 1-3 and that enemy is
        still alive.
        """
        enemies = [self.enemy_1, self.enemy_2, self.enemy_3]
        while True:
            choice = input("Target (1-3): ")
            if (choice.isdigit() and 1 <= int(choice) <= 3
                    and enemies[int(choice) - 1].health > 0):
                return enemies[int(choice) - 1]
            fight_print("Pick a living enemy.")

    def apply_weapon_status(self, enemy):
        """Maybe apply the equipped weapon's status effect to an enemy.

        The effect is applied with the weapon's "Chance" (e.g. 0.3 = 30%) and
        lasts "Duration" enemy turns. Weapons without a status do nothing.
        """
        status, chance, duration = self.player.inv.weapon_status()
        if status and random.random() < chance:
            enemy.effects[status] = duration
            fight_print(f"{enemy.name} is now under the influence of "
                        f"{status}!")

    def use_item_menu(self):
        """Let the player use an item during the fight.

        Lists the items that have a "Target". Enemy items ask for a target
        first. Returns True if an item was used (which uses up the turn) and
        False if the player cancelled, so they can choose another action.
        """
        inv = self.player.inv
        names = [n for n in inv.inventory["Items"]
                 if "Target" in inv.inventory["Items"][n]]
        if not names:
            print("\nYou have no usable items.")
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
        """Play one turn for an enemy.

        Order of a turn:
        1. Status effects tick (Poison/Bleeding damage, countdown). The enemy
           can die from this.
        2. A stunned enemy skips its turn.
        3. A Healer heals the ally with the lowest HP instead of attacking.
        4. Otherwise the enemy attacks. The player dodges if a random number
           is below temp_avoidance. A hit deals attack - temp_defence damage,
           or at least 1 if the player's defence is as high as the attack.
        """
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
                # key=lambda e: e.health makes min() compare
                # the enemies by their HP
                target = min(others, key=lambda e: e.health)
                before = target.health
                target.health = min(target.health + enemy.heal,
                                    target.max_health)
                healed = round(target.health - before, 1)
                fight_print(f"\n{enemy.name} heals {target.name} for "
                            f"{healed} HP!"
                            f"\n{target.name} HP: "
                            f"{round(target.health, 1)}")
                return

        if self.player.temp_avoidance < random.random():
            if self.player.temp_defence >= enemy.attack:
                self.player.health -= 1
                fight_print("\n" + enemy.name + " attacked you!"
                            + "\nDamage: " + str(1)
                            + "\nYour Health: "
                            + str(round(self.player.health, 1))
                            + "\n")
            else:
                self.player.health = (self.player.health
                                      - (enemy.attack
                                         - self.player.temp_defence))
                if self.player.health > 0:
                    fight_print("\n" + enemy.name + " attacked you!"
                                + "\nDamage: "
                                + str(round(enemy.attack
                                            - self.player.temp_defence, 1))
                                + "\nYour Health: "
                                + str(round(self.player.health, 1))
                                + "\n")
                else:
                    fight_print("\n" + enemy.name + " attacked you!"
                                + "\nDamage: "
                                + str(round(enemy.attack
                                            - self.player.temp_defence, 1)))
                    fight_print("You are Dead!")
        else:
            fight_print("\nYou avoided the enemy's attack")

    def speed_check(self):
        """Run the rounds until the player or all enemies are dead.

        At the start of every round, everyone is sorted by speed (highest
        first) to get the turn order. On the player's turn they choose to
        attack, Focus or use an item; enemies act through enemy_attack().
        Dead enemies are skipped, and the round stops early if the player
        dies.
        """
        while self.player.health > 0 and (self.enemy_1.health
                                          + self.enemy_2.health
                                          + self.enemy_3.health) > 0:
            # Turn order is rebuilt every round, so speed boosts from
            # Focus or equipment (temp_speed) count from the next round
            battlefield = {"Player": [self.player.health, self.player.attack,
                                      self.player.defence,
                                      self.player.avoidance,
                                      self.player.temp_speed],
                           "Enemy 1": [round(self.enemy_1.health, 1),
                                       self.enemy_1.attack,
                                       self.enemy_1.defence,
                                       self.enemy_1.avoidance,
                                       self.enemy_1.speed],
                           "Enemy 2": [round(self.enemy_2.health, 1),
                                       self.enemy_2.attack,
                                       self.enemy_2.defence,
                                       self.enemy_2.avoidance,
                                       self.enemy_2.speed],
                           "Enemy 3": [round(self.enemy_3.health, 1),
                                       self.enemy_3.attack,
                                       self.enemy_3.defence,
                                       self.enemy_3.avoidance,
                                       self.enemy_3.speed]}
            # Sort the entries by speed (index 4 of each list), fastest first
            move_order = sorted(battlefield.items(),
                                key=lambda item: item[1][4], reverse=True)
            for move, speed in move_order:
                # print(str(move))
                # The player only gets a turn while an enemy is alive
                # (enemies can die from Poison/Bleeding on their own turn)
                if move == "Player" and (self.enemy_1.health
                                         + self.enemy_2.health
                                         + self.enemy_3.health) > 0:
                    # Repeat until the player has made a valid choice
                    while True:
                        try:
                            command = int(input(
                                "Enter your command: "
                                + "\n1.Attack Enemy"
                                + "\n2.Focus: Increase one stat by 1"
                                "\n3. Use an Item"
                                "\n"))
                            if command == 1:
                                self.opponent_choice()
                                self.enemies_status()
                                break
                            elif command == 2:
                                self.focus()
                                break
                            elif command == 3:
                                if self.use_item_menu():
                                    self.enemies_status()
                                    break
                            else:
                                print("Enter number between 1-3!")
                            # elif move in battlefield
                            # --> Idea to make the code smaller
                            #   print("JAAAA")
                        except ValueError:
                            print("You neeed to enter a number!")
                elif move == "Enemy 1" and self.enemy_1.health > 0:
                    self.enemy_attack(self.enemy_1)
                    if self.player.health <= 0:
                        break

                elif move == "Enemy 2" and self.enemy_2.health > 0:
                    self.enemy_attack(self.enemy_2)
                    if self.player.health <= 0:
                        break

                elif move == "Enemy 3" and self.enemy_3.health > 0:
                    self.enemy_attack(self.enemy_3)
                    if self.player.health <= 0:
                        break

    def resolve_fight(self, exp_reward):
        """Finish the fight and return "dead" or "alive".

        If the player survived, their temp stats are reset and they get
        exp_reward EXP (which can level them up). The story uses the return
        value to decide whether to continue or offer a retry.
        """
        if self.player.health <= 0:
            return "dead"
        self.player.reset_temp_stats()
        self.player.gain_exp(exp_reward)
        return "alive"
