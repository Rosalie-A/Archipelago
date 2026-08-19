import typing
from dataclasses import dataclass
from Options import Option, DefaultOnToggle, Choice, PerGameCommonOptions, Range, OptionSet, Toggle

characters = ["Mario", "Mallow", "Geno", "Bowser", "Toadstool"]
random_characters = ["Random One", "Random Two", "Random Three", "Random Four", "All"]
# Party

class ShuffleCharacters(DefaultOnToggle):
    """placeholder"""
    display_name = "Shuffle Characters"

class MaxCharacters(Range):
    """placeholder"""
    range_start = 1
    range_end = 5
    default = 5
    display_name = "Max Characters"

class AllowEarlyAllySwitching(DefaultOnToggle):
    """placeholder"""
    display_name = "Allow Early Ally Switching"
    
class StartingCharacterCount(Range):
    """placeholder"""
    range_start = 1
    range_end = 5
    default = 3
    display_name = "Starting Character Count"
    
class LeadCharacter(Choice):
    """placeholder"""
    option_mario = 0
    option_mallow = 1
    option_geno = 2
    option_bowser = 3
    option_toadstool = 4
    default = 0
    display_name = "Lead Character"
    
class MarioPlacement(Choice):
    """placeholder"""
    option_starting = 0
    option_available = 1
    option_absent = 2
    default = 1
    display_name = "Mario Placement"
    
class MallowPlacement(Choice):
    """placeholder"""
    option_starting = 0
    option_available = 1
    option_absent = 2
    default = 1
    display_name = "Mallow Placement"
    
class GenoPlacement(Choice):
    """placeholder"""
    option_starting = 0
    option_available = 1
    option_absent = 2
    default = 1
    display_name = "Geno Placement"
    
class BowserPlacement(Choice):
    """placeholder"""
    option_starting = 0
    option_available = 1
    option_absent = 2
    default = 1
    display_name = "Bowser Placement"
    
class ToadstoolPlacement(Choice):
    """placeholder"""
    option_starting = 0
    option_available = 1
    option_absent = 2
    default = 1
    display_name = "Toadstool Placement"

class PlayAsLeadCharacter(Toggle):
    """placeholder"""
    display_name = "Play As Lead Character"

# Equipment

class EquipmentPermissions(Choice):
    """placeholder"""
    option_default_permissions = 0
    option_default_all_accessories = 1
    option_random_permissions = 2
    option_random_all_accessories = 3
    default = 0
    display_name = "Equipment Permissions"

class EquipmentProperties(Choice):
    """placeholder"""
    option_default_properties = 0
    option_buffs_added = 1
    option_full_random = 2
    display_name = "Equipment Properties"

class IgnoreNamesakeProperties(Toggle):
    """placeholder"""
    display_name = "Ignore Namesake Properties"

class StarPieceHints(DefaultOnToggle):
    """placeholder"""
    display_name = "Star Piece Hints"

# Stats and Spells

class EXPMultiplier(Choice):
    """placeholder"""
    option_vanilla = 0
    option_double = 1
    option_triple = 2
    default = 0
    display_name = "EXP Multiplier"

class RandomizeCharacterStats(Toggle):
    """placeholder"""
    display_name = "Randomize Character Stats"

class RandomizeLearnedSpells(Toggle):
    """placeholder"""
    display_name = "Randomize Learned Spells"

class RandomizeSpellStats(Toggle):
    """placeholder"""
    display_name = "Randomize Spell Stats"

class InfuseElements(Toggle):
    """placeholder"""
    display_name = "Infuse Spell Elements"

class RandomizeSpellElements(Toggle):
    """placeholder"""
    display_name = "Randomize Character Spell Elements"

class UncapSuperJumps(Toggle):
    """placeholder"""
    display_name = "Uncap Super Jumps"

class UncapMaxFP(Toggle):
    """placeholder"""
    display_name = "Uncap Max FP"

