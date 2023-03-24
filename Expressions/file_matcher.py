import fnmatch
from fnmatch import fnmatchcase
import os

def list_files():
    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, "*.txt"):
            print("Text files: ", file)

        if fnmatch.fnmatch(file, "*.rb"):
            print("Text files: ", file)

        if fnmatch.fnmatch(file, "*.yml"):
            print("Text files: ", file)

        if fnmatch.fnmatch(file, "*.py"):
            print("Text files: ", file)


#list_files()

players = [
        "Jose Altuve 2B",
        "Carlos Correa SS",
        "Alex Bregman 3B",
        "Scooter Gennett 2B"
        ]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print("players that play 2B: ", second_base_players)