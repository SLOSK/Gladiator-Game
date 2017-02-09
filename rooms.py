#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      jude.sidloski
#
# Created:     07/03/2014
# Copyright:   (c) jude.sidloski 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import objects

class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0, surroundings='blank', objects = []):
        """ Create a new location """
        self.x = x
        self.y = y
        self.location = (self.x, self.y)
        self.roomitems = objects
        self.surroundings = surroundings
    def north(self):
        self.y += 1
        self.location = (self.x, self.y)
    def south(self):
        self.y -= 1
        self.location = (self.x, self.y)
    def west(self):
        self.x -= 1
        self.location = (self.x, self.y)
    def east(self):
        self.x += 1
        self.location = (self.x, self.y)

    def additem(self, item):
        self.roomitems.append(item)

    def removeitem(self, item):
        self.roomitems.remove(item)

    def description(self):
        print(self.surroundings)
        for obj in self.roomitems:
            ob = objects.objindex[obj]
            ob.description()
location = Point(0,0)


def testnorth():
    location.north()
    for loc in locations:
        if location.location == loc:
            location.south()
            return True
    location.south()

def testsouth():
    location.south()
    for loc in locations:
        if location.location == loc:
            location.north()
            return True
    location.north()

def testeast():
    location.east()
    for loc in locations:
        if location.location == loc:
            location.west()
            return True
    location.west()

def testwest():
    location.west()
    for loc in locations:
        if location.location == loc:
            location.east()
            return True
    location.east()



TheBeach = Point(0, 0,
        "You are on a beach. You can walk east down the shoreline ",
        ["peasants outfit"]
                )
EastShore = Point(1, 0,
        "The beach stretches on and on, and the ocean laps against your "
        "ankles. ",
        ["stick", "crab"]
                 )

locations = {(0, 0): TheBeach, (1, 0): EastShore}


