"""Moving engine: lets the player walk between locations.

explore() is the main game loop. It shows where the player is, runs
the location's event, and offers a menu to move, pick up items, open
the inventory or read the instructions.
"""
from .location import LOCATION_NAMES


def explore(player, locations, start):
    """Run the game loop from `start` until the game ends.

    events_done and items_taken are sets that remember which locations
    have already had their event and items, so they only happen once.
    Returns "restart" if the player chooses to restart after dying, or
    "finished" when a location marked with "end" has been completed.
    """
    current = start
    events_done = set()
    items_taken = set()

    while True:
        loc = locations[current]
        print("\n" + loc["desc"])

        # Event runs once, on the first visit
        if "event" in loc and current not in events_done:
            result = loc["event"](player)
            if result == "dead":
                print("\nYou died.")
                print("1. Restart the whole game")
                print("2. Retry this fight")
                death_choice = input("> ")
                if death_choice == "1":
                    return "restart"
                # Only the first death is remembered, for the ending in
                # villa_event
                if not player.has_died:
                    player.has_died = True
                    player.died_at = LOCATION_NAMES.get(current, current)
                # Retry: full health, and 'continue' restarts the loop at the
                # same place. The event isn't in events_done yet, so the
                # fight happens again.
                player.health = player.max_health
                continue

            events_done.add(current)

        if loc.get("end"):
            return "finished"

        # Build the menu: items lying around first, then exits
        options = []
        if loc.get("items") and current not in items_taken:
            names = ", ".join(f"{n} x{a}" for _, n, a in loc["items"])
            options.append((f"Pick up: {names}", ("take", None)))

        for exit_ in loc["exits"]:
            label, target = exit_[0], exit_[1]
            # A third value in an exit is the list of items needed to unlock it
            required = exit_[2] if len(exit_) > 2 else []
            missing = [n for c, n in required
                       if not player.inv.has_amount(c, n, 1)]
            if missing:
                options.append((f"{label} (locked)", ("locked", missing)))
            else:
                options.append((label, ("go", target)))

        # Each option is (text shown, (action, value)); enumerate(..., 1)
        # numbers the menu from 1
        for i, (label, _) in enumerate(options, 1):
            print(f"{i}. {label}")
        print("O. Open inventory")
        print("S. Show stats")
        print("I. Instructions")
        choice = input("> ")

        if choice.strip().lower() == "i":
            print(INSTRUCTIONS)
            continue

        if choice.strip().lower() == "s":
            player.player_status()
            continue

        if choice.strip().lower() == "o":
            player.inv.open_inventory()
            print("1. Equip something")
            print("2. View equipped items")
            print("3. Use an item")
            print("Enter. Back")
            sub_choice = input("> ")
            if sub_choice == "1":
                player.inv.equip()
            elif sub_choice == "2":
                player.inv.show_equipped()
            elif sub_choice == "3":
                player.inv.use_item_menu(player)
            continue

        if not choice.isdigit() or not 1 <= int(choice) <= len(options):
            print("Please enter a number between 1 and "
                  + str(len(options)) + ".")
            continue

        # Unpack the chosen option's action and act on it
        kind, value = options[int(choice) - 1][1]
        if kind == "go":
            current = value
        elif kind == "take":
            for category, name, amount in loc["items"]:
                player.inv.pick_up(category, name, amount)
                print(f"You picked up: {name} x{amount}")
            items_taken.add(current)
        else:
            print(f"It's locked. You need: {', '.join(value)}")


# Help text shown when the player types I in the menu
INSTRUCTIONS = """
HOW TO PLAY

Combat (each round you choose one):
  1. Attack Enemy   - pick a target, deal (your Attack - their Defence) \
damage.
  2. Focus          - boost one of your stats (Attack, Defence, Avoidance,
                       Speed) by a fixed amount for the rest of THIS fight
                       only. It resets back to normal once the fight ends.
  3. Use an Item    - Bread heals you; Lavendel is thrown at an enemy \
and puts it to sleep.

Speed decides turn order each round - whoever has the higher Speed acts
first, enemies included.

Avoidance is a chance to dodge an attack completely - yours is your chance
to dodge an enemy hit, an enemy's is their chance to dodge your attack.

Outside combat:
  O - open your inventory: equip gear, view what's equipped, or use a
      self-targeted item (like Bread) to heal up.
  S - show your stats (level, EXP, HP, and stats with gear bonuses).
  I - show these instructions again, any time.

If you die, you can restart the whole game from scratch, or retry the
fight you just lost with full health.
"""
