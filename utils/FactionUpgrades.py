factionsDict = {
    # Comparisons for full and abbreviation factions, also colors will be checked in here
    "Fairy": ["FR", 0xff99ff],
    "Elf": ["EL", 0x33cc33],
    "Angel": ["AN", 0x99ccff],
    "Goblin": ["GB", 0x585800],
    "Undead": ["UD", 0x3b0058],
    "Demon": ["DM", 0xc00000],
    "Titan": ["TT", 0xffd966],
    "Druid": ["DD", 0x833c0c],
    "Faceless": ["FC", 0x6432c7],
    "Dwarf": ["DN", 0x2828c6],
    "Drow": ["DW", 0x840058],
    "Dragon": ["DG", 0x27af27],
    "Archon": ["AR", 0xc5dff8],
    "Djinn": ["DJ", 0xa78bd9],
    "Makers": ["MK", 0xf0f0f0],
    "Mercenary": ["MC", 0x000000]
}

factionUpgradesDict = {
    # Fairy
    "FR1": "Pixie Dust Fertilizer",
    "FR2": "Fairy Workers",
    "FR3": "Kind Hearts",
    "FR4": "Fairy Cuisine",
    "FR5": "Golden Pots",
    "FR6": "Spellsmith",
    "FR7": "Starmetal Alloys",
    "FR8": "Rainbow Link",
    "FR9": "Swarm of Fairies",
    "FR10": "Bubble Swarm",
    "FR11": "Pheromones",
    "FR12": "Dream Catchers",

    # Elf
    "EL1": "Elven Mint",
    "EL2": "Elven Treasure Casing",
    "EL3": "Ancient Clicking Arts",
    "EL4": "Elven Emissary",
    "EL5": "Elven Efficiency",
    "EL6": "Secret Clicking Techniques",
    "EL7": "Elven Diplomacy",
    "EL8": "Elven Luck",
    "EL9": "Sylvan Treasure Frills",
    "EL10": "Wooden Dice",
    "EL11": "Camouflage",
    "EL12": "Elven Discipline",

    # Angel
    "AN1": "Holy Bells",
    "AN2": "Angelic Determination",
    "AN3": "Angel Feathers",
    "AN4": "Guardian Angels",
    "AN5": "Angelic Wisdom",
    "AN6": "Archangel Feathers",
    "AN7": "Magical Gates",
    "AN8": "Angelic Dominance",
    "AN9": "Wings of Liberty",
    "AN10": "Heaven's Brilliance",
    "AN11": "Angelic Fortitude",
    "AN12": "Seraphim Wings",

    # Goblin
    "GB1": "Strong Currency",
    "GB2": "Slave Trading",
    "GB3": "Cheap Materials",
    "GB4": "Black Market",
    "GB5": "Goblin Economists",
    "GB6": "Hobgoblin Gladiators",
    "GB7": "Goblin Central Bank",
    "GB8": "Fool's Gold",
    "GB9": "Green Fingers Discount",
    "GB10": "Fools Gems",
    "GB11": "Money is Magic",
    "GB12": "Lousy Architecture",

    # Undead
    "UD1": "The Walking Dead",
    "UD2": "Deadened Muscles",
    "UD3": "Death Temples",
    "UD4": "Unholy Rituals",
    "UD5": "Corpse Supply",
    "UD6": "Plagued Buildings",
    "UD7": "Dead Fields",
    "UD8": "Tireless Workers",
    "UD9": "Undead Resilience",
    "UD10": "Flesh Servants",
    "UD11": "Eternal Servitude",
    "UD12": "Zombie Apocalypse",

    # Demon
    "DM1": "Torture Chambers",
    "DM2": "Devil Tyrant",
    "DM3": "Evil Conquerors",
    "DM4": "Lava Pits",
    "DM5": "Demon Overseers",
    "DM6": "Demonic Presence",
    "DM7": "Infernal Magic",
    "DM8": "Burning Legion",
    "DM9": "Very Bad Guys",
    "DM10": "Abyssal Furnace",
    "DM11": "Demonic Fury",
    "DM12": "Devastation",

    # Titan
    "TT1": "Colossal Forge",
    "TT2": "Charged Clicks",
    "TT3": "Titan Obelisk",
    "TT4": "Titan Drill",
    "TT5": "Charged Structures",
    "TT6": "Titan Sized Walls",
    "TT7": "Cyclopean Strength",
    "TT8": "Heavy Coins",
    "TT9": "Oversized Legends",
    "TT10": "Giant Market",
    "TT11": "Titanic Authority",
    "TT12": "Colossus Kingdom",

    # Druid
    "DD1": "Druidic Vocabulary",
    "DD2": "Animal Companions",
    "DD3": "Natural Recycling",
    "DD4": "Earthly Bond",
    "DD5": "Bardic Knowledge",
    "DD6": "Shapeshifting",
    "DD7": "Mabinogion",
    "DD8": "Earthly Soul",
    "DD9": "Building Jungle",
    "DD10": "Building Vines",
    "DD11": "Lunar Cycle",
    "DD12": "Grove Farming",

    # Faceless
    "FC1": "Territorial Expanse",
    "FC2": "Evolutive Mutation",
    "FC3": "Deep Memory",
    "FC4": "Gold Synthesis",
    "FC5": "Mitosis",
    "FC6": "Overgrowth",
    "FC7": "Magical Treasure",
    "FC8": "Abominations",
    "FC9": "Hive Mind",
    "FC10": "Primal Knowledge",
    "FC11": "Forbidden Language",
    "FC12": "Dimension Door",

    # Dwarf
    "DN1": "Dwarven Ale",
    "DN2": "Expert Masonry",
    "DN3": "Mining Prodigies",
    "DN4": "Underground Citadels",
    "DN5": "Indestructible Treasure",
    "DN6": "Bearded Assistants",
    "DN7": "Battlehammers",
    "DN8": "Magic Resistance",
    "DN9": "Overwatch",
    "DN10": "Solidity",
    "DN11": "Stonetalking",
    "DN12": "Refined Minerals",

    # Drow
    "DW1": "Underworld Tyranny",
    "DW2": "Honor Among Killers",
    "DW3": "Shadow Advance",
    "DW4": "Mana Addicts",
    "DW5": "Blood Sacrifices",
    "DW6": "Blackmail",
    "DW7": "Spider Gods",
    "DW8": "Professional Assassins",
    "DW9": "Blade Dance",
    "DW10": "Spider Clerics",
    "DW11": "Ancillae Obscure",
    "DW12": "Crystal Servants",

    # Dragon
    "DG1": "Dragonscales",
    "DG2": "Iron Flight",
    "DG3": "Eternal Wisdom",
    "DG4": "Dragonborn",
    "DG5": "Bountiful Hoard",
    "DG6": "Sharp Claws",
    "DG7": "Ancient Hunger",
    "DG8": "Imposing Presence",
    "DG9": "Chromatic Scales",
    "DG10": "Fang Food",
    "DG11": "Wyrm's Rest",
    "DG12": "Draconic Supremacy",

    # Archon
    "AR1": "Star Trading",
    "AR2": "Energy Recharge",
    "AR3": "Cosmic Resonance",
    "AR4": "Constellation",
    "AR5": "Archon Pride",
    "AR6": "Absent-mindedness",
    "AR7": "Superior Consciousness",
    "AR8": "Strange Attraction",
    "AR9": "Arcane Core",
    "AR10": "Purity of Form",
    "AR11": "Absolute Hierarchy",
    "AR12": "Essence Extractor",

    # Djinn
    "DJ1": "The Desire Within",
    "DJ2": "Forbidden Will",
    "DJ3": "Magical Circuit",
    "DJ4": "Aura of Magic",
    "DJ5": "Spiritual Bindings",
    "DJ6": "Wild Surge",
    "DJ7": "Wishing Well",
    "DJ8": "Flashy Storm",
    "DJ9": "Mana Creatures",
    "DJ10": "Wishes Come True",
    "DJ11": "Blue Powder",
    "DJ12": "Academic Prodigy",

    # Makers
    "MK1": "Hand of the Makers",
    "MK2": "Everlasting Materials",
    "MK3": "Infinite Improvements",
    "MK4": "Magical Shards",
    "MK5": "Treasure Mosaic",
    "MK6": "Art of Commerce",
    "MK7": "Stone Carving",
    "MK8": "Past Trade",
    "MK9": "Structural Stability",
    "MK10": "Valuable Antiquity",
    "MK11": "Bedrock Foundations",
    "MK12": "Reality Marble"
}

