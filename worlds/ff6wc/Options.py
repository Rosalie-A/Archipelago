import math
import typing

from BaseClasses import MultiWorld
from Options import Option, DefaultOnToggle, Range, Toggle, DeathLink, Choice, TextChoice, FreeText


class CharacterCount(Range):
    """Sets the number of characters needed to access the final battle"""
    display_name = "Characters Required"
    range_start = 0
    range_end = 14
    default = 8


class EsperCount(Range):
    """Sets the number of Espers needed to access the final battle"""
    display_name = "Espers Required"
    range_start = 0
    range_end = 27
    default = 12


class DragonCount(Range):
    """Sets the number of dragons needed to access the final battle"""
    display_name = "Dragons Required"
    range_start = 0
    range_end = 8
    default = 2

class BossCount(Range):
    """Sets the number of bosses required to access the final battle"""
    display_name = "Bosses Required"
    range_start = 0
    range_end = 40
    default = 0

class StartingCharacterCount(Range):
    """Sets the number of starting characters"""
    display_name = "Starting Character Count"
    range_start = 1
    range_end = 4
    default = 2

class StartingCharacter1(Choice):
    """Starting Character 1"""
    display_name = "Starting Character 1"
    option_terra = 0
    option_locke = 1
    option_edgar = 2
    option_sabin = 3
    option_celes = 4
    option_shadow = 5
    option_cyan = 6
    option_gau = 7
    option_setzer = 8
    option_mog = 9
    option_strago = 10
    option_relm = 11
    option_gogo = 12
    option_umaro = 13
    option_random_with_no_gogo_or_umaro = 14
    default = 14

class StartingCharacter2(Choice):
    """Starting Character 2. Only used if Starting Character Count is 2+"""
    display_name = "Starting Character 2"
    option_terra = 0
    option_locke = 1
    option_edgar = 2
    option_sabin = 3
    option_celes = 4
    option_shadow = 5
    option_cyan = 6
    option_gau = 7
    option_setzer = 8
    option_mog = 9
    option_strago = 10
    option_relm = 11
    option_gogo = 12
    option_umaro = 13
    option_none = 14
    option_random_with_no_gogo_or_umaro = 15
    default = 15

class StartingCharacter3(Choice):
    """Starting Character 3. Only used if Starting Character Count is 3+"""
    display_name = "Starting Character 3"
    option_terra = 0
    option_locke = 1
    option_edgar = 2
    option_sabin = 3
    option_celes = 4
    option_shadow = 5
    option_cyan = 6
    option_gau = 7
    option_setzer = 8
    option_mog = 9
    option_strago = 10
    option_relm = 11
    option_gogo = 12
    option_umaro = 13
    option_none = 14
    option_random_with_no_gogo_or_umaro = 15
    default = 14

class StartingCharacter4(Choice):
    """Starting Character 4. Only used if Starting Character Count is 4"""
    display_name = "Starting Character 4"
    option_terra = 0
    option_locke = 1
    option_edgar = 2
    option_sabin = 3
    option_celes = 4
    option_shadow = 5
    option_cyan = 6
    option_gau = 7
    option_setzer = 8
    option_mog = 9
    option_strago = 10
    option_relm = 11
    option_gogo = 12
    option_umaro = 13
    option_none = 14
    option_random_with_no_gogo_or_umaro = 15
    default = 14

class RandomizedStats(Choice):
    """Modify character base stats, as a range of percentages applied to their vanilla stats.
    Options include vanilla (100%), Light (85-125%), Moderate (50-150%), Boosted (100-1750%) and Wild (0-200%)"""
    display_name = "Randomized Stats"
    option_vanilla = 0
    option_light = 1
    option_moderate = 2
    option_boosted = 3
    option_wild = 4
    default = 1

class RandomizedCommands(Choice):
    """Randomize everyone's unique commands. Random Vanilla will pull only from the base list of commands.
    Random Most will include Relic-modified commands, and Random All includes temporary character commands
    like Shock"""
    display_name = "Randomized Commands"
    option_vanilla = 0
    option_random_vanilla = 1
    option_random_most = 2
    option_random_all = 3
    default = 2

class BattleRewardMultiplier(Choice):
    """Multiplies the rewards (EXP, MP, GP) from enemies."""
    display_name = "Battle Reward Multiplier"
    option_vanilla = 0
    option_double = 1
    option_triple = 2
    option_quadruple = 3
    option_quintuple = 4
    default = 2

