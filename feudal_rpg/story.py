"""Story events: one function per scene of the game.

Each event gets the player, prints the story with story_print(), usually
starts a fight and hands out rewards. Every event returns "alive" or
"dead"; world.explore() uses that to continue or offer a retry.
Events are linked to places in location.py.
"""

import time
from . import enemies
from .fight import Fight
from .text_tempo import story_print


def intro_event(player):
    """The opening scene at the player's house.

    The player first fights with weaker intro stats and is meant to lose:
    if their HP drops to 0 it is set back to 1, so they survive. After
    "a year later" the stats go back to normal, the player gets the
    Pitchfork and fights the mercenaries again, this time for real.
    """
    player.player_stats_intro()
    story_print("""
It's the 14th century. You've just harvested your crops. In a normal year,
this would be a disastrous result, but this wasn't a normal year—you've
done pretty well.

Unfortunately, your neighbors haven't fared as well, and as \
unfortunate as it gets,
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
believe in the tales of the berserker. Suddenly, you find yourself in
a brawl with the mercenaries.
""")

    guard_1, guard_2, guard_3 = enemies.spawn("Mercenary", 3)
    fight = Fight(player, guard_1, guard_2, guard_3)
    fight.fight_start()
    fight.speed_check()

    if player.health <= 0:
        player.health = 1

    story_print(
        "\nWell, not quite dead, but you can barely move,"
        " one of them looks at you, almost as if he's worried, "
        "and then all three of them leave with your provisions...")

    story_print("""
A year later.

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

    player.player_stats_normal()
    player.inv.pick_up("Weapons", "Pitchfork", 1)
    player.inv.equiped["Weapon"] = "Pitchfork"
    m1, m2, m3 = enemies.spawn("Mercenary", 3)
    fight = Fight(player, m1, m2, m3)
    fight.fight_start()
    fight.speed_check()
    if fight.resolve_fight(6) == "dead":
        return "dead"
    else:
        return "alive"


def village_orphans_event(player):
    """Optional fight to help orphans at the neighbor's house.

    If the player helps and wins, they can give 2 Bread. Giving it (only
    possible if they have 2) rewards them with 3 Lavendel.
    """
    story_print("A group of orphaned teenagers huddles near the well while "
                "two mercenaries shove them around.")
    choice = input("1. Help them fight off the mercenaries\n"
                   "2. Keep going\n> ")
    if choice != "1":
        story_print("You keep going, leaving the orphans to fend for "
                    "themselves.")
        return "alive"

    mercenary_1, mercenary_2 = enemies.spawn("Mercenary", 2)
    # Fight always needs three enemies; an empty one with 0 HP counts as
    # already dead, so this becomes a 2-enemy fight
    filler = enemies.Enemies("", 0, 0, 0, 0, 1)
    fight = Fight(player, mercenary_1, mercenary_2, filler)
    fight.fight_start()
    fight.speed_check()

    if fight.resolve_fight(4) == "dead":
        return "dead"

    story_print("The orphans thank you, then hesitate. "
                "\"Do you have anything to eat?\"")
    food_choice = input("1. Give them 2 Bread\n"
                        "2. Say you have nothing to spare\n> ")
    if food_choice == "1" and player.inv.has_amount("Items", "Bread", 2):
        player.inv.remove_amount("Items", "Bread", 2)
        story_print("They let you into their home. Their mother used to "
                    "gather herbs here.")
        player.inv.pick_up("Items", "Lavendel", 3)
        print("You received: Lavendel x3")
    elif food_choice == "1":
        story_print("You reach for bread you don't have. Your pockets are "
                    "empty.")
    else:
        story_print("The only thing you helped with is reminding them of "
                    "their hunger.")

    return "alive"


def forest_event(player):
    """Fight against three wolves; the reward is the Pagan Pendant."""
    story_print("You know this route by heart; you've used it every week "
                "to get into town. This time, however, you come across "
                "creatures on your way that you've heard of more often than "
                "you've actually seen... wolves. The drought hasn't just "
                "affected people, and now you're going to feel the effects.")
    wolf_1, wolf_2, wolf_3 = enemies.spawn("Wolf", 3)
    fight = Fight(player, wolf_1, wolf_2, wolf_3)
    fight.fight_start()
    fight.speed_check()

    if fight.resolve_fight(10) == "dead":
        return "dead"

    story_print("Among the roots, a pagan pendant hangs from a branch.")
    player.inv.pick_up("Accessories", "Pagan Pendant", 1)
    print("You received: Pagan Pendant")
    return "alive"


def farmstead_event(player):
    """Fight a Healer and two Elite Mercenaries; reward: Tunic and Bread."""
    story_print("A healer and two elite mercenaries stand guard over the "
                "farmstead.")
    healer = enemies.spawn("Healer")
    elite_1, elite_2 = enemies.spawn("Elite Mercenary", 2)
    fight = Fight(player, healer, elite_1, elite_2)
    fight.fight_start()
    fight.speed_check()

    if fight.resolve_fight(15) == "dead":
        return "dead"

    story_print("You step into the abandoned house and find a tunic "
                "hanging by the door.")
    player.inv.pick_up("Armor", "Tunic", 1)
    player.inv.pick_up("Items", "Bread", 2)
    print("You received: Tunic and 2x Bread")
    return "alive"


def east_part_event(player):
    """Fight a General and two Elite Guards for the East Villa Key."""
    story_print("The eastern approach to the villa is guarded — a hardened"
                " general and two of his elite men block the way.")
    general = enemies.spawn("General")
    elite_1, elite_2 = enemies.spawn("Elite Guard", 2)
    fight = Fight(player, general, elite_1, elite_2)
    fight.fight_start()
    fight.speed_check()

    if fight.resolve_fight(30) == "dead":
        return "dead"

    story_print("You search the general's body and find a heavy iron key.")
    player.inv.pick_up("Items", "East Villa Key", 1)
    print("You received: East Villa Key")
    return "alive"


def west_part_event(player):
    """Fight a General and two Elite Guards for the West Villa Key."""
    story_print("The western approach is guarded the same way — a general"
                " and two elite men, watching the road to the villa.")
    general = enemies.spawn("General")
    elite_1, elite_2 = enemies.spawn("Elite Guard", 2)
    fight = Fight(player, general, elite_1, elite_2)
    fight.fight_start()
    fight.speed_check()

    if fight.resolve_fight(30) == "dead":
        return "dead"

    story_print("You search the general's body and find a second iron key.")
    player.inv.pick_up("Items", "West Villa Key", 1)
    print("You received: West Villa Key")
    return "alive"


def dusted_entrance_event(player):
    """A quiz about the story; all answers right gives the Sickle.

    Each question is a tuple of (question, answer options, correct
    answer). correct counts the right answers and is compared to the
    number of questions at the end.
    """
    story_print("A hooded man leans against the wall of a dusted, "
                "half-forgotten side street. \"Answer me a few things,\" "
                "he says, \"and I'll make it worth your while.\"")

    questions = [
        ("What do peasants owe their feudal lord from the harvest?",
         ["1. Taxes", "2. Nothing", "3. A song"], "1"),
        ("What weapon did you take up against the mercenaries?",
         ["1. A sword", "2. A pitchfork", "3. A bow"], "2"),
        ("What did the orphaned teenagers ask you for?",
         ["1. Gold", "2. Food", "3. Shelter"], "2"),
    ]

    correct = 0
    for question, options, answer in questions:
        story_print(question)
        for option in options:
            print(option)
        choice = input("> ")
        if choice == answer:
            print("Correct.")
            correct += 1
        else:
            print("Wrong.")

    if correct == len(questions):
        story_print("The man smiles. \"Sharp mind. Take this for your "
                    "trouble.\"")
        player.inv.pick_up("Weapons", "Sickle", 1)
        story_print("You received: Sickle")
    else:
        story_print("The man shrugs. \"Not quite. Maybe next time.\"")

    return "alive"


def villa_event(player):
    """Final fight against the Landlord; ends the game.

    If the player died at some point (and retried), a different ending
    reveals that everything after the death was only imagined.
    player.died_at holds the place of that first death.
    """
    story_print("The villa gates creak open. Your feudal lord stands waiting,"
                " unarmed men at his sides — he never expected you to make it"
                " this far.")
    landlord = enemies.spawn("Landlord")
    filler_1 = enemies.Enemies("", 0, 0, 0, 0, 1)
    filler_2 = enemies.Enemies("", 0, 0, 0, 0, 1)
    fight = Fight(player, landlord, filler_1, filler_2)
    fight.fight_start()
    fight.speed_check()

    if fight.resolve_fight(0) == "dead":
        return "dead"

    if player.has_died:
        story_print("The lord falls. For the first time in years, the "
                    "harvest is yours to keep.")
        story_print(f"""
...except that's not what happened.

You died back in {player.died_at}. Everything since then — the keys, the
guards, the questions on that dusted street, this final blow against the
man who ruined your family — none of it happened. It was just the story
you wished for, playing out in your head as the light went out.

I'm sorry. I got carried away telling it. I should have stopped when it
ended.
""")
    else:
        story_print("The lord falls. For the first time in years, the "
                    "harvest is yours to keep.")

    return "alive"
