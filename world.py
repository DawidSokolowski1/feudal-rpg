
 #moving engine
 
def explore(player, locations, start):
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
            required = exit_[2] if len(exit_) > 2 else []
            missing = [n for c, n in required if not player.inv.has_amount(c, n, 1)]
            if missing:
                options.append((f"{label} (locked)", ("locked", missing)))
            else:
                options.append((label, ("go", target)))
 
        for i, (label, _) in enumerate(options, 1):
            print(f"{i}. {label}")
        print("O. Open inventory")
        choice = input("> ")
 
        if choice.strip().lower() == "o":
            player.inv.open_inventory()
            print("1. Equip something")
            print("2. View equipped items")
            print("Enter. Back")
            sub_choice = input("> ")
            if sub_choice == "1":
                player.inv.equip()
            elif sub_choice == "2":
                player.inv.show_equipped()
            continue
 
        if not choice.isdigit() or not 1 <= int(choice) <= len(options):
            print("Invalid choice.")
            continue
 
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