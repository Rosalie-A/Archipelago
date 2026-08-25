from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import Has, Or, And, HasAll
from .Requirement import Requirement, BossesRequirement, LocationClearRequirement, OpenRequirement, SpellsRequirement
from .RequirementItems import *
from ...Options import SMRPGOptions, BanditsWayGate, KeroSewersGate, ForestMazeGate, PipeVaultGate, MolevilleGate, \
    BoosterTowerGate, ShuffleMarioDoll, BoosterHillGate, MarrymoreGate, SeaGate, YaridovichGate, LandsEndGate, \
    BelomeTempleGate, MonstroTownGate, NimbusLandGate, BarrelVolcanoGate, BowsersKeepGate, FactoryGate, \
    FireworksTradeSequence, StarPiecesRequired

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

class Open(OpenRequirement):
    pass

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

class HasDamagingSpells(SpellsRequirement):
    items_needed = [DamagingSpells]

class HasMushroomKingdom(LocationClearRequirement):
    items_needed = [MushroomKingdom]

class HasBanditsWay(LocationClearRequirement):
    items_needed = [BanditsWay]

class HasForestMaze(LocationClearRequirement):
    items_needed = [ForestMaze]

class HasMolevilleMines(LocationClearRequirement):
    items_needed = [MolevilleMines]

class HasBelomeTemple(LocationClearRequirement):
    items_needed = [BelomeTemple]

class HasBoosterTower(LocationClearRequirement):
    items_needed = [BoosterTower]

class HasSeasideTown(LocationClearRequirement):
    items_needed = [SeasideTown]

class HasMallowForBanditsWay(Requirement):
    items_needed = [Mallow]
    option_filter = OptionFilter(BanditsWayGate, BanditsWayGate.option_mallow)

class HasHammerBrosForBanditsWay(Requirement):
    items_needed = [HammerBros]
    option_filter = OptionFilter(BanditsWayGate, BanditsWayGate.option_hammer_bros)

class HasMushroomWayForBanditsWay(LocationClearRequirement):
    items_needed = [MushroomWay]
    option_filter = OptionFilter(BanditsWayGate, BanditsWayGate.option_mushroom_way)

class BanditsWayOpen(Requirement):
    option_filter = OptionFilter(BanditsWayGate, BanditsWayGate.option_open)

class CanAccessBanditsWay(Requirement):
    rule = Or(
        HasMallowForBanditsWay.get_rule(),
        HasHammerBrosForBanditsWay.get_rule(),
        HasMushroomWayForBanditsWay.get_rule(),
        BanditsWayOpen.get_rule()
    )

class HasMallowForKeroSewers(Requirement):
    items_needed = [Mallow]
    option_filter = OptionFilter(KeroSewersGate, KeroSewersGate.option_mallow)

class HasMackForKeroSewers(Requirement):
    items_needed = [Mack]
    option_filter = OptionFilter(KeroSewersGate, KeroSewersGate.option_mack)

class HasMushroomKingdomForKeroSewers(LocationClearRequirement):
    items_needed = [MushroomKingdom]
    option_filter = OptionFilter(KeroSewersGate, KeroSewersGate.option_mushroom_kingdom)

class HasRareFrogCoinForKeroSewers(Requirement):
    items_needed = [RareFrogCoin]
    option_filter = OptionFilter(KeroSewersGate, KeroSewersGate.option_rare_frog_coin)

class KeroSewersOpen(Requirement):
    option_filter = OptionFilter(KeroSewersGate, KeroSewersGate.option_open)

# Kero Sewers can also be accessed from Land's End, so it's defined below

class HasCricketPieForForestMaze(Requirement):
    items_needed = [CricketPie]
    option_filter = OptionFilter(ForestMazeGate, ForestMazeGate.option_cricket_pie)

class ForestMazeOpen(Requirement):
    other_requirements_or = [Open]
    option_filter = OptionFilter(ForestMazeGate, ForestMazeGate.option_open)

