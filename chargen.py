import random
import math

BasicAbilities = (
    "Barbarian Rage",
    "2nd Wind",
    "Action Surge",
    "Upgrade Hit Dice",
    "+1 AC",
    "Sneak Attack",
    "Mobile Feat",
    "+2 Ranged/Thrown Attacks",
    "Arcane Cantrip Table (Int)",
    "Divine Cantrip Table (Wis)",
    "Inate Cantrip Table (Cha)",
    "Bardic Inspiration",
    "Wis Bonus to AC",
    "Dex Bonus to AC",
    "Cha Bonus to AC",
    "Int Bonus to AC",
    "Prof with All Armor Types",
    "All Martial Weapons",
    "Improvised Weapons and Armor"
)
Tier1Abilities = (
    "Reckless Attack",
    "Jack of All Trades",
    "Song of Rest",
    "Level 1 Spells (Divine)",
    "Wild Shape",
    "Improved Critical",
    "Martial Arts",
    "Lay on Hands",
    "Cunning Action",
    "Telepathy 30 feet",
    "At will: Mage Armor",
    "No longer sleeps",
    "Can Speak with Animals",
    "See in Magical Darkness",
    "Any time you hit a creature with an attack, it's movement speed is reduced by 10'",
    "Diguise Self at will",
    "Silent Image at will",
    "Gain a familiar"
)
D6 = (1,6)

Races = (
    "Elf",
    "Human",
    "Dwarf",
    "Halfling",
    "Gnome",
    "Half-Elf",
    "Half-Orc",
    "IETS"
)

# Str,Dex,Con,Wis,Int,Cha, # of Random Stat Boosts
RacialStatBonuses = {
    "Elf":          [0, 2, 0, 1, 1, 1, 4],
    "Human":        [1, 1, 1, 1, 1, 1, 4],
    "Dwarf":        [2, 0, 2, 1, 0, 0, 4],
    "Halfling":     [0, 2, 1, 1, 0, 1, 4],
    "Gnome":        [0, 1, 1, 0, 2, 0, 5],
    "Half-Elf":     [1, 1, 1, 1, 1, 2, 2],
    "Half-Orc":     [2, 0, 2, 0, 0, 0, 5],
    "IETS":         [0, 0, 0, 0, 0, 0, 9]
}

RacialAbilities = {
    "Elf": [
        "Speed: 35"
        "Dark-Vision 60",
        "Sleep-Immune",
        "Charm Resistant",
        "Meditate for 4 Hours = Long Rest",
        "Prof in Perception"
    ],
    "Human":[
        "Speed: 30"],
    "Dwarf":[
        "Speed: 25"
        "Posion Resistant",
        "Dark-Vision 60",
        "Advantage on history checks related to stone"
    ],
    "Halfling":[
        "Speed: 25",
        "Lucky (reroll first 1 on d20)",
        "Advantage vs frightened",
        "Hide behind larger creatures"
    ],
    "Gnome":[
        "Speed: 25",
        "Darkvision 60",
        "Advantage on ST vs magic",
        "Double Prof bonus related to magic items"
    ],
    "Half-Elf":[
        "Speed: 30",
        "Darkvision 60",
        "Advantage vs charm/sleep"
    ],
    "Half-Orc":[
        "Speed: 30",
        "Darkvision 60",
        "If reduced to 0, drop to 1 instead (1/LR)",
        "Extra die when scoring crit"
    ],
    "IETS":[
        "Speed: 1D6*10 (Reroll each combat round)",
        "Roll 1d4-2 extra times on ability table"
    ]
}
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

Tier 1 does not include level 1, keeping the level 1 table seperate
"""
BasicAbilTable = CharGenTab(BasicAbilities, (1, len(BasicAbilities)))
RaceTable = CharGenTab(Races, (1, len(Races)))
Guy1 = CharStats(2, 2)
Guy1.NewAbil(BasicAbilTable, 4)
Guy1.rollRace(RaceTable, RacialStatBonuses, RacialAbilities)
print(Guy1)
