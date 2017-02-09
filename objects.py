#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jude.sidloski
#
# Created:     11/03/2014
# Copyright:   (c) jude.sidloski 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
class Character:

    def __init__(self, name, desc='none', bab=0, hp=0,
                 arm=0, exp=0, loot='nothing'):
        self.dex = 0
        self.con = 0
        self.str = 0
        self.exp = exp
        self.expreq = (10, 30, 75, 200, 400, 800, 1200, 2000)
        self.level = 1
        self.loot = loot
        self.name, self. desc, self.bab, self.hp, self.arm =\
            name, desc, bab, hp, arm
        self.atk = bab + self.str
        self.ac, self.touchac, self.ffac =\
                    10 + self.dex + arm, 10 + self.dex, 10 + arm
        self.weapon = ('no weapon')
        self.armor = ('no armor')
        objindex[name] = self

        self.combatcommands = [('help', self.help), ('m', self.medium),
    ('l', self.light), ('c', self.charge), ('r', self.run),('h', self.heavy)]

    def description(self):
        print(self.desc)

    def levelcheck(self):
        ''' called after battle to check if the player gains a level '''
        for i in self.expreq:
            try:
                if self.exp > i:
                    self.level += 1
                    print("You have gained a level!")
                    print("You are now level", self.level, "!")
                    self.expreq = self.expreq[1:]
                    player.levelup()
                    print(self.expreq)
            except: return

    def levelup(self):

        skillpoints = 10
        stats = [[0, "attack"], [0, "health"], [0, "defense"] ]

        def pointinput(n, sp):
            print("How many points would you like to put in", n, "?")
            x = input('>')
            if x == 'reset':
                return x
            try:
                wx = int(x)
                if wx <= sp and wx >= 0:
                    print("The value at 1 point is", x)
                    return x
                else:
                    print("You don't have that number of skillpoints!")
                    return pointinput(n, sp)

            except:
                print("Invalid!")
                return pointinput(n, sp)

        def confirm(stats, skillpoints):

            if skillpoints != 0:
                print("You have", skillpoints, "skill points to spend. Type"
                      " reset at anytime to restart,the leveling process.")
                for n in stats:
                    sp_response = pointinput(n[1], skillpoints)
                    if sp_response == 'reset':
                        skillpoints = 10
                        stats = [[0, "attack"], [0, "health"], [0, "defense"]]
                        break
                    else:
                        print("returned it is", sp_response)
                        skillpoints -= int(sp_response)
                        n[0] += int(sp_response)
            elif skillpoints == 0:
                print("You are spending:")
                print(stats[0][0], "in attack")
                print(stats[1][0], "in health")
                print(stats[2][0], "in defense\n")
                confirmq = input("type 'y' to confirm \n'>'")
                if confirmq == 'y':
                    player.str += stats[0][0]
                    player.con += stats[1][0]
                    player.dex += stats[2][0]
                    player.bab += 1
                    player.atk = player.bab + player.str
                    player.ac, player.touchac, player.ffac =\
                        10 + player.dex + player.arm, 10 + player.dex, 10 + player.arm
                    player.hp = 10 + ((1/2)*player.con) * player.level
                    print("Congratulations!\n")
                    return
                elif confirmq != 'y':
                    skillpoints = 10
                    stre = 0
                    con = 0
                    dex = 0
            confirm(stats, skillpoints)

        confirm(stats, skillpoints)

    def attack(self, opp, ab, dmgb):
        wep = objindex[self.weapon]
        atkroll = random.randint(1, 20)
        if atkroll == 20:
            dmg = (random.randint(wep.mindmg, wep.maxdmg) +
                (self.str * dmgb))
            if random.randint(1,20) + (self.atk * ab) > opp.ac:
                dmg = (dmg + random.randint(wep.mindmg,
                       wep.maxdmg) + (self.str * dmgb))
                print(self.name, "scores a Critical Strike!")
            else:
                print(self.name, "gets a good hit!")
                dmg += 2
        elif atkroll + (self.atk * ab) > opp.ac:
            dmg = (random.randint(wep.mindmg, wep.maxdmg) +
                (self.str * dmgb))
            print(self.name, "hit!")
        else:
            dmg = 0
            print(self.name, "misses!")
        opp.hp = opp.hp - dmg
        print(opp.name, "Takes", dmg, "damage!")
        print(opp.name, "Has", opp.hp, "health!\n")
    def light(self, opp):
        self.attack(opp, 1.5, 0.5)
    def medium(self, opp):
        self.attack(opp, 1, 1)
    def heavy(self, opp):
        self.attack(opp, 0.5, 1.5)
    def charge(self, opp):

        self.attack(opp, 2, 2)
        for buff in empty_bufftimers:
            if buff == None:
                buff = BuffTimer(self.ac, 0.25, 2)
                bufftimers.append(buff)
                break
        print("{0}'s armor class is reduced for 2 rounds!".format(self.name))
    def run(self, obj):
        print("You ran away!")
        return False
    def help(self):
        print("The commands available in combat are:", "(l)ight", "(m)edium",
              "(h)eavy", "(c)harge", "(r)un", "help", sep = '\n'
             )

class Object:

    def __init__(self, name, desc = 'none'):
        self.name, self.desc = name, desc
        objindex[name] = self
    def description(self):
        print(self.desc)


class Weapon(Object):

    def __init__(self, name, desc = 'none', mindmg = 1, maxdmg = 8, crit = 'x 2'):
        self.name, self.desc, self.mindmg, self.maxdmg, self.crit =\
                    name, desc, mindmg, maxdmg, crit
        self.atkbonus = 0
        objindex[name] = self

class Armor(Object):
    def __init__(self, name, desc = 'none', acb = 0):
        self.name, self.desc, self.acb = name, desc, acb
        objindex[name] = self

buff1=buff2=buff3=buff4=buff5=buff6=buff7=buff8=None
buff9=buff10=buff11=buff12=buff13=buff14=buff15=None
buff16=buff17=buff18=buff19=buff20=None

empty_bufftimers = [buff1, buff2, buff3, buff4, buff5, buff6, buff7, buff8,
                    buff9, buff10, buff11, buff12, buff13, buff14, buff15,
                    buff16, buff17, buff18, buff19, buff20]
bufftimers = []
class BuffTimer:

    def __init__(self, stat, debuff, time):
        self.debuff, self.time = debuff, time
        self.debuff = -(player.ac * debuff)

        self.buffcount = 0
        player.ac += self.debuff
        int(player.ac)

    def checker(self):
        if self.buffcount == self.time:
            player.ac -= self.debuff
            int(player.ac)
            bufftimers.remove(self)
            self = None

objindex = {}

stick = Weapon('stick', "A stick is here. It is a hefty piece of driftwood ",
                1, 6)
no_wep = Weapon('no weapon', mindmg = 1, maxdmg = 4)

no_arm = Armor('no armor', 'none', 0)
peasants_outfit = Armor('peasants outfit',
                        'A peasants outfit is on the ground. '+
                        'It is a well worn brown cotton that doesn\'t do '+
                        'much besides cover your skin. ',
                         1)

player = Character("Player", "none", bab = 0, hp = 20, arm = 0)
crab = Character('crab', 'A mighty crab snaps his claws at you. '+
                    "Beware the crab!", 3, 5, 4, 10, "crab")