class CanAccessForestMaze(Requirement):
    rule = Or(HasCricketPieForForestMaze.get_rule(), ForestMazeOpen.get_rule())

class CanAccessGardener(LocationClearRequirement):
    items_needed = [ForestMaze, MolevilleMines]

class CanAccessGardenerChests(Requirement):
    rule = And(
        HasAll(ItemNames.SEED, ItemNames.FERTILIZER),
        CanAccessGardener.get_rule()
    )

class HasGenoForPipeVaultAccess(Requirement):
    items_needed = [Geno]
    option_filter = OptionFilter(PipeVaultGate, PipeVaultGate.option_geno)

class HasBowyerForPipeVaultAccess(Requirement):
    items_needed = [Bowyer]
    option_filter = OptionFilter(PipeVaultGate, PipeVaultGate.option_bowyer)

class HasForestMazeForPipeVaultAccess(LocationClearRequirement):
    items_needed = [ForestMaze]
    option_filter = OptionFilter(PipeVaultGate, PipeVaultGate.option_forest_maze)

class PipeVaultOpen(Requirement):
    option_filter = OptionFilter(PipeVaultGate, PipeVaultGate.option_open)

class CanAccessPipeVault(Requirement):
    rule = Or(
        HasGenoForPipeVaultAccess.get_rule(),
        HasBowyerForPipeVaultAccess.get_rule(),
        HasForestMazeForPipeVaultAccess.get_rule(),
        PipeVaultOpen.get_rule()
    )

class HasGenoForMolevilleMinesAccess(Requirement):
    items_needed = [Geno]
    option_filter = OptionFilter(MolevilleGate, MolevilleGate.option_geno)

class HasForestMazeForMolevilleMinesAccess(LocationClearRequirement):
    items_needed = [ForestMaze]
    option_filter = OptionFilter(MolevilleGate, MolevilleGate.option_forest_maze)

class HasBowyerForMolevilleMinesAccess(Requirement):
    items_needed = [Bowyer]
    option_filter = OptionFilter(MolevilleGate, MolevilleGate.option_bowyer)

class HasBoshiForMolevilleMinesAccess(Requirement):
    items_needed = [RaceCookies]
    option_filter = OptionFilter(MolevilleGate, MolevilleGate.option_boshi)

class MolevilleMinesOpen(Requirement):
    option_filter = OptionFilter(MolevilleGate, MolevilleGate.option_open)

class CanAccessMolevilleMines(Requirement):
    rule = Or(
        HasGenoForMolevilleMinesAccess.get_rule(),
        HasBowyerForMolevilleMinesAccess.get_rule(),
        HasForestMazeForMolevilleMinesAccess.get_rule(),
        HasBoshiForMolevilleMinesAccess.get_rule(),
        MolevilleMinesOpen.get_rule()
    )

class CanAccessInnerMolevilleMines(Requirement):
    rule = And(
        Has(ItemNames.BAMBINO_BOMB),
        CanAccessMolevilleMines.get_rule()
    )

class CanClearMolevilleMines(LocationClearRequirement):
    items_needed = [MolevilleMines]

class PostgameMolevilleAccess(Requirement):
    rule = And(
        Has(ItemNames.STAY_VOUCHER),
        NotEarlyGame.get_rule(),
        CanClearMolevilleMines.get_rule()
    )

class CanAccessTreasureSeller1(LocationClearRequirement):
    items_needed = [MolevilleMines]

class CanClearSunkenShip(LocationClearRequirement):
    items_needed = [SunkenShip]

class CanAccessTreasureSeller2(Requirement):
    rule = And(
        CanClearSunkenShip.get_rule(),
        NotEarlyGame.get_rule(),
        CanAccessTreasureSeller1.get_rule()
    )

class CanClearBarrelVolcano(LocationClearRequirement):
    items_needed = [BarrelVolcano]

class CanAccessTreasureSeller3(Requirement):
    rule = And(
        CanClearBarrelVolcano.get_rule(),
        NotEarlyGame.get_rule(),
        CanAccessTreasureSeller2.get_rule()
    )