researchBranchesdict = {
    "Spellcraft": "http://musicfamily.org/realm/Factions/picks/Spellcraftr.png",
    "Craftsmanship": "http://musicfamily.org/realm/Factions/picks/Craftsmanshipr.png",
    "Divine": "http://musicfamily.org/realm/Factions/picks/Diviner.png",
    "Economics": "http://musicfamily.org/realm/Factions/picks/Economicsr.png",
    "Alchemy": "http://musicfamily.org/realm/Factions/picks/Alchemyr.png",
    "Warfare": "http://musicfamily.org/realm/Factions/picks/Warfarer.png",
    "Forbidden": "http://musicfamily.org/realm/Factions/picks/Forbiddenr.png"
}

artifactsList = [
    "Ancient Stoneslab 1",
    "Fossilized Piece of Bark 1",
    "Bone Fragment 1",
    "Ancient Stoneslab 2",
    "Fossilized Piece of Bark 2",
    "Bone Fragment 2",
    "Key to the Lost City",
    "Ancient Device",
    "Earth Core",
    "Horn of the Kings",
    "Flame of Bondelnar",
    "Spiky Rough Egg",
    "Obsidian Shard",
    "First Iron Fragment",
    "Second Iron Fragment",
    "Third Iron Fragment",
    "First Crystal Fragment",
    "Second Crystal Fragment",
    "Third Crystal Fragment",
    "First Stone Fragment",
    "Second Stone Fragment",
    "Third Stone Fragment",
    "Obsidian Crown",
    "Forgotten Relic",
    "Rough Stone",
    "Scarab of Fortune",
    "Chocolate Cookie",
    "Fossilized Rodent",
    "Power Orb",
    "Pink Carrot",
    "Bottled Voice",
    "Lucky Clover",
    "Mini-treasure",
    "Pillar Fragment",
    "Divine Sword",
    "Ancient Coin Piece",
    "Goblin Purse",
    "Rotten Organ",
    "Jaw Bone",
    "Demonic Figurine",
    "Demon Horn",
    "Huge Titan Statue",
    "Titan Shield",
    "Glyph Table",
    "Stone of Balance",
    "Translucent Goo",
    "Octopus-shaped Helmet",
    "Dwarven Bow",
    "Stone Tankard",
    "Ceremonial Dagger",
    "Arachnid Figurine",
    "Steel Plate",
    "Black Sword",
    "Dragon Fang",
    "Dragon Soul",
    "Vanilla Flavor Juice",
    "Ancient Cocoa Bean",
    "Know Your Enemy, Part I",
    "Voodoo Doll",
    "Wall Fragment",
    "Fortune Teller Machine",
    "Dawnstone",
    "Duskstone",
    "Ancient Heirloom",
    "Know Your Enemy, Part II",
    "Veteran Figurine",
    "Wall Chunk",
    "Excavated Mirage",
    "Ancestral Hourglass",
    "Silk Cloth",
    "Raw Emerald",
    "Fossilized Wing",
    "Spiked Whip",
    "Dusty Coffin",
    "Crystallized Lava",
    "Titan Helmet",
    "Branch of the Life Tree",
    "Nightmare Figment",
    "Beard Hair",
    "Poison Vial",
    "Dragon Scale",
    "Lantern of Guidance",
    "Oil Lamp",
    "Spark of Life",
    "Planetary Force",
    "Mercenary Insiginia",
    "Mana Loom",
    "Factory",
    "Mythos",
    "Vault",
    "Athanor",
    "Battlefield",
    "Apeiron",
    "Glowing Wing",
    "Sylvan Mirror",
    "Solid Cloud",
    "Orc Fang Necklace",
    "Blood Chalice",
    "Demon Tail",
    "Frozen Lightning",
    "Primal Leaf",
    "The Blackest Ink"
]

