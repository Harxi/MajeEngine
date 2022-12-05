import os, random, sys

from engine import entity, items, events
import gameCommands, data

def updateScreen():
    data.x, data.y = os.get_terminal_size()

while True:
    updateScreen() # set size
    print(f"{f'{chr(10)}'.join(map(lambda x: str(gameCommands.commands.showCommands[x]), gameCommands.commands.showCommands))}") # help command
    option = input('') # Command
    try:
        gameCommands.commands.commands[option].function() # call command
    except:
        pass # if uncorrect comman