class RandomizedBosses(Choice):
    """Modifies boss encounters. Shuffled mixes up the vanilla bosses (so you'll still have one of each). Random
    will roll each slot independently, making it likely a boss will show up multiple times or not at all."""
    display_name = "Randomized Bosses"
    option_vanilla = 0
    option_shuffled = 1
    option_randomized = 2
    default = 1

class RandomEncounters(Choice):
    """Modifies random encounters. The Wild setting mixes bosses into the pool of encounters"""
    display_name = "Random Encounters"
    option_vanilla = 0
    option_randomized = 1
    option_wild = 2
    default = 1

class EsperSpells(Choice):
    """Modifies the spells taught by Espers. Shuffle mixes around the vanilla learnsets, while
    Random rolls new options for every Esper. Random Tiered weights powerful spells to be less common."""
    display_name = "Esper Spells"
    option_vanilla = 0
    option_shuffled = 1
    option_randomized = 2
    option_random_tiered = 3
    default = 1

class EsperBonuses(Choice):
    """Modifies level up bonuses from Espers. Shuffle mixes around the vanilla bonuses, while Random
    rolls new options for every Esper"""
    display_name = "Esper Bonuses"
    option_vanilla = 0
    option_shuffled = 1
    option_randomized = 2
    default = 1

class EsperEquipability(Choice):
    """Modifies who can equip each esper. Random rolls a set of characters for each Esper, while Balanced
    Random attempts to give every character the same number of Espers to equip"""
    display_name = "Esper Equipability"
    option_vanilla = 0
    option_randomized = 1
    option_balanced_random = 2
    default = 0

class NaturalMagic(Choice):
    """Modifies which two characters learn Magic via level up, and what they learn"""
    display_name = "Natural Magic"
    option_vanilla = 0
    option_random_characters = 1
    option_random_spells = 2
    option_both = 3
    default = 3

class StartingGP(Range):
    """Starting supply of GP"""
    display_name = "Starting GP"
    range_start = 0
    range_end = 50000
    default = 30000

class RandomizedShops(Choice):
    """Modifies shop inventories. Random can result in anything, while Random Tiered weights more powerful items
    to be less common"""
    display_name = "Randomized Shops"
    option_vanilla = 0
    option_randomized = 1
    option_random_tiered = 2
    default = 2

class SpellcastingItems(Choice):
    """Controls if Rods, Super Balls, and elemental Shields are allowed in shops. Limited removes Shields and
    makes rods and Super Balls very expensive"""
    display_name = "Spellcasting Items"
    option_vanilla = 0
    option_limited = 1
    option_none = 2
    default = 1

class Equipment(Choice):
    """Modifies who can use what equipment. Shuffled mixes each character's equipability with another's,
    while Balanced Random ensures every item is usable by seven characters."""
    display_name = "Equipment"
    option_vanilla = 0
    option_shuffled = 1
    option_randomized = 2
    option_balanced_random = 3
    default = 1

class AllowStrongestItems(DefaultOnToggle):
    """Controls if EXP Eggs, Illuminas, and Paladin Shields can appear in the game."""
    display_name = "Allow Strongest Items"

class RandomizeZozoClock(DefaultOnToggle):
    """Randomize the clock puzzle in Zozo."""
    display_name = "Randomize Zozo Clock"

class Treasuresanity(Choice):
    """Mixes all treasure chests and the like into the location pool. Not recommended for beginners.
    Additional Gating prevents having to double dip dungeons where you don't have the character needed to clear"""
    display_name = "Treasuresanity"
    option_off = 0
    option_on = 1
    option_on_with_additional_gating = 2

class EnableFlagstring(FreeText):
    """Enables the Flagstring option. Set this to "true" to use a custom Worlds Collide flagstring"""
    display_name = "Enable Flagstring"
    default = "false"

class Flagstring(FreeText):
    """Custom flagstring. For advanced users only: will override most other options"""
    display_name = "Flagstring"
    default = "flagstring_here"