class AvailableSpells(OptionSet):
    """placeholder"""
    valid_keys = [
        "Jump", "Fire Orb", "Super Jump", "Super Flame", "Ultra Jump", "Ultra Flame",
        "Thunderbolt", "HP Rain", "Psychopath", "Shocker", "Snowy", "Star Rain",
        "Geno Beam", "Geno Boost", "Geno Whirl", "Geno Blast", "Geno Flash",
        "Terrorize", "Poison Gas", "Crusher", "Bowser Crush",
        "Therapy", "Group Hug", "Sleepy Time", "Come Back", "Mute", "Psych Bomb"
    ]
    default = valid_keys
    display_name = "Available Spells"

# Star Pieces and Bosses

class ShuffleStarPieces(Toggle):
    """placeholder"""
    display_name = "Shuffle Star Pieces"

class TotalStarPieces(Range):
    """placeholder"""
    range_start = 0
    range_end = 7
    default = 6
    display_name = "Total Star Pieces"

class ProgressionLogicDifficulty(Choice):
    """placeholder"""
    option_normal = 0
    option_hard = 1
    default = 0
    display_name = "Progression Logic Difficulty"

class DisperseStarPieces(Toggle):
    """placeholder"""
    display_name = "Disperse Star Pieces"

# Items

class ShuffleItems(Toggle):
    """placeholder"""
    display_name = "Shuffle Items"

class ItemPoolQuality(Choice):
    """placeholder"""
    option_original = 0
    option_full_random = 1
    option_mostly_random = 2
    option_empty = 3
    display_name = "Item Pool Quality"

class BiasItemShuffle(Toggle):
    """placeholder"""
    display_name = "Bias Item Shuffle"

class AnnoyingChests(Toggle):
    """placceholder"""
    display_name = "Annoying Chests"

class NoStarEgg(Toggle):
    """placeholder"""
    display_name = "No Star Egg"

class RestrictSpecialEquips(Toggle):
    """placeholder"""
    display_name = "Restrict Special Equips"

class EXPStarsAnywhere(Toggle):
    """placeholder"""
    display_name = "EXP Stars Anywhere"

class ShuffleBoosterHillFlowers(Toggle):
    """placeholder"""
    display_name = "Shuffle Booster Hill Flowers"

class ShuffleRegularCoins(Toggle):
    """placeholder"""
    display_name = "Shuffle Regular Coins"

class MimicsAnywhere(Toggle):
    """placeholder"""
    display_name = "Mimics Anywhere"

class SlotsAnywhere(Toggle):
    """placeholder"""
    display_name = "Slots Anywhere"

class ShuffleBeetlemania(Toggle):
    """placeholder"""
    display_name = "Shuffle Beetlemania"

class ShuffleMagikoopaChest(Toggle):
    """placeholder"""
    display_name = "Shuffle Magikoopa Chest"

class ShuffleWeddingGear(Toggle):
    """placeholder"""
    display_name = "Shuffle Wedding Gear"

class ShuffleMarioDoll(Toggle):
    """placeholder"""
    display_name = "Shuffle Mario Doll"

class ShuffleCookies(Toggle):
    """placeholder"""
    display_name = "Shuffle Cookies"

class FireworksTradeSequence(Choice):
    """placeholder"""
    option_vanilla = 0
    option_shuffle_one = 1
    option_progressive = 2
    display_name = "Fireworks Trade Sequence"

# Progression Availability

class KeyItemsAnywhere(Toggle):
    """placeholder"""
    display_name = "Key Items Anywhere"

class StarPiecesAnywhere(Toggle):
    """placeholder"""
    display_name = "Star Pieces Anywhere"

class SpellsAnywhere(Toggle):
    """placeholder"""
    display_name = "Spells Anywhere"

class InvisibleFlagsAnywhere(Toggle):
    """placeholder"""
    display_name = "Invisible Flags Anywhere"

class EnableRemakeContent(Toggle):
    """placeholder"""
    display_name = "Enable Remake Content"

# Progression Gating