class HasMarioForBoosterTowerAccess(Requirement):
    items_needed = [Mario]
    option_filter = OptionFilter(BoosterTowerGate, BoosterTowerGate.option_mario)

class HasMallowForBoosterTowerAccess(Requirement):
    items_needed = [Mallow]
    option_filter = OptionFilter(BoosterTowerGate, BoosterTowerGate.option_mallow)

class HasGenoForBoosterTowerAccess(Requirement):
    items_needed = [Geno]
    option_filter = OptionFilter(BoosterTowerGate, BoosterTowerGate.option_geno)

class HasBowserForBoosterTowerAccess(Requirement):
    items_needed = [Bowser]
    option_filter = OptionFilter(BoosterTowerGate, BoosterTowerGate.option_bowser)

class HasToadstoolForBoosterTowerAccess(Requirement):
    items_needed = [Toadstool]
    option_filter = OptionFilter(BoosterTowerGate, BoosterTowerGate.option_toadstool)

class HasMolevilleMinesForBoosterTowerAccess(LocationClearRequirement):
    items_needed = [MolevilleMines]
    option_filter = OptionFilter(BoosterTowerGate, BoosterTowerGate.option_moleville_mines)

class HasPunchinelloForBoosterTowerAccess(Requirement):
    items_needed = [Punchinello1]
    option_filter = OptionFilter(BoosterTowerGate, BoosterTowerGate.option_punchinello)

class BoosterTowerOpen(Requirement):
    option_filter = OptionFilter(BoosterTowerGate, BoosterTowerGate.option_open)

class CanAccessBoosterTower(Requirement):
    rule = Or(
        HasMarioForBoosterTowerAccess.get_rule(),
        HasMallowForBoosterTowerAccess.get_rule(),
        HasGenoForBoosterTowerAccess.get_rule(),
        HasBowserForBoosterTowerAccess.get_rule(),
        HasToadstoolForBoosterTowerAccess.get_rule(),
        HasMolevilleMinesForBoosterTowerAccess.get_rule(),
        HasPunchinelloForBoosterTowerAccess.get_rule(),
        BoosterTowerOpen.get_rule()
    )

class HasMarioDollForCurtainAccess(Requirement):
    items_needed = [MarioDoll]
    option_filter = OptionFilter(ShuffleMarioDoll, ShuffleMarioDoll.option_true)

class CurtainOpen(Requirement):
    option_filter = OptionFilter(ShuffleMarioDoll, ShuffleMarioDoll.option_false)

class CanAccessCurtain(Requirement):
    rule = And(
        Or(
            HasMarioDollForCurtainAccess.get_rule(),
            CurtainOpen.get_rule()
        ),
        NotEarlyGame.get_rule()
    )

class CanClearBoosterTower(LocationClearRequirement):
    items_needed = [BoosterTower]

class PostgameCurtainAccess(Requirement):
    rule = And(
        Has(ItemNames.STAY_VOUCHER),
        NotEarlyGame.get_rule(),
        CanClearBoosterTower.get_rule()
    )

class HasBoosterTowerForBoosterHill(LocationClearRequirement):
    items_needed = [BoosterTower]
    option_filter = OptionFilter(BoosterHillGate, BoosterHillGate.option_booster_tower)

class HasKnifeGuyCrateGuyForBoosterHill(Requirement):
    items_needed = [KnifeGuyCrateGuy]
    option_filter = OptionFilter(BoosterHillGate, BoosterHillGate.option_knife_guy_crate_guy)

class BoosterHillOpen(Requirement):
    option_filter = OptionFilter(BoosterHillGate, BoosterHillGate.option_open)

class CanAccessBoosterHill(Requirement):
    rule = Or(
        HasBoosterTowerForBoosterHill.get_rule(),
        HasKnifeGuyCrateGuyForBoosterHill.get_rule(),
        BoosterHillOpen.get_rule()
    )

class HasBoosterTowerForMarrymore(LocationClearRequirement):
    items_needed = [BoosterTower]
    option_filter = OptionFilter(MarrymoreGate, MarrymoreGate.option_booster_tower)