ff6wc_options: typing.Dict[str, type(Option)] = {
    "CharacterCount": CharacterCount,
    "EsperCount": EsperCount,
    "DragonCount": DragonCount,
    "BossCount": BossCount,
    "StartingCharacterCount": StartingCharacterCount,
    "StartingCharacter1": StartingCharacter1,
    "StartingCharacter2": StartingCharacter2,
    "StartingCharacter3": StartingCharacter3,
    "StartingCharacter4": StartingCharacter4,
    "RandomizedStats": RandomizedStats,
    "RandomizedCommands": RandomizedCommands,
    "BattleRewardMultiplier": BattleRewardMultiplier,
    "RandomizedBosses": RandomizedBosses,
    "RandomEncounters": RandomEncounters,
    "EsperSpells": EsperSpells,
    "EsperBonuses": EsperBonuses,
    "EsperEquipability": EsperEquipability,
    "NaturalMagic": NaturalMagic,
    "StartingGP": StartingGP,
    "RandomizedShops": RandomizedShops,
    "SpellcastingItems": SpellcastingItems,
    "Equipment": Equipment,
    "AllowStrongestItems": AllowStrongestItems,
    "RandomizeZozoClock": RandomizeZozoClock,
    "Treasuresanity": Treasuresanity,
    "EnableFlagstring": EnableFlagstring,
    "Flagstring": Flagstring
}

def generate_flagstring(multiworld: MultiWorld, player: int, starting_characters):
    if multiworld.EnableFlagstring[player].value == 'true':
        flags = multiworld.Flagstring[player].value.split(" ")
    else:
        flags = [
            *generate_settings_string(),
            *generate_objectives_string(multiworld, player),
            *generate_party_string(multiworld, player, starting_characters),
            *generate_commands_string(multiworld, player),
            *generate_battle_string(multiworld, player),
            *generate_magic_string(multiworld, player),
            *generate_items_string(multiworld, player),
            *generate_gameplay_string(multiworld, player),
            *generate_graphics_string(),
            *generate_accessibility_string(),
            *generate_fixes_string()
        ]
        flags = [_ for _ in flags if len(_) > 0]
    return flags


def generate_settings_string():
    # Character gating is always on, and we want the spoiler log
    return ["-cg", "-sl"]

def generate_objectives_string(multiworld: MultiWorld, player: int):
    character_count = multiworld.CharacterCount[player]
    esper_count = multiworld.EsperCount[player]
    dragon_count = multiworld.DragonCount[player]
    boss_count = multiworld.BossCount[player]

    # fb = final battle unlock
    fb_character_string = f".2.{character_count}.{character_count}" if character_count > 0 else ""
    fb_esper_string = f".4.{esper_count}.{esper_count}" if esper_count > 0 else ""
    fb_dragon_string = f".6.{dragon_count}.{dragon_count}" if dragon_count > 0 else ""
    fb_boss_string = f".8.{boss_count}.{boss_count}" if boss_count > 0 else ""
    conditions = 0
    if character_count > 0:
        conditions += 1
    if esper_count > 0:
        conditions += 1
    if dragon_count > 0:
        conditions += 1
    if boss_count > 0:
        conditions += 1
    fb_base = f"2.{conditions}.{conditions}"
    fb_string = ["-oa", fb_base + fb_character_string + fb_esper_string + fb_dragon_string + fb_boss_string]

    character_count = min(14, character_count + 3)
    esper_count = min(27, esper_count + 3)
    dragon_count = min(8, dragon_count + 3)
    boss_count = min(40, boss_count + 3)
    conditions = math.ceil(conditions / 2)
    # kts = kefka's tower skip
    kts_character_string = f".2.{character_count}.{character_count}" if character_count > 0 else ""
    kts_esper_string = f".4.{esper_count}.{esper_count}" if esper_count > 0 else ""
    kts_dragon_string = f".6.{dragon_count}.{dragon_count}" if dragon_count > 0 else ""
    kts_boss_string = f".8.{boss_count}.{boss_count}" if boss_count > 0 else ""
    kts_base = f"3.{conditions}.{conditions}"
    kts_string = ["-ob", kts_base + kts_character_string + kts_esper_string + kts_dragon_string + kts_boss_string]

    swdtech_learn = ["-oc", "30.8.8.1.1.11.8"]
    magitek_upgrade = ["-od", "59.1.1.11.31"]

    return [*fb_string, *kts_string, *swdtech_learn, *magitek_upgrade]