class BanditsWayGate(Choice):
    """placeholder"""
    option_mallow = 0
    option_mushroom_way = 1
    option_hammer_bros = 2
    option_open = 3
    default = 0
    display_name = "Bandit's Way Gate"

class KeroSewersGate(Choice):
    """placeholder"""
    option_mallow = 0
    option_mack = 1
    option_mushroom_kingdom = 2
    option_rare_frog_coin = 3
    option_open = 4
    default = 0
    display_name = "Kero Sewers Gate"

class ForestMazeGate(Choice):
    """placeholder"""
    option_cricket_pie = 0
    option_open = 1
    default = 0
    display_name = "Forest Maze Gate"

class PipeVaultGate(Choice):
    """placeholder"""
    option_geno = 0
    option_forest_maze = 1
    option_bowyer = 2
    option_open = 3
    default = 3
    display_name = "Pipe Vault Gate"

class MolevilleGate(Choice):
    """placeholder"""
    option_geno = 0
    option_forest_maze = 1
    option_bowyer = 2
    option_boshi = 3
    option_open = 4
    default = 4
    display_name = "Moleville Gate"

class BoosterTowerGate(Choice):
    """placeholder"""
    option_mario = 0
    option_mallow = 1
    option_geno = 2
    option_bowser = 3
    option_toadstool = 4
    option_moleville_mines = 5
    option_punchinello = 6
    option_open = 7
    default = 3
    display_name = "Booster Tower Gate"

class BoosterHillGate(Choice):
    """placeholder"""
    option_booster_tower = 0
    option_knife_guy_crate_guy = 1
    option_open = 2
    default = 2
    display_name = "Booster Hill Gate"

class MarrymoreGate(Choice):
    """placeholder"""
    option_booster_hill = 0
    option_booster_tower = 1
    option_knife_guy_crate_guy = 2
    option_open = 3
    default = 0
    display_name = "Marrymore Gate"

class YaridovichGate(Choice):
    """placeholder"""
    option_sunken_ship = 0
    option_johnny = 1
    option_open = 2
    default = 0
    display_name = "Yaridovich Gate"

class SeaGate(Choice):
    """placeholder"""
    option_toadstool = 0
    option_four_star_pieces = 1
    option_bundt = 2
    option_marrymore = 3
    option_open = 4
    default = 1
    display_name = "Sea Gate"

class LandsEndGate(Choice):
    """placeholder"""
    option_five_star_pieces = 0
    option_elder = 1
    option_yaridovich = 2
    option_seaside_town = 3
    option_open = 4
    default = 4
    display_name = "Land's End Gate"

class BelomeTempleGate(Choice):
    """placeholder"""
    option_key = 0
    option_open = 1
    default = 1
    display_name = "Belome Temple Gate"

class MonstroTownGate(Choice):
    """placeholder"""
    option_lands_end = 0
    option_belome_2 = 1
    option_open = 2
    default = 0
    display_name = "Monstro Town Gate"

class SkipMustyFearsSequence(Toggle):
    """placeholder"""
    display_name = "Skip Musty Fears Sequence"

class NimbusLandGate(Choice):
    """placeholder"""
    option_bean_valley = 0
    option_megasmilax = 1
    option_gold_paint = 2
    option_open = 3
    default = 3
    display_name = "Nimbus Land Gate"

class BarrelVolcanoGate(Choice):
    """placeholder"""
    option_nimbus_land = 0
    option_valentina = 1
    option_open = 2
    default = 0
    display_name = "Barrel Volcano Gate"

class BowsersKeepGate(Choice):
    """placeholder"""
    option_six_star_pieces = 0
    option_barrel_volcano = 1
    option_axem_rangers = 2
    option_open = 3
    default = 1
    display_name = "Bowser's Keep Gate"

class FactoryGate(Choice):
    """placeholder"""
    option_open_with_bowsers_keep = 0
    option_finish_bowsers_keep = 1
    option_six_star_pieces = 2
    option_exor = 3
    default = 1
    display_name = "Factory Gate"

