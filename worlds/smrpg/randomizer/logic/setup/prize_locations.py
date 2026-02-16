from __future__ import annotations

from randomizer.progression.prizelocations import *
from randomizer.types.flags import (
    WinCondition, WinConditions,
    AvailableCharacters, AvailableSpells,
    FixKnifeGuy,
    FireworksSetting, FireworksOptions,
    StartingCharacters,
    NimbusGate, NimbusGating,
    Remake,
    InvisibleFlagsSetting,
    KeyItemsAnywhere,
    StarPieceAvailability,
    ShuffleCoins,
    SpellsAnywhere,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    CompareVarToConst,
    SummonObjectToSpecificLevel,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.area_object import (
    AreaObject,
)
from typing import cast, TYPE_CHECKING
from copy import copy

from ...types.prizelocation import (
    PrizeLocation,
    TreasureChestLocation,
    EventLocation,
    StandingLocation,
    RiverLocation,
    BoosterHillLocation,
    StandardPrizeLocation,
    SpellSlotLocation,
    BossFightLocation,
    StarPieceLocation,
    CharacterRecruitmentLocation,
    KeyItemLocation
)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def set_locations(world: GameWorld) -> None:
    # establish all functional prize locations
    # regardless if they will have their contents shuffled or not

    world.locations = {
        StartingItem1Location: StartingItem1Location(),
        StartingItem2Location: StartingItem2Location(),
        StartingItem3Location: StartingItem3Location(),
        StartingItem4Location: StartingItem4Location(),
        StartingCharacter1: StartingCharacter1(),
        MushroomWay1LowerChest: MushroomWay1LowerChest(),
        MushroomWay1UpperChest: MushroomWay1UpperChest(),
        MushroomWay1ToadRescue: MushroomWay1ToadRescue(),
        MushroomWay2LedgeChest: MushroomWay2LedgeChest(),
        MushroomWay2ToadRescue: MushroomWay2ToadRescue(),
        MushroomWayRightGoomba: MushroomWayRightGoomba(),
        MushrooomWayBossFight: MushrooomWayBossFight(),
        MushroomWayStarPiece: MushroomWayStarPiece(),
        MushroomWayBossFightRewardItem: MushroomWayBossFightRewardItem(),
        MushroomWayCharacter: MushroomWayCharacter(),
        MushroomKingdomMainHall: MushroomKingdomMainHall(),
        MushroomKingdomLiberatedVaultLeft: MushroomKingdomLiberatedVaultLeft(),
        MushroomKingdomLiberatedVaultRight: MushroomKingdomLiberatedVaultRight(),
        MushroomKingdomLiberatedVaultMiddle: MushroomKingdomLiberatedVaultMiddle(),
        MushroomKingdomChair: MushroomKingdomChair(),
        MushroomKingdomFreeShopItem: MushroomKingdomFreeShopItem(),
        MushroomKingdomShopBasementLeft: MushroomKingdomShopBasementLeft(),
        MushroomKingdomShopBasementRight: MushroomKingdomShopBasementRight(),
        MushroomKingdomWalletGuyFirstRewardLocation: MushroomKingdomWalletGuyFirstRewardLocation(),
        MushroomKingdomWalletGuySecondRewardLocation: MushroomKingdomWalletGuySecondRewardLocation(),
        MushroomKingdomOccupiedOutdoorGuardLocation: MushroomKingdomOccupiedOutdoorGuardLocation(),
        MushroomKingdomOccupiedCastleToadRescueLocation: MushroomKingdomOccupiedCastleToadRescueLocation(),
        MushroomKingdomOccupiedFamilyRescueLocation: MushroomKingdomOccupiedFamilyRescueLocation(),
        MushroomKingdomOccupiedGuestRoomLocation: MushroomKingdomOccupiedGuestRoomLocation(),
        MushroomKingdomBossFight: MushroomKingdomBossFight(),
        MushroomKingdomStarPiece: MushroomKingdomStarPiece(),
        MushroomKingdomStoreExchangeLocation: MushroomKingdomStoreExchangeLocation(),
        MushroomKingdomInnPurchaseLocation: MushroomKingdomInnPurchaseLocation(),
        BanditsWayFlowerJumpLocation: BanditsWayFlowerJumpLocation(),
        BanditsWayCoin1Location: BanditsWayCoin1Location(),
        BanditsWayCoin2Location: BanditsWayCoin2Location(),
        BanditsWayCoin3Location: BanditsWayCoin3Location(),
        BanditsWayDogChestLocation: BanditsWayDogChestLocation(),
        BanditsWayPlatformsLeftChestLocation: BanditsWayPlatformsLeftChestLocation(),
        BanditsWayPlatformsRightChestLocation: BanditsWayPlatformsRightChestLocation(),
        BanditsWayDeadEndChestLocation: BanditsWayDeadEndChestLocation(),
        BanditsWayBossFight: BanditsWayBossFight(),
        BanditsWayStarPiece: BanditsWayStarPiece(),
        BanditsWayBossFirstItemDropLocation: BanditsWayBossFirstItemDropLocation(),
        BanditsWayBossSecondItemDropLocation: BanditsWayBossSecondItemDropLocation(),
        KeroSewersStairRoomLeftChestLocation: KeroSewersStairRoomLeftChestLocation(),
        KeroSewersStairRoomRightChestLocation: KeroSewersStairRoomRightChestLocation(),
        Mimic1BossFight: Mimic1BossFight(),
        Mimic1DropRewardLocation: Mimic1DropRewardLocation(),
        Mimic1StarPiece: Mimic1StarPiece(),
        Mimic1ReloadRewardLocation: Mimic1ReloadRewardLocation(),
        KeroSewersFourRatRoomChestLocation: KeroSewersFourRatRoomChestLocation(),
        KeroSewersBeforeBelomeLowerLocation: KeroSewersBeforeBelomeLowerLocation(),
        KeroSewersBeforeBelomeUpperBeforeFlipLocation: KeroSewersBeforeBelomeUpperBeforeFlipLocation(),
        KeroSewersBeforeBelomeUpperAfterFlipLocation: KeroSewersBeforeBelomeUpperAfterFlipLocation(),
        KeroSewersBossFight: KeroSewersBossFight(),
        KeroSewersStarPiece: KeroSewersStarPiece(),
        MidasRiverFirstCompletionRewardLocation: MidasRiverFirstCompletionRewardLocation(),
        MidasRiverBottomLeftCaveLocation: MidasRiverBottomLeftCaveLocation(),
        MidasRiverBottomRightCaveLocation: MidasRiverBottomRightCaveLocation(),
        TadpolePondCricketPieExchangeLocation: TadpolePondCricketPieExchangeLocation(),
        TadpolePondCricketJamExchangeLocation: TadpolePondCricketJamExchangeLocation(),
        MelodyBayFirstRewardLocation: MelodyBayFirstRewardLocation(),
        MelodyBaySecondRewardLocation: MelodyBaySecondRewardLocation(),
        MelodyBayThirdRewardLocation: MelodyBayThirdRewardLocation(),
        RoseWaySwingingPlatformRoomLocation: RoseWaySwingingPlatformRoomLocation(),
        RoseWayLeftIslandLocation: RoseWayLeftIslandLocation(),
        RoseWayMiddleIslandLocation: RoseWayMiddleIslandLocation(),
        RoseWayCoin1Location: RoseWayCoin1Location(),
        RoseWayCoin2Location: RoseWayCoin2Location(),
        RoseWayCoin3Location: RoseWayCoin3Location(),
        RoseWayCoin4Location: RoseWayCoin4Location(),
        RoseWayCoin5Location: RoseWayCoin5Location(),
        RoseWayFiveChestRoomTopLocation: RoseWayFiveChestRoomTopLocation(),
        RoseWayFiveChestRoomBottomLeftLocation: RoseWayFiveChestRoomBottomLeftLocation(),
        RoseWayFiveChestRoomRightLocation: RoseWayFiveChestRoomRightLocation(),
        RoseWayFiveChestRoomLeftLocation: RoseWayFiveChestRoomLeftLocation(),
        RoseWayFiveChestRoomBottomRightLocation: RoseWayFiveChestRoomBottomRightLocation(),
        RoseTownShopLeftChestLocation: RoseTownShopLeftChestLocation(),
        RoseTownShopRightChestLocation: RoseTownShopRightChestLocation(),
        RoseTownCloudRightChestLocation: RoseTownCloudRightChestLocation(),
        RoseTownCloudLeftChestLocation: RoseTownCloudLeftChestLocation(),
        RoseTownInnToadPrizeLocation: RoseTownInnToadPrizeLocation(),
        RoseTownInnGazPrizeLocation: RoseTownInnGazPrizeLocation(),
        RoseTownTreasureHouseLeftChestLocation: RoseTownTreasureHouseLeftChestLocation(),
        RoseTownTreasureHouseRightChestLocation: RoseTownTreasureHouseRightChestLocation(),
        RoseTownTreasureHouseMazeRewardLocation: RoseTownTreasureHouseMazeRewardLocation(),
        RoseTownTreasureHouseUpperChestLocation: RoseTownTreasureHouseUpperChestLocation(),
        ForestMazeFirstRoomLocation: ForestMazeFirstRoomLocation(),
        ForestMazeFirstUndergroundExitLocation: ForestMazeFirstUndergroundExitLocation(),
        ForestMazeUndergroundWigglerChestLocation: ForestMazeUndergroundWigglerChestLocation(),
        ForestMazeUndergroundBottomRightTrunkChestLocation: ForestMazeUndergroundBottomRightTrunkChestLocation(),
        ForestMazeUndergroundMiddleLeftChestLocation: ForestMazeUndergroundMiddleLeftChestLocation(),
        ForestMazeInnerMazeEntranceLocation: ForestMazeInnerMazeEntranceLocation(),
        ForestMazeSecretTopRightChestLocation: ForestMazeSecretTopRightChestLocation(),
        ForestMazeSecretBottomRightChestLocation: ForestMazeSecretBottomRightChestLocation(),
        ForestMazeSecretTopMiddleChestLocation: ForestMazeSecretTopMiddleChestLocation(),
        ForestMazeSecretBottomMiddleChestLocation: ForestMazeSecretBottomMiddleChestLocation(),
        ForestMazeSecretLeftChestLocation: ForestMazeSecretLeftChestLocation(),
        ForestMazeBossFight: ForestMazeBossFight(),
        ForestMazeStarPiece: ForestMazeStarPiece(),
        ForestMazeCharacter: ForestMazeCharacter(),
        PipeVaultSlidingCoinRoomBackChestLocation: PipeVaultSlidingCoinRoomBackChestLocation(),
        PipeVaultSlidingCoinRoomMiddleChestLocation: PipeVaultSlidingCoinRoomMiddleChestLocation(),
        PipeVaultSlidingCoinRoomFrontChestLocation: PipeVaultSlidingCoinRoomFrontChestLocation(),
        PipeVaultSlidingCoinRoomCoin1Location: PipeVaultSlidingCoinRoomCoin1Location(),
        PipeVaultSlidingCoinRoomCoin2Location: PipeVaultSlidingCoinRoomCoin2Location(),
        PipeVaultSlidingCoinRoomCoin3Location: PipeVaultSlidingCoinRoomCoin3Location(),
        PipeVaultSlidingCoinRoomCoin4Location: PipeVaultSlidingCoinRoomCoin4Location(),
        PipeVaultSlidingCoinRoomCoin5Location: PipeVaultSlidingCoinRoomCoin5Location(),
        PipeVaultSlidingCoinRoomCrouchItemLocation: PipeVaultSlidingCoinRoomCrouchItemLocation(),
        PipeVaultGoombaThumpinFirstPrizeLocation: PipeVaultGoombaThumpinFirstPrizeLocation(),
        PipeVaultGoombaThumpinSecondPrizeLocation: PipeVaultGoombaThumpinSecondPrizeLocation(),
        PipeVaultRisingPlatformChestLocation: PipeVaultRisingPlatformChestLocation(),
        PipeVaultChompweedChestLocation: PipeVaultChompweedChestLocation(),
        YosterEntranceChestLocation: YosterEntranceChestLocation(),
        YosterRacePrize1Location: YosterRacePrize1Location(),
        YosterRacePrize2Location: YosterRacePrize2Location(),
        YosterRacePrize3Location: YosterRacePrize3Location(),
        BucketGirlRewardLocation: BucketGirlRewardLocation(),
        TreasureShopItem1: TreasureShopItem1(),
        TreasureShopItem2: TreasureShopItem2(),
        TreasureShopItem3: TreasureShopItem3(),
        OuterMinesTrampolineHenchmanLocation: OuterMinesTrampolineHenchmanLocation(),
        OuterMinesLeftHenchmanLocation: OuterMinesLeftHenchmanLocation(),
        OuterMinesRightHenchmanLocation: OuterMinesRightHenchmanLocation(),
        OuterMinesBossPrizeLocation: OuterMinesBossPrizeLocation(),
        OuterMinesBossFight: OuterMinesBossFight(),
        OuterMinesStarPiece: OuterMinesStarPiece(),
        InnerMinesTracksChestLocation: InnerMinesTracksChestLocation(),
        InnerMinesShyguyCartLocation: InnerMinesShyguyCartLocation(),
        InnerMinesBoxesChestLocation: InnerMinesBoxesChestLocation(),
        InnerMinesSaveBlockChestLocation: InnerMinesSaveBlockChestLocation(),
        InnerMinesHighUpChestLocation: InnerMinesHighUpChestLocation(),
        InnerMinesBossFight: InnerMinesBossFight(),
        InnerMinesStarPiece: InnerMinesStarPiece(),
        InnerMinesCharacter: InnerMinesCharacter(),
        BoosterPassBushLocation: BoosterPassBushLocation(),
        BoosterPassFirstRoomLeftChestLocation: BoosterPassFirstRoomLeftChestLocation(),
        BoosterPassFirstRoomRightChestLocation: BoosterPassFirstRoomRightChestLocation(),
        BoosterPassSecondRoomFlowerLocation: BoosterPassSecondRoomFlowerLocation(),
        BoosterPassSecretMiddleChestLocation: BoosterPassSecretMiddleChestLocation(),
        BoosterPassSecretRightChestLocation: BoosterPassSecretRightChestLocation(),
        BoosterPassSecretLeftChestLocation: BoosterPassSecretLeftChestLocation(),
        BoosterTowerSpookumStairsLocation: BoosterTowerSpookumStairsLocation(),
        BoosterTowerTrainRoomCreviceLocation: BoosterTowerTrainRoomCreviceLocation(),
        BoosterTowerChestNearThwompLocation: BoosterTowerChestNearThwompLocation(),
        BoosterTowerFallingChestLocation: BoosterTowerFallingChestLocation(),
        BoosterTowerKnifeGuyPrizeLocation: BoosterTowerKnifeGuyPrizeLocation(),
        BoosterTowerPortraitPrizeLocation: BoosterTowerPortraitPrizeLocation(),
        BoosterTowerElderKeyItemLocation: BoosterTowerElderKeyItemLocation(),
        BoosterTowerParachuteRoomChestLocation: BoosterTowerParachuteRoomChestLocation(),
        BoosterTowerParachuteRoomCreviceLocation: BoosterTowerParachuteRoomCreviceLocation(),
        BoosterTowerCheckerboardRightmostItemLocation: BoosterTowerCheckerboardRightmostItemLocation(),
        BoosterTowerCheckerboardTopItemLocation: BoosterTowerCheckerboardTopItemLocation(),
        BoosterTowerCheckerboardLeftmostItemLocation: BoosterTowerCheckerboardLeftmostItemLocation(),
        BoosterTowerCheckerboardUpperRightItemLocation: BoosterTowerCheckerboardUpperRightItemLocation(),
        BoosterTowerCheckerboardBottomItemLocation: BoosterTowerCheckerboardBottomItemLocation(),
        BoosterTowerCheckerboardCoin1Location: BoosterTowerCheckerboardCoin1Location(),
        BoosterTowerCheckerboardCoin2Location: BoosterTowerCheckerboardCoin2Location(),
        BoosterTowerCheckerboardCoin3Location: BoosterTowerCheckerboardCoin3Location(),
        BoosterTowerCheckerboardCoin4Location: BoosterTowerCheckerboardCoin4Location(),
        BoosterTowerCheckerboardCoin5Location: BoosterTowerCheckerboardCoin5Location(),
        BoosterTowerCheckerboardCoin6Location: BoosterTowerCheckerboardCoin6Location(),
        BoosterTowerCheckerboardCoin7Location: BoosterTowerCheckerboardCoin7Location(),
        BoosterTowerCheckerboardCoin8Location: BoosterTowerCheckerboardCoin8Location(),
        BoosterTowerCheckerboardCoin9Location: BoosterTowerCheckerboardCoin9Location(),
        BoosterTowerRoomKeyChestLocation: BoosterTowerRoomKeyChestLocation(),
        BoosterTowerTopFloorLowerChestLocation: BoosterTowerTopFloorLowerChestLocation(),
        BoosterTowerTopFloorUpperChestLocation: BoosterTowerTopFloorUpperChestLocation(),
        BoosterTowerTopFloorCornerChestLocation: BoosterTowerTopFloorCornerChestLocation(),
        BoosterTowerCurtainGamePrizeLocation: BoosterTowerCurtainGamePrizeLocation(),
        BoosterTowerIndoorBossFight: BoosterTowerIndoorBossFight(),
        BoosterTowerIndoorStarPiece: BoosterTowerIndoorStarPiece(),
        BoosterTowerBalconyBossFight: BoosterTowerBalconyBossFight(),
        BoosterTowerBalconyStarPiece: BoosterTowerBalconyStarPiece(),
        BoosterHillGuaranteedItem1: BoosterHillGuaranteedItem1(),
        BoosterHillGuaranteedItem2: BoosterHillGuaranteedItem2(),
        BoosterHillGuaranteedItem3: BoosterHillGuaranteedItem3(),
        BoosterHillGuaranteedItem4: BoosterHillGuaranteedItem4(),
        BoosterHillGuaranteedItem5: BoosterHillGuaranteedItem5(),
        BoosterHillGuaranteedItem6: BoosterHillGuaranteedItem6(),
        BoosterHillGuaranteedItem7: BoosterHillGuaranteedItem7(),
        BoosterHillGuaranteedItem8: BoosterHillGuaranteedItem8(),
        BoosterHillGuaranteedItem9: BoosterHillGuaranteedItem9(),
        BoosterHillGuaranteedItem10: BoosterHillGuaranteedItem10(),
        BoosterHillGuaranteedItem11: BoosterHillGuaranteedItem11(),
        BoosterHillGuaranteedItem12: BoosterHillGuaranteedItem12(),
        BoosterHillGuaranteedItem13: BoosterHillGuaranteedItem13(),
        BoosterHillGuaranteedItem14: BoosterHillGuaranteedItem14(),
        BoosterHillGuaranteedItem15: BoosterHillGuaranteedItem15(),
        BoosterHillGuaranteedItem16: BoosterHillGuaranteedItem16(),
        MarrymoreFirstSuitePrizeLocation: MarrymoreFirstSuitePrizeLocation(),
        MarrymoreSecondSuitePrizeLocation: MarrymoreSecondSuitePrizeLocation(),
        MarrymoreThirdSuitePrizeLocation: MarrymoreThirdSuitePrizeLocation(),
        MarrymoreFourthSuitePrizeLocation: MarrymoreFourthSuitePrizeLocation(),
        MarrymoreFifthSuitePrizeLocation: MarrymoreFifthSuitePrizeLocation(),
        MarrymoreSixthSuitePrizeLocation: MarrymoreSixthSuitePrizeLocation(),
        MarrymoreBigTipLocation: MarrymoreBigTipLocation(),
        MarrymoreHotelChestLocation: MarrymoreHotelChestLocation(),
        MarrymoreSnifit1Location: MarrymoreSnifit1Location(),
        MarrymoreSnifit2Location: MarrymoreSnifit2Location(),
        MarrymoreSnifit3Location: MarrymoreSnifit3Location(),
        MarrymoreAltarHeadLocation: MarrymoreAltarHeadLocation(),
        MarrymoreBossFight: MarrymoreBossFight(),
        MarrymoreBossFightStarPiece: MarrymoreBossFightStarPiece(),
        MarrymoreCharacter: MarrymoreCharacter(),
        StarHillStarPiece: StarHillStarPiece(),
        FrogDiscipleLocation1: FrogDiscipleLocation1(),
        FrogDiscipleLocation2: FrogDiscipleLocation2(),
        FrogDiscipleLocation3: FrogDiscipleLocation3(),
        FrogDiscipleLocation4: FrogDiscipleLocation4(),
        FrogDiscipleLocation5: FrogDiscipleLocation5(),
        SeasideBeachBossFight: SeasideBeachBossFight(),
        SeasideBeachStarPiece: SeasideBeachStarPiece(),
        SeasideTownBossPrizeLocation: SeasideTownBossPrizeLocation(),
        SeasideTownShedRescueLocation: SeasideTownShedRescueLocation(),
        SeaStarslapRoomChestLocation: SeaStarslapRoomChestLocation(),
        SeaSaveRoomBackChestLocation: SeaSaveRoomBackChestLocation(),
        SeaSaveRoomMiddleChestLocation: SeaSaveRoomMiddleChestLocation(),
        SeaSaveRoomFrontChestLocation: SeaSaveRoomFrontChestLocation(),
        SeaWhirlpoolChestLocation: SeaWhirlpoolChestLocation(),
        ShipRatStairsChestLocation: ShipRatStairsChestLocation(),
        ShipRatStairsBoxesLocation: ShipRatStairsBoxesLocation(),
        ShipTroopaPuzzleLocation: ShipTroopaPuzzleLocation(),
        ShipTrampolinePuzzle: ShipTrampolinePuzzle(),
        Ship3DMazePuzzle: Ship3DMazePuzzle(),
        ShipShopChestLocation: ShipShopChestLocation(),
        ShipCoinSnakePuzzleLocation: ShipCoinSnakePuzzleLocation(),
        ShipCannonballPuzzle: ShipCannonballPuzzle(),
        ShipBarrelPuzzle: ShipBarrelPuzzle(),
        ShipPasswordBossFight: ShipPasswordBossFight(),
        ShipPasswordStarPiece: ShipPasswordStarPiece(),
        EarlyInnerShipLeftChestLocation: EarlyInnerShipLeftChestLocation(),
        EarlyInnerShipRightChestLocation: EarlyInnerShipRightChestLocation(),
        InnerShipCloneRoomChestLocation: InnerShipCloneRoomChestLocation(),
        InnerShipBehindBoxesChestLocation: InnerShipBehindBoxesChestLocation(),
        InnerShipSaveRoomLeftChestLocation: InnerShipSaveRoomLeftChestLocation(),
        InnerShipSaveRoomRightChestLocation: InnerShipSaveRoomRightChestLocation(),
        Mimic2DropRewardLocation: Mimic2DropRewardLocation(),
        Mimic2BossFight: Mimic2BossFight(),
        Mimic2StarPiece: Mimic2StarPiece(),
        Mimic2ReloadRewardLocation: Mimic2ReloadRewardLocation(),
        InnerShipFirstUnderwaterRoomBottomItemLocation: InnerShipFirstUnderwaterRoomBottomItemLocation(),
        InnerShipFirstUnderwaterRoomTopItemLocation: InnerShipFirstUnderwaterRoomTopItemLocation(),
        InnerShipFirstUnderwaterRoomLeftItemLocation: InnerShipFirstUnderwaterRoomLeftItemLocation(),
        InnerShipFirstUnderwaterRoomMiddleItemLocation: InnerShipFirstUnderwaterRoomMiddleItemLocation(),
        InnerShipSecretRoomChestLocation: InnerShipSecretRoomChestLocation(),
        InnerShipPoolRoomLocation: InnerShipPoolRoomLocation(),
        InnerShipBeforeBossChestLocation: InnerShipBeforeBossChestLocation(),
        ShipFinalBossFight: ShipFinalBossFight(),
        ShipFinalStarPiece: ShipFinalStarPiece(),
        LandsEndRisingPlatformChestLocation: LandsEndRisingPlatformChestLocation(),
        LandsEndChowPitStaticChestLocation: LandsEndChowPitStaticChestLocation(),
        LandsEndChowPitMovingChestLocation: LandsEndChowPitMovingChestLocation(),
        LandsEndBeeTowerChestLocation: LandsEndBeeTowerChestLocation(),
        LandsEndGrottoEntranceChestLocation: LandsEndGrottoEntranceChestLocation(),
        LandsEndGrottoCornerChestLocation: LandsEndGrottoCornerChestLocation(),
        LandsEndGrottoEndChestLocation: LandsEndGrottoEndChestLocation(),
        LandsEndUndergroundSaveBoxChestLocation: LandsEndUndergroundSaveBoxChestLocation(),
        LandsEndFirstPurchasableChestLocation: LandsEndFirstPurchasableChestLocation(),
        LandsEndSecondPurchasableChestLocation: LandsEndSecondPurchasableChestLocation(),
        TroopaClimbSub12PrizeLocation: TroopaClimbSub12PrizeLocation(),
        LandsEndCloudBoss: LandsEndCloudBoss(),
        LandsEndCloudStarPiece: LandsEndCloudStarPiece(),
        BelomeTempleFortuneTellerLocation: BelomeTempleFortuneTellerLocation(),
        BelomeTempleLMRChestLocation: BelomeTempleLMRChestLocation(),
        BelomeTempleLRMChestLocation: BelomeTempleLRMChestLocation(),
        BelomeTempleRLMChestLocation: BelomeTempleRLMChestLocation(),
        BelomeTempleRMLChestLocation: BelomeTempleRMLChestLocation(),
        BelomeBeforeBossRightChestLocation: BelomeBeforeBossRightChestLocation(),
        BelomeBeforeBossLowerLeftChestLocation: BelomeBeforeBossLowerLeftChestLocation(),
        BelomeBeforeBossMiddleChestLocation: BelomeBeforeBossMiddleChestLocation(),
        BelomeBeforeBossUpperLeftChestLocation: BelomeBeforeBossUpperLeftChestLocation(),
        BelomeTempleTreasuryUpperCornerLeftItemLocation: BelomeTempleTreasuryUpperCornerLeftItemLocation(),
        BelomeTempleTreasuryUpperCornerLowerLeftItemLocation: BelomeTempleTreasuryUpperCornerLowerLeftItemLocation(),
        BelomeTempleTreasuryUpperCornerTopItemLocation: BelomeTempleTreasuryUpperCornerTopItemLocation(),
        BelomeTempleTreasuryTopmostItemLocation: BelomeTempleTreasuryTopmostItemLocation(),
        BelomeTempleTreasuryMidLeftItemLocation: BelomeTempleTreasuryMidLeftItemLocation(),
        BelomeTempleTreasuryAlmostTopItemLocation: BelomeTempleTreasuryAlmostTopItemLocation(),
        BelomeTempleTreasuryAlmostLeftmostItemLocation: BelomeTempleTreasuryAlmostLeftmostItemLocation(),
        BelomeTempleTreasuryOuterUpperRightItemLocation: BelomeTempleTreasuryOuterUpperRightItemLocation(),
        BelomeTempleTreasuryInnerUpperRightItemLocation: BelomeTempleTreasuryInnerUpperRightItemLocation(),
        BelomeTempleTreasuryLowestItemsRightLocation: BelomeTempleTreasuryLowestItemsRightLocation(),
        BelomeTempleTreasuryLowerOuterBottomRightItemLocation: BelomeTempleTreasuryLowerOuterBottomRightItemLocation(),
        BelomeTempleTreasuryRightmostItemLocation: BelomeTempleTreasuryRightmostItemLocation(),
        BelomeTempleTreasuryBottomLeftCornerItemLocation: BelomeTempleTreasuryBottomLeftCornerItemLocation(),
        BelomeTempleTreasuryLowestItemsLeftLocation: BelomeTempleTreasuryLowestItemsLeftLocation(),
        BelomeTempleTreasuryUpperOuterBottomRightItemLocation: BelomeTempleTreasuryUpperOuterBottomRightItemLocation(),
        TempleBossFight: TempleBossFight(),
        TempleBossFightStarPiece: TempleBossFightStarPiece(),
        MonstroEntranceLocation: MonstroEntranceLocation(),
        MonstroThwompItemLocation: MonstroThwompItemLocation(),
        DojoFirstFight: DojoFirstFight(),
        DojoFirstFightStarPiece: DojoFirstFightStarPiece(),
        DojoSecondFight: DojoSecondFight(),
        DojoSecondFightStarPiece: DojoSecondFightStarPiece(),
        DojoThirdFight: DojoThirdFight(),
        DojoThirdFightStarPiece: DojoThirdFightStarPiece(),
        DojoFourthFight: DojoFourthFight(),
        DojoFourthFightStarPiece: DojoFourthFightStarPiece(),
        MonstroDojoClearRewardLocation: MonstroDojoClearRewardLocation(),
        MonstroSealedDoorBossFight: MonstroSealedDoorBossFight(),
        MonstroSealedDoorStarPiece: MonstroSealedDoorStarPiece(),
        MonstroSealedDoorClearRewardLocation: MonstroSealedDoorClearRewardLocation(),
        MonstroFlagExchangeLocation: MonstroFlagExchangeLocation(),
        BeanValleyFirstDeadEndLocation: BeanValleyFirstDeadEndLocation(),
        BeanValleyFirstProgressChestLocation: BeanValleyFirstProgressChestLocation(),
        BeanValleyLeftPiranhaPipeLocation: BeanValleyLeftPiranhaPipeLocation(),
        BeanValleyBottomLeftPiranhaPipeLocation: BeanValleyBottomLeftPiranhaPipeLocation(),
        BeanValleyBottomRightPiranhaPipeUpperLocation: BeanValleyBottomRightPiranhaPipeUpperLocation(),
        BeanValleyBottomRightPiranhaPipeLowerLocation: BeanValleyBottomRightPiranhaPipeLowerLocation(),
        BeanValleyRightPipeLeftChestLocation: BeanValleyRightPipeLeftChestLocation(),
        Mimic3BossFight: Mimic3BossFight(),
        Mimic3StarPiece: Mimic3StarPiece(),
        BeanValleyRightPipeRightChestLocation: BeanValleyRightPipeRightChestLocation(),
        BeanValleyRightPipeUnderStairsLocation: BeanValleyRightPipeUnderStairsLocation(),
        BeanValleyRightPipeAboveGroundLocation: BeanValleyRightPipeAboveGroundLocation(),
        BeanValleyPlanterBossFight: BeanValleyPlanterBossFight(),
        BeanValleyPlanterStarPiece: BeanValleyPlanterStarPiece(),
        BeanValleyBossNoteLocation: BeanValleyBossNoteLocation(),
        BeanstalkLowestChestLocation: BeanstalkLowestChestLocation(),
        BeanValley1stRoomFloatingItemLocation: BeanValley1stRoomFloatingItemLocation(),
        BeanValley1stRoomMiddleCoinLocation: BeanValley1stRoomMiddleCoinLocation(),
        BeanValley1stRoomUpperCoinLocation: BeanValley1stRoomUpperCoinLocation(),
        BeanValley1stRoomLowerCoinLocation: BeanValley1stRoomLowerCoinLocation(),
        Beanstalk2ndRoomFloatingItemLocation: Beanstalk2ndRoomFloatingItemLocation(),
        Beanstalk2ndRoomCoin1Location: Beanstalk2ndRoomCoin1Location(),
        Beanstalk2ndRoomCoin2Location: Beanstalk2ndRoomCoin2Location(),
        Beanstalk2ndRoomCoin3Location: Beanstalk2ndRoomCoin3Location(),
        BeanValleyEastBeanstalkCoin1Location: BeanValleyEastBeanstalkCoin1Location(),
        BeanValleyEastBeanstalkCoin2Location: BeanValleyEastBeanstalkCoin2Location(),
        BeanValleyEastBeanstalkCoin3Location: BeanValleyEastBeanstalkCoin3Location(),
        BeanValleyEastBeanstalkCoin4Location: BeanValleyEastBeanstalkCoin4Location(),
        BeanValleyEastBeanstalkCoin5Location: BeanValleyEastBeanstalkCoin5Location(),
        BeanValleyWestBeanstalkCoin1Location: BeanValleyWestBeanstalkCoin1Location(),
        BeanValleyWestBeanstalkCoin2Location: BeanValleyWestBeanstalkCoin2Location(),
        BeanValleyWestBeanstalkCoin3Location: BeanValleyWestBeanstalkCoin3Location(),
        BeanValleyWestBeanstalkFloatingItemLocation: BeanValleyWestBeanstalkFloatingItemLocation(),
        BeanstalkUpperCloudLeftChestLocation: BeanstalkUpperCloudLeftChestLocation(),
        BeanstalkUpperCloudRightChestLocation: BeanstalkUpperCloudRightChestLocation(),
        BeanstalkLowerCloudLeftChestLocation: BeanstalkLowerCloudLeftChestLocation(),
        BeanstalkLowerCloudRightChestLocation: BeanstalkLowerCloudRightChestLocation(),
        CasinoGrateGuyPrizeLocation: CasinoGrateGuyPrizeLocation(),
        NimbusShopChestLocation: NimbusShopChestLocation(),
        NimbusInnDreamPrize1Location: NimbusInnDreamPrize1Location(),
        NimbusInnDreamPrize2Location: NimbusInnDreamPrize2Location(),
        NimbusCastleStatueGamePrizeLocation: NimbusCastleStatueGamePrizeLocation(),
        StatueRoomBossFight: StatueRoomBossFight(),
        StatueRoomStarPiece: StatueRoomStarPiece(),
        NimbusCastleOuterPrisonCellarRightNPCLocation: NimbusCastleOuterPrisonCellarRightNPCLocation(),
        NimbusCastleOuterPrisonCellarLeftNPCLocation: NimbusCastleOuterPrisonCellarLeftNPCLocation(),
        NimbusCastleBusinessCentreOccupiedChestLocation: NimbusCastleBusinessCentreOccupiedChestLocation(),
        NimbusCastleCornerBridgeChestLocation: NimbusCastleCornerBridgeChestLocation(),
        NimbusCastleOutOfBoundsChestLocation: NimbusCastleOutOfBoundsChestLocation(),
        NimbusCastleAboveJawfulChestLocation: NimbusCastleAboveJawfulChestLocation(),
        NimbusCastleSingleGoldBirdChestLocation: NimbusCastleSingleGoldBirdChestLocation(),
        NimbusCastleTwoLevelLowerChestLocation: NimbusCastleTwoLevelLowerChestLocation(),
        GiantEggBossFight: GiantEggBossFight(),
        GiantEggStarPiece: GiantEggStarPiece(),
        NimbusCastleGiantEggRewardLocation: NimbusCastleGiantEggRewardLocation(),
        NimbusCastleTwoLevelUpperChestLocation: NimbusCastleTwoLevelUpperChestLocation(),
        NimbusCastleBackHallwayOccupiedChestLocation: NimbusCastleBackHallwayOccupiedChestLocation(),
        NimbusFinalBossFight: NimbusFinalBossFight(),
        NimbusFinalStarPiece: NimbusFinalStarPiece(),
        NimbusCastleBackHallwayLiberatedChestLocation: NimbusCastleBackHallwayLiberatedChestLocation(),
        NimbusCastleBusinessCentreLiberatedChestLocation: NimbusCastleBusinessCentreLiberatedChestLocation(),
        NimbusLandRightSideLocation: NimbusLandRightSideLocation(),
        NimbusLandCrocoItemLocation: NimbusLandCrocoItemLocation(),
        NimbusLandInnerCellarLocation: NimbusLandInnerCellarLocation(),
        VolcanoLavaCoveLeftChestLocation: VolcanoLavaCoveLeftChestLocation(),
        VolcanoLavaCoveRightChestLocation: VolcanoLavaCoveRightChestLocation(),
        VolcanoEarlyProgressChestLeftLocation: VolcanoEarlyProgressChestLeftLocation(),
        VolcanoEarlyProgressChestRightLocation: VolcanoEarlyProgressChestRightLocation(),
        VolcanoEarlyProgressThirdChestLocation: VolcanoEarlyProgressThirdChestLocation(),
        VolcanoLavaPoolLocation: VolcanoLavaPoolLocation(),
        VolcanoReverseRecoilItemLocation: VolcanoReverseRecoilItemLocation(),
        VolcanoRightDonutItemLocation: VolcanoRightDonutItemLocation(),
        VolcanoLeftDonutItemLocation: VolcanoLeftDonutItemLocation(),
        VolcanoSaveRoomLowerChestLocation: VolcanoSaveRoomLowerChestLocation(),
        VolcanoSaveRoomUpperChestLocation: VolcanoSaveRoomUpperChestLocation(),
        VolcanoShopEntranceChestLocation: VolcanoShopEntranceChestLocation(),
        VolcanoBridgeBossFight: VolcanoBridgeBossFight(),
        VolcanoBridgeStarPiece: VolcanoBridgeStarPiece(),
        VolcanoExitBossFight: VolcanoExitBossFight(),
        VolcanoExitStarPiece: VolcanoExitStarPiece(),
        KeepDarkRoomChestLocation: KeepDarkRoomChestLocation(),
        KeepFirstCrocoShopLeftChestLocation: KeepFirstCrocoShopLeftChestLocation(),
        KeepFirstCrocoShopRightChestLocation: KeepFirstCrocoShopRightChestLocation(),
        KeepInvisibleBridgeFrontChestLocation: KeepInvisibleBridgeFrontChestLocation(),
        KeepInvisibleBridgeRightChestLocation: KeepInvisibleBridgeRightChestLocation(),
        KeepInvisibleBridgeLeftChestLocation: KeepInvisibleBridgeLeftChestLocation(),
        KeepInvisibleBridgeBackChestLocation: KeepInvisibleBridgeBackChestLocation(),
        KeepInvisibleBridgeCoin1Location: KeepInvisibleBridgeCoin1Location(),
        KeepInvisibleBridgeCoin2Location: KeepInvisibleBridgeCoin2Location(),
        KeepInvisibleBridgeCoin3Location: KeepInvisibleBridgeCoin3Location(),
        KeepInvisibleBridgeCoin4Location: KeepInvisibleBridgeCoin4Location(),
        KeepXYPlatformsBackLeftChestLocation: KeepXYPlatformsBackLeftChestLocation(),
        KeepXYPlatformsFrontLeftChestLocation: KeepXYPlatformsFrontLeftChestLocation(),
        KeepXYPlatformsFrontRightChestLocation: KeepXYPlatformsFrontRightChestLocation(),
        KeepXYPlatformsBackRightChestLocation: KeepXYPlatformsBackRightChestLocation(),
        KeepElevatorRoomChestLocation: KeepElevatorRoomChestLocation(),
        KeepCannonballRoomFrontRightChestLocation: KeepCannonballRoomFrontRightChestLocation(),
        KeepCannonballRoomBackChestLocation: KeepCannonballRoomBackChestLocation(),
        KeepCannonballFrontLeftChestLocation: KeepCannonballFrontLeftChestLocation(),
        KeepCannonballMidRightChestLocation: KeepCannonballMidRightChestLocation(),
        KeepCannonballMidLeftChestLocation: KeepCannonballMidLeftChestLocation(),
        KeepCannonballCoin1Location: KeepCannonballCoin1Location(),
        KeepCannonballCoin2Location: KeepCannonballCoin2Location(),
        KeepCannonballCoin3Location: KeepCannonballCoin3Location(),
        KeepCannonballCoin4Location: KeepCannonballCoin4Location(),
        KeepCannonballCoin5Location: KeepCannonballCoin5Location(),
        KeepCannonballCoin6Location: KeepCannonballCoin6Location(),
        KeepCannonballCoin7Location: KeepCannonballCoin7Location(),
        KeepCannonballCoin8Location: KeepCannonballCoin8Location(),
        KeepRotatingPlatformsFrontChestLocation: KeepRotatingPlatformsFrontChestLocation(),
        KeepRotatingPlatformsFrontMidLeftChestLocation: KeepRotatingPlatformsFrontMidLeftChestLocation(),
        KeepRotatingPlatformsBackMidRightChestLocation: KeepRotatingPlatformsBackMidRightChestLocation(),
        KeepRotatingPlatformsFrontMidRightChestLocation: KeepRotatingPlatformsFrontMidRightChestLocation(),
        KeepRotatingPlatformsBackMidLeftChestLocation: KeepRotatingPlatformsBackMidLeftChestLocation(),
        KeepRotatingPlatformsBackChestLocation: KeepRotatingPlatformsBackChestLocation(),
        ObstacleCourseFinalFight: ObstacleCourseFinalFight(),
        ObstacleCourseFinalFightStarPiece: ObstacleCourseFinalFightStarPiece(),
        KeepDoorRewardChest1Location: KeepDoorRewardChest1Location(),
        KeepDoorRewardChest2Location: KeepDoorRewardChest2Location(),
        KeepDoorRewardChest3Location: KeepDoorRewardChest3Location(),
        KeepDoorRewardChest4Location: KeepDoorRewardChest4Location(),
        KeepDoorRewardChest5Location: KeepDoorRewardChest5Location(),
        KeepDoorRewardChest6Location: KeepDoorRewardChest6Location(),
        KeepAfterObstaclesBossFight: KeepAfterObstaclesBossFight(),
        KeepAfterObstaclesStarPiece: KeepAfterObstaclesStarPiece(),
        KeepAfterObstaclesBossChestLocation: KeepAfterObstaclesBossChestLocation(),
        KeepChandelierBossFight: KeepChandelierBossFight(),
        KeepChandelierStarPiece: KeepChandelierStarPiece(),
        KeepFinalBossFight: KeepFinalBossFight(),
        KeepFinalStarPiece: KeepFinalStarPiece(),
        OuterFactorySaveRoomChestLocation: OuterFactorySaveRoomChestLocation(),
        FactoryBoltPlatformsChestLocation: FactoryBoltPlatformsChestLocation(),
        FactoryEntranceBossFight: FactoryEntranceBossFight(),
        FactoryEntranceStarPiece: FactoryEntranceStarPiece(),
        FactoryAxemConveyorsChestLocation: FactoryAxemConveyorsChestLocation(),
        FactoryTreasurePitBackChestLocation: FactoryTreasurePitBackChestLocation(),
        FactoryTreasurePitFrontChestLocation: FactoryTreasurePitFrontChestLocation(),
        FactoryBigConveyorRoomFirstChestLocation: FactoryBigConveyorRoomFirstChestLocation(),
        FactoryBigConveyorRoomSecondChestLocation: FactoryBigConveyorRoomSecondChestLocation(),
        FactoryBehindNinjasRightChestLocation: FactoryBehindNinjasRightChestLocation(),
        FactoryBehindNinjasLeftChestLocation: FactoryBehindNinjasLeftChestLocation(),
        FactoryTransitionBossFight: FactoryTransitionBossFight(),
        FactoryTransitionStarPiece: FactoryTransitionStarPiece(),
        InnerFactoryFirstFight: InnerFactoryFirstFight(),
        InnerFactoryFirstFightStarPiece: InnerFactoryFirstFightStarPiece(),
        InnerFactoryToadGiftLocation: InnerFactoryToadGiftLocation(),
        InnerFactorySecondFight: InnerFactorySecondFight(),
        InnerFactorySecondFightStarPiece: InnerFactorySecondFightStarPiece(),
        InnerFactoryThirdFight: InnerFactoryThirdFight(),
        InnerFactoryThirdFightStarPiece: InnerFactoryThirdFightStarPiece(),
        InnerFactoryFourthFight: InnerFactoryFourthFight(),
        InnerFactoryFourthFightStarPiece: InnerFactoryFourthFightStarPiece(),
        FinalBossFight: FinalBossFight(),
    }


    # Only include FinalBossFightStarPiece if win condition is not FACTORY
    # (when FACTORY is the win condition, defeating the final boss ends the game
    # so there's no opportunity to collect the star piece)
    if not world.settings.is_flag_value(WinCondition, WinConditions.FACTORY):
        world.locations[FinalBossFightStarPiece] = FinalBossFightStarPiece()

    if not world.settings.isflag_enabled(SpellsAnywhere):
        included_charaters = [m.value for m in world.settings.get_flag(AvailableCharacters).enabled]
        if MARIO_Ally in included_charaters:
            world.locations = {
                **world.locations,
                MarioSpell1: MarioSpell1(),
                MarioSpell2: MarioSpell2(),
                MarioSpell3: MarioSpell3(),
                MarioSpell4: MarioSpell4(),
                MarioSpell5: MarioSpell5(),
                MarioSpell6: MarioSpell6(),
            }
        if MALLOW_Ally in included_charaters:
            world.locations = {
                **world.locations,
                MallowSpell1: MallowSpell1(),
                MallowSpell2: MallowSpell2(),
                MallowSpell3: MallowSpell3(),
                MallowSpell4: MallowSpell4(),
                MallowSpell5: MallowSpell5(),
                MallowSpell6: MallowSpell6(),
            }
        if GENO_Ally in included_charaters:
            world.locations = {
                **world.locations,
                GenoSpell1: GenoSpell1(),
                GenoSpell2: GenoSpell2(),
                GenoSpell3: GenoSpell3(),
                GenoSpell4: GenoSpell4(),
                GenoSpell5: GenoSpell5(),
                GenoSpell6: GenoSpell6(),
            }
        if BOWSER_Ally in included_charaters:
            world.locations = {
                **world.locations,
                BowserSpell1: BowserSpell1(),
                BowserSpell2: BowserSpell2(),
                BowserSpell3: BowserSpell3(),
                BowserSpell4: BowserSpell4(),
                BowserSpell5: BowserSpell5(),
                BowserSpell6: BowserSpell6(),
            }
        if TOADSTOOL_Ally in included_charaters:
            world.locations = {
                **world.locations,
                ToadstoolSpell1: ToadstoolSpell1(),
                ToadstoolSpell2: ToadstoolSpell2(),
                ToadstoolSpell3: ToadstoolSpell3(),
                ToadstoolSpell4: ToadstoolSpell4(),
                ToadstoolSpell5: ToadstoolSpell5(),
                ToadstoolSpell6: ToadstoolSpell6(),
            }

    # Only add Super Jump reward locations if Super Jump spell is enabled
    available_spells = world.settings.get_flag(AvailableSpells)
    super_jump_enabled = any(
        spell_opt.value == SuperJumpSpell for spell_opt in available_spells.enabled
    )
    if super_jump_enabled:
        world.locations = {
            **world.locations,
            MonstroFirstSuperJumpRewardLocation: MonstroFirstSuperJumpRewardLocation(),
            MonstroSecondSuperJumpRewardLocation: MonstroSecondSuperJumpRewardLocation(),
        }

    if world.settings.isflag_enabled(FixKnifeGuy):
        world.locations = {
            **world.locations,
            BoosterTowerKnifeGuy2PrizeLocation: BoosterTowerKnifeGuy2PrizeLocation(),
        }

    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        fwshop = FireworksShopItemLocation()
        fwshop._originally_held = ProgressiveFireworksPrize
        fwshop.set_prize(ProgressiveFireworksPrize())
        world.locations = {
            **world.locations,
            FireworksShopItemLocation: fwshop,
            PurtendStoreLocation: PurtendStoreLocation(),
            CookieTraderLocation: CookieTraderLocation(),
        }
        world.get_item(FireworksItem).set_price(0)
        world.get_item(ShinyStoneItem).set_price(0)
        world.get_item(CarboCookieItem).set_price(0)
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        world.locations = {
            **world.locations,
            FireworksShopItemLocation: FireworksShopItemLocation(),
        }
        world.get_item(FireworksItem).set_price(0)
        world.get_item(ShinyStoneItem).set_price(0)
        world.get_item(CarboCookieItem).set_price(0)

    strchars = world.settings.get_flag(StartingCharacters)
    startmax = len(strchars.enabled)
    if startmax >= 2:
        world.locations = {
            **world.locations,
            StartingCharacter2: StartingCharacter2(),
        }
    if startmax >= 3:
        world.locations = {
            **world.locations,
            StartingCharacter3: StartingCharacter3(),
        }
    if startmax >= 4:
        world.locations = {
            **world.locations,
            StartingCharacter4: StartingCharacter4(),
        }
    if startmax >= 5:
        world.locations = {
            **world.locations,
            StartingCharacter5: StartingCharacter5(),
        }
    # Resolve starting character selections (handles "Random_X" values)
    # and assign prizes to the starting character locations
    resolved_allies = strchars.resolve_random_selections()  # Uses seeded global random
    # Map allies by index to their prize classes (allies are all the same type)
    ally_to_prize: dict[int, type] = {
        MARIO_Ally.index: MarioRecruitmentPrize,
        MALLOW_Ally.index: MallowRecruitmentPrize,
        GENO_Ally.index: GenoRecruitmentPrize,
        BOWSER_Ally.index: BowserRecruitmentPrize,
        TOADSTOOL_Ally.index: ToadstoolRecruitmentPrize,
    }
    starting_char_locations = [
        StartingCharacter1,
        StartingCharacter2,
        StartingCharacter3,
        StartingCharacter4,
        StartingCharacter5,
    ]
    for i, ally in enumerate(resolved_allies):
        if i < len(starting_char_locations):
            loc_type = starting_char_locations[i]
            if loc_type in world.locations:
                prize_cls = ally_to_prize.get(ally.index)
                if prize_cls:
                    world.locations[loc_type].set_prize(prize_cls())

    if world.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
        world.locations = {
            **world.locations,
            GarroFreeItem: GarroFreeItem(),
        }

    # Optionally include remake content.
    if world.settings.get_flag(Remake).enabled:
        world.locations = {
            **world.locations,
            PostgameVoucherLocation: PostgameVoucherLocation(),
            MushroomWayLeftItemRemake: MushroomWayLeftItemRemake(),
            MushroomWayRightItemRemake: MushroomWayRightItemRemake(),
            InnerMinesPostgameBossFight: InnerMinesPostgameBossFight(),
            InnerMinesPostgameStarPiece: InnerMinesPostgameStarPiece(),
            InnerMinesPostgameDrop: InnerMinesPostgameDrop(),
            BoosterTowerIndoorBossFightRemake: BoosterTowerIndoorBossFightRemake(),
            BoosterTowerIndoorStarPieceRemake: BoosterTowerIndoorStarPieceRemake(),
            BoosterTowerRemakeBossFightPrizeLocation: BoosterTowerRemakeBossFightPrizeLocation(),
            MarrymoreBossFightRemake: MarrymoreBossFightRemake(),
            MarrymoreBossFightStarPieceRemake: MarrymoreBossFightStarPieceRemake(),
            MarrymoreBossFightRemakeItemDrop: MarrymoreBossFightRemakeItemDrop(),
            ShipPostgameBossFight: ShipPostgameBossFight(),
            ShipPostgameFightItemDrop: ShipPostgameFightItemDrop(),
            ShipPostgameStarPiece: ShipPostgameStarPiece(),
            TempleBossFightPostgame: TempleBossFightPostgame(),
            TempleBossFightStarPiecePostgame: TempleBossFightStarPiecePostgame(),
            TemplePostgameFightItemDrop: TemplePostgameFightItemDrop(),
            DojoFifthFight: DojoFifthFight(),
            DojoFifthFightStarPiece: DojoFifthFightStarPiece(),
            MonstroDojoPostgameClearRewardLocation: MonstroDojoPostgameClearRewardLocation(),
            LandsEndCaveSideRemake: LandsEndCaveSideRemake(),
        }
        # Only include Monstro sealed door postgame locations if win condition is not SEALED
        # (when SEALED is the win condition, defeating the sealed door boss ends the game
        # so there's no opportunity to collect postgame rewards)
        if not world.settings.is_flag_value(WinCondition, WinConditions.SEALED):
            world.locations[MonstroSealedDoorBossFightPostgame] = (
                MonstroSealedDoorBossFightPostgame()
            )
            world.locations[MonstroSealedDoorStarPiecePostgame] = (
                MonstroSealedDoorStarPiecePostgame()
            )
            world.locations[MonstroSealedDoorClearRewardLocationPostgame] = (
                MonstroSealedDoorClearRewardLocationPostgame()
            )
        # Checks for postgame-unlocking bosses by default expect an impossible value.
        # Enabling the remake flag sets it to the correct value, 7.
        world.event_scripts.get_script_by_id(E0225_CHECK_VOUCHER_UNLOCK).set_contents([
            Return()
        ])
        room = world.rooms._rooms[R204_MUSHROOM_WAY_AREA_02]
        assert room is not None
        room.get_npc_by_target_id(NPC_10).set_visible(True)
        room.get_npc_by_target_id(NPC_11).set_visible(True)
        room = world.rooms._rooms[R142_LANDS_END_AREA_05_SKY_BRIDGE]
        assert room is not None
        room.get_npc_by_target_id(NPC_19).set_visible(True)


    invisible_item_pool = [
        MariosPadBedFlag,
        RoseTownSignFlag,
        YosterIsleGoalFlag,
        MariosPadSteamwhistleFlag,
        MariosPadLanternFlag,
        MariosPadHatFlag,
        MushroomWayTreeFlag,
        MushroomKingdomSignFlag,
        MushroomKingdomEmptyHouseFlag,
        ChancellorThroneFlag,
        BanditsWayFlowerFlag,
        KeroStairsFlag,
        KeroGateFlag,
        MidasTreesFlag,
        TadpoleCabinetFlag,
        RoseWayDirtPatchFlag,
        RoseTownHydrantFlag,
        RoseTownSinkFlag,
        RoseTownBowserFlag,
        RoseTownGardenerHydrantFlag,
        RoseTownGardenerBucketFlag,
        RoseTownGardenerLeafFlag,
        ForestMazeSecretStumpFlag,
        ForestMazeSecretMushroomsFlag,
        ForestMazeSecretWigglerFlag,
        PipeVaultExteriorFlag,
        PipeVaultRedPipeFlag,
        YosterIsleHutFlag,
        MolevilleHydrantFlag,
        MolevilleMountainBushFlag,
        MolevilleBedFlag,
        MolevilleMinesArrowsFlag,
        MolevilleMinesCeilingFlag,
        MolevilleMinesEntryFlag,
        BoosterPassCornerBushFlag,
        BoosterTowerExteriorSignFlag,
        BoosterTowerDeskFlag,
        BoosterTowerMasherRoomFlag,
        BoosterTowerCurtainFlag,
        BoosterTowerThwompInvisibleFlag,
        BoosterTowerBrokenFrameFlag,
        BoosterTowerBeetleCageFlag,
        BoosterTowerToyBoxFlag,
        MarrymoreOutsideCrateFlag,
        MarrymoreHallwayFlag,
        MarrymoreSuiteBedFlag,
        MarrymoreKitchenFlag,
        MarrymoreFireplaceFlag,
        MarrymoreOrganFlag,
        MarrymoreAltarFlag,
        StarHillNorthStarFlag,
        SeasideTownAnchorFlag,
        SeasideTownHydrantFlag,
        SeasideTownBucketFlag,
        SeasideTownFlowersFlag,
        SeasideTownShedBoxFlag,
        SeaArrowFlag,
        SeaBoxesFlag,
        SeaStalagnateFlag,
        SeaUnderwaterSailFlag,
        ShipBarrelPileFlag,
        ShipDoorMarkerFlag,
        ShipButtonFlag,
        ShipSwitchFlag,
        LandsEndPlatformFlag,
        LandsEndCannonFlag,
        LandsEndArrowFlag,
        LandsEndHillFlag,
        LandsEndTwoHillFlag,
        LandsEndStalagmiteFlag,
        LandsEndCliffBushFlag,
        LandsEndSignFlag,
        DojoBonsaiFlag,
        MonstroEntranceSignFlag,
        MonstroBatFlag,
        MonstroFanFlag,
        MonstroShellFlag,
        BeanValleyPipeFlag,
        BeanValleyBeanstalkBlockFlag,
        CasinoBellFlag,
        NimbusGoldGoombaFlag,
        NimbusInnLobbyFlag,
        NimbusPlantFlag,
        NimbusBirdFlag,
        NimbusHotSpringsFlag,
        VolcanoShipsFlag,
        KeepPostObstacleBossRoomFlag,
        KeepThwompFlag,
        FactoryCanopyFlag,
        FactoryLugnutFlag,
        FactoryTrampolineFlag,
        FactoryButtonFlag,
    ]

    # Check if invisible item locations have already been initialized
    # This prevents duplication when set_locations is called multiple times during shuffle retries
    if world._invisible_item_locations is not None:
        # Reuse the stored invisible item locations - just add them to world.locations
        invisible_flag_locations = world._invisible_item_locations
    else:
        # First time initialization - create invisible item locations and modify rooms
        invisible_flag_locations = {}

        # Check for debug override of invisible flags
        debug_invisible_flags: list[type] | None = None
        if world.settings.debug_mode:
            from randomizer.debug import load_debug_config, get_location_class
            config = load_debug_config()
            flag_names = config.get("invisible_flags", [])
            if len(flag_names) == 3:
                debug_invisible_flags = []
                for name in flag_names:
                    cls = get_location_class(name)
                    if cls is not None:
                        debug_invisible_flags.append(cls)
                    else:
                        debug_invisible_flags = None
                        break

        for i in range(0, 3):
            # choose the three invisible item locations
            if debug_invisible_flags is not None:
                location_cls = debug_invisible_flags[i]
            elif not world.settings.isflag_enabled(InvisibleFlagsSetting):
                location_cls = invisible_item_pool[i]
            else:
                # Filter out locations in rooms that are too full (>27 objects)
                valid_pool = []
                for loc_cls in invisible_item_pool:
                    # Create a temporary instance to check room capacity
                    temp_loc = loc_cls(0)
                    can_use = True
                    for r in temp_loc._rooms:
                        room = world.rooms._rooms[r]
                        if room is not None and len(room.objects) > 27:  # 0x1B, leaves no room for +0x14
                            can_use = False
                            break
                    if can_use:
                        valid_pool.append(loc_cls)

                if not valid_pool:
                    raise Exception(f"No valid rooms available for invisible flag {i+1}! All candidate rooms are too full.")

                location_cls = random.choice(valid_pool)

            location = cast(InvisibleFlagLocation, location_cls(i))
            for r in location._rooms:
                # place them in rooms and set visibility triggers
                room = world.rooms._rooms[r]
                assert room is not None

                # Double-check room capacity before creating AreaObject
                num_objects = len(room.objects)
                calculated_id = num_objects + 0x14
                if calculated_id > 0x2F:
                    raise Exception(
                        f"Room {r} ({location_cls.__name__}) has too many objects!\n"
                        f"  Objects in room: {num_objects}\n"
                        f"  Calculated NPC ID: 0x{calculated_id:02X} (requires <= 0x2F)\n"
                        f"  Max objects allowed: 27 (0x1B)"
                    )

                n = location.npc
                n_id = AreaObject(calculated_id)
                n.set_visible(False)
                world.event_scripts.get_script_by_id(
                    E0091_INVISIBLE_ITEM_SUMMONER
                ).insert_before_nth_command(0, SummonObjectToSpecificLevel(n_id, r))
                room.add_object(location.npc)
            # set hint text
            if i == 0:
                world.update_dialog(
                    DI1108_RESERVED_FOR_DRYBONESFLAG_HINT,
                    "DRY BONES:\n" + location.clue_text,
                )
            elif i == 1:
                world.update_dialog(
                    DI1109_RESERVED_FOR_GREAPERFLAG_HINT,
                    "GREAPER:\n" + location.clue_text,
                )
            elif i == 2:
                world.update_dialog(
                    DI1107_RESERVED_FOR_BIGBOOFLAG_HINT,
                    "THE BIG BOO:\n" + location.clue_text,
                )
            invisible_flag_locations[location_cls] = location

        # Store the invisible item locations for reuse on retry
        world._invisible_item_locations = invisible_flag_locations

    world.locations = {**world.locations, **invisible_flag_locations}
    
    world.chest_locations = [
        loc for loc in world.locations.values() if isinstance(loc, TreasureChestLocation)
    ]
    world.standard_locations = [
        loc for loc in world.locations.values() if isinstance(loc, (TreasureChestLocation, EventLocation, StandingLocation, RiverLocation, BoosterHillLocation, FrogDiscipleLocation))
    ]
    world.coin_locations = [
        loc for loc in world.locations.values() if isinstance(loc, (TreasureChestLocation, EventLocation, StandingLocation))
    ]
    world.spell_locations = [
        loc for loc in world.locations.values() if isinstance(loc, SpellSlotLocation)
    ]
    world.boss_fight_locations = [
        loc for loc in world.locations.values() if isinstance(loc, BossFightLocation)
    ]
    world.star_piece_locations = [
        loc for loc in world.locations.values() if isinstance(loc, StarPieceLocation)
    ]
    world.extra_star_piece_locations = copy(world.star_piece_locations)
    if world.settings.isflag_enabled(StarPieceAvailability):
        world.extra_star_piece_locations.extend(world.standard_locations)
        world.event_scripts.get_command_by_identifier("EVENT_947_jmp_to_event_107", JmpToEvent).set_destination(E0949_FROGFUCIUS_HINT_TREASURE_CHESTS)
    world.key_item_locations = [
        loc for loc in world.locations.values() if isinstance(loc, KeyItemLocation)
    ]
    world.extra_key_item_locations = copy(world.key_item_locations)
    if world.settings.isflag_enabled(KeyItemsAnywhere):
        world.extra_key_item_locations.extend(world.standard_locations)
    world.character_recruitment_locations = [
        loc for loc in world.locations.values() if isinstance(loc, CharacterRecruitmentLocation)
    ]