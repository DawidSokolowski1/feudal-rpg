#story

import time
import enemies
from fight import Fight
from text_tempo import story_print







def chapter_1_intro():
    story_print("""
It's the 14th century. You've just harvested your crops. In a normal year,
this would be a disastrous result, but this wasn't a normal year—you've
done pretty well.

Unfortunately, your neighbors haven't fared as well, and as unfortunate as it gets,
your harvest is first and foremost meant to satisfy your feudal lord.

So it's no surprise that during a dinner with your family, his mercenaries
walk in as if they own the place and take away sacks of the harvest. But
as this happens, you notice that the mercenaries are taking more than
agreed upon.

You get up from the table to point out their mistake—in truth, you
wonder how they could fail to see it, leaving you with scraps that will
never be enough to survive the winter.

But all you hear is that you'd better get back to the table.

Anger wells up inside you to the point that your children begin to
believe in the tales of the berserker.Suddenly, you find yourself in 
a brawl with the mercenaries. 
""")


def chapter_1_after_intro_fight():
    story_print(
    "\nWell, not quite dead, but you can barely move,"
    " one of them looks at you, almost as if he’s worried, "
    "and then all three of them leave with your provisions...")


def chapter_1_year_later():
    story_print("""\n
A year later

Despite the adversities, you managed to survive the winter; exactly a
year has passed since that memorable, humiliating incident.

You're sitting at the table again; your daughter asks you for a piece
of bread, so you break off a piece and hand it to her.

But a moment later, you hear it clatter to the floor; you're alone in
the room. You shake off this blissful daydream. Any moment now, the
mercenaries will appear to collect the provisions, but you've decided
to change the terms of the agreement. You reach for your sharpened
pitchforks and sit down at the table with them. Moments later, the
door opens.
""")

def village_orphans_event(player):
    story_print("A group of orphaned teenagers huddles near the well while "
                "two mercenaries shove them around.")
    choice = input("1. Help them fight off the mercenaries\n2. Keep going\n> ")
 
    if choice != "1":
        story_print("You keep going, leaving the orphans to fend for themselves.")
        return
 
    mercenary_1, mercenary_2 = enemies.spawn("Mercenary", 2)
    filler = enemies.Enemies("", 0, 0, 0, 0, 1)
    fight = Fight(player, mercenary_1, mercenary_2, filler)
    fight.fight_start()
    fight.speed_check()
 
    if player.health <= 0:
        player.health = 1
    player.reset_temp_stats()
 
    story_print("The orphans thank you, then hesitate. \"Do you have anything to eat?\"")
    food_choice = input("1. Give them 2 Bread\n2. Say you have nothing to spare\n> ")
 
    if food_choice == "1" and player.inv.has_amount("Items", "Bread", 2):
        player.inv.remove_amount("Items", "Bread", 2)
        story_print("They let you into their home. Their mother used to gather herbs here.")
        player.inv.pick_up("Items", "Lavendel", 3)
        print("You received: Lavendel x3")
    elif food_choice == "1":
        story_print("You reach for bread you don't have. Your pockets are empty.")
    else:
        story_print("The only thing you helped with is reminding them of their hunger.")

