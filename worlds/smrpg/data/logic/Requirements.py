from .Requirement import Requirement, BossesRequirement
from .RequirementItems import *
from ...Options import SMRPGOptions

all_characters = [Mario, Mallow, Geno, Bowser, Toadstool]

class HasMario(Requirement):
    items_needed = [Mario]

class HasMallow(Requirement):
    items_needed = [Mallow]

class HasGeno(Requirement):
    items_needed = [Geno]

class HasBowser(Requirement):
    items_needed = [Bowser]

class HasToadstool(Requirement):
    items_needed = [Toadstool]

class HasAnyCharacter(Requirement):
    other_requirements_or = [HasMario, HasMallow, HasGeno, HasBowser, HasToadstool]

class HasAllFireworks(Requirement):
    items_needed = [Fireworks, ShinyStone, CarboCookie]

class HasBrightCard(Requirement):
    items_needed = [BrightCard]

class HasCricketPie(Requirement):
    items_needed = [CricketPie]

class HasCricketPieAndJam(Requirement):
    items_needed = [CricketPie, CricketJam]

class HasRaceCookies(Requirement):
    items_needed = [RaceCookies]

class HasElderKey(Requirement):
    items_needed = [ElderKey]

class HasRoomKey(Requirement):
    items_needed = [RoomKey]

class HasFourStarPieces(StarPieceRequirement):
    items_needed = [StarPiece]
    count = 4

class HasFiveStarPieces(StarPieceRequirement):
    items_needed = [StarPiece]
    count = 5

class HasSixStarPieces(StarPieceRequirement):
    items_needed = [StarPiece]
    count = 6

class HasVariableStarPieces(StarPieceRequirement):
    items_needed = [StarPiece]

class NotEarlyGame(BossesRequirement):
    items_needed = [BossFights]
    count = 5

class HasDamagingSpells(Requirement):
    items_needed = [DamagingSpells]

class HasMushroomKingdom(Requirement):
    items_needed = [MushroomKingdom]

class HasBanditsWay(Requirement):
    items_needed = [BanditsWay]

class HasForestMaze(Requirement):
    items_needed = [ForestMaze]

class HasMolevilleMines(Requirement):
    items_needed = [MolevilleMines]

class HasBelomeTemple(Requirement):
    items_needed = [BelomeTemple]

class HasBoosterTower(Requirement):
    items_needed = [BoosterTower]

class HasSeasideTown(Requirement):
    items_needed = [SeasideTown]

class HasMallowForBanditsWay(Requirement):
    items_needed = [Mallow]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.bandits_way_gate == options.bandits_way_gate.option_mallow

class HasHammerBrosForBanditsWay(Requirement):
    items_needed = [HammerBros]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.bandits_way_gate == options.bandits_way_gate.option_hammer_bros

class HasMushroomWayForBanditsWay(Requirement):
    items_needed = [MushroomWay]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.bandits_way_gate == options.bandits_way_gate.option_mushroom_way

class BanditsWayOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.bandits_way_gate == options.bandits_way_gate.option_open

class CanAccessBanditsWay(Requirement):
    other_requirements_or = [
        HasMallowForBanditsWay, HasHammerBrosForBanditsWay,
        HasMushroomWayForBanditsWay, BanditsWayOpen
    ]

class HasMallowForKeroSewers(Requirement):
    items_needed = [Mallow]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.kero_sewers_gate == options.kero_sewers_gate.option_mallow

class HasMackForKeroSewers(Requirement):
    items_needed = [Mack]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.kero_sewers_gate == options.kero_sewers_gate.option_mack

class HasMushroomKingdomForKeroSewers(Requirement):
    items_needed = [MushroomKingdom]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.kero_sewers_gate == options.kero_sewers_gate.option_mushroom_kingdom

class HasRareFrogCoinForKeroSewers(Requirement):
    items_needed = [RareFrogCoin]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.kero_sewers_gate == options.kero_sewers_gate.option_rare_frog_coin

class KeroSewersOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.kero_sewers_gate == options.kero_sewers_gate.option_open

# Kero Sewers can also be accessed from Land's End, so it's defined below

class HasCricketPieForForestMaze(Requirement):
    items_needed = [CricketPie]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.forest_maze_gate == options.forest_maze_gate.option_cricket_pie

class ForestMazeOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.forest_maze_gate == options.forest_maze_gate.option_open

class CanAccessForestMaze(Requirement):
    other_requirements_or = [HasCricketPieForForestMaze, ForestMazeOpen]

