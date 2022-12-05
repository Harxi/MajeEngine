import os, random, sys

from engine import entity, items, events
import gameCommands, data

def updateScreen():
    data.x, data.y = os.get_terminal_size()

player = entity.Entity(name = "Name", health = 100, maxHealth = 100, damage = 1, xp = 0, lvl = 1, coins = 0, reqxp = 250, type = "Player", items = [], weapon = data.items["BaseSword"], armor = data.items["BaseArmor"], events = data.dispatcher) # is entity

while True:
    updateScreen() # set size
    print(f"{f'{chr(10)}'.join(map(lambda x: str(gameCommands.commands.showCommands[x]), gameCommands.commands.showCommands))}") # help command
    option = input('') # Command
    try:
        gameCommands.commands.commands[option].function() # call command
    except:
        pass # if uncorrect comman