class ReplaceWorstItems(Toggle):
    """placeholder"""
    display_name = "Replace Worst Items"

class RandomizePoisonMushroomEffect(Toggle):
    """placeholder"""
    display_name = "Randomize Poison Mushroom Effect"

class EXPStarBehavior(Choice):
    """placeholder"""
    option_vanilla = 0
    option_star_pieces = 1
    option_bosses = 2
    option_none = 3
    default = 0
    display_name = "EXP Star Behavior"

class LookTheOtherWayThreshold(Range):
    """placeholder"""
    range_start = 1
    range_end = 255
    default = 1
    display_name = "Look The Other Way Threshold"

class KnifeGuyThreshold(Range):
    """placeholder"""
    range_start = 1
    range_end = 254
    default = 1
    display_name = "Knife Guy Threshold"

class SuitePrize1Threshold(Range):
    """placeholder"""
    range_start = 1
    range_end = 249
    default = 1
    display_name = "Marrymore Suit Prize 1 Threshold"

class SuitePrize2Threshold(Range):
    """placeholder"""
    range_start = 2
    range_end = 250
    default = 2
    display_name = "Marrymore Suit Prize 2 Threshold"

class SuitePrize3Threshold(Range):
    """placeholder"""
    range_start = 3
    range_end = 251
    default = 3
    display_name = "Marrymore Suit Prize 3 Threshold"

class SuitePrize4Threshold(Range):
    """placeholder"""
    range_start = 4
    range_end = 252
    default = 4
    display_name = "Marrymore Suit Prize 4 Threshold"

class SuitePrize5Threshold(Range):
    """placeholder"""
    range_start = 5
    range_end = 253
    default = 5
    display_name = "Marrymore Suit Prize 5 Threshold"

class SuitePrize6Threshold(Range):
    """placeholder"""
    range_start = 6
    range_end = 254
    default = 6
    display_name = "Marrymore Suit Prize 6 Threshold"

class SuperJumpPrize1Threshold(Range):
    """placeholder"""
    range_start = 1
    range_end = 99
    default = 30
    display_name = "Super Jump Prize 1 Threshold"

class SuperJumpPrize2Threshold(Range):
    """placeholder"""
    range_start = 2
    range_end = 100
    default = 100
    display_name = "Super Jump Prize 2 Threshold"

class FixKnifeGuy(Toggle):
    """placeholder"""
    display_name = "Fix Knife Guy"

class KnifeGuyFixedPrizeThreshold(Range):
    """placeholder"""
    range_start = 2
    range_end = 255
    default = 2
    display_name = "Knife Guy Fixed Prize Threshold"

class BowserDoorRequirements(Range):
    """placeholder"""
    range_start = 1
    range_end = 6
    default = 4
    display_name = "Required Bowser Door Count"

class StarPiecesRequired(Range):
    """placeholder"""
    range_start = 0
    range_end = 7
    default = 6
    display_name = "Star Pieces Required"

class CasinoWarp(Toggle):
    """placeholder"""
    display_name = "Casino Warp"

class BucketWarp(Toggle):
    """placeholder"""
    display_name = "Bucket Warp"

class FastTravel(Toggle):
    """placeholder"""
    display_name = "Fast Travel"

class WinCondition(Choice):
    """placeholder"""
    option_factory = 0
    option_smithy = 1
    option_stars = 2
    option_sealed_door = 3
    default = 0
    display_name = "Win Condition"

# Puzzles

class ShuffleBallSolitaire(Toggle):
    """placeholdder"""
    display_name = "Shuffle Ball Solitaire"

class ShuffleMagicButtons(Toggle):
    """placeholdder"""
    display_name = "Shuffle Magic Buttons"

class ShuffleQuizQuestions(Toggle):
    """placeholdder"""
    display_name = "Shuffle Quiz Questions"