class CanAccessGardener(Requirement):
    items_needed = [ForestMaze, MolevilleMines]

class CanAccessGardenerChests(Requirement):
    items_needed = [Seed, Fertilizer]
    other_requirements_and = [CanAccessGardener]

class HasGenoForPipeVaultAccess(Requirement):
    items_needed = [Geno]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.pipe_vault_gate == options.pipe_vault_gate.option_geno

class HasBowyerForPipeVaultAccess(Requirement):
    items_needed = [Bowyer]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.pipe_vault_gate == options.pipe_vault_gate.option_bowyer

class HasForestMazeForPipeVaultAccess(Requirement):
    items_needed = [ForestMaze]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.pipe_vault_gate == options.pipe_vault_gate.option_forest_maze

class PipeVaultOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.pipe_vault_gate == options.pipe_vault_gate.option_open

class CanAccessPipeVault(Requirement):
    other_requirements_or = [
        HasGenoForPipeVaultAccess, HasBowyerForPipeVaultAccess,
        HasForestMazeForPipeVaultAccess
    ]

class HasGenoForMolevilleMinesAccess(Requirement):
    items_needed = [Geno]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.moleville_gate == options.moleville_gate.option_geno

class HasForestMazeForMolevilleMinesAccess(Requirement):
    items_needed = [ForestMaze]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.moleville_gate == options.moleville_gate.option_forest_maze

class HasBowyerForMolevilleMinesAccess(Requirement):
    items_needed = [Bowyer]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.moleville_gate == options.moleville_gate.option_bowyer

class HasBoshiForMolevilleMinesAccess(Requirement):
    items_needed = [Boshi]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.moleville_gate == options.moleville_gate.option_boshi

class MolevilleMinesOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.moleville_gate == options.moleville_gate.option_open

class CanAccessMolevilleMines(Requirement):
    other_requirements_or = [
        HasGenoForMolevilleMinesAccess, HasBowyerForMolevilleMinesAccess,
        HasForestMazeForMolevilleMinesAccess, HasBoshiForMolevilleMinesAccess,
        MolevilleMinesOpen
    ]

class CanAccessInnerMolevilleMines(Requirement):
    items_needed = [BambinoBomb]
    other_requirements_or = [CanAccessMolevilleMines]

class PostgameMolevilleAccess(Requirement):
    items_needed = [BambinoBomb, StayVoucher, MolevilleMines]
    other_requirements_and = [NotEarlyGame]

class CanAccessTreasureSeller1(Requirement):
    items_needed = [MolevilleMines]

class CanAccessTreasureSeller2(Requirement):
    items_needed = [SunkenShip]
    other_requirements_or = [CanAccessTreasureSeller1]

class CanAccessTreasureSeller3(Requirement):
    items_needed = [BarrelVolcano]
    other_requirements_or = [CanAccessTreasureSeller1]

class HasMarioForBoosterTowerAccess(Requirement):
    items_needed = [Mario]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_tower_gate == options.booster_tower_gate.option_mario

class HasMallowForBoosterTowerAccess(Requirement):
    items_needed = [Mallow]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_tower_gate == options.booster_tower_gate.option_mallow

class HasGenoForBoosterTowerAccess(Requirement):
    items_needed = [Geno]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_tower_gate == options.booster_tower_gate.option_geno

class HasBowserForBoosterTowerAccess(Requirement):
    items_needed = [Bowser]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_tower_gate == options.booster_tower_gate.option_bowser

class HasToadstoolForBoosterTowerAccess(Requirement):
    items_needed = [Toadstool]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_tower_gate == options.booster_tower_gate.option_toadstool

class HasMolevilleMinesForBoosterTowerAccess(Requirement):
    items_needed = [MolevilleMines]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_tower_gate == options.booster_tower_gate.option_moleville_mines

class HasPunchinelloForBoosterTowerAccess(Requirement):
    items_needed = [Punchinello1]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_tower_gate == options.booster_tower_gate.option_punchinello

class BoosterTowerOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_tower_gate == options.booster_tower_gate.option_open

class CanAccessBoosterTower(Requirement):
    other_requirements_or = [
        HasMarioForBoosterTowerAccess, HasMallowForBoosterTowerAccess, HasGenoForBoosterTowerAccess,
        HasBowserForBoosterTowerAccess, HasToadstoolForBoosterTowerAccess, HasMolevilleMinesForBoosterTowerAccess,
        HasPunchinelloForBoosterTowerAccess, BoosterTowerOpen
    ]