def generate_party_string(multiworld: MultiWorld, player: int, starting_characters):
    character_count = multiworld.StartingCharacterCount[player].value

    if character_count < 4:
        starting_characters.extend(["", "", ""])

    character_one = starting_characters[0]
    character_two = starting_characters[1] if character_count >= 2 else ""
    character_three = starting_characters[2] if character_count >= 3 else ""
    character_four = starting_characters[3] if character_count == 4 else ""

    character_one = "-sc1=" + str.lower(character_one)
    character_two = "-sc2=" + str.lower(character_two) if character_count >= 2 else ""
    character_three = "-sc3=" + str.lower(character_three) if character_count >= 3 else ""
    character_four = "-sc4=" + str.lower(character_four) if character_count == 4 else ""

    stat_min = 100
    stat_max = 100
    if multiworld.RandomizedStats == 1: # Light
        stat_min = 85
        stat_max = 125
    elif multiworld.RandomizedStats == 2: # Moderate
        stat_min = 50
        stat_max = 150
    elif multiworld.RandomizedStats == 3: # Boosted
        stat_min = 100
        stat_max = 175
    elif multiworld.RandomizedStats == 4: # Wild
        stat_min = 0
        stat_max = 200

    stat_string = [f"-csrp", f"{stat_min}", f"{stat_max}"]

    equipable_umaro = "-eu"

    return [character_one, character_two, character_three, character_four, *stat_string, equipable_umaro]

def generate_commands_string(multiworld: MultiWorld, player: int):
    command_strings = []
    if multiworld.RandomizedCommands[player] == 0: # Vanilla
        command_strings = ["-com=03050708091011121315191629"]
    if multiworld.RandomizedCommands[player] == 1: # Randomized Vanilla
        command_strings = ["-com=03050708091011121315191629", "-scc"]
    if multiworld.RandomizedCommands[player].value >= 2: # Random Most/Random All
        forbid_commands_strings = ["-rec1=28", "-rec2=27", "-rec3=26"] if multiworld.RandomizedCommands[player] == 3 else ""
        command_strings = ["-com=98989898989898989898989898", *forbid_commands_strings]

    steal_command_strings = ["-sch", "-fc"] # Higher Steal Chance, Fix Capture Bugs
    swdtech_command_strings = ["-fst", "-sel"] # Fast SwdTech, Everyone Learns
    tools_command_strings = ["-sto=1"] # One starting Tool
    blitz_command_strings = ["-brl", "-bel"] # Bum Rush Last, Everyone Learns
    # Start with 3-5 Lores, +/- 25% MP cost, Everyone Learns
    lore_command_strings = ["-slr", "3", "5", "-lmprp", "75", "125", "-lel"]
    sketch_command_strings = ["-scis"] # Improved Sketch/Control
    # Start with one Dance, Shuffle Abilities, Display Abilities, No Stumble, Everyone Learns
    dance_command_strings = ["-sdr", "1", "1", "-das", "-dda", "-dns", "-del"]
    rage_command_strings = ["-srr", "10", "20", "-rnl"] # Start with 10-20 Rages, No Leap
    other_command_string = ["-stra"] #SwdTech/Runic All

    return [*command_strings, *steal_command_strings, *swdtech_command_strings, *tools_command_strings,
            *blitz_command_strings, *lore_command_strings, *sketch_command_strings, *dance_command_strings,
            *rage_command_strings, *other_command_string]

def generate_battle_string(multiworld: MultiWorld, player: int):
    reward_value = multiworld.BattleRewardMultiplier[player] + 1
    rewards_strings = [f"-xpm={reward_value}", f"-mpm={reward_value}", f"-gpm={reward_value}", "-be"]

    boss_string = ""
    if multiworld.RandomizedBosses[player] == 1:
        boss_string = "-bbs"
    elif multiworld.RandomizedBosses[player] == 2:
        boss_string = "-bbr"

    statue_string = "-stloc=mix" # Mix statues into the general pool

    dragon_string = "-drloc=shuffle" # Shuffle dragons amongst each other

    # Scaling factor of 2, abilities scale keeping elements, max level scale is 40, dragons get scaled
    scaling_string = ["-lsc=2", "-hmc=2", "-xgc=2", "-ase=2", "-msl=40", "-sed"]

    return [*rewards_strings, boss_string, statue_string, dragon_string, *scaling_string]