class HasKnifeGuyCrateGuyForMarrymore(Requirement):
    items_needed = [KnifeGuyCrateGuy]
    option_filter = OptionFilter(MarrymoreGate, MarrymoreGate.option_knife_guy_crate_guy)

class HasBoosterHillForMarrymore(Requirement):
    rule = CanAccessBoosterHill.get_rule()
    option_filter = OptionFilter(MarrymoreGate, MarrymoreGate.option_booster_hill)

class MarrymoreOpen(Requirement):
    option_filter = OptionFilter(MarrymoreGate, MarrymoreGate.option_open)

class CanAccessMarrymoreChapel(Requirement):
    rule = Or(
        HasBoosterTowerForMarrymore.get_rule(),
        HasKnifeGuyCrateGuyForMarrymore.get_rule(),
        HasBoosterHillForMarrymore.get_rule(),
        MarrymoreOpen.get_rule()
    )

class CanAccessMarrymoreBoss(Requirement):
    rule = And(
        HasAll(*[member.name for member in WeddingGear.members]),
        CanAccessMarrymoreChapel.get_rule(),
        NotEarlyGame.get_rule()
    )

class CanClearMarrymore(LocationClearRequirement):
    items_needed = [Marrymore]

class PostgameMarrymoreAccess(Requirement):
    rule = And(
        Has(ItemNames.STAY_VOUCHER),
        CanClearMarrymore.get_rule(),
        NotEarlyGame.get_rule()
    )

class HasToadstoolForSeaAccess(Requirement):
    items_needed = [Toadstool]
    option_filter = OptionFilter(SeaGate, SeaGate.option_toadstool)

class HasMarrymoreForSeaAccess(LocationClearRequirement):
    items_needed = [Marrymore]
    option_filter = OptionFilter(SeaGate, SeaGate.option_marrymore)

class HasBundtForSeaAccess(Requirement):
    items_needed = [Bundt1]
    option_filter = OptionFilter(SeaGate, SeaGate.option_bundt)

class HasFourStarPiecesForSeaAccess(StarPieceRequirement):
    count = 4
    option_filter = OptionFilter(SeaGate, SeaGate.option_four_star_pieces)

class SeaOpen(Requirement):
    option_filter = OptionFilter(SeaGate, SeaGate.option_open)

class CanAccessSea(Requirement):
    rule = And(
        Or(
            HasToadstoolForSeaAccess.get_rule(),
            HasMarrymoreForSeaAccess.get_rule(),
            HasBundtForSeaAccess.get_rule(),
            HasFourStarPiecesForSeaAccess.get_rule(),
            SeaOpen.get_rule()
        ),
        NotEarlyGame.get_rule()
    )

class PostgameSunkenShipAccess(Requirement):
    rule = And(
        Has(ItemNames.STAY_VOUCHER),
        NotEarlyGame.get_rule(),
        CanClearSunkenShip.get_rule()
    )

class HasSunkenShipForSeasideBossAccess(LocationClearRequirement):
    items_needed = [SunkenShip]
    option_filter = OptionFilter(YaridovichGate, YaridovichGate.option_sunken_ship)

class HasJohnnyForSeasideBossAccess(Requirement):
    items_needed = [Johnny1]
    option_filter = OptionFilter(YaridovichGate, YaridovichGate.option_johnny)

class SeasideBossOpen(Requirement):
    option_filter = OptionFilter(YaridovichGate, YaridovichGate.option_open)

class CanAccessSeasideBoss(Requirement):
    rule = And(
        Or(
            HasSunkenShipForSeasideBossAccess.get_rule(),
            HasJohnnyForSeasideBossAccess.get_rule(),
            SeasideBossOpen.get_rule()
        ),
        NotEarlyGame.get_rule()
    )

class HasFiveStarPiecesForLandsEnd(StarPieceRequirement):
    count = 5
    option_filter = OptionFilter(LandsEndGate, LandsEndGate.option_five_star_pieces)