class HasMarioDollForCurtainAccess(Requirement):
    items_needed = [MarioDoll]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.shuffle_mario_doll == options.shuffle_mario_doll.option_true

class CurtainOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.shuffle_mario_doll == options.shuffle_mario_doll.option_false

class CanAccessCurtain(Requirement):
    other_requirements_or = [HasMarioDollForCurtainAccess, CurtainOpen]
    other_requirements_and = [NotEarlyGame]

class PostgameCurtainAccess(Requirement):
    items_needed = [StayVoucher, BoosterTower]
    other_requirements_and = [NotEarlyGame]

class HasBoosterTowerForBoosterHill(Requirement):
    items_needed = [BoosterTower]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_hill_gate == options.booster_hill_gate.option_booster_tower

class HasKnifeGuyCrateGuyForBoosterHill(Requirement):
    items_needed = [KnifeGuyCrateGuy]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_hill_gate == options.booster_hill_gate.option_knife_guy_crate_guy

class BoosterHillOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.booster_hill_gate == options.booster_hill_gate.option_open

class CanAccessBoosterHill(Requirement):
    other_requirements_or = [
        HasBoosterTowerForBoosterHill, HasKnifeGuyCrateGuyForBoosterHill, BoosterHillOpen
    ]

class HasBoosterTowerForMarrymore(Requirement):
    items_needed = [BoosterTower]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.marrymore_gate == options.marrymore_gate.option_booster_tower

class HasKnifeGuyCrateGuyForMarrymore(Requirement):
    items_needed = [KnifeGuyCrateGuy]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.marrymore_gate == options.marrymore_gate.option_knife_guy_crate_guy

class HasBoosterHillForMarrymore(Requirement):
    items_needed = [BoosterHill]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.marrymore_gate == options.marrymore_gate.option_booster_hill

class MarrymoreOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.marrymore_gate == options.marrymore_gate.option_open

class CanAccessMarrymoreChapel(Requirement):
    other_requirements_or = [
        HasBoosterTowerForMarrymore, HasKnifeGuyCrateGuyForMarrymore,
        HasBoosterHillForMarrymore, MarrymoreOpen
    ]

class CanAccessMarrymoreBoss(Requirement):
    items_needed = [member for member in WeddingGear.members]
    other_requirements_and = [CanAccessMarrymoreChapel, NotEarlyGame]

class PostgameMarrymoreAccess(Requirement):
    items_needed = [StayVoucher, Marrymore]
    other_requirements_and = [NotEarlyGame]

class HasToadstoolForSeaAccess(Requirement):
    items_needed = [Toadstool]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.sea_gate == options.sea_gate.option_toadstool

class HasMarrymoreForSeaAccess(Requirement):
    items_needed = [Marrymore]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.sea_gate == options.sea_gate.option_marrymore

class HasBundtForSeaAccess(Requirement):
    items_needed = [Bundt1]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.sea_gate == options.sea_gate.option_bundt

class HasFourStarPiecesForSeaAccess(Requirement):
    other_requirements_or = [HasFourStarPieces]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.sea_gate == options.sea_gate.option_four_star_pieces

class SeaOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.sea_gate == options.sea_gate.option_open

class CanAccessSea(Requirement):
    other_requirements_or = [
        HasToadstoolForSeaAccess, HasMarrymoreForSeaAccess,
        HasBundtForSeaAccess, HasFourStarPiecesForSeaAccess, SeaOpen
    ]

class CanClearSunkenShip(Requirement):
    other_requirements_and = [CanAccessSea, NotEarlyGame]

class PostgameSunkenShipAccess(Requirement):
    items_needed = [StayVoucher, SunkenShip]
    other_requirements_and = [NotEarlyGame]

class HasSunkenShipForSeasideBossAccess(Requirement):
    items_needed = [SunkenShip]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.yaridovich_gate == options.yaridovich_gate.option_sunken_ship

class HasJohnnyForSeasideBossAccess(Requirement):
    items_needed = [Johnny1]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.yaridovich_gate == options.yaridovich_gate.option_johnny

class SeasideBossOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.yaridovich_gate == options.yaridovich_gate.option_open

class CanAccessSeasideBoss(Requirement):
    other_requirements_or = [
        HasSunkenShipForSeasideBossAccess, HasJohnnyForSeasideBossAccess, SeasideBossOpen
    ]

    other_requirements_and = [NotEarlyGame]