class IncludeNonSMRPGQuestions(Toggle):
    """placeholdder"""
    display_name = "Include Non-SMRPG Questions"

class RandomizeTadpolePondSong(Toggle):
    """placeholdder"""
    display_name = "Randomize Tadpole Pond songs"

class RandomizeSunkenShipPassword(Toggle):
    """placeholdder"""
    display_name = "Randomize Sunken Ship Passwords"

class BoosterHillRedBarrels(Toggle):
    """placeholdder"""
    display_name = "Booster Hill Red Barrels"

class BowserDoorShuffle(Toggle):
    """placeholdder"""
    display_name = "Shuffle Bowser's Keep Doors"

class SkipMinecart(Toggle):
    """placeholdder"""
    display_name = "Skip Minecart"

class RandomMinecartTrack(Toggle):
    """placeholdder"""
    display_name = "Shuffle Ball Solitaire"

class SkipShoguns(Toggle):
    """placeholder"""
    display_name = "Skip Land's End Shoguns"

class BetterEventRNG(Toggle):
    """placeholdder"""
    display_name = "Better Event RNG"

# Shops

class ShuffleShops(Toggle):
    """placeholder"""
    display_name = "Shuffle Shops"

class ShopQuality(Choice):
    """placeholder"""
    option_vanilla = 0
    option_full_random = 1
    option_mostly_random = 2
    option_all = 3
    option_empty = 4
    default = 0
    display_name = "Shop Quality"

class BiasShopShuffle(Toggle):
    """placeholder"""
    display_name = "Bias Shop Shuffle"

class NoPickMeUps(Toggle):
    """placeholder"""
    display_name = "No Pick Me Ups"

class ShowEquips(Toggle):
    """placeholder"""
    display_name = "Show Equips"

class FreeShops(Toggle):
    """placeholder"""
    display_name = "Free Shops"

class ProtectSpecialItems(OptionSet):
    """placeholder"""
    valid_keys = ["Lucky Jewel", "See Ya", "EarlierTimes", "Goodie Bag", "Progressive Eggs", "Star Egg"]
    default = valid_keys
    display_name = "Protect Special Items"

# Enemies and Bosses

class BossShuffle(Toggle):
    """placeholder"""
    display_name = "Boss Shuffle"

class BossScaleOptions(Choice):
    """placeholder"""
    option_vanilla = 0
    option_match_area = 1
    option_fully_random = 2
    option_godmode = 3
    default = 1
    display_name = "Boss Scaling"

class PostBossAutoHeal(Choice):
    """placeholder"""
    option_all = 0
    option_vanilla = 1
    option_none = 2
    default = 1
    display_name = "Boss Shuffle"

class KeepMiniBossSpritesIntact(Toggle):
    """placeholder"""
    display_name = "Keep Mini Boss Sprites Intact"

class DifferentiateRepeatedBosses(Toggle):
    """placeholder"""
    display_name = "Differentiate Repeated Bosses"

class RandomizeEnemyStats(Choice):
    """placeholder"""
    option_disabled = 0
    option_numbers_only = 1
    option_full_random = 2
    default = 0
    display_name = "Randomize Enemy Stats"

class RandomizeEnemyDrops(Toggle):
    """placeholder"""
    display_name = "Randomize Enemy Drops"

class RandomizeEnemyFormations(Toggle):
    """placeholder"""
    display_name = "Randomize Enemy Formations"

class RandomizeEnemySpells(Toggle):
    """placeholder"""
    display_name = "Randomize Enemy Spells"

class NoRegularEnemyEXP(Toggle):
    """placeholder"""
    display_name = "No Regular Enemy EXP"

class NoBossEXP(Toggle):
    """placeholder"""
    display_name = "No Boss EXP"

class Punchinello2BobombDifficulty(Choice):
    """placeholder"""
    option_zero_percent = 0
    option_twenty_five_percent = 1
    option_fifty_percent = 2
    option_seventy_five_percent = 3
    option_hundred_percent = 4
    display_name = "Punchinello 2 Bob-omb Difficulty"

