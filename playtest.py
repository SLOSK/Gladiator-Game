#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jude.sidloski
#
# Created:     13/03/2014
# Copyright:   (c) jude.sidloski 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import objects
import rooms
import commands

alive = True
print("Welcome to Crab Killer 0.01!")
objects.player.name = input("What is your name?\n>")
print("Well,", objects.player.name, "It is your lucky day! Today you begin an",
      "exciting adventure! First you must decide your initial skills.")
objects.player.levelup()
print("Type 'help' for a list of commands.")
rooms.currentlocation = rooms.locations[rooms.location.location]
rooms.currentlocation.description()
while alive == True:
    commands.prompt()
    if objects.player.hp < 0:
        alive = False
print("It's over! Good game!")
input("----------------------------------------------------------------------")
