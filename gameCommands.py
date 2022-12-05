import os, random, sys

from engine import commands, events, items, entity
import data

def updateScreen():
    data.x, data.y = os.get_terminal_size()

exampleCommand = commands.Command("name|name2|name3", "exampleCommand")
@exampleCommand.command
def exmp():
    print("Hello, World")

commands = commands.Commands(exampleCommand)