class SkipBossFights(Toggle):
    """placeholder"""
    display_name = "Skip Boss Fights"

class NoGenoWhirlExor(Toggle):
    """placeholder"""
    display_name = "No Geno Whirl Exor"

class FixMagikoopa(Toggle):
    """placeholder"""
    display_name = "Fix Magikoopa"

class FixInvincibility(Toggle):
    """placeholder"""
    display_name = "Fix Invincibility"

class NoOHKOBossAllies(Toggle):
    """placeholder"""
    display_name = "No OHKO Boss Allies"

class StartWithSeeYa(Toggle):
    """placeholder"""
    display_name = "Start With See Ya"

# Cosmetics and Accessibility

class MarioPalette(Choice):
    """placeholder"""
    option_mario = 0
    option_jumpman = 1
    option_fire_mario = 2
    option_luigi = 3
    option_fire_luigi = 4
    option_wario = 5
    option_waluigi = 6
    option_builder = 7
    option_mega_man = 8
    option_grey = 9
    option_zombio = 10
    option_sponge = 11
    option_pretzel = 12
    option_marlon = 13
    option_grand_dad = 14
    option_blue_two = 15
    option_kris = 16
    display_name = "Mario Palette"

class MallowPalette(Choice):
    """placeholder"""
    option_mallow = 0
    option_mokura = 1
    option_frog = 2
    option_palom = 3
    option_porom = 4
    option_cloud = 5
    option_stormy = 6
    option_light = 7
    option_water = 8
    option_red = 9
    option_mint = 10
    option_demon = 11
    option_rain_cloud = 12
    display_name = "Mallow Palette"

class GenoPalette(Choice):
    """placeholder"""
    option_geno = 0
    option_millnium = 1
    option_magikoopa = 2
    option_magikoopa_red = 3
    option_link = 4
    option_vlador = 5
    option_light = 6
    option_purple = 7
    option_grey = 8
    option_green = 9
    option_dark = 10
    option_ralsei = 11
    display_name = "Geno Palette"

class BowserPalette(Choice):
    """placeholder"""
    option_bowser = 0
    option_dry_bones = 1
    option_culex = 2
    option_wabowser = 3
    option_red = 4
    option_dark = 5
    option_korush = 6
    option_zeccet = 7
    option_melee_blue = 8
    option_s_king = 9
    option_susie = 10
    display_name = "Bowser Palette"

class ToadstoolPalette(Choice):
    """placeholder"""
    option_toadstool = 0
    option_daisy = 1
    option_pauline = 2
    option_rosalina = 3
    option_palutena = 4
    option_kumatora = 5
    option_tia = 6
    option_kairi = 7
    option_leena = 8
    option_esmeralda = 9
    option_miku = 10
    option_jasmine = 11
    option_kotori = 12
    option_zombie = 13
    option_blood_peach = 14
    option_demon = 15
    option_red = 16
    option_green = 17
    option_blue = 18
    option_black = 19
    option_indigo = 20
    option_shadow_queen = 21
    display_name = "Toadstool Palette"

class ChangeNamesToMatchPalettes(Toggle):
    """placeholder"""
    display_name = "Change Names to Match Palette"

class UseRemakeNames(Toggle):
    """placeholder"""
    display_name = "Use Remake Names"

class UseCanonNames(Toggle):
    """placeholder"""
    display_name = "Use Canon Names"

class RenameToadstoolToPeach(Toggle):
    """placeholder"""
    display_name = "Rename Toadstool To Peach"

class JapaneseABXYButtons(Toggle):
    """placeholder"""
    display_name = "Japanese ABXY Buttons"

class RandomizeBattleMusic(Toggle):
    """placeholder"""
    display_name = "Change Names to Match Palette"

