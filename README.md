# Feudal RPG

A text-based RPG written in Python, set in the 14th century. You play a
peasant pushed too far by his feudal lord's mercenaries — fight your way
through the surrounding villages and city to take back what's yours.

Built as the final project for an intro Python course at TU Dortmund.

## Setup

Requires Python 3.10+ and `pandas`. Works on macOS, Linux and Windows.

```bash
git clone <your repo URL>
cd feudal-rpg
pip install pandas
python3 -m feudal_rpg
```

On Windows, use `python` or `py` instead of `python3`.

- Run the command from the project folder (the one containing
  `feudal_rpg/`). The game is a package, so starting `feudal_rpg/__main__.py`
  directly (e.g. with an IDE's Run button) does not work.
- Run it in a real terminal (e.g. the VS Code terminal), because the
  letter-by-letter text needs keyboard access. Press any key while text is
  printing to skip to the end of it.
- If you use [uv](https://docs.astral.sh/uv/), `uv run python -m feudal_rpg`
  installs `pandas` automatically.

## How to play

- Type the number of a menu option and press Enter.
- Press `O` at any time to open your inventory (equip items, view what's
  equipped).
- Combat is turn-based: choose to attack, use an item, or (in most fights)
  focus on boosting a stat for that fight.
- If you die, you'll be offered a choice: restart the whole game, or retry
  the fight you just lost.
- Leveling up lets you choose which stat to improve.

## Project structure

| File | What it does |
|---|---|
| `main.py` | Entry point. Creates the player and starts exploration. |
| `world.py` | Generic engine for moving between locations — no story content. |
| `location.py` | Map data: locations, exits, and which event/fight is tied to each. |
| `story.py` | All narrative text and the event/fight functions for each location. |
| `fight.py` | Combat system: turn order, attacks, status effects, focus. |
| `Player.py` | Player stats, leveling, and stat upgrades. |
| `Inventory.py` | Items, equipment, and the inventory system. |
| `enemies.py` | Enemy stats and spawning. |
| `intro.py` | Character creation (name, age, zodiac sign). |

## Course topics covered

- Primitives, control flow, functions, containers — used throughout
- Classes and inheritance — `Player`, `Enemies`, `Fight`, `Intro`
  (`Player` inherits from `Intro`)
- `pandas` — used to render the inventory table
- Git/GitHub — version control
