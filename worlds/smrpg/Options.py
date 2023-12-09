import typing
from Options import Option, DefaultOnToggle, Choice, Range, Toggle


class StarPieceGoal(Choice):
    """
    Six or seven Star Pieces to fight Smithy.
    """
    display_name = "Star Piece Goal"
    option_six = 0
    option_seven = 1


class StarPiecesInBowsersKeep(DefaultOnToggle):
    """
    Star Pieces can be located on the Bowser's Keep boss slots: Magikoopa, Boomer, and Exor.
    If toggled off, Bowser's Keep will be unavailable until the requisite number of Star Pieces have been
    obtained and will be your route to the Factory. If toggled on, the Factory is opened as soon as the requisite
    number of Star Pieces have been obtained.
    """
    display_name = "Star Pieces in Bowser's Keep"


class BowsersKeepDoors(Range):
    """
    How many doors required to clear the middle of Bowser's Keep.
    """
    display_name = "Bowser's Keep Doors"
    range_start = 1
    range_end = 6
    default = 2


class ShuffleBowsersKeepDoors(DefaultOnToggle):
    """
    If toggled on, each door could contain any three rooms from the six doors. If toggled off, behaves like vanilla:
    two action doors, two battle doors, two puzzle doors.
    """
    display_name = "Shuffle Bowser's Keep Doors"


class CulexsLairPossible(DefaultOnToggle):
    """
    A Star Piece might be located on the boss in Culex's Lair, and Culex's reward (normally the Quartz Charm)
    might be required.
    """
    display_name = "Culex's Lair Possible"


class RandomizeEnemies(Choice):
    """
    Randomize all enemies. Mild randomizes their drops and formations. Moderate includes enemy stats and attack
    stats and effects. Severe includes their spell lists. Extreme is Severe, but with no safety checks -- have fun!
    """
    display_name = "Randomize Enemies"
    option_none = 0
    option_mild = 1
    option_moderate = 2
    option_severe = 3
    option_extreme = 4
    default = 1


class RandomizeBosses(DefaultOnToggle):
    """
    Randomize boss locations. Bosses will have their stats scaled to their location. This doesn't include spell stats:
    Breaker Beam will still hurt coming from Croco's slot.
    """
    display_name = "Randomize Bosses"


class RandomizeCharacterStats(DefaultOnToggle):
    """
    Stats for each character will be randomized.
    """
    display_name = "Randomize Character Stats"


class RandomizeCharacterSpells(DefaultOnToggle):
    """
    Randomize character learned spells and their spell powers
    """
    display_name = "Randomize Character Spells"


class StartingCharacterCount(Choice):
    """
    Start with one or three characters. Clearing Forest Maze or Marrymore will recruit a new character. If starting
    with one character, clearing Mushroom Way or Moleville will recruit a new character as well.
    """
    display_name = "Starting Character Count"
    option_one = 0
    option_three = 1
    default = 1


class StartingCharacter(Choice):
    """
    Choose which character you start with. If starting with three characters, this chooses the first one.
    """
    display_name = "Starting Character"
    option_mario = 0
    option_mallow = 1
    option_geno = 2
    option_bowser = 3
    option_toadstool = 4
    default = "random"


class RandomizeCharacterPalettes(DefaultOnToggle):
    """
    Randomize character palettes. Some come with fun names!
    """
    display_name = "Randomize Character Palettes"


class RandomizeEquipment(Choice):
    """
    Randomize equipment. Mild randomizes who can equip each piece of gear. Moderate randomizes stats and buffs. Severe
    removes safety checks for the status protection pins guarding against their status and a minimum number of instant
    KO protection items.
    """
    display_name = "Randomize Equipment"
    option_mild = 0
    option_moderate = 1
    option_severe = 2
    default = 0


class SuperJumpsNotRequired(Toggle):
    """
    Toggled on, this prevents progression items from being at the reward for thirty and a hundred Super Jumps.
    Toggled off, those locations may be required.
    """


class FreeShops(Toggle):
    """
    Toggled on, this gives you 9999 Coins, 99 Frog Coins, and makes shop prices all be one Coin/Frog Coin.
    Toggled off, shops will charge normal prices and you'll start with no Coins or Frog Coins.
    """


smrpg_options: typing.Dict[str, type(Option)] = {
    "StarPieceGoal": StarPieceGoal,
    "StarPiecesInBowsersKeep": StarPiecesInBowsersKeep,
    "BowsersKeepDoors": BowsersKeepDoors,
    "ShuffleBowsersKeepDoors": ShuffleBowsersKeepDoors,
    "CulexsLairPossible": CulexsLairPossible,
    "RandomizeEnemies": RandomizeEnemies,
    "RandomizeBosses": RandomizeBosses,
    "RandomizeCharacterStats": RandomizeCharacterStats,
    "RandomizeCharacterSpells": RandomizeCharacterSpells,
    "StartingCharacterCount": StartingCharacterCount,
    "StartingCharacter": StartingCharacter,
    "RandomizeCharacterPalettes": RandomizeCharacterPalettes,
    "RandomizeEquipment": RandomizeEquipment,
    "SuperJumpsNotRequired": SuperJumpsNotRequired,
    "FreeShops": FreeShops
}

def build_flag_string(options: typing.Dict[str, typing.Any]):
    key_flags = build_key_flags(options)
    character_flags = "Cj"
    treasure_flags = ""
    shop_flags = "Sc4"
    battle_flags = "X2"
    challenge_flags = "P1 Nbmq"
    tweaks_flags = "W -showequips"


def build_key_flags(options: typing.Dict[str, typing.Any]):
    key_flags = "Ksb R"
    if options["StarPieceGoal"] == StarPieceGoal.option_seven:
        key_flags += "7"
    if options["StarPiecesInBowsersKeep"] == StarPiecesInBowsersKeep.option_true:
        key_flags += "k"
    if options["CulexsLairPossible"] == CulexsLairPossible.option_true:
        key_flags += "c"
    return key_flags

def build_character_flags(options: typing.Dict[str, typing.Any]):
    character_flags = "Cj"
    starting_character_lookup = {
        "option_mario": "Ym",
        "option_mallow": "Yw",
        "option_geno": "Yg",
        "option_bowser": "Yb",
        "option_toadstool": "Yt",
    }
    if options["RandomizeCharacterStats"] == RandomizeCharacterStats.option_true:
        character_flags += "s"
    if options["RandomizeCharacterSpells"] == RandomizeCharacterSpells.option_true:
        character_flags += "pl"
    if options["StartingCharacterCount"] == StartingCharacterCount.option_one:
        character_flags += " -nfc"
    if options["StartingCharacter"] not in starting_character_lookup.keys():
        character_flags += f" {starting_character_lookup[options['StartingCharacter']]}"
    if options["RandomizeCharacterPalettes"] == RandomizeCharacterPalettes.option_true:
        character_flags += " -palette"
    return character_flags

def build_shop_flags(options: typing.Dict[str, typing.Any]):
    shop_flags = "Sc4"
    if options["FreeShops"] == FreeShops.option_true:
        shop_flags += " -freeshops"
    return shop_flags

def build_enemy_flags()


