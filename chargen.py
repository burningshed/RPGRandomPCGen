import random
import math

Abilities = ("Barbarian Rage","2nd Wind","Action Surge","Upgrade Hit Dice","+1 AC",
            "Sneak Attack","Mobile Feat","+2 Ranged/Thrown Attacks",
            "Arcane Cantrip Table (Int)","Divine Cantrip Table (Wis)",
            "Inate Cantrip Table (Cha)","Bardic Inspiration",
            "Wis Bonus to AC","Dex Bonus to AC","Cha Bonus to AC","Prof with All Armor Types",
             "All Martial Weapons","Improvised Weapons and Armor")
D6 = (1,6)

Races = ("Elf","Human","Dwarf","Halfling","Gnome","Half-Elf","Half-Orc")
# Str,Dex,Con,Wis,Int,Cha, # of Random Stat Boosts

RacialStatBonuses = {"Elf":[0,2,0,1,1,1,4],"Human":[1,1,1,1,1,1,3],"Dwarf":[2,0,2,1,0,0,4],"Halfling":[0,2,1,1,0,1,4],"Gnome":[0,1,1,0,2,0,5],"Half-Elf":[1,1,1,1,1,2,2],"Half-Orc":[2,0,2,0,0,0,5]}
RacialAbilities = {"Elf":["Dark-Vision 60","Sleep-Immune","Charm Resistant","Meditate for 4 Hours  = Long Rest"],"Human":[],"Dwarf":["Posion Resistant","Dark-Vision 60"]}
class CharGenTab:
    Table = ()
    dice = (0,0)

    def __init__(self, newTab, dice):
        self.Table = newTab
        self.dice = dice

    def roll(self):
        val = 0
        for ii in range(self.dice[0]):
            val = val + random.randint(0,self.dice[1]-1)

        return self.Table[val]

class charStats:
    # Should Rewrite this using a dictionary
    StatList = ["Str","Dex","Con","Wis","Int","Cha"]
    Stats = {"Str":0,"Dex":0,"Con":0,"Wis":0,"Int":0,"Cha":0}
    Abilities = []
    Race = ""

    def __init__(self, numDice, keep):
        for stat in self.StatList:
            self.Stats[stat] = self.rollStat(numDice,keep)

    def rollStat(self, numDice, keep):
        sides = math.floor(20/keep)
        keepers = [0] * keep
        lowest = (0,20)
        for ii in range(numDice):
            roll = random.randint(1,sides)
            if ii < keep:
                keepers[ii] = roll
                if roll < lowest[1]:
                    lowest = (ii,roll)
            else:
                if roll > lowest[1]:
                    keepers[lowest[0]] = roll
                    lowest = (lowest[0],roll)
                    for jj in range(keep):
                        if keepers[jj] < lowest[1]:
                            lowest = (jj,keepers[jj])
        total = sum(keepers)

        return total

    def NewAbil(self, table, number):
        for ii in range(number):
            self.Abilities.append(table.roll())

    def rollRace(self,RaceTab,RaceBonusTab):
        self.Race = RaceTab.roll()
        StatBonuses = RaceBonusTab[self.Race]
        self.incRandAbil(StatBonuses[6])
        for ii in range(len(StatBonuses)-1):
            stat = self.StatList[ii]
            self.Stats[stat] = self.Stats[stat] + StatBonuses[ii]

    def incRandAbil(self, num):
        for ii in range(num):
            Abil = random.randint(0,len(self.StatList)-1)
            Abil = self.StatList[Abil]
            self.Stats[Abil] = self.Stats[Abil] + 1

    def __str__(self):
        statString = ""
        for stat in self.StatList:
            statString = statString + "\n" + stat + ": " + str(self.Stats[stat])

        return ("Race: " + self.Race +
            "\nAbilities:\n" + '\n'.join(self.Abilities) + statString)



AbilTable = CharGenTab(Abilities,(1,len(Abilities)))
RaceTable = CharGenTab(Races,(1,len(Races)))
Guy1 = charStats(2,2)
Guy1.NewAbil(AbilTable,4)
Guy1.rollRace(RaceTable,RacialStatBonuses)
print(Guy1)