def getFactionColour(faction):
    # Gets the color from dictionary if value matches abbreviation
    for key, value in factionsDict.items():
        if faction in [key, value[0]]:
            return int(value[1])


def getFactionAbbr(faction):
    # Gets the faction abbreviation, returns True if found, and also the abbreviation/color, False otherwise

    for key, value in factionsDict.items():
        if key == faction:
            return True, value[0], value[1]

    return False, None, None


def getFactionUpgradeName(faction):
    # Checks the 3-letter abbreviation, returns the title of upgrade if found
    if faction in factionUpgradesDict:
        return factionUpgradesDict[faction]


def getFactionNameFull(faction):
    for key, value in factionsDict.items():
        if faction in value:
            return key

    return None

def fastArtifactSearch(artifact):
    artList = []
    artifact = artifact.lower()

    for line in artifactsList:
        if artifact in line.lower():
            artList.append(line)

    if artifact in ['kye 1', 'kye i', 'kye', 'kye1']:
        artList.append("Know Your Enemy, Part I")

    if artifact in ['kye 2', 'kye ii', 'kye', 'kye2']:
        artList.append("Know Your Enemy, Part II")

    if artifact in ['ftm']:
        artList.append("Fortune Teller Machine")

    if artifact in ['vfj']:
        artList.append("Vanilla Flavor Juice")

    if artifact in ['vf']:
        artList.append("Veteran Figurine")

    return artList