class HasYaridovichForLandsEnd(Requirement):
    items_needed = [Yaridovich]
    option_filter = OptionFilter(LandsEndGate, LandsEndGate.option_yaridovich)

class CanClearSeasideTown(LocationClearRequirement):
    items_needed = [SeasideTown]

class HasSeasideTownForLandsEnd(LocationClearRequirement):
    items_needed = [SeasideTown]
    option_filter = OptionFilter(LandsEndGate, LandsEndGate.option_seaside_town)

class HasSeasideElder(Requirement):
    rule = And(
        Has(ItemNames.SHED_KEY),
        CanClearSunkenShip.get_rule()
    )

class HasSeasideElderForLandsEnd(Requirement):
    rule = And(
        Has(ItemNames.SHED_KEY),
        CanClearSunkenShip.get_rule()
    )
    option_filter = OptionFilter(LandsEndGate, LandsEndGate.option_elder)

class LandsEndOpen(Requirement):
    option_filter = OptionFilter(LandsEndGate, LandsEndGate.option_open)

class CanAccessLandsEnd(Requirement):
    rule = And(
        Or(
            HasYaridovichForLandsEnd.get_rule(),
            HasSeasideTownForLandsEnd.get_rule(),
            HasSeasideElderForLandsEnd.get_rule(),
            HasFiveStarPiecesForLandsEnd.get_rule(),
            LandsEndOpen.get_rule()
        ),
        NotEarlyGame.get_rule()
    )

class CanAccessKeroSewers(Requirement):
    rule = Or(
        HasMallowForKeroSewers.get_rule(),
        HasMackForKeroSewers.get_rule(),
        HasMushroomKingdomForKeroSewers.get_rule(),
        HasRareFrogCoinForKeroSewers.get_rule(),
        KeroSewersOpen.get_rule(),
        CanAccessLandsEnd.get_rule()
    )

class HasTempleKey(Requirement):
    items_needed = [TempleKey]

class HasTempleKeyForTempleBossAccess(Requirement):
    items_needed = [TempleKey]
    option_filter = OptionFilter(BelomeTempleGate, BelomeTempleGate.option_key)

class TempleBossOpen(Requirement):
    option_filter = OptionFilter(BelomeTempleGate, BelomeTempleGate.option_open)

class CanAccessTempleBoss(Requirement):
    rule = And(
        Or(
            HasTempleKeyForTempleBossAccess.get_rule(),
            TempleBossOpen.get_rule()
        ),
        NotEarlyGame.get_rule(),
        CanAccessLandsEnd.get_rule()
    )

class CanClearBelomeTemple(LocationClearRequirement):
    items_needed = [BelomeTemple]

class PostgameTempleBossAccess(Requirement):
    rule = And(
        Has(ItemNames.STAY_VOUCHER),
        NotEarlyGame.get_rule(),
        CanClearBelomeTemple.get_rule()
    )

class HasLandsEndForMonstroTown(Requirement):
    rule = And(
        NotEarlyGame.get_rule(),
        CanClearBelomeTemple.get_rule()
    )
    option_filter = OptionFilter(MonstroTownGate, MonstroTownGate.option_lands_end)

class HasBelome2ForMonstroTown(Requirement):
    items_needed = [Belome2]
    option_filter = OptionFilter(MonstroTownGate, MonstroTownGate.option_belome_2)

class MonstroTownOpen(Requirement):
    option_filter = OptionFilter(MonstroTownGate, MonstroTownGate.option_open)

class CanAccessMonstroTown(Requirement):
    rule = Or(
        HasLandsEndForMonstroTown.get_rule(),
        HasBelome2ForMonstroTown.get_rule(),
        MonstroTownOpen.get_rule()
    )

class CanClearDojo(LocationClearRequirement):
    items_needed = [Dojo]

class PostgameDojoBossAccess(Requirement):
    rule = And(
        Has(ItemNames.STAY_VOUCHER),
        NotEarlyGame.get_rule(),
        CanClearDojo.get_rule()
    )

