"""
Generates random D&D 5E characters based on random tables
"""
import random
import math
import json


class CharGenTab:
    """
    Rollable table object, takes an arbitrary length list and a tuple,
    dice notation: xdy -> tuple: (x,y)
    use roll method to return a value from the table
    """
    table = ()
    dice = (0, 0)

    def __init__(self, newTab, dice):
        self.table = newTab
        self.dice = dice

    def roll(self):
        """Using dice and table returns a value from table"""
        val = 0
        for _ in range(self.dice[0]):
            val = val + random.randint(0, self.dice[1]-1)

        return self.table[val]

class CharStats:
    """
    Generates and stores the stats and abilities for new characters,
    provide number of dice to roll and how many to keep to constructor.
    """
    StatList = ["Str", "Dex", "Con", "Wis", "Int", "Cha"]
    Stats = {"Str":0, "Dex":0, "Con":0, "Wis":0, "Int":0, "Cha":0}
    StandardAbilities = []
    Abilities = []
    Race = ""

    def __init__(self, numDice, keep):
        for stat in self.StatList:
            self.Stats[stat] = self.rollStat(numDice, keep)

    def rollStat(self, numDice, keep):
        """
        takes number of dice and number to keep and returns a number roughly 1-20
        (exact bounds will vary with number of dice kept)
        """
        sides = math.floor(20/keep)
        keepers = [0] * keep
        lowest = (0, 20)
        for ii in range(numDice):
            roll = random.randint(1, sides)
            if ii < keep:
                keepers[ii] = roll
                if roll < lowest[1]:
                    lowest = (ii, roll)
            else:
                if roll > lowest[1]:
                    keepers[lowest[0]] = roll
                    lowest = (lowest[0], roll)
                    for jj in range(keep):
                        if keepers[jj] < lowest[1]:
                            lowest = (jj, keepers[jj])
        total = sum(keepers)

        return total

    def NewAbil(self, table, number):
        """Using provided table adds a number of new abilities equal to number"""
        for _ in range(number):
            self.Abilities.append(table.roll())

    def rollRace(self,RaceTab,RaceBonusTab,RacialAbil):
        """
        sets characters race atribute to result from provided table
        applies bonuses based on RaceBonusTab
        """
        self.Race = RaceTab.roll()
        StatBonuses = RaceBonusTab[self.Race]
        self.incRandAbil(StatBonuses[6])
        for ii in range(len(StatBonuses)-1):
            stat = self.StatList[ii]
            self.Stats[stat] = self.Stats[stat] + StatBonuses[ii]
        self.StandardAbilities = self.StandardAbilities + RacialAbil[self.Race]

    def incRandAbil(self, num):
        """used by rollRace, for random stat bonuses to help balance races"""
        for _ in range(num):
            Abil = random.randint(0,len(self.StatList)-1)
            Abil = self.StatList[Abil]
            self.Stats[Abil] = self.Stats[Abil] + 1

    def LvlUp(self, table, number):
        """
        Similar to NewAbil, but prints out the new abilities while adding them
        (so it is easier to update character sheet)
        """
        Abil = []
        for _ in range(number):
            Abil = table.roll()
            print(Abil)
            self.Abilities.append(Abil)

    def __str__(self):
        statString = ""
        for stat in self.StatList:
            statString = statString + "\n" + stat + ": " + str(self.Stats[stat])

        return ("Race: " + self.Race +
                "\nBasic Abilities:\n" + '\n'.join(self.StandardAbilities) +
                "\n---------------------\n"+
                "Rolled Abilities:\n" + '\n'.join(self.Abilities) + statString)


"""
Basic Idea for leveling up - a different table which gets rolled on at each tier
Tier 1 - 2-4
Tier 2 - 5-10
Tier 3 - 11-16
Tier 4 - 17-20

Tier 1 includes starting abilities
"""
file_name = "Escape.tab"
fp = open(file_name,"r")
tables = json.load(fp)

BasicAbilTable = CharGenTab(tables["BasicAbilities"], (1, len(tables["BasicAbilities"])))
Tier1Abil = tables["BasicAbilities"] + tables["Tier1Abilities"]
Tier1AbilTable = CharGenTab(Tier1Abil, (1,len(Tier1Abil)))
RaceTable = CharGenTab(tables["Races"], (1, len(tables["Races"])))
Guy1 = CharStats(2, 2)
Guy1.NewAbil(BasicAbilTable, 4)
Guy1.rollRace(RaceTable, tables["RacialStatBonuses"], tables["RacialAbilities"])
print(Guy1)
#Guy1.LvlUp(Tier1AbilTable,1)
fp.close()
