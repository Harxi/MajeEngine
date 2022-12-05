import os, sys

from engine import commands, entity, events, items

# GAME DATA

platform = {
    "win32": "cls",
    "linux": "clear"
}

dispatcher = events.Events()
x, y = os.get_terminal_size()

# ITEMS
items = {
    "BaseSword": items.Sword("Деревянный меч", "Меч оточеный в тренеровках", "base", 1, 0.08),
    "BaseArmor": items.Armor("Тряпки", "Тряпки, которые даже от мороза не спасут", "base", 0)
}

# FUNCTIONS

def clearScreen():
    os.system(platform[sys.platform])