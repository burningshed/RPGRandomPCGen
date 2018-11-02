import pickle
import json

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

file_name = "Escape"
RAPick = pickle.dumps(RacialAbilities,protocol=0)
print(RAPick)
print(pickle.loads(RAPick))

print("\n\n JSON TEST \n\n")
RAJS = json.dumps(RacialAbilities)
print(RAJS)
print(json.loads(RAJS))