class HasFiveStarPiecesForLandsEnd(Requirement):
    other_requirements_or = [HasFiveStarPieces]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.lands_end_gate == options.lands_end_gate.option_five_star_pieces

class HasYaridovichForLandsEnd(Requirement):
    items_needed = [Yaridovich]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.lands_end_gate == options.lands_end_gate.option_yaridovich

class HasSeasideTownForLandsEnd(Requirement):
    items_needed = [SeasideTown]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.lands_end_gate == options.lands_end_gate.option_seaside_town

class HasSeasideElderForLandsEnd(Requirement):
    items_needed = [ShedKey, SeasideTown]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.lands_end_gate == options.lands_end_gate.option_elder

class LandsEndOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.lands_end_gate == options.lands_end_gate.option_open

class CanAccessLandsEnd(Requirement):
    other_requirements_or = [
        HasYaridovichForLandsEnd, HasSeasideTownForLandsEnd,
        HasSeasideElderForLandsEnd, HasFiveStarPiecesForLandsEnd,
        LandsEndOpen
    ]

class CanAccessKeroSewers(Requirement):
    other_requirements_or = [
        HasMallowForKeroSewers, HasMackForKeroSewers, HasMushroomKingdomForKeroSewers,
        HasRareFrogCoinForKeroSewers, KeroSewersOpen, CanAccessLandsEnd
    ]

class HasTempleKey(Requirement):
    items_needed = [TempleKey]

class HasTempleKeyForTempleBossAccess(Requirement):
    items_needed = [TempleKey]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.belome_temple_gate == options.belome_temple_gate.option_key

class TempleBossOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.belome_temple_gate == options.belome_temple_gate.option_open

class CanAccessTempleBoss(Requirement):
    other_requirements_or = [HasTempleKeyForTempleBossAccess, TempleBossOpen]
    other_requirements_and = [NotEarlyGame, CanAccessLandsEnd]

class PostgameTempleBossAccess(Requirement):
    items_needed = [StayVoucher, BelomeTemple]
    other_requirements_and = [NotEarlyGame]

class HasLandsEndForMonstroTown(Requirement):
    other_requirements_and = [NotEarlyGame, CanAccessTempleBoss]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.monstro_town_gate == options.monstro_town_gate.option_lands_end

class HasBelome2ForMonstroTown(Requirement):
    items_needed = [Belome2]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.monstro_town_gate == options.monstro_town_gate.option_belome_2

class MonstroTownOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.monstro_town_gate == options.monstro_town_gate.option_open

class CanAccessMonstroTown(Requirement):
    other_requirements_or = [
        HasLandsEndForMonstroTown, HasBelome2ForMonstroTown, MonstroTownOpen
    ]

class PostgameDojoBossAccess(Requirement):
    items_needed = [StayVoucher, Dojo]
    other_requirements_and = [NotEarlyGame]

class HasBeanValleyForNimbusLand(Requirement):
    items_needed = [BeanValley]
    other_requirements_and = [NotEarlyGame]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.nimbus_land_gate == options.nimbus_land_gate.option_bean_valley

class HasMegasmilaxForNimbusLand(Requirement):
    items_needed = [Megasmilax]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.nimbus_land_gate == options.nimbus_land_gate.option_megasmilax

class NimbusLandOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return (options.nimbus_land_gate == options.nimbus_land_gate.option_open
                or options.nimbus_land_gate == options.nimbus_land_gate.option_gold_paint)

class CanAccessNimbusLand(Requirement):
    other_requirements_or = [
        HasBeanValleyForNimbusLand, HasMegasmilaxForNimbusLand, NimbusLandOpen
    ]

class HasGoldPaintForNimbusCastleAccess(Requirement):
    items_needed = [GoldPaint]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.nimbus_land_gate == options.nimbus_land_gate.option_gold_paint

class NimbusCastleOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.nimbus_land_gate == options.nimbus_land_gate.option_open


class CanAccessNimbusCastle(Requirement):
    other_requirements_or = [HasGoldPaintForNimbusCastleAccess, NimbusCastleOpen]
    other_requirements_and = [CanAccessNimbusLand]

class CanAccessInnerNimbus(Requirement):
    items_needed = [CastleKey1]
    other_requirements_and = [CanAccessNimbusCastle]

class CanAccessInnerNimbusBoss(Requirement):
    other_requirements_and = [CanAccessInnerNimbus, NotEarlyGame]

class CanAccessLateNimbus(Requirement):
    items_needed = [CastleKey2]
    other_requirements_and = [CanAccessInnerNimbus]