class CanClearBeanValley(LocationClearRequirement):
    items_needed = [BeanValley]

class HasBeanValleyForNimbusLand(Requirement):
    rule = And(
        CanClearBeanValley.get_rule(),
        NotEarlyGame.get_rule()
    )
    option_filter = OptionFilter(NimbusLandGate, NimbusLandGate.option_bean_valley)

class HasMegasmilaxForNimbusLand(Requirement):
    items_needed = [Megasmilax]
    option_filter = OptionFilter(NimbusLandGate, NimbusLandGate.option_megasmilax)

class NimbusLandOpen(Requirement):
    option_filter = OptionFilter(
        NimbusLandGate,
        [
            NimbusLandGate.option_gold_paint,
            NimbusLandGate.option_open
        ],
        operator="in"
    )

class CanAccessNimbusLand(Requirement):
    rule = Or(
        HasBeanValleyForNimbusLand.get_rule(),
        HasMegasmilaxForNimbusLand.get_rule(),
        NimbusLandOpen.get_rule()
    )

class HasGoldPaintForNimbusCastleAccess(Requirement):
    items_needed = [GoldPaint]
    option_filter = OptionFilter(NimbusLandGate, NimbusLandGate.option_gold_paint)

class NimbusCastleOpen(Requirement):
    option_filter = OptionFilter(NimbusLandGate, NimbusLandGate.option_open)


class CanAccessNimbusCastle(Requirement):
    rule = And(
        Or(
            HasGoldPaintForNimbusCastleAccess.get_rule(),
            NimbusCastleOpen.get_rule()
        ),
        CanAccessNimbusLand.get_rule()
    )

class CanAccessInnerNimbus(Requirement):
    rule = And(
        Has(ItemNames.CASTLE_KEY_1),
        CanAccessNimbusCastle.get_rule()
    )

class CanAccessInnerNimbusBoss(Requirement):
    rule = And(
        CanAccessInnerNimbus.get_rule(),
        NotEarlyGame.get_rule()
    )

class CanAccessLateNimbus(Requirement):
    rule = And(
        Has(ItemNames.CASTLE_KEY_2),
        CanAccessInnerNimbus.get_rule()
    )

class CanClearNimbusBoss(Requirement):
    rule = And(
        CanAccessLateNimbus.get_rule(),
        NotEarlyGame.get_rule()
    )

class HasNimbusLandForBarrelVolcano(LocationClearRequirement):
    items_needed = [NimbusLand]
    option_filter = OptionFilter(BarrelVolcanoGate, BarrelVolcanoGate.option_nimbus_land)

class HasValentinaForBarrelVolcano(Requirement):
    items_needed = [Valentina]
    option_filter = OptionFilter(BarrelVolcanoGate, BarrelVolcanoGate.option_valentina)

class BarrelVolcanoOpen(Requirement):
    option_filter = OptionFilter(BarrelVolcanoGate, BarrelVolcanoGate.option_open)

class CanAccessBarrelVolcano(Requirement):
    rule = And(
        Or(
            HasNimbusLandForBarrelVolcano.get_rule(),
            HasValentinaForBarrelVolcano.get_rule(),
            BarrelVolcanoOpen.get_rule()
        ),
        NotEarlyGame.get_rule()
    )

class HasBarrelVolcanoForBowsersKeep(LocationClearRequirement):
    items_needed = [BarrelVolcano]
    option_filter = OptionFilter(BowsersKeepGate, BowsersKeepGate.option_barrel_volcano)

class HasAxemRangerForBowsersKeep(Requirement):
    items_needed = [AxemRangers]
    option_filter = OptionFilter(BowsersKeepGate, BowsersKeepGate.option_axem_rangers)

class HasSixStarPiecesForBowsersKeep(StarPieceRequirement):
    count = 6
    option_filter = OptionFilter(BowsersKeepGate, BowsersKeepGate.option_six_star_pieces)