class BattleMusicOptions(OptionSet):
    """placeholder"""
    valid_keys = [
        "Fight Against Monsters",
        "Fight Against Stronger Monsters",
        "Fight Against An Armed Boss",
        "Fight Against Smithy 1",
        "Mountain Railroad",
        "Booster Hill",
        "Barrel Volcano",
        "Fight Against Culex"
    ]
    default = valid_keys
    display_name = "Battle Music Options"

class RemoveFlashes(Toggle):
    """placeholder"""
    display_name = "Remove Flashes"

class HoldBToAdvanceText(Toggle):
    """placeholder"""
    display_name = "Hold B To Advance Text"

@dataclass
class SMRPGOptions(PerGameCommonOptions):
    shuffle_characters: ShuffleCharacters
    max_characters: MaxCharacters
    allow_early_ally_switching: AllowEarlyAllySwitching
    starting_character_count: StartingCharacterCount
    lead_character: LeadCharacter
    mario_placement: MarioPlacement
    mallow_placement: MallowPlacement
    geno_placement: GenoPlacement
    bowser_placement: BowserPlacement
    toadstool_placement: ToadstoolPlacement
    play_as_lead_character: PlayAsLeadCharacter
    equipment_permissions: EquipmentPermissions
    equipment_properties: EquipmentProperties
    ignore_namesake_properties: IgnoreNamesakeProperties
    star_piece_hints: StarPieceHints
    exp_multiplier: EXPMultiplier
    randomize_character_stats: RandomizeCharacterStats
    randomize_learned_spells: RandomizeLearnedSpells
    randomize_spell_stats: RandomizeSpellStats
    infuse_elements: InfuseElements
    randomize_spell_elements: RandomizeSpellElements
    uncap_super_jumps: UncapSuperJumps
    uncap_max_fp: UncapMaxFP
    available_spells: AvailableSpells
    shuffle_star_pieces: ShuffleStarPieces
    total_star_pieces: TotalStarPieces
    progression_logic_difficulty: ProgressionLogicDifficulty
    disperse_star_pieces: DisperseStarPieces
    shuffle_items: ShuffleItems
    item_pool_quality: ItemPoolQuality
    bias_item_shuffle: BiasItemShuffle
    annoying_chests: AnnoyingChests
    no_star_egg: NoStarEgg
    restrict_special_equips: RestrictSpecialEquips
    exp_stars_anywhere: EXPStarsAnywhere
    shuffle_booster_hill_flowers: ShuffleBoosterHillFlowers
    shuffle_regular_coins: ShuffleRegularCoins
    mimics_anywhere: MimicsAnywhere
    slots_anywhere: SlotsAnywhere
    shuffle_beetlemania: ShuffleBeetlemania
    shuffle_magikoopa_chest: ShuffleMagikoopaChest
    shuffle_wedding_gear: ShuffleWeddingGear
    shuffle_mario_doll: ShuffleMarioDoll
    shuffle_cookies: ShuffleCookies
    fireworks_trade_sequence: FireworksTradeSequence
    key_items_anywhere: KeyItemsAnywhere
    star_pieces_anywhere: StarPiecesAnywhere
    spells_anywhere: SpellsAnywhere
    invisible_flags_anywhere: InvisibleFlagsAnywhere
    enable_remake_content: EnableRemakeContent
    bandits_way_gate: BanditsWayGate
    kero_sewers_gate: KeroSewersGate
    forest_maze_gate: ForestMazeGate
    pipe_vault_gate: PipeVaultGate
    moleville_gate: MolevilleGate
    booster_tower_gate: BoosterTowerGate
    booster_hill_gate: BoosterHillGate
    marrymore_gate: MarrymoreGate
    yaridovich_gate: YaridovichGate
    sea_gate: SeaGate
    lands_end_gate: LandsEndGate
    belome_temple_gate: BelomeTempleGate
    monstro_town_gate: MonstroTownGate
    skip_musty_fears_sequence: SkipMustyFearsSequence
    nimbus_land_gate: NimbusLandGate
    barrel_volcano_gate: BarrelVolcanoGate
    bowsers_keep_gate: BowsersKeepGate
    factory_gate: FactoryGate
    replace_worst_items: ReplaceWorstItems
    randomize_poison_mushroom_effect: RandomizePoisonMushroomEffect
    exp_star_behavior: EXPStarBehavior
    look_the_other_way_threshold: LookTheOtherWayThreshold
    knife_guy_threshold: KnifeGuyThreshold
    suite_prize_1_threshold: SuitePrize1Threshold
    suite_prize_2_threshold: SuitePrize2Threshold
    suite_prize_3_threshold: SuitePrize3Threshold
    suite_prize_4_threshold: SuitePrize4Threshold
    suite_prize_5_threshold: SuitePrize5Threshold
    suite_prize_6_threshold: SuitePrize6Threshold
    super_jump_prize_1_threshold: SuperJumpPrize1Threshold
    fix_knife_guy: FixKnifeGuy
    knife_guy_fixed_prize_threshold: KnifeGuyFixedPrizeThreshold
    bowser_door_requirements: BowserDoorRequirements
    star_pieces_required: StarPiecesRequired
    casino_warp: CasinoWarp
    bucket_warp: BucketWarp
    fast_travel: FastTravel
    win_condition: WinCondition
    shuffle_ball_solitaire: ShuffleBallSolitaire
    shuffle_magic_buttons: ShuffleMagicButtons
    shuffle_quiz_questions: ShuffleQuizQuestions
    include_non_smrpg_questions: IncludeNonSMRPGQuestions
    randomize_tadpole_pond_song: RandomizeTadpolePondSong
    randomize_sunken_ship_password: RandomizeSunkenShipPassword
    booster_hill_red_barrels: BoosterHillRedBarrels
    bowser_door_shuffle: BowserDoorShuffle
    skip_minecart: SkipMinecart
    random_minecart_track: RandomMinecartTrack
    skip_shoguns: SkipShoguns
    better_event_rng: BetterEventRNG
    shuffle_shops: ShuffleShops
    shop_quality: ShopQuality
    bias_shop_shuffle: BiasShopShuffle
    no_pick_me_ups: NoPickMeUps
    show_equips: ShowEquips
    free_shops: FreeShops
    protect_special_items: ProtectSpecialItems
    boss_shuffle: BossShuffle
    boss_scale_options: BossScaleOptions
    post_boss_auto_heal: PostBossAutoHeal
    keep_mini_boss_sprites_intact: KeepMiniBossSpritesIntact
    differentiate_repeated_bosses: DifferentiateRepeatedBosses
    randomize_enemy_stats: RandomizeEnemyStats
    randomize_enemy_drops: RandomizeEnemyDrops
    randomize_enemy_formations: RandomizeEnemyFormations
    randomize_enemy_spells: RandomizeEnemySpells
    no_regular_enemy_exp: NoRegularEnemyEXP
    no_boss_exp: NoBossEXP
    punchinello_2_bobomb_difficulty: Punchinello2BobombDifficulty
    skip_boss_fights: SkipBossFights
    no_geno_whirl_exor: NoGenoWhirlExor
    fix_magikoopa: FixMagikoopa
    fix_invincibility: FixInvincibility
    no_ohko_boss_allies: NoOHKOBossAllies
    start_with_see_ya: StartWithSeeYa
    mario_palette: MarioPalette
    mallow_palette: MallowPalette
    geno_palette: GenoPalette
    bowser_palette: BowserPalette
    toadstool_palette: ToadstoolPalette
    change_names_to_match_palettes: ChangeNamesToMatchPalettes
    use_remake_names: UseRemakeNames
    use_canon_names: UseCanonNames
    rename_toadstool_to_peach: RenameToadstoolToPeach
    japanese_abxy_buttons: JapaneseABXYButtons
    randomize_battle_music: RandomizeBattleMusic
    battle_music_options: BattleMusicOptions
    remove_flashes: RemoveFlashes
    hold_b_to_advance_text: HoldBToAdvanceText