class CanClearNimbusBoss(Requirement):
    other_requirements_and = [CanAccessLateNimbus, NotEarlyGame]

class HasNimbusLandForBarrelVolcano(Requirement):
    items_needed = [NimbusLand]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.barrel_volcano_gate == options.barrel_volcano_gate.option_nimbus_land

class HasValentinaForBarrelVolcano(Requirement):
    items_needed = [Valentina]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.barrel_volcano_gate == options.barrel_volcano_gate.option_valentina

class BarrelVolcanoOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.barrel_volcano_gate == options.barrel_volcano_gate.option_open

class CanAccessBarrelVolcano(Requirement):
    other_requirements_or = [
        HasNimbusLandForBarrelVolcano, HasValentinaForBarrelVolcano, BarrelVolcanoOpen
    ]

class CanClearBarrelVolcano(Requirement):
    other_requirements_and = [CanAccessBarrelVolcano, NotEarlyGame]

class HasBarrelVolcanoForBowsersKeep(Requirement):
    items_needed = [BarrelVolcano]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.bowsers_keep_gate == options.bowsers_keep_gate.option_barrel_volcano

class HasAxemRangerForBowsersKeep(Requirement):
    items_needed = [AxemRangers]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.bowsers_keep_gate == options.bowsers_keep_gate.option_axem_rangers

class HasSixStarPiecesForBowsersKeep(Requirement):
    other_requirements_or = [HasSixStarPieces]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.bowsers_keep_gate == options.bowsers_keep_gate.option_six_star_pieces

class BowsersKeepOpen(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.bowsers_keep_gate == options.bowsers_keep_gate.option_open

class CanAccessBowsersKeep(Requirement):
    other_requirements_or = [
        HasBarrelVolcanoForBowsersKeep, HasAxemRangerForBowsersKeep,
        HasSixStarPiecesForBowsersKeep, BowsersKeepOpen
    ]

class CanClearBowsersKeep(Requirement):
    other_requirements_and = [CanAccessBowsersKeep, HasDamagingSpells, NotEarlyGame]

class HasSixStarPiecesForFactory(Requirement):
    other_requirements_or = [HasSixStarPieces]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.factory_gate == options.factory_gate.option_six_star_pieces

class HasExorForFactory(Requirement):
    items_needed = [Exor]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.factory_gate == options.factory_gate.option_exor

class HasBowsersKeepForFactory(Requirement):
    items_needed = [BowsersKeep]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.factory_gate == options.factory_gate.option_finish_bowsers_keep

class FactoryOpen(Requirement):
    other_requirements_or = [CanAccessBowsersKeep]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.factory_gate == options.factory_gate.option_open_with_bowsers_keep

class CanAccessFactory(Requirement):
    other_requirements_or = [
        HasSixStarPiecesForFactory, HasBowsersKeepForFactory,
        HasExorForFactory, FactoryOpen
    ]

class HasNonProgressiveFireworksForFinalBoss(Requirement):
    items_needed = [Fireworks]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.fireworks_trade_sequence == options.fireworks_trade_sequence.option_shuffle_one

class HasProgressiveFireworksForFinalBoss(Requirement):
    other_requirements_or = [HasAllFireworks]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.fireworks_trade_sequence == options.fireworks_trade_sequence.option_progressive

class HasNonShuffledFireworksForFinalBoss(Requirement):
    other_requirements_or = [HasAnyCharacter]

    @staticmethod
    def check_option_enabled(options: "SMRPGOptions") -> bool:
        return options.fireworks_trade_sequence == options.fireworks_trade_sequence.option_vanilla

class HasFireworksForFinalBoss(Requirement):
    other_requirements_or = [
        HasNonProgressiveFireworksForFinalBoss, HasProgressiveFireworksForFinalBoss,
        HasNonShuffledFireworksForFinalBoss
    ]

class CanAccessFinalBossSlot(Requirement):
    other_requirements_and = [NotEarlyGame, HasVariableStarPieces]
    other_requirements_or = [CanAccessFactory, HasFireworksForFinalBoss, HasBrightCard]

class CanAccessSealedDoorBoss(Requirement):
    items_needed = [ShinyStone]
    other_requirements_and = [CanAccessMonstroTown, NotEarlyGame]

class PostgameSealedDoorBoss(Requirement):
    items_needed = [SealedDoor, StayVoucher, ExtraShinyStone]
    other_requirements_and = [NotEarlyGame]