class BowsersKeepOpen(Requirement):
    option_filter = OptionFilter(BowsersKeepGate, BowsersKeepGate.option_open)

class CanAccessBowsersKeep(Requirement):
    rule = And(
        Or(
            HasBarrelVolcanoForBowsersKeep.get_rule(),
            HasAxemRangerForBowsersKeep.get_rule(),
            HasSixStarPiecesForBowsersKeep.get_rule(),
            BowsersKeepOpen.get_rule()
        ),
        NotEarlyGame.get_rule()
    )

class CanClearBowsersKeep(Requirement):
    rule = And(
        CanAccessBowsersKeep.get_rule(),
        HasDamagingSpells.get_rule(),
        NotEarlyGame.get_rule()
    )

class HasSixStarPiecesForFactory(StarPieceRequirement):
    count = 6
    option_filter = OptionFilter(FactoryGate, FactoryGate.option_six_star_pieces)

class HasExorForFactory(Requirement):
    items_needed = [Exor]
    option_filter = OptionFilter(FactoryGate, FactoryGate.option_exor)

class HasBowsersKeepForFactory(LocationClearRequirement):
    items_needed = [BowsersKeep]
    option_filter = OptionFilter(FactoryGate, FactoryGate.option_finish_bowsers_keep)

class FactoryOpen(Requirement):
    rule = CanAccessBowsersKeep.get_rule()
    option_filter = OptionFilter(FactoryGate, FactoryGate.option_open_with_bowsers_keep)

class CanAccessFactory(Requirement):
    rule = Or(
        HasSixStarPiecesForFactory.get_rule(),
        HasBowsersKeepForFactory.get_rule(),
        HasExorForFactory.get_rule(),
        FactoryOpen.get_rule()
    )

class HasNonProgressiveFireworksForFinalBoss(Requirement):
    items_needed = [Fireworks]
    option_filter = OptionFilter(FireworksTradeSequence, FireworksTradeSequence.option_shuffle_one)

class HasProgressiveFireworksForFinalBoss(Requirement):
    items_needed = [Fireworks, ShinyStone, CarboCookie]
    option_filter = OptionFilter(FireworksTradeSequence, FireworksTradeSequence.option_progressive)

class HasNonShuffledFireworksForFinalBoss(Requirement):
    option_filter = OptionFilter(FireworksTradeSequence, FireworksTradeSequence.option_vanilla)

class HasFireworksForFinalBoss(Requirement):
    rule = Or(
        HasNonProgressiveFireworksForFinalBoss.get_rule(),
        HasProgressiveFireworksForFinalBoss.get_rule(),
        HasNonShuffledFireworksForFinalBoss.get_rule()
    )

class CanAccessFinalBossSlot(Requirement):
    rule = And(
        Or(
            CanAccessFactory.get_rule(),
            HasFireworksForFinalBoss.get_rule(),
            HasBrightCard.get_rule()
        ),
        NotEarlyGame.get_rule(),
        Has(ItemNames.STAR_PIECE, FromOption(StarPiecesRequired))
    )

class CanAccessSealedDoorBoss(Requirement):
    rule = And(
        Has(ItemNames.SHINY_STONE),
        CanAccessMonstroTown.get_rule(),
        NotEarlyGame.get_rule()
    )
    items_needed = [ShinyStone]
    other_requirements_and = [CanAccessMonstroTown, NotEarlyGame]

class PostgameSealedDoorBoss(Requirement):
    rule = And(
        CanAccessSealedDoorBoss.get_rule(),
        HasAll(ItemNames.STAY_VOUCHER, ItemNames.EXTRA_SHINY_STONE),
    )

class CanFightMimic1(Requirement):
    items_needed = [MimicLauncher1]

class CanFightMimic2(Requirement):
    rule = And(
        Has(ItemNames.SECOND_MIMIC_LAUNCHER),
        NotEarlyGame.get_rule()
    )

class CanFightMimic3(Requirement):
    rule = And(
        Has(ItemNames.THIRD_MIMIC_LAUNCHER),
        NotEarlyGame.get_rule()
    )