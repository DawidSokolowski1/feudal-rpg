# location
"""All places in the game. To add a location, add one entry to LOCATIONS
and, if it needs a scene, one function in story.py.

Keys of a location (only "desc" and "exits" are required):
    desc   - text shown every time the player arrives
    exits  - list of (label, target_location) or
             (label, target_location, [(category, item_name), ...]) for a
             locked exit that needs at least 1 of each listed item
    items  - list of (category, name, amount) lying around, taken once
             via a menu option
    event  - function(player) that runs once, on the first visit
    end    - True if the game should stop after this location's event

Current layout (linear): house -> neighbors_house -> forest -> farmstead
"""
from . import story

LOCATIONS = {
    "house": {
        "desc": "Your house. It's modest, but it's yours.",
        "event": story.intro_event,
        "items": [("Items", "Bread", 5)],
        "exits": [
            ("Go to the neighbor's house", "neighbors_house"),
            ("Go to the forest", "forest"),
        ],
    },
    "neighbors_house": {
        "desc": "",
        "event": story.village_orphans_event,
        "exits": [
            ("Go back home", "house"),
            ("Go to the forest", "forest"),
        ],
    },
    "forest": {
        "desc": "The forest is dense and quiet",
        "event": story.forest_event,
        "exits": [
            ("Go back to the neighbor's house", "neighbors_house"),
            ("Head to the farmstead", "farmstead"),
        ],
    },
    "farmstead": {
        "desc": "Your neighbor's farmstead lies just past the field."
                " Smoke no longer rises from the chimney.",
        "event": story.farmstead_event,
        "exits": [
            ("Go back to the forest", "forest"),
            ("Head to the city", "city"),
        ],
    },

    "city": {
        "desc": "The city gates open onto a quiet, uneasy square. Paths lead"
                " east, west, toward a walled villa, and down a dusted side"
                " street.",
        "exits": [
            ("Go back to the farmstead", "farmstead"),
            ("Go east", "east_part"),
            ("Go west", "west_part"),
            ("Follow the dusted entrance", "dusted_entrance"),
            ("Enter the landlord's villa", "villa",
             [("Items", "East Villa Key"), ("Items", "West Villa Key")]),
        ],
    },
    "east_part": {
        "desc": "The eastern road toward the villa.",
        "event": story.east_part_event,
        "exits": [
            ("Go back to the city", "city"),
        ],
    },
    "west_part": {
        "desc": "The western road toward the villa.",
        "event": story.west_part_event,
        "exits": [
            ("Go back to the city", "city"),
        ],
    },
    "dusted_entrance": {
        "desc": "A dusted, half-forgotten side street.",
        "event": story.dusted_entrance_event,
        "exits": [
            ("Go back to the city", "city"),
        ],
    },
    "villa": {
        "desc": "The landlord's villa.",
        "event": story.villa_event,
        "exits": [],
        "end": True,
    }

    # Template for a new location — copy, rename, fill in:
    # "somewhere": {
    #     "desc": "...",
    #     "items": [("Items", "SomeItem", 1)],          # optional
    #     "event": story.some_new_event_function,       # optional
    #     "exits": [
    #         ("Go somewhere else", "other_key"),
    #         ("Enter the locked door", "vault",
    #          [("Items", "Landlord Key 1"),
    #           ("Items", "Landlord Key 2")]),  # optional lock
    #     ],
    # },
}

LOCATION_NAMES = {
    "house": "your house",
    "neighbors_house": "the neighbor's house",
    "forest": "the forest",
    "farmstead": "the farmstead",
    "city": "the city",
    "east_part": "the eastern road",
    "west_part": "the western road",
    "dusted_entrance": "the dusted side street",
    "villa": "the landlord's villa",
}
