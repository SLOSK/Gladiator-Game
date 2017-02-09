#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jude.sidloski
#
# Created:     05/03/2014
# Copyright:   (c) jude.sidloski 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import rooms
import objects
def prompt(p = '>'):
    """ Takes the users input and translates it
        into commands the computer understands. """
    res = input(p)
    for cmd, cmdr in commands:
        if res.startswith(cmd):
            obj = res[(len(cmd)) + 1:]
            return cmdr(obj)
    print("Invalid!")

def take(obj):
    """ Adds an object to the users inventory """
    try:
        if type(objects.objindex[obj]) == objects.Character:
            print("You can't take that!")
            return
    except:
        pass
    if obj in rooms.currentlocation.roomitems:
        inventory.append(obj)
        rooms.currentlocation.roomitems.remove(obj)
        print("You took the", obj)
    else:
        print("There is no", obj, "here!")

def drop(obj):
    """ Drops an object from the inventory into the current room """
    if obj in inventory:
        inventory.remove(obj)
        rooms.currentlocation.roomitems.append(obj)
        print("You dropped the", obj)
def inventory(obj):
    """ Shows the current inventory """
    if obj != '':
        print("Invalid command!")
        return
    print(inventory)

def stats(obj):
    """ Gives the player info about themselves """
    if obj != '':
        print("Invalid command!")
        return
    print("Name:", objects.player.name)
    print("EXP:", objects.player.exp)
    print("Health:", objects.player.hp)
    print("Attack:", objects.player.atk)
    print("Defense:", objects.player.ac)
    print("Weapon:", objects.player.weapon)
    print("Armor:", objects.player.armor)

def attack(obj):

    if obj in rooms.currentlocation.roomitems:
        opp = objects.objindex[obj]

        combat = True
        cround = 0
        print("You have entered combat! Type 'help' for combat commands.\n")
        while combat == True:

            if combatprompt(cround, opp) == False:
                return
            if opp.hp < 0:
                while len(objects.bufftimers) != 0:
                    for buff in objects.bufftimers:
                        buff.buffcount += 1
                        buff.checker()

                print("You killed the", opp.name)
                combat = False
                objects.player.exp += opp.exp
                print("You've gained", opp.exp, "EXP! You now have",
                      objects.player.exp, "EXP!")
                objects.player.levelcheck()
                print("The", opp.name, "dropped:", opp.loot)
                print("You are out of combat.\n")
                rooms.currentlocation.removeitem(obj)
                rooms.currentlocation.additem(opp.loot)
                rooms.currentlocation.description()
            cround +=1

    else:
        print("There is no", obj, "here!")

def combatprompt(cround, opp, p = '>'):
    """ Takes the users input and translates it
    into commands the computer understands """

    if objects.player.hp < 0:
        print("You are dead!")
        return False
    for buff in objects.bufftimers:
        buff.buffcount += 1
        buff.checker()
    res = input(p)
    for cmd, cmdr in objects.player.combatcommands:
        if res.startswith('help'):
            return objects.player.help()
        elif len(res) != 1:
            print("Invalid command!")
            return
        elif res.startswith(cmd):
            if cround != 0:
                opp.medium(objects.player)
            return cmdr(opp)

    print("Invalid!")



def equip(obj):
    if obj == "":
        print("You are holding", objects.player.weapon)
        print("You are wearing", objects.player.armor)
        return
    if obj in objects.objindex.keys():
        if type(objects.objindex[obj]) == objects.Weapon and obj in inventory:
            if objects.player.weapon != "no weapon":
                inventory.append(objects.player.weapon)
            objects.player.weapon = obj
            inventory.remove(obj)
            print("You equipped the", obj)
        elif type(objects.objindex[obj]) == objects.Armor and obj in inventory:
            if objects.player.armor != 'no armor':
                inventory.append(objects.player.weapon)
            objects.player.armor = obj
            inventory.remove(obj)
            a = objects.player
            armor = objects.objindex[a.armor]
            a.arm = armor.acb
            a.ac, a.touchac, a.ffac =\
                    10 + a.dex + a.arm, 10 + a.dex, 10 + a.arm
            print("You have equipped the", obj)
            print(a.name, "'s armor class is now ", a.ac, '!', sep = '')
        else:
            print("Cannot equip", obj)
    else:
        print("Cannot equip", obj)
def unequip(obj):
    try:
        if type(objects.objindex[obj]) == objects.Weapon and \
                                      objects.player.weapon == obj:
            inventory.append(objects.player.weapon)
            objects.player.weapon = 'no weapon'
        elif type (objects.objindex[obj]) == objects.Armor and \
                                      objects.player.armor == obj:
            inventory.append(objects.player.armor)
            objects.player.armor = 'no armor'
            a = objects.player
            armor = objects.objindex[a.armor]
            a.arm = armor.acb
            a.ac, a.touchac, a.ffac =\
                    10 + a.dex + a.arm, 10 + a.dex, 10 + a.arm
            print(a.name, "'s armor class is now ", a.ac, '!', sep = '')
        else:
            print("You have no", obj, "equipped.")
            return
    except:
        print("There is no", obj)
        return
    print("You unequipped the", obj)

def look(obj):
    if obj != '':
        print("Invalid command!")
        return
    rooms.currentlocation.description()

def south(obj):
    if obj != '':
        print("Invalid command!")
        return
    if rooms.testsouth():
        rooms.location.south()
        rooms.currentlocation = rooms.locations[rooms.location.location]
        rooms.currentlocation.description()
    else:
        print("Cannot go that way!")
def north(obj):
    if rooms.testnorth():
        rooms.location.north()
        rooms.currentlocation = rooms.locations[rooms.location.location]
        rooms.currentlocation.description()
    else:
        print("Cannot go that way!")
def east(obj):
    if obj != '':
        print("Invalid command!")
        return
    if rooms.testeast():
        rooms.location.east()
        rooms.currentlocation = rooms.locations[rooms.location.location]
        rooms.currentlocation.description()
    else:
        print("Cannot go that way!")
def west(obj):
    if obj != '':
        print("Invalid command!")
        return
    if rooms.testwest():
        rooms.location.west()
        rooms.currentlocation = rooms.locations[rooms.location.location]
        rooms.currentlocation.description()
    else:
        print("Cannot go that way!")

def helpme(obj):
    if obj != '':
        print("Invalid command!")
        return
    print("Valid commands are:", "north", "south", "east", "west", "take",
     "drop", "i (inventory)", "s (stats)", "attack", "equip", "unequip", "look", sep = '\n')

commands = [('take', take), ('pick up', take), ('grab', take),
('drop', drop), ('i', inventory), ('attack', attack), ('hit', attack),
('equip', equip), ('use', equip), ('unequip', unequip), ('north', north),
('south', south), ('east', east), ('west', west), ('help', helpme),
('look', look), ('s', stats)]
inventory = []