def generate_magic_string(multiworld: MultiWorld, player: int):
    spell_strings = ["-mmprp", "75", "125"] # Spell cost +/- 25%

    esper_spells_strings = [""]
    if multiworld.EsperSpells[player] == 1:
        esper_spells_strings = ["-ess"] # Shuffle Esper spells
    elif multiworld.EsperSpells[player] == 2:
        esper_spells_strings = ["-esr", "1", "5"] # Fully randomize Esper spells
    elif multiworld.EsperSpells[player] == 3:
        esper_spells_strings = ["-esrt"] # Randomize Esper spells with tiered weighting

    esper_bonuses_string = ""
    if multiworld.EsperBonuses[player] == 1: # Shuffled bonuses
        esper_bonuses_string = "-ebs"
    elif multiworld.EsperBonuses[player] == 2: # Random bonuses
        esper_bonuses_string = "-ebr=70"

    esper_equipability_string = ""
    if multiworld.EsperEquipability[player] == 1: # Random equipability
        esper_equipability_string = ["-eer", "1", "12"]
    elif multiworld.EsperEquipability[player] == 2: # Balanced random equipability
        esper_equipability_string = ["-eebr", "6"]

    multi_summon_string = "-ems"

    natural_magic_strings = ["-nmmi"] # Show who has Natural Magic
    if multiworld.NaturalMagic[player] == 1 or multiworld.NaturalMagic == 3: # Random characters
        natural_magic_strings.extend(["-nm1=random", "-nm2=random"])
    if multiworld.NaturalMagic[player] == 2 or multiworld.NaturalMagic == 3: # Random learnsets
        natural_magic_strings.extend(["-rns1", "-rns2", "-rnl1", "-rnl2"])

    return [*spell_strings, *esper_spells_strings, esper_bonuses_string, *esper_equipability_string,
            multi_summon_string, *natural_magic_strings]

def generate_items_string(multiworld: MultiWorld, player: int):
    starting_gp_string = f"-gp={multiworld.StartingGP[player]}"
    # Three Moogle Charms, a Warp Stone, and five Fenix Downs
    starting_items_strings = ["-smc=3", "-sws=1", "-sfd=5"]

    # 75-125% shop prices, five Dried Meat shops, no priceless items
    shops_strings = ["-sprp", "75", "125", "-sdm", "5", "-npi"]
    if multiworld.RandomizedShops[player] == 1: # Shuffled shops
        shops_strings.extend(["-slsr"])
    elif multiworld.RandomizedShops[player] == 2: # Randomized Shops
        shops_strings.extend(["-sirt"])

    spellcasting_items_string = []
    if multiworld.SpellcastingItems[player] == 1: # Limited
        spellcasting_items_string = ["-sebr", "-sesb", "-snes"]
    elif multiworld.SpellcastingItems[player] == 2: # None
        spellcasting_items_string = ["-snbr", "-snsb", "-snes"]

    # Moogle Charms equipable by all, no Moogle Charms in item pool, no Sprint Shoes in pool
    # Stronger Atma Weapon, 8-32 battles to uncurse Cursed Shield
    equipability_strings = ["-mca", "-nmc", "-noshoes", "-saw", "-csb", "8", "32"]
    if multiworld.AllowStrongestItems[player] == False:
        equipability_strings.extend(["-nee", "-nil", "-nfps"])
    if multiworld.Equipment[player] == 1: # Shuffled
        equipability_strings.extend(["-iesr=0", "-iersr=0"])
    elif multiworld.Equipment[player] == 2: # Random
        equipability_strings.extend(["-ier", "1", "14", "-ierr", "1", "14"])
    elif multiworld.Equipment[player] == 3: # Balanced Random
        equipability_strings.extend(["-iebr=6", "-ierbr=6"])
    return [starting_gp_string, *starting_items_strings, *shops_strings,
            *spellcasting_items_string, *equipability_strings]

def generate_gameplay_string(multiworld: MultiWorld, player: int):
    # B Dash, randomized Coliseum rewards and enemies, randomize Auction House minor items
    gameplay_strings = ["-move=bd", "-cor", "-crr", "-crvr", "50", "250", "-crm", "-ari"]
    if multiworld.AllowStrongestItems[player] == False:
        gameplay_strings.extend(["-cnee", "-cnil"])
    if multiworld.RandomizeZozoClock[player] == True:
        gameplay_strings.extend(["-rc"])
    return gameplay_strings

def generate_graphics_string():
    # Lowercase the names.
    return ["-name=Terra.Locke.Cyan.Shadow.Edgar.Sabin.Celes.Strago.Relm.Setzer.Mog.Gau.Gogo.Umaro "]

def generate_accessibility_string():
    # Remove flashing, add high contrast world map
    return ["-frm", "-wmhc"]

def generate_fixes_string():
    # Bug fixes, and Magimaster can cast his final spell because I'm a jerk.
    return ["-fedc", "-fe", "-fbs", "-fvd", "-fj", "-dgne", "-wnz", "-cmd"]
