"""Enemy definitions and spawning.

Enemies are simple stat containers with a small set of combat-relevant
attributes (health, attack, defence, avoidance, speed) plus a dict of
temporary status effects (Poison, Bleeding, Stun) applied during a fight.

ENEMY_TEMPLATES holds the base stats for each enemy type by name;
spawn() is the only way new enemies should be created during actual
gameplay (it reads from the templates), so that all "Guard"s, all
"Mercenary"s etc. start identical.
"""


class Enemies:
    """A single enemy instance with combat stats and active status effects."""

    def __init__(self, name, health, attack, defence, avoidance, speed):
        """Create an enemy with the given stats and no status effects.

        Normally called through spawn(), which fills in the values from
        ENEMY_TEMPLATES. max_health remembers the starting health so a
        Healer can't heal this enemy above it. effects maps a status
        name to the number of turns it has left, e.g. {"Poison": 3}.
        """
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defence = defence
        self.avoidance = avoidance
        self.speed = speed
        self.effects = {}

    def show_stats(self):
        """Print this enemy's stats in a simple readable block."""
        print(f"Name: {self.name} \nHealth: {self.health} "
              f"\nAttack: {self.attack} \nDefence: {self.defence} "
              f"\nAvoidance: {self.avoidance} \nSpeed: {self.speed}")

    def tick_effects(self):
        """Apply one turn of damage-over-time effects and count them down.

        Called by the fight once per enemy turn. Poison and Bleeding
        each take 1 HP. The dict comprehension then builds a new effects
        dict where every effect has 1 turn less, and drops the effects
        that were on their last turn (t > 1 keeps only those that still
        have turns left).
        """
        if "Poison" in self.effects:
            self.health -= 1
        if "Bleeding" in self.effects:
            self.health -= 1
        self.effects = {e: t - 1 for e, t in self.effects.items()
                        if t > 1}

    def is_stunned(self):
        """Return True if this enemy currently can't act.

        The fight checks this before tick_effects(), so a stun lasts
        for the enemy's turn even if it runs out during that turn.
        """
        return "Stun" in self.effects


# Base stats for every enemy type the game can spawn. "heal" is only
# present on the Healer and is read by spawn() to give that enemy its
# heal-ally behavior.
# It is a dict of dicts: the key is the enemy name, the value holds its stats.
ENEMY_TEMPLATES = {
    "Mercenary": {"health": 4, "attack": 3, "defence": 1,
                  "avoidance": 0, "speed": 1},
    "Elite Mercenary": {"health": 6, "attack": 5, "defence": 2,
                        "avoidance": 0.1, "speed": 1.9},
    "Guard": {"health": 6, "attack": 3, "defence": 1,
              "avoidance": 0.1, "speed": 2},
    "Fast Knight": {"health": 8, "attack": 3, "defence": 3,
                    "avoidance": 0.2, "speed": 10},
    "Healer": {"health": 5, "attack": 1, "defence": 1,
               "avoidance": 0, "speed": 2, "heal": 3},
    "Wolf": {"health": 4, "attack": 3, "defence": 0,
             "avoidance": 0.2, "speed": 2},
    "General": {"health": 10, "attack": 4, "defence": 2,
                "avoidance": 0.1, "speed": 3, "ignore_defence": True},
    "Elite Guard": {"health": 7, "attack": 4, "defence": 2,
                    "avoidance": 0.1, "speed": 2},
    "Landlord": {"health": 14, "attack": 5, "defence": 3,
                 "avoidance": 0.15, "speed": 3},
}


def spawn(name, count=1):
    """Create one or more Enemies from a template in ENEMY_TEMPLATES.

    With count=1, returns a single Enemies instance named exactly `name`.
    With count>1, returns a list of `count` instances named "{name} 1",
    "{name} 2", etc., each with a fresh copy of the same base stats.
    """
    # Look up the base stats for this enemy type
    stats = ENEMY_TEMPLATES[name]
    # One enemy: return the object itself, not a list
    if count == 1:
        enemy = Enemies(name, stats["health"], stats["attack"],
                        stats["defence"], stats["avoidance"], stats["speed"])
        # .get() returns 0 if the template has no "heal" key,
        # so only the Healer ends up with a heal value above 0
        enemy.heal = stats.get("heal", 0)
        return enemy
    # Several enemies: build a list, numbering them from 1
    # (i starts at 0, so i+1 gives "Mercenary 1", "Mercenary 2", ...)
    result = []
    for i in range(count):
        enemy = Enemies(f"{name} {i + 1}", stats["health"], stats["attack"],
                        stats["defence"], stats["avoidance"], stats["speed"])
        enemy.heal = stats.get("heal", 0)
        result.append(enemy)
    return result
