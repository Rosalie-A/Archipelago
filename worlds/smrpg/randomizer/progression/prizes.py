from __future__ import annotations
from re import M
from typing import TYPE_CHECKING

from ..data.overworld_scripts.event.scripts.script_3645 import NPC_2
from ..data.variables.dialog_names import *
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScript,
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    Return,
    SetVarToConst,
    JmpToEvent,
    Inc,
    SetBit,
    CharacterJoinsParty,
    ClearBit,
    RunDialog,
    ApplySolidityModToLevel,
    ApplyTileModToLevel,
    RemoveObjectFromSpecificLevel,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_3
from ..data.variables.variable_names import *
from ..data.variables.overworld_sfx_names import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    MARIO,
    MALLOW,
    GENO,
    BOWSER,
    TOADSTOOL,
)
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    FormationMember,
)
from ..data.packs.pack_collection import (
    FORM0055,
    FORM0096,
    FORM0123,
    FORM0124,
    FORM0137,
    FORM0216,
    FORM0217,
    FORM0251,
    FORM0258,
    FORM0259,
    FORM0260,
    FORM0261,
    FORM0266,
    FORM0267,
    FORM0268,
    FORM0269,
    FORM0271,
    FORM0273,
    FORM0274,
    FORM0276,
    FORM0277,
    FORM0278,
    FORM0279,
    FORM0281,
    FORM0282,
    FORM0283,
    FORM0284,
    FORM0285,
    FORM0286,
    FORM0287,
    FORM0288,
    FORM0289,
    FORM0290,
    FORM0291,
    FORM0292,
    FORM0293,
    FORM0294,
    FORM0295,
    FORM0296,
    FORM0297,
    FORM0298,
    FORM0299,
    FORM0314,
    FORM0315,
    FORM0316,
    FORM0317,
    FORM0322,
)
from ..data.items.items import (
    CrystalShardItem,
    ExtraShinyStoneItem,
    HammerItem,
    FroggieStickItem,
    NokNokShellItem,
    PunchGloveItem,
    FingerShotItem,
    CymbalsItem,
    ChompItem,
    MasherItem,
    ChompShellItem,
    StayVoucherItem,
    SuperHammerItem,
    HandGunItem,
    WhompGloveItem,
    SlapGloveItem,
    TroopaShellItem,
    ParasolItem,
    HurlyGlovesItem,
    DoublePunchItem,
    RibbitStickItem,
    SpikedLinkItem,
    MegaGloveItem,
    WarFanItem,
    HandCannonItem,
    StickyGloveItem,
    UltraHammerItem,
    SuperSlapItem,
    DrillClawItem,
    StarGunItem,
    SonicCymbalItem,
    LazyShellItem,
    FryingPanItem,
    LuckyHammerItem,
    ShirtItem,
    PantsItem,
    ThickShirtItem,
    ThickPantsItem,
    MegaShirtItem,
    MegaPantsItem,
    WorkPantsItem,
    MegaCapeItem,
    HappyShirtItem,
    HappyPantsItem,
    HappyCapeItem,
    HappyShellItem,
    PolkaDressItem,
    SailorShirtItem,
    SailorPantsItem,
    SailorCapeItem,
    NauticaDressItem,
    CourageShellItem,
    FuzzyShirtItem,
    FuzzyPantsItem,
    FuzzyCapeItem,
    FuzzyDressItem,
    FireShirtItem,
    FirePantsItem,
    FireCapeItem,
    FireShellItem,
    FireDressItem,
    HeroShirtItem,
    PrincePantsItem,
    StarCapeItem,
    HealShellItem,
    RoyalDressItem,
    SuperSuitItem,
    ZoomShoesItem,
    SafetyBadgeItem,
    JumpShoesItem,
    SafetyRingItem,
    AmuletItem,
    ScroogeRingItem,
    ExpBoosterItem,
    AttackScarfItem,
    RareScarfItem,
    BtubRingItem,
    AntidotePinItem,
    WakeUpPinItem,
    FearlessPinItem,
    TrueformPinItem,
    CoinTrickItem,
    GhostMedalItem,
    JinxBeltItem,
    FeatherItem,
    TroopaPinItem,
    SignalRingItem,
    QuartzCharmItem,
    MushroomItem,
    MidMushroomItem,
    MaxMushroomItem,
    HoneySyrupItem,
    MapleSyrupItem,
    RoyalSyrupItem,
    PickMeUpItem,
    AbleJuiceItem,
    BracerItem,
    EnergizerItem,
    YoshiAdeItem,
    RedEssenceItem,
    KerokeroColaItem,
    YoshiCookieItem,
    PureWaterItem,
    SleepyBombItem,
    BadMushroomItem,
    FireBombItem,
    IceBombItem,
    FlowerTabItem,
    FlowerJarItem,
    FlowerBoxItem,
    YoshiCandyItem,
    FroggieDrinkItem,
    MukuCookieItem,
    ElixirItem,
    MegalixirItem,
    SeeYaItem,
    TempleKeyItem,
    GoodieBagItem,
    EarlierTimesItem,
    FreshenUpItem,
    RareFrogCoinItem,
    WalletItem,
    CricketPieItem,
    RockCandyItem,
    CastleKey1Item,
    CastleKey2Item,
    BambinoBombItem,
    RoomKeyItem,
    ElderKeyItem,
    ShedKeyItem,
    FrightBombItem,
    BeetleBoxItem,
    LuckyJewelItem,
    CrystallineItem,
    PowerBlastItem,
    WiltShroomItem,
    RottenMushItem,
    MoldyMushItem,
    SeedItem,
    FertilizerItem,
    BigBooFlagItem,
    DryBonesFlagItem,
    GreaperFlagItem,
    CricketJamItem,
    FireworksItem,
    BrightCardItem,
    StarEggItem,
    ShoesItem,
    BroochItem,
    RingItem,
    CrownItem,
    LazyShellItem2,
    MushroomItem2,
    WonderChompItem,
    Stella023Item,
    SageStickItem,
    TeamworkBandItem,
    EnduringBroochItem,
)
from ..data.variables.variable_names import *
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *
from ..data.variables.battlefield_names import *
from ..data.enemies.enemies import *
from ..data.variables.battle_event_names import *
from ..data.physical_objects.bosses import *
from ..data.physical_objects.henchmen import *
from ..data.physical_objects.characters import (
    MarioCharacterNPC,
    MallowCharacterNPC,
    GenoCharacterNPC,
    BowserCharacterNPC,
    ToadstoolCharacterNPC,
)
from ..data.allies.allies import (
    MARIO_Ally,
    MALLOW_Ally,
    GENO_Ally,
    BOWSER_Ally,
    TOADSTOOL_Ally,
)
from ..types.prize import (
    BossFightHenchman,
    CharacterName,
    FrogCoinQuantityPrize,
    EXPStarPrize,
    StandardPrize,
    CoinQuantityPrize,
    SlotsPrize,
    BossFightPrize,
    CharacterPrize,
    StarPiecePrize,
    ItemPrize,
    SpellPrize,
    MimicFightInitiatorPrize,
    TreasureHunterNickname,
    ProgressiveItemPrize,
    WeddingGearPrize,
    SpecialItemPrizeType,
    KeyPrize,
)
from ..data.spells.spells import (
    JumpSpell,
    FireOrbSpell,
    SuperJumpSpell,
    SuperFlameSpell,
    UltraJumpSpell,
    UltraFlameSpell,
    ThunderboltSpell,
    HPRainSpell,
    PsychopathSpell,
    ShockerSpell,
    SnowySpell,
    PsychBombSpell,
    GenoBeamSpell,
    GenoBoostSpell,
    GenoWhirlSpell,
    GenoBlastSpell,
    GenoFlashSpell,
    TerrorizeSpell,
    PoisonGasSpell,
    CrusherSpell,
    BowserCrushSpell,
    TherapySpell,
    GroupHugSpell,
    MuteSpell,
    SleepyTimeSpell,
    ComeBackSpell,
    StarRainSpell,
)
from ..data.variables.overworld_sfx_names import *
from ..data.physical_objects.items import *

# Note: Gating flags are imported lazily in _get_gating_flags() to avoid circular import
# (flags.py → prizelocations.py → prizes.py → flags.py)

_gating_flags_cache: dict | None = None


def _get_gating_flags():
    """Lazily import and cache gating flags to avoid circular import."""
    global _gating_flags_cache
    if _gating_flags_cache is None:
        from ..types.flags import (
            BanditsWayGating,
            BanditsWayGate,
            KeroSewersGate,
            KeroSewersGating,
            BoosterTowerGate,
            BoosterTowerGating,
            PipeVaultGate,
            PipeVaultGating,
            Moleville1Gate,
            Moleville1Gating,
            ForestMazeGate,
            ForestMazeGating,
            BoosterHillGate,
            BoosterHillGating,
            MarrymoreGate,
            MarrymoreGating,
            YaridovichGate,
            YaridovichGating,
            SeaGate,
            SeaGating,
            LandsEndGate,
            LandsEndGating,
            BelomeTempleGate,
            BelomeTempleGating,
            MonstroTownGate,
            MonstroTownGating,
            NimbusGate,
            NimbusGating,
            BarrelVolcanoGate,
            BarrelVolcanoGating,
            BowsersKeepGate,
            BowsersKeepGating,
            FactoryGate,
            FactoryGating,
        )

        _gating_flags_cache = {
            "BanditsWayGating": BanditsWayGating,
            "BanditsWayGate": BanditsWayGate,
            "KeroSewersGate": KeroSewersGate,
            "KeroSewersGating": KeroSewersGating,
            "BoosterTowerGate": BoosterTowerGate,
            "BoosterTowerGating": BoosterTowerGating,
            "PipeVaultGate": PipeVaultGate,
            "PipeVaultGating": PipeVaultGating,
            "Moleville1Gate": Moleville1Gate,
            "Moleville1Gating": Moleville1Gating,
            "ForestMazeGate": ForestMazeGate,
            "ForestMazeGating": ForestMazeGating,
            "BoosterHillGate": BoosterHillGate,
            "BoosterHillGating": BoosterHillGating,
            "MarrymoreGate": MarrymoreGate,
            "MarrymoreGating": MarrymoreGating,
            "YaridovichGate": YaridovichGate,
            "YaridovichGating": YaridovichGating,
            "SeaGate": SeaGate,
            "SeaGating": SeaGating,
            "LandsEndGate": LandsEndGate,
            "LandsEndGating": LandsEndGating,
            "BelomeTempleGate": BelomeTempleGate,
            "BelomeTempleGating": BelomeTempleGating,
            "MonstroTownGate": MonstroTownGate,
            "MonstroTownGating": MonstroTownGating,
            "NimbusGate": NimbusGate,
            "NimbusGating": NimbusGating,
            "BarrelVolcanoGate": BarrelVolcanoGate,
            "BarrelVolcanoGating": BarrelVolcanoGating,
            "BowsersKeepGate": BowsersKeepGate,
            "BowsersKeepGating": BowsersKeepGating,
            "FactoryGate": FactoryGate,
            "FactoryGating": FactoryGating,
        }
    return _gating_flags_cache


# Convenience function to get a specific flag
def _gf(name: str):
    """Get a gating flag by name."""
    return _get_gating_flags()[name]


if TYPE_CHECKING:
    from ..types.gameworld import GameWorld

### Real items ###


class HammerPrize(ItemPrize):
    item = HammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject
    


class FroggiestickPrize(ItemPrize):
    item = FroggieStickItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff", description="It looks pretty good at bonking."
    )
    _monstro_shuffle = True
    _model = StickObject


class NokNokShellPrize(ItemPrize):
    item = NokNokShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell", description="There's no turtle inside of it."
    )
    _model = GreenShellObject


class PunchGlovePrize(ItemPrize):
    item = PunchGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class FingerShotPrize(ItemPrize):
    item = FingerShotItem
    _nickname = TreasureHunterNickname(
        nickname="Pellet Shooter", description="It was probably owned by a kid."
    )


class CymbalsPrize(ItemPrize):
    item = CymbalsItem
    _nickname = TreasureHunterNickname(
        nickname="Percussion Plate", description="I bet it could get pretty loud."
    )
    _model = MusicObject


class ChompPrize(ItemPrize):
    item = ChompItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Chain Chomp", description="It's hungry to stir up some trouble."
    )
    _monstro_shuffle = True
    _model = ChompObject


class MasherPrize(ItemPrize):
    item = MasherItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject


class ChompShellPrize(ItemPrize):
    item = ChompShellItem
    _nickname = TreasureHunterNickname(
        nickname="Chomp Exoskeleton",
        description="I didn't even know those things\n could shed their skin.",
    )
    _model = ChompObject


class SuperHammerPrize(ItemPrize):
    item = SuperHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject


class HandGunPrize(ItemPrize):
    item = HandGunItem
    _nickname = TreasureHunterNickname(
        nickname="BB Gun", description="I'll throw in some ammo, too."
    )


class WhompGlovePrize(ItemPrize):
    item = WhompGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class SlapGlovePrize(ItemPrize):
    item = SlapGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class TroopaShellPrize(ItemPrize):
    item = TroopaShellItem
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _model = RedShellObject


class ParasolPrize(ItemPrize):
    item = ParasolItem
    _nickname = TreasureHunterNickname(
        nickname="Umbrella", description="There's no turtle inside of it."
    )
    _model = ParasolObject


class HurlyGlovesPrize(ItemPrize):
    item = HurlyGlovesItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class DoublePunchPrize(ItemPrize):
    item = DoublePunchItem
    _nickname = TreasureHunterNickname(
        nickname="Rocket Launcher",
        description="Be careful, it could take your\n hands clean off.",
    )
    _model = GloveObject


class RibbitStickPrize(ItemPrize):
    item = RibbitStickItem
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff", description="It looks pretty good at bonking."
    )
    _model = StickObject


class SpikedLinkPrize(ItemPrize):
    item = SpikedLinkItem
    _nickname = TreasureHunterNickname(
        nickname="Chain Chomp", description="This one's got thorns on it."
    )
    _model = ChompObject


class MegaGlovePrize(ItemPrize):
    item = MegaGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class WarFanPrize(ItemPrize):
    item = WarFanItem
    _nickname = TreasureHunterNickname(
        nickname="Spiked Fan", description="Pretty, but deadly!"
    )
    _model = FanObject


class HandCannonPrize(ItemPrize):
    item = HandCannonItem
    _nickname = TreasureHunterNickname(
        nickname="Cannon Launcher", description="You need strong elbows for this!"
    )


class StickyGlovePrize(ItemPrize):
    item = StickyGloveItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class UltraHammerPrize(ItemPrize):
    item = UltraHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject


class SuperSlapPrize(ItemPrize):
    item = SuperSlapItem
    _nickname = TreasureHunterNickname(
        nickname="Glove", description="You don't drink water out of it."
    )
    _model = GloveObject


class DrillClawPrize(ItemPrize):
    item = DrillClawItem
    _nickname = TreasureHunterNickname(
        nickname="Drilling Appendage",
        description="I bet you could do some real damage\n with this.",
    )
    _model = GloveObject


class StarGunPrize(ItemPrize):
    item = StarGunItem
    _nickname = TreasureHunterNickname(
        nickname="Celestial Launcher",
        description="I bet you could do some real damage\n with this.",
    )
    _model = TinyStarObject


class SonicCymbalPrize(ItemPrize):
    item = SonicCymbalItem
    _nickname = TreasureHunterNickname(
        nickname="Psych Percussion",
        description="This could catch monsters\n off-guard.",
    )
    _model = MusicObject


class LazyShellWeaponPrize(ItemPrize):
    item = LazyShellItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _monstro_shuffle = True
    _model = RedShellObject


class FryingPanPrize(ItemPrize):
    item = FryingPanItem
    _nickname = TreasureHunterNickname(
        nickname="Metal Plate", description="Don't know what it’s used for."
    )
    _model = FryingPanObject


class WonderChompPrize(ItemPrize):
    item = WonderChompItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Chomp",
        description="It's hungry to stir up some BIG\n trouble.",
    )
    remake_only = True
    _monstro_shuffle = True
    _model = ChompObject


class Stella023Prize(ItemPrize):
    item = Stella023Item
    _nickname = TreasureHunterNickname(
        nickname="Cool Gun", description="Why does it remind me of a train?"
    )
    remake_only = True
    _monstro_shuffle = True
    _model = TinyStarObject


class SageStickPrize(ItemPrize):
    item = SageStickItem
    _nickname = TreasureHunterNickname(
        nickname="Caster's Staff", description="It looks pretty good at bonking."
    )
    remake_only = True
    _monstro_shuffle = True
    _model = StickObject


class LuckyHammerPrize(ItemPrize):
    item = LuckyHammerItem
    _nickname = TreasureHunterNickname(
        nickname="Hammer", description="I'm not sure if it does anything\n else."
    )
    _model = HammerObject


class ShirtPrize(ItemPrize):
    item = ShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Overalls", description="Don't go to work without 'em!"
    )


class PantsPrize(ItemPrize):
    item = PantsItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Pants", description="They're comfy and easy to wear."
    )


class ThickShirtPrize(ItemPrize):
    item = ThickShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue/Red Overalls", description="They look pretty sturdy."
    )


class ThickPantsPrize(ItemPrize):
    item = ThickPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Pants", description="They're comfy and easy to wear."
    )


class MegaShirtPrize(ItemPrize):
    item = MegaShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls", description="You're sure to stand out in these!"
    )


class MegaPantsPrize(ItemPrize):
    item = MegaPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Striped Red Pants",
        description="Made from only the finest threads\n in Mysidia.",
    )


class WorkPantsPrize(ItemPrize):
    item = WorkPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Stained Pants", description="They look a bit worn out."
    )


class MegaCapePrize(ItemPrize):
    item = MegaCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Cape", description="It looks pretty cool, right?"
    )


class HappyShirtPrize(ItemPrize):
    item = HappyShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls", description="You're sure to stand out in these!"
    )


class HappyPantsPrize(ItemPrize):
    item = HappyPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Pink Pants", description="They're all the rage these days!"
    )


class HappyCapePrize(ItemPrize):
    item = HappyCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Rainbow Cape", description="I'd be proud to wear this!"
    )


class HappyShellPrize(ItemPrize):
    item = HappyShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell", description="There's no turtle inside of it."
    )
    _model = GreenShellObject


class PolkaDressPrize(ItemPrize):
    item = PolkaDressItem
    _nickname = TreasureHunterNickname(
        nickname="Pink Dress", description="For serious fashionistas."
    )


class SailorShirtPrize(ItemPrize):
    item = SailorShirtItem
    _nickname = TreasureHunterNickname(
        nickname="White Overalls", description="Built for life on the sea."
    )


class SailorPantsPrize(ItemPrize):
    item = SailorPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Pants", description="They're comfy and easy to wear."
    )


class SailorCapePrize(ItemPrize):
    item = SailorCapeItem
    _nickname = TreasureHunterNickname(
        nickname="White Cape", description="Built for life on the sea."
    )


class NauticaDressPrize(ItemPrize):
    item = NauticaDressItem
    _nickname = TreasureHunterNickname(
        nickname="School Uniform", description="The neckerchief is included."
    )


class CourageShellPrize(ItemPrize):
    item = CourageShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell", description="There's no turtle inside of it."
    )
    _model = GreenShellObject


class FuzzyShirtPrize(ItemPrize):
    item = FuzzyShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Green Overalls", description="Made of the finest fleece."
    )


class FuzzyPantsPrize(ItemPrize):
    item = FuzzyPantsItem
    _nickname = TreasureHunterNickname(
        nickname="Striped Red Pants",
        description="Made from only the finest threads\n in Mysidia.",
    )


class FuzzyCapePrize(ItemPrize):
    item = FuzzyCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Cape", description="Made of the finest fleece."
    )


class FuzzyDressPrize(ItemPrize):
    item = FuzzyDressItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Dress", description="Made of the finest fleece."
    )


class FireShirtPrize(ItemPrize):
    item = FireShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Overalls", description="You're sure to stand out in these!"
    )


class FirePantsPrize(ItemPrize):
    item = FirePantsItem
    _nickname = TreasureHunterNickname(
        nickname="Red Pants", description="Stylish AND warm!"
    )


class FireCapePrize(ItemPrize):
    item = FireCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Cape", description="The pattern on it is pretty cool."
    )


class FireShellPrize(ItemPrize):
    item = FireShellItem
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _model = RedShellObject


class FireDressPrize(ItemPrize):
    item = FireDressItem
    _nickname = TreasureHunterNickname(
        nickname="Red Dress", description="The pattern on it is pretty cool."
    )


class HeroShirtPrize(ItemPrize):
    item = HeroShirtItem
    _nickname = TreasureHunterNickname(
        nickname="Blue/Red Overalls", description="They look pretty sturdy."
    )


class PrincePantsPrize(ItemPrize):
    item = PrincePantsItem
    _nickname = TreasureHunterNickname(
        nickname="Flash Pants", description="You'll look like a superhero in\n these!"
    )
    _model = CrownObject


class StarCapePrize(ItemPrize):
    item = StarCapeItem
    _nickname = TreasureHunterNickname(
        nickname="Freedom Cape", description="It's red, white, and blue."
    )
    _model = TinyStarObject


class HealShellPrize(ItemPrize):
    item = HealShellItem
    _nickname = TreasureHunterNickname(
        nickname="Green Shell", description="There's no turtle inside of it."
    )
    _model = GreenShellObject


class RoyalDressPrize(ItemPrize):
    item = RoyalDressItem
    _nickname = TreasureHunterNickname(
        nickname="Fancy Dress", description="Check out the gold trim!"
    )
    _model = CrownObject


class SuperSuitPrize(ItemPrize):
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    item = SuperSuitItem
    _nickname = TreasureHunterNickname(
        nickname="Jumpsuit", description="It looks pretty powerful, right?"
    )
    _monstro_shuffle = True


class LazyShellArmorPrize(ItemPrize):
    item = LazyShellItem2
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Shell", description="There's no turtle inside of it."
    )
    _monstro_shuffle = True
    _model = RedShellObject


class ZoomShoesPrize(ItemPrize):
    item = ZoomShoesItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_2
    _nickname = TreasureHunterNickname(
        nickname="Red Vans", description="I bet you can run really fast in\n these."
    )
    _monstro_shuffle = True
    _model = ShoesObject


class SafetyBadgePrize(ItemPrize):
    item = SafetyBadgeItem
    _nickname = TreasureHunterNickname(
        nickname="Rainbow Button",
        description="I don't really follow politics, but\n this button looks like it's against\n a lot of things.",
    )
    _model = BroochObject


class JumpShoesPrize(ItemPrize):
    item = JumpShoesItem
    _nickname = TreasureHunterNickname(
        nickname="Brown Clogs", description="Check out the thick soles!"
    )
    _model = ShoesObject


class SafetyRingPrize(ItemPrize):
    item = SafetyRingItem
    _nickname = TreasureHunterNickname(
        nickname="Protective Charm", description="Never go into battle without it."
    )
    _model = RingObject


class AmuletPrize(ItemPrize):
    item = AmuletItem
    _nickname = TreasureHunterNickname(
        nickname="Stinky Charm", description="It'll help you weather the elements."
    )
    _model = CardObject


class ScroogeRingPrize(ItemPrize):
    item = ScroogeRingItem
    _nickname = TreasureHunterNickname(
        nickname="Mage Totem", description="It might help with spellcasting."
    )
    _model = RingObject


class ExpBoosterPrize(ItemPrize):
    item = ExpBoosterItem
    _nickname = TreasureHunterNickname(
        nickname="Training Device", description="This'll make you strong in no time!"
    )


class AttackScarfPrize(ItemPrize):
    item = AttackScarfItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Starry Scarf", description="It could save your life!"
    )
    _monstro_shuffle = True


class RareScarfPrize(ItemPrize):
    item = RareScarfItem
    _nickname = TreasureHunterNickname(
        nickname="White Cloth", description="You don't see these around often."
    )


class BtubRingPrize(ItemPrize):
    item = BtubRingItem
    _nickname = TreasureHunterNickname(
        nickname="Wedding Ring", description="For that special someone!"
    )
    _model = RingObject


class AntidotePinPrize(ItemPrize):
    item = AntidotePinItem
    _nickname = TreasureHunterNickname(
        nickname="Green Button", description="Looks like an environmentalist\n thing."
    )
    _model = BroochObject


class WakeUpPinPrize(ItemPrize):
    item = WakeUpPinItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Button", description="Looks like an anti-fur thing."
    )
    _model = BroochObject


class FearlessPinPrize(ItemPrize):
    item = FearlessPinItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Button", description="Who you gonna call?\n GHOSTBUSTERS!"
    )
    _model = BroochObject


class TrueformPinPrize(ItemPrize):
    item = TrueformPinItem
    _nickname = TreasureHunterNickname(
        nickname="Orange Button",
        description="For someone who doesn't like\n scarecrows.",
    )
    _model = BroochObject


class CoinTrickPrize(ItemPrize):
    item = CoinTrickItem
    _nickname = TreasureHunterNickname(
        nickname="Fortune Charm", description="It's sure to make you very rich."
    )


class GhostMedalPrize(ItemPrize):
    item = GhostMedalItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Military Decoration", description="I wonder what powers it bestows?"
    )
    _monstro_shuffle = True


class JinxBeltPrize(ItemPrize):
    item = JinxBeltItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Black Sash", description="A true fighter would love this."
    )
    _monstro_shuffle = True


class FeatherPrize(ItemPrize):
    item = FeatherItem
    _nickname = TreasureHunterNickname(
        nickname="Fluttering Quill", description="It's pretty exotic, isn't it?"
    )
    _model = FeatherObject


class TroopaPinPrize(ItemPrize):
    item = TroopaPinItem
    _nickname = TreasureHunterNickname(
        nickname="Military Decoration", description="I wonder what powers it bestows?"
    )
    _model = BroochObject


class SignalRingPrize(ItemPrize):
    item = SignalRingItem
    _nickname = TreasureHunterNickname(
        nickname="Bell Charm", description="I wonder what it can help you find?"
    )
    _model = RingObject


class QuartzCharmPrize(ItemPrize):
    item = QuartzCharmItem
    _importance = SpecialItemPrizeType.SPECIAL_EQUIP_TIER_1
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not.",
    )
    _monstro_shuffle = True
    _model = CrystalObject


class TeamworkBandPrize(ItemPrize):
    item = TeamworkBandItem
    _nickname = TreasureHunterNickname(
        nickname="Friendship Bracelet",
        description="Maybe the real treasure is the\n friends we made along the way.",
    )
    remake_only = True
    _monstro_shuffle = True


class EnduringBroochPrize(ItemPrize):
    item = EnduringBroochItem
    _nickname = TreasureHunterNickname(
        nickname="Shiny Brooch", description="It looks pretty stylish."
    )
    remake_only = True
    _monstro_shuffle = True
    _model = BroochObject


class MushroomPrize(ItemPrize):
    item = MushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = RedMushroomObject


class MidMushroomPrize(ItemPrize):
    item = MidMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Green Mushroom", description="It's just food, right?"
    )
    _model = GreenMushroomObject


class MaxMushroomPrize(ItemPrize):
    item = MaxMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Mushroom", description="It's just food, right?"
    )
    _model = YellowMushroomObject


class HoneySyrupPrize(ItemPrize):
    item = HoneySyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = RedSyrupObject


class MapleSyrupPrize(ItemPrize):
    item = MapleSyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = GreenSyrupObject


class RoyalSyrupPrize(ItemPrize):
    item = RoyalSyrupItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = YellowSyrupObject


class PickMeUpPrize(ItemPrize):
    item = PickMeUpItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = StarDrinkObject


class AbleJuicePrize(ItemPrize):
    item = AbleJuiceItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = RDrinkObject


class BracerPrize(ItemPrize):
    item = BracerItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = DDrinkObject


class EnergizerPrize(ItemPrize):
    item = EnergizerItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = PDrinkObject


class YoshiAdePrize(ItemPrize):
    item = YoshiAdeItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = GreenJuiceObject


class RedEssencePrize(ItemPrize):
    item = RedEssenceItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = RedJuiceObject


class KerokeroColaPrize(ItemPrize):
    item = KerokeroColaItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = FrogDrinkObject


class YoshiCookiePrize(ItemPrize):
    item = YoshiCookieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good", description="Looks tasty, doesn't it?"
    )
    _model = CookieObject


class PureWaterPrize(ItemPrize):
    item = PureWaterItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = BlueSyrupObject


class SleepyBombPrize(ItemPrize):
    item = SleepyBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = YellowBombObject


class BadMushroomPrize(ItemPrize):
    item = BadMushroomItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = RedMushroomObject


class FireBombPrize(ItemPrize):
    item = FireBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = RedBombObject


class IceBombPrize(ItemPrize):
    item = IceBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = BlueBombObject


class FlowerTabPrize(ItemPrize):
    item = FlowerTabItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Capsule", description="You collect these, right?"
    )


class FlowerJarPrize(ItemPrize):
    item = FlowerJarItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Set", description="You collect these, right?"
    )


class FlowerBoxPrize(ItemPrize):
    item = FlowerBoxItem
    _nickname = TreasureHunterNickname(
        nickname="Flower Gift", description="You collect these, right?"
    )


class YoshiCandyPrize(ItemPrize):
    item = YoshiCandyItem
    _nickname = TreasureHunterNickname(
        nickname="Candy Piece", description="I wonder what flavor it is?"
    )
    _model = GreenCandyObject


class FroggieDrinkPrize(ItemPrize):
    item = FroggieDrinkItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = YellowMusicDrinkObject


class MukuCookiePrize(ItemPrize):
    item = MukuCookieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good", description="Looks tasty, doesn't it?"
    )
    _model = CookieObject


class ElixirPrize(ItemPrize):
    item = ElixirItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = BlueMusicDrinkObject


class MegalixirPrize(ItemPrize):
    item = MegalixirItem
    _nickname = TreasureHunterNickname(
        nickname="Red Drink", description="I wonder what flavor it is?"
    )
    _model = RedMusicDrinkObject


class SeeYaPrize(ItemPrize):
    item = SeeYaItem
    _nickname = TreasureHunterNickname(
        nickname="Eject Button", description="Seems useful in a pinch, doesn't\n it?"
    )


class TempleKeyPrize(ItemPrize, KeyPrize):
    item = TempleKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class GoodieBagPrize(ItemPrize):
    item = GoodieBagItem
    _nickname = TreasureHunterNickname(
        nickname="Coin Sack", description="It could make you rich!"
    )


class EarlierTimesPrize(ItemPrize):
    item = EarlierTimesItem
    _nickname = TreasureHunterNickname(
        nickname="Reset Button", description="Sounds useful in a pinch, doesn't\n it?"
    )


class FreshenUpPrize(ItemPrize):
    item = FreshenUpItem
    _nickname = TreasureHunterNickname(
        nickname="Blue Drink", description="I wonder what flavor it is?"
    )
    _model = RDrinkObject


class RareFrogCoinPrize(ItemPrize, KeyPrize):
    item = RareFrogCoinItem
    _nickname = TreasureHunterNickname(
        nickname="Green Coin", description="It looks different from most Frog \nCoins."
    )
    _model = SmallFrogCoinObject


class WalletPrize(ItemPrize, KeyPrize):
    item = WalletItem
    _nickname = TreasureHunterNickname(
        nickname="Coin Sack", description="It looks like it belongs to someone."
    )


class CricketPiePrize(ItemPrize, KeyPrize):
    item = CricketPieItem
    _nickname = TreasureHunterNickname(
        nickname="Baked Good", description="Looks tasty, doesn't it?"
    )
    _model = CookieObject


class RockCandyPrize(ItemPrize):
    item = RockCandyItem
    _nickname = TreasureHunterNickname(
        nickname="Candy Piece", description="I wonder what flavor it is?"
    )
    _model = BlueCandyObject


class CastleKey1Prize(ItemPrize, KeyPrize):
    item = CastleKey1Item
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class CastleKey2Prize(ItemPrize, KeyPrize):
    item = CastleKey2Item
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class BambinoBombPrize(ItemPrize, KeyPrize):
    item = BambinoBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = MicrobombObject


class ProgressiveCardPrize(ProgressiveItemPrize, KeyPrize):
    _nickname = TreasureHunterNickname(
        nickname="Membership Card",
        description="It's sure to bring you an air of\n prestige.",
    )
    _model = CardObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3086_JUICE_BAR_CARD_UPGRADE)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3097_JUICE_BAR_CARD_NPC_GRANT)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3110_FREESTANDING_JUICE_BAR_CARD_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3396_MIDAS_CAVE_PROGRESSIVE_CARD_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3115_HILL_PROGRESSIVE_CARD)])


class ProgressiveEggPrize(ProgressiveItemPrize):
    _nickname = TreasureHunterNickname(
        nickname="Mystery Egg",
        description="I have no idea what it does!\n It sort of grows on ya, huh?",
    )
    _model = EggObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3087_PROGRESSIVE_EGG_UPGRADE)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3098_PROGRESSIVE_EGG_NPC_GRANT)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3111_FREESTANDING_PROGRESSIVE_EGG_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3397_MIDAS_CAVE_PROGRESSIVE_EGG_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3114_HILL_PROGRESSIVE_EGG)])


class ExtraShinyStonePrize(ItemPrize, KeyPrize):
    item = ExtraShinyStoneItem
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not.",
    )
    remake_only = True
    _model = CrystalObject


class CrystalShardPrize(ItemPrize, KeyPrize):
    item = CrystalShardItem
    _nickname = TreasureHunterNickname(
        nickname="Crystal",
        description="It might have special powers.\n Or it might not.",
    )
    remake_only = True
    _model = CrystalObject


class RoomKeyPrize(ItemPrize, KeyPrize):
    item = RoomKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class ElderKeyPrize(ItemPrize, KeyPrize):
    item = ElderKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class ShedKeyPrize(ItemPrize, KeyPrize):
    item = ShedKeyItem
    _nickname = TreasureHunterNickname(
        nickname="Golden Key", description="I wonder what it opens?"
    )
    _model = KeyObject


class FrightBombPrize(ItemPrize):
    item = FrightBombItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = GreenBombObject


class BeetleBoxPrize(ItemPrize):
    item = BeetleBoxItem
    _model = BeetleObject


class LuckyJewelPrize(ItemPrize):
    item = LuckyJewelItem
    _nickname = TreasureHunterNickname(
        nickname="Lucky Jewel",
        description="It’s sure to bring you plenty of\n good luck.",
    )
    _model = CrystalObject


class CrystallinePrize(ItemPrize):
    item = CrystallineItem
    _nickname = TreasureHunterNickname(
        nickname="Yellow Drink", description="I wonder what flavor it is?"
    )
    _model = DDrinkObject


class PowerBlastPrize(ItemPrize):
    item = PowerBlastItem
    _nickname = TreasureHunterNickname(
        nickname="Green Drink", description="I wonder what flavor it is?"
    )
    _model = PDrinkObject


class WiltShroomPrize(ItemPrize):
    item = WiltShroomItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = BananaObject


class RottenMushPrize(ItemPrize):
    item = RottenMushItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = BananaObject


class MoldyMushPrize(ItemPrize):
    item = MoldyMushItem
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = BananaObject


class SeedPrize(ItemPrize, KeyPrize):
    item = SeedItem
    _nickname = TreasureHunterNickname(
        nickname="Mysterious Seed", description="I wonder what will grow from it?"
    )
    _model = BerryObject


class FertilizerPrize(ItemPrize, KeyPrize):
    item = FertilizerItem
    _nickname = TreasureHunterNickname(
        nickname="Bag of Dirt",
        description="It seems different from the soil\n I dug it out of.",
    )


class BigBooFlagPrize(ItemPrize, KeyPrize):
    item = BigBooFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking for\n this?",
    )
    _model = CardObject


class DryBonesFlagPrize(ItemPrize, KeyPrize):
    item = DryBonesFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking fon\n this?",
    )
    _model = CardObject


class GreaperFlagPrize(ItemPrize, KeyPrize):
    item = GreaperFlagItem
    _nickname = TreasureHunterNickname(
        nickname="Invisible Flag",
        description="I wonder if someone is looking for\n this?",
    )
    _model = CardObject


class CricketJamPrize(ItemPrize, KeyPrize):
    item = CricketJamItem
    _nickname = TreasureHunterNickname(
        nickname="Green Jelly", description="I wonder what flavor it is?"
    )
    _model = GreenJuiceObject


class RegularFireworksPrize(ItemPrize):
    item = FireworksItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )


class ProgressiveFireworksPrize(ProgressiveItemPrize, KeyPrize):
    item = FireworksItem
    _nickname = TreasureHunterNickname(
        nickname="Explosive Device", description="Don't try this at home!"
    )
    _model = ProgressiveFireworksObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3100_PROGRESSIVE_FIREWORKS_CHEST_GRANT)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0185_NPC_QUEST_GRANT_PROGRESSIVE_FIREWORKS)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3113_FREESTANDING_PROGRESSIVE_FIREWORKS_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3399_MIDAS_CAVE_PROGRESSIVE_FIREWORK_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0217_HILL_FIREWORKS)])


class StayVoucherPrize(ItemPrize):
    item = StayVoucherItem
    _nickname = TreasureHunterNickname(
        nickname="Special Ticket",
        description="You can probably redeem it at a\n fancy hotel.",
    )
    remake_only = True
    _model = CardObject


class BrightCardPrize(ItemPrize, KeyPrize):
    item = BrightCardItem
    _nickname = TreasureHunterNickname(
        nickname="Membership Card",
        description="It's sure to bring you an air of\n prestige.",
    )
    _model = CardObject


class PoisonMushroomPrize(ItemPrize):
    item = MushroomItem2
    _nickname = TreasureHunterNickname(
        nickname="Red Mushroom", description="It's just food, right?"
    )
    _model = RedMushroomObject


class StarEggPrize(ItemPrize):
    item = StarEggItem
    _nickname = TreasureHunterNickname(
        nickname="Mystery Egg",
        description="I have no idea what it does!\n It sort of grows on ya, huh?",
    )
    _model = EggObject


### Other kinds of prizes ###


class BeetlemaniaPrize(StandardPrize):
    _nickname = TreasureHunterNickname(
        nickname="Video Game",
        description="It's pretty addictive.",
    )
    _model = BeetleObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0162_CHEST_GRANT_BEETLEMANIA)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0161_NPC_QUEST_GRANT_BEETLEMANIA)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3109_FREESTANDING_BEETLEMANIA_GRANT)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3395_MIDAS_CAVE_BEETLEMANIA_GRANTER)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0218_HILL_BEETLEMANIA)])


class ShoesPrize(WeddingGearPrize, KeyPrize):
    item = ShoesItem
    _nickname = TreasureHunterNickname(
        nickname="Ruby Slippers", description="Do you think they'll take you\n home?"
    )
    _model = ShoesObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3943_SHOES_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3931_GET_SHOES)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3935_FREESTANDING_SHOES)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3939_RIVER_SHOES)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, ShoesItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


class BroochPrize(WeddingGearPrize, KeyPrize):
    item = BroochItem
    _nickname = TreasureHunterNickname(
        nickname="Shiny Brooch", description="It looks pretty stylish."
    )
    _model = BroochObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3944_BROOCH_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3932_GET_BROOCH)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3936_FREESTANDING_BROOCH)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3940_RIVER_BROOCH)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, BroochItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


class RingPrize(WeddingGearPrize, KeyPrize):
    item = RingItem
    _nickname = TreasureHunterNickname(
        nickname="Wedding Ring", description="For that special someone!"
    )
    _model = RingObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3945_RING_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3933_GET_RING)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3937_FREESTANDING_RING)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3941_RIVER_RING)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, RingItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


class CrownPrize(WeddingGearPrize, KeyPrize):
    item = CrownItem
    _nickname = TreasureHunterNickname(
        nickname="Gold Crown", description="It looks pretty important!"
    )
    _model = CrownObject

    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3946_CROWN_CHEST)])

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3934_GET_CROWN)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3938_FREESTANDING_CROWN)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3942_RIVER_CROWN)])

    @property
    def hill_grant(self) -> EventScript:
        return EventScript(
            [
                Inc(WEDDING_GEAR_COUNTER),
                SetVarToConst(ITEM_ID, CrownItem),
                JmpToEvent(E0215_HILL_ITEM),
            ]
        )


class GoldPaintPrize(ItemPrize, KeyPrize):
    item = GoldPaintItem
    _nickname = TreasureHunterNickname(
        nickname="Chrome Coat", description="It'll make you look shiny!"
    )
    _model = YellowJuiceObject


class RecoveryMushroomPrize(StandardPrize):
    _model = RecoveryMushroomObject
    _packet_data = (SPR0195_FLOWER, 1)

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 0),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )

    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0397_HEAL_IN_TOADSTOOLS_ROOM)])

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E2822_ASYNC_NO_ANIMATION_MUSHROOM)])


class YouMissed(StandardPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3081_YOU_MISSED)])


class Nothing(YouMissed):
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0256_RETURN)])


class InfiniteCoinsPrize(StandardPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [SetVarToConst(ITEM_ID, 240), JmpToEvent(E3074_COIN_CHEST_MULTI_HIT_1)]
        )


class Coins1Prize(CoinQuantityPrize):
    _amount: int = 1
    _model = SmallCoinObject

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN)])


class Coins5Prize(CoinQuantityPrize):
    _amount = 5


class Coins8Prize(CoinQuantityPrize):
    _amount = 8


class Coins10Prize(CoinQuantityPrize):
    _amount: int = 10

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3146_FREESTANDING_BIG_COIN)])


class Coins20Prize(CoinQuantityPrize):
    _amount = 20


class Coins50Prize(CoinQuantityPrize):
    _amount = 50


class Coins100Prize(CoinQuantityPrize):
    _amount = 100


class Coins150Prize(CoinQuantityPrize):
    _amount = 150


class FirstMimicFightLauncher(MimicFightInitiatorPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3124_MIMIC_1_CHEST)])


class SecondMimicFightLauncher(MimicFightInitiatorPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3126_MIMIC_2_CHEST)])


class ThirdMimicFightLauncher(MimicFightInitiatorPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E2493_MIMIC_3)])


class FrogCoin1Prize(FrogCoinQuantityPrize):
    _amount = 1

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3083_FREESTANDING_SHUFFLED_FROG_COIN)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E2816_ASYNC_NO_ANIMATION_FROG_COIN)])


class FrogCoin2Prize(FrogCoinQuantityPrize):
    _amount = 2


class FrogCoin3Prize(FrogCoinQuantityPrize):
    _amount = 3


class FrogCoin10Prize(FrogCoinQuantityPrize):
    _amount = 10


class FrogCoin20Prize(FrogCoinQuantityPrize):
    _amount = 20


class BanditsWayStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class KeroSewersStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 1),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class MolevilleMinesStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 2),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class SeaStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 3),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class LandsEndVolcanoStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 5),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class NimbusLandStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 7),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class LandsEndStar2Prize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 8),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


class LandsEndStar3Prize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 9),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


# Star pieces


class StarPiece1(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_1


class StarPiece2(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_2


class StarPiece3(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_3


class StarPiece4(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_4


class StarPiece5(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_5


class StarPiece6(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_6


class StarPiece7(StarPiecePrize):
    _hint = SIGNAL_RING_STAR_PIECE_7


# Spells


class JumpSpellPrize(SpellPrize):
    _spell = JumpSpell
    _chest_event_id = E0900_CHEST_SPELL_1
    _npc_grant_event_id = E0952_NPC_SPELL_1
    _standing_grant_event_id = E0978_FREESTANDING_SPELL_1
    _river_grant_event_id = E1022_HILL_RIVER_SPELL_1
    _hill_grant_event_id = E1022_HILL_RIVER_SPELL_1
    character_replacement_ids = [
        "spell_1_character",
        "freestanding_spell_1_character",
        "hill_river_spell_1_character",
        "npc_spell_1_character"
    ]
    packet_replacement_ids = [
        "spell_1_elemental_packet"
    ]
    _dialog_id = DI1947_LEARN_SPELL_1
    _autoterm_dialog_id = DI1948_LEARN_SPELL_1_AUTOTERM
    _placement_id = 1


class FireOrbSpellPrize(SpellPrize):
    _spell = FireOrbSpell
    _chest_event_id = E0901_CHEST_SPELL_2
    _npc_grant_event_id = E0953_NPC_SPELL_2
    _standing_grant_event_id = E0992_FREESTANDING_SPELL_2
    _river_grant_event_id = E1023_HILL_RIVER_SPELL_2
    _hill_grant_event_id = E1023_HILL_RIVER_SPELL_2
    character_replacement_ids = [
        "spell_2_character",
        "freestanding_spell_2_character",
        "hill_river_spell_2_character",
        "npc_spell_2_character"
    ]
    packet_replacement_ids = [
        "spell_2_elemental_packet"
    ]
    _dialog_id = DI1949_LEARN_SPELL_2
    _autoterm_dialog_id = DI1950_LEARN_SPELL_2_AUTOTERM
    _placement_id = 2

class SuperJumpSpellPrize(SpellPrize):
    _spell = SuperJumpSpell
    _chest_event_id = E0902_CHEST_SPELL_3
    _npc_grant_event_id = E0954_NPC_SPELL_3
    _standing_grant_event_id = E0993_FREESTANDING_SPELL_3
    _river_grant_event_id = E1024_HILL_RIVER_SPELL_3
    _hill_grant_event_id = E1024_HILL_RIVER_SPELL_3
    character_replacement_ids = [
        "spell_3_character",
        "freestanding_spell_3_character",
        "hill_river_spell_3_character",
        "npc_spell_3_character"
    ]
    packet_replacement_ids = [
        "spell_3_elemental_packet"
    ]
    _dialog_id = DI1951_LEARN_SPELL_3
    _autoterm_dialog_id = DI1952_LEARN_SPELL_3_AUTOTERM
    _placement_id = 3


class SuperFlameSpellPrize(SpellPrize):
    _spell = SuperFlameSpell
    _chest_event_id = E0903_CHEST_SPELL_4
    _npc_grant_event_id = E0955_NPC_SPELL_4
    _standing_grant_event_id = E0994_FREESTANDING_SPELL_4
    _river_grant_event_id = E1025_HILL_RIVER_SPELL_4
    _hill_grant_event_id = E1025_HILL_RIVER_SPELL_4
    character_replacement_ids = [
        "spell_4_character",
        "freestanding_spell_4_character",
        "hill_river_spell_4_character",
        "npc_spell_4_character"
    ]
    packet_replacement_ids = [
        "spell_4_elemental_packet"
    ]
    _dialog_id = DI1953_LEARN_SPELL_4
    _autoterm_dialog_id = DI1954_LEARN_SPELL_4_AUTOTERM
    _placement_id = 4


class UltraJumpSpellPrize(SpellPrize):
    _spell = UltraJumpSpell
    _chest_event_id = E0904_CHEST_SPELL_5
    _npc_grant_event_id = E0956_NPC_SPELL_5
    _standing_grant_event_id = E0995_FREESTANDING_SPELL_5
    _river_grant_event_id = E1026_HILL_RIVER_SPELL_5
    _hill_grant_event_id = E1026_HILL_RIVER_SPELL_5
    character_replacement_ids = [
        "spell_5_character",
        "freestanding_spell_5_character",
        "hill_river_spell_5_character",
        "npc_spell_5_character"
    ]
    packet_replacement_ids = [
        "spell_5_elemental_packet"
    ]
    _dialog_id = DI1955_LEARN_SPELL_5
    _autoterm_dialog_id = DI1956_LEARN_SPELL_5_AUTOTERM
    _placement_id = 5


class UltraFlameSpellPrize(SpellPrize):
    _spell = UltraFlameSpell
    _chest_event_id = E0905_CHEST_SPELL_6
    _npc_grant_event_id = E0957_NPC_SPELL_6
    _standing_grant_event_id = E0996_FREESTANDING_SPELL_6
    _river_grant_event_id = E1027_HILL_RIVER_SPELL_6
    _hill_grant_event_id = E1027_HILL_RIVER_SPELL_6
    character_replacement_ids = [
        "spell_6_character",
        "freestanding_spell_6_character",
        "hill_river_spell_6_character",
        "npc_spell_6_character"
    ]
    packet_replacement_ids = [
        "spell_6_elemental_packet"
    ]
    _dialog_id = DI1957_LEARN_SPELL_6
    _autoterm_dialog_id = DI1958_LEARN_SPELL_6_AUTOTERM
    _placement_id = 6


class ThunderboltSpellPrize(SpellPrize):
    _spell = ThunderboltSpell
    _chest_event_id = E0906_CHEST_SPELL_7
    _npc_grant_event_id = E0958_NPC_SPELL_7
    _standing_grant_event_id = E0997_FREESTANDING_SPELL_7
    _river_grant_event_id = E1028_HILL_RIVER_SPELL_7
    _hill_grant_event_id = E1028_HILL_RIVER_SPELL_7
    character_replacement_ids = [
        "spell_7_character",
        "freestanding_spell_7_character",
        "hill_river_spell_7_character",
        "npc_spell_7_character"
    ]
    packet_replacement_ids = [
        "spell_7_elemental_packet"
    ]
    _dialog_id = DI1959_LEARN_SPELL_7
    _autoterm_dialog_id = DI1960_LEARN_SPELL_7_AUTOTERM
    _placement_id = 7


class HPRainSpellPrize(SpellPrize):
    _spell = HPRainSpell
    _chest_event_id = E0907_CHEST_SPELL_8
    _npc_grant_event_id = E0959_NPC_SPELL_8
    _standing_grant_event_id = E0999_FREESTANDING_SPELL_8
    _river_grant_event_id = E1029_HILL_RIVER_SPELL_8
    _hill_grant_event_id = E1029_HILL_RIVER_SPELL_8
    character_replacement_ids = [
        "spell_8_character",
        "freestanding_spell_8_character",
        "hill_river_spell_8_character",
        "npc_spell_8_character"
    ]
    packet_replacement_ids = [
        "spell_8_elemental_packet"
    ]
    _dialog_id = DI1961_LEARN_SPELL_8
    _autoterm_dialog_id = DI1962_LEARN_SPELL_8_AUTOTERM
    _placement_id = 8


class PsychopathSpellPrize(SpellPrize):
    _spell = PsychopathSpell
    _chest_event_id = E0908_CHEST_SPELL_9
    _npc_grant_event_id = E0960_NPC_SPELL_9
    _standing_grant_event_id = E1000_FREESTANDING_SPELL_9
    _river_grant_event_id = E1030_HILL_RIVER_SPELL_9
    _hill_grant_event_id = E1030_HILL_RIVER_SPELL_9
    character_replacement_ids = [
        "spell_9_character",
        "freestanding_spell_9_character",
        "hill_river_spell_9_character",
        "npc_spell_9_character"
    ]
    packet_replacement_ids = [
        "spell_9_elemental_packet"
    ]
    _dialog_id = DI1963_LEARN_SPELL_9
    _autoterm_dialog_id = DI1964_LEARN_SPELL_9_AUTOTERM
    _placement_id = 9


class ShockerSpellPrize(SpellPrize):
    _spell = ShockerSpell
    _chest_event_id = E0909_CHEST_SPELL_10
    _npc_grant_event_id = E0961_NPC_SPELL_10
    _standing_grant_event_id = E1001_FREESTANDING_SPELL_10
    _river_grant_event_id = E1031_HILL_RIVER_SPELL_10
    _hill_grant_event_id = E1031_HILL_RIVER_SPELL_10
    character_replacement_ids = [
        "spell_10_character",
        "freestanding_spell_10_character",
        "hill_river_spell_10_character",
        "npc_spell_10_character"
    ]
    packet_replacement_ids = [
        "spell_10_elemental_packet"
    ]
    _dialog_id = DI1965_LEARN_SPELL_10
    _autoterm_dialog_id = DI1966_LEARN_SPELL_10_AUTOTERM
    _placement_id = 10


class SnowyPrize(SpellPrize):
    _spell = SnowySpell
    _chest_event_id = E0910_CHEST_SPELL_11
    _npc_grant_event_id = E0962_NPC_SPELL_11
    _standing_grant_event_id = E1002_FREESTANDING_SPELL_11
    _river_grant_event_id = E1032_HILL_RIVER_SPELL_11
    _hill_grant_event_id = E1032_HILL_RIVER_SPELL_11
    character_replacement_ids = [
        "spell_11_character",
        "freestanding_spell_11_character",
        "hill_river_spell_11_character",
        "npc_spell_11_character"
    ]
    packet_replacement_ids = [
        "spell_11_elemental_packet"
    ]
    _dialog_id = DI1967_LEARN_SPELL_11
    _autoterm_dialog_id = DI1968_LEARN_SPELL_11_AUTOTERM
    _placement_id = 11


class StarRainSpellPrize(SpellPrize):
    _spell = StarRainSpell
    _chest_event_id = E0911_CHEST_SPELL_12
    _npc_grant_event_id = E0963_NPC_SPELL_12
    _standing_grant_event_id = E1003_FREESTANDING_SPELL_12
    _river_grant_event_id = E1033_HILL_RIVER_SPELL_12
    _hill_grant_event_id = E1033_HILL_RIVER_SPELL_12
    character_replacement_ids = [
        "spell_12_character",
        "freestanding_spell_12_character",
        "hill_river_spell_12_character",
        "npc_spell_12_character"
    ]
    packet_replacement_ids = [
        "spell_12_elemental_packet"
    ]
    _dialog_id = DI1969_LEARN_SPELL_12
    _autoterm_dialog_id = DI1970_LEARN_SPELL_12_AUTOTERM
    _placement_id = 12


class GenoBeamSpellPrize(SpellPrize):
    _spell = GenoBeamSpell
    _chest_event_id = E0912_CHEST_SPELL_13
    _npc_grant_event_id = E0964_NPC_SPELL_13
    _standing_grant_event_id = E1004_FREESTANDING_SPELL_13
    _river_grant_event_id = E1034_HILL_RIVER_SPELL_13
    _hill_grant_event_id = E1034_HILL_RIVER_SPELL_13
    character_replacement_ids = [
        "spell_13_character",
        "freestanding_spell_13_character",
        "hill_river_spell_13_character",
        "npc_spell_13_character"
    ]
    packet_replacement_ids = [
        "spell_13_elemental_packet"
    ]
    _dialog_id = DI1971_LEARN_SPELL_13
    _autoterm_dialog_id = DI1972_LEARN_SPELL_13_AUTOTERM
    _placement_id = 13


class GenoBoostSpellPrize(SpellPrize):
    _spell = GenoBoostSpell
    _chest_event_id = E0913_CHEST_SPELL_14
    _npc_grant_event_id = E0965_NPC_SPELL_14
    _standing_grant_event_id = E1005_FREESTANDING_SPELL_14
    _river_grant_event_id = E1035_HILL_RIVER_SPELL_14
    _hill_grant_event_id = E1035_HILL_RIVER_SPELL_14
    character_replacement_ids = [
        "spell_14_character",
        "freestanding_spell_14_character",
        "hill_river_spell_14_character",
        "npc_spell_14_character"
    ]
    packet_replacement_ids = [
        "spell_14_elemental_packet"
    ]
    _dialog_id = DI1973_LEARN_SPELL_14
    _autoterm_dialog_id = DI1974_LEARN_SPELL_14_AUTOTERM
    _placement_id = 14


class GenoWhirlSpellPrize(SpellPrize):
    _spell = GenoWhirlSpell
    _chest_event_id = E0914_CHEST_SPELL_15
    _npc_grant_event_id = E1048_NPC_SPELL_15
    _standing_grant_event_id = E1049_FREESTANDING_SPELL_15
    _river_grant_event_id = E1050_HILL_RIVER_SPELL_15
    _hill_grant_event_id = E1050_HILL_RIVER_SPELL_15
    character_replacement_ids = [
        "spell_15_character",
        "freestanding_spell_15_character",
        "hill_river_spell_15_character",
        "npc_spell_15_character"
    ]
    packet_replacement_ids = [
        "spell_15_elemental_packet"
    ]
    _dialog_id = DI1975_LEARN_SPELL_15
    _autoterm_dialog_id = DI1976_LEARN_SPELL_15_AUTOTERM
    _placement_id = 15


class GenoBlastSpellPrize(SpellPrize):
    _spell = GenoBlastSpell
    _chest_event_id = E0915_CHEST_SPELL_16
    _npc_grant_event_id = E0966_NPC_SPELL_16
    _standing_grant_event_id = E1006_FREESTANDING_SPELL_16
    _river_grant_event_id = E1036_HILL_RIVER_SPELL_16
    _hill_grant_event_id = E1036_HILL_RIVER_SPELL_16
    character_replacement_ids = [
        "spell_16_character",
        "freestanding_spell_16_character",
        "hill_river_spell_16_character",
        "npc_spell_16_character"
    ]
    packet_replacement_ids = [
        "spell_16_elemental_packet"
    ]
    _dialog_id = DI1977_LEARN_SPELL_16
    _autoterm_dialog_id = DI1978_LEARN_SPELL_16_AUTOTERM
    _placement_id = 16


class GenoFlashSpellPrize(SpellPrize):
    _spell = GenoFlashSpell
    _chest_event_id = E0916_CHEST_SPELL_17
    _npc_grant_event_id = E0967_NPC_SPELL_17
    _standing_grant_event_id = E1007_FREESTANDING_SPELL_17
    _river_grant_event_id = E1037_HILL_RIVER_SPELL_17
    _hill_grant_event_id = E1037_HILL_RIVER_SPELL_17
    character_replacement_ids = [
        "spell_17_character",
        "freestanding_spell_17_character",
        "hill_river_spell_17_character",
        "npc_spell_17_character"
    ]
    packet_replacement_ids = [
        "spell_17_elemental_packet"
    ]
    _dialog_id = DI1979_LEARN_SPELL_17
    _autoterm_dialog_id = DI1980_LEARN_SPELL_17_AUTOTERM
    _placement_id = 17


class TerrorizeSpellPrize(SpellPrize):
    _spell = TerrorizeSpell
    _chest_event_id = E0918_CHEST_SPELL_18
    _npc_grant_event_id = E0968_NPC_SPELL_18
    _standing_grant_event_id = E1012_FREESTANDING_SPELL_18
    _river_grant_event_id = E1038_HILL_RIVER_SPELL_18
    _hill_grant_event_id = E1038_HILL_RIVER_SPELL_18
    character_replacement_ids = [
        "spell_18_character",
        "freestanding_spell_18_character",
        "hill_river_spell_18_character",
        "npc_spell_18_character"
    ]
    packet_replacement_ids = [
        "spell_18_elemental_packet"
    ]
    _dialog_id = DI1981_LEARN_SPELL_18
    _autoterm_dialog_id = DI1982_LEARN_SPELL_18_AUTOTERM
    _placement_id = 18


class PoisonGasSpellPrize(SpellPrize):
    _spell = PoisonGasSpell
    _chest_event_id = E0919_CHEST_SPELL_19
    _npc_grant_event_id = E0969_NPC_SPELL_19
    _standing_grant_event_id = E1013_FREESTANDING_SPELL_19
    _river_grant_event_id = E1039_HILL_RIVER_SPELL_19
    _hill_grant_event_id = E1039_HILL_RIVER_SPELL_19
    character_replacement_ids = [
        "spell_19_character",
        "freestanding_spell_19_character",
        "hill_river_spell_19_character",
        "npc_spell_19_character"
    ]
    packet_replacement_ids = [
        "spell_19_elemental_packet"
    ]
    _dialog_id = DI1983_LEARN_SPELL_19
    _autoterm_dialog_id = DI1984_LEARN_SPELL_19_AUTOTERM
    _placement_id = 19


class CrusherSpellPrize(SpellPrize):
    _spell = CrusherSpell
    _chest_event_id = E0920_CHEST_SPELL_20
    _npc_grant_event_id = E0970_NPC_SPELL_20
    _standing_grant_event_id = E1014_FREESTANDING_SPELL_20
    _river_grant_event_id = E1040_HILL_RIVER_SPELL_20
    _hill_grant_event_id = E1040_HILL_RIVER_SPELL_20
    character_replacement_ids = [
        "spell_20_character",
        "freestanding_spell_20_character",
        "hill_river_spell_20_character",
        "npc_spell_20_character"
    ]
    packet_replacement_ids = [
        "spell_20_elemental_packet"
    ]
    _dialog_id = DI1985_LEARN_SPELL_20
    _autoterm_dialog_id = DI1986_LEARN_SPELL_20_AUTOTERM
    _placement_id = 20


class BowserCrushSpellPrize(SpellPrize):
    _spell = BowserCrushSpell
    _chest_event_id = E0921_CHEST_SPELL_21
    _npc_grant_event_id = E0971_NPC_SPELL_21
    _standing_grant_event_id = E1015_FREESTANDING_SPELL_21
    _river_grant_event_id = E1041_HILL_RIVER_SPELL_21
    _hill_grant_event_id = E1041_HILL_RIVER_SPELL_21
    character_replacement_ids = [
        "spell_21_character",
        "freestanding_spell_21_character",
        "hill_river_spell_21_character",
        "npc_spell_21_character"
    ]
    packet_replacement_ids = [
        "spell_21_elemental_packet"
    ]
    _dialog_id = DI1987_LEARN_SPELL_21
    _autoterm_dialog_id = DI1988_LEARN_SPELL_21_AUTOTERM
    _placement_id = 21


class TherapySpellPrize(SpellPrize):
    _spell = TherapySpell
    _chest_event_id = E0922_CHEST_SPELL_22
    _npc_grant_event_id = E0972_NPC_SPELL_22
    _standing_grant_event_id = E1016_FREESTANDING_SPELL_22
    _river_grant_event_id = E1042_HILL_RIVER_SPELL_22
    _hill_grant_event_id = E1042_HILL_RIVER_SPELL_22
    character_replacement_ids = [
        "spell_22_character",
        "freestanding_spell_22_character",
        "hill_river_spell_22_character",
        "npc_spell_22_character"
    ]
    packet_replacement_ids = [
        "spell_22_elemental_packet"
    ]
    _dialog_id = DI1989_LEARN_SPELL_22
    _autoterm_dialog_id = DI1990_LEARN_SPELL_22_AUTOTERM
    _placement_id = 22


class GroupHugSpellPrize(SpellPrize):
    _spell = GroupHugSpell
    _chest_event_id = E0923_CHEST_SPELL_23
    _npc_grant_event_id = E0973_NPC_SPELL_23
    _standing_grant_event_id = E1017_FREESTANDING_SPELL_23
    _river_grant_event_id = E1043_HILL_RIVER_SPELL_23
    _hill_grant_event_id = E1043_HILL_RIVER_SPELL_23
    character_replacement_ids = [
        "spell_23_character",
        "freestanding_spell_23_character",
        "hill_river_spell_23_character",
        "npc_spell_23_character"
    ]
    packet_replacement_ids = [
        "spell_23_elemental_packet"
    ]
    _dialog_id = DI1991_LEARN_SPELL_23
    _autoterm_dialog_id = DI1992_LEARN_SPELL_23_AUTOTERM
    _placement_id = 23


class MuteSpellPrize(SpellPrize):
    _spell = MuteSpell
    _chest_event_id = E0924_CHEST_SPELL_24
    _npc_grant_event_id = E0974_NPC_SPELL_24
    _standing_grant_event_id = E1018_FREESTANDING_SPELL_24
    _river_grant_event_id = E1044_HILL_RIVER_SPELL_24
    _hill_grant_event_id = E1044_HILL_RIVER_SPELL_24
    character_replacement_ids = [
        "spell_24_character",
        "freestanding_spell_24_character",
        "hill_river_spell_24_character",
        "npc_spell_24_character"
    ]
    packet_replacement_ids = [
        "spell_24_elemental_packet"
    ]
    _dialog_id = DI1993_LEARN_SPELL_24
    _autoterm_dialog_id = DI1994_LEARN_SPELL_24_AUTOTERM
    _placement_id = 24


class SleepyTimeSpellPrize(SpellPrize):
    _spell = SleepyTimeSpell
    _chest_event_id = E0925_CHEST_SPELL_25
    _npc_grant_event_id = E0975_NPC_SPELL_25
    _standing_grant_event_id = E1019_FREESTANDING_SPELL_25
    _river_grant_event_id = E1045_HILL_RIVER_SPELL_25
    _hill_grant_event_id = E1045_HILL_RIVER_SPELL_25
    character_replacement_ids = [
        "spell_25_character",
        "freestanding_spell_25_character",
        "hill_river_spell_25_character",
        "npc_spell_25_character"
    ]
    packet_replacement_ids = [
        "spell_25_elemental_packet"
    ]
    _dialog_id = DI1995_LEARN_SPELL_25
    _autoterm_dialog_id = DI1996_LEARN_SPELL_25_AUTOTERM
    _placement_id = 25


class ComeBackSpellPrize(SpellPrize):
    _spell = ComeBackSpell
    _chest_event_id = E0926_CHEST_SPELL_26
    _npc_grant_event_id = E0976_NPC_SPELL_26
    _standing_grant_event_id = E1020_FREESTANDING_SPELL_26
    _river_grant_event_id = E1046_HILL_RIVER_SPELL_26
    _hill_grant_event_id = E1046_HILL_RIVER_SPELL_26
    character_replacement_ids = [
        "spell_26_character",
        "freestanding_spell_26_character",
        "hill_river_spell_26_character",
        "npc_spell_26_character"
    ]
    packet_replacement_ids = [
        "spell_26_elemental_packet"
    ]
    _dialog_id = DI1997_LEARN_SPELL_26
    _autoterm_dialog_id = DI1998_LEARN_SPELL_26_AUTOTERM
    _placement_id = 26


class PsychBombSpellPrize(SpellPrize):
    _spell = PsychBombSpell
    _chest_event_id = E0927_CHEST_SPELL_27
    _npc_grant_event_id = E0977_NPC_SPELL_27
    _standing_grant_event_id = E1021_FREESTANDING_SPELL_27
    _river_grant_event_id = E1047_HILL_RIVER_SPELL_27
    _hill_grant_event_id = E1047_HILL_RIVER_SPELL_27
    character_replacement_ids = [
        "spell_27_character",
        "freestanding_spell_27_character",
        "hill_river_spell_27_character",
        "npc_spell_27_character"
    ]
    packet_replacement_ids = [
        "spell_27_elemental_packet"
    ]
    _dialog_id = DI1999_LEARN_SPELL_27
    _autoterm_dialog_id = DI2000_LEARN_SPELL_27_AUTOTERM
    _placement_id = 27


# Characters
class MarioRecruitmentPrize(CharacterPrize):
    _ally = MARIO_Ally
    _name_props = CharacterName(
        "`MARIO_NAME`", "man", "guy", "sir", "mister", "Mr", "mate", ", man"
    )
    _character_model = MarioCharacterNPC

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(MARIO)]
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1179_MARIO_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").MARIO
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


class MallowRecruitmentPrize(CharacterPrize):
    _ally = MALLOW_Ally
    _name_props = CharacterName(
        "`MALLOW_NAME`", "boy", "guy", "sir", "mister", "Mr", "kid", ", kid"
    )
    _character_model = MallowCharacterNPC

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(MALLOW)]
        if world.settings.is_flag_value(
            _gf("BanditsWayGate"), _gf("BanditsWayGating").MALLOW
        ):
            output.extend(
                [
                    SetBit(MAP_BANDITS_WAY),
                    SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
                ]
            )
        if world.settings.is_flag_value(
            _gf("KeroSewersGate"), _gf("KeroSewersGating").MALLOW
        ):
            output.extend(
                [
                    ClearBit(SEWERS_CLOSED),
                ]
            )
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1180_MALLOW_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").MALLOW
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


class GenoRecruitmentPrize(CharacterPrize):
    _ally = GENO_Ally
    _name_props = CharacterName(
        "`GENO_NAME`", "man", "guy", "sir", "mister", "Mr", "mate", ", man"
    )
    _character_model = GenoCharacterNPC

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(GENO)]
        if world.settings.is_flag_value(
            _gf("PipeVaultGate"), _gf("PipeVaultGating").GENO
        ):
            output.extend(
                [
                    ClearBit(PIPE_VAULT_GATED),
                ]
            )
        if world.settings.is_flag_value(
            _gf("Moleville1Gate"), _gf("Moleville1Gating").GENO
        ):
            output.extend(
                [
                    ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING),
                ]
            )
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1181_GENO_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").GENO
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


class BowserRecruitmentPrize(CharacterPrize):
    _ally = BOWSER_Ally
    _name_props = CharacterName(
        "`BOWSER_NAME`", "man", "guy", "sir", "mister", "Mr", "mate", ", man"
    )
    _character_model = BowserCharacterNPC

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(BOWSER)]
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1182_BOWSER_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").BOWSER
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


class ToadstoolRecruitmentPrize(CharacterPrize):
    _ally = TOADSTOOL_Ally
    _name_props = CharacterName(
        "`PEACH_NAME`", "woman", "gal", "ma'am", "miss", "Ms", "lass", ""
    )
    _character_model = ToadstoolCharacterNPC

    def recruit(self, world: GameWorld, show_dialog: bool = False) -> EventScript:
        output: list[UsableEventScriptCommand] = [CharacterJoinsParty(TOADSTOOL)]
        if world.settings.is_flag_value(_gf("SeaGate"), _gf("SeaGating").TOADSTOOL):
            output.extend(
                [
                    SetBit(MAP_SEA),
                    SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
                ]
            )
        if show_dialog:
            output.append(
                RunDialog(
                    dialog_id=DI1183_TOADSTOOL_JOINS,
                    above_object=BOWSER,
                    closable=True,
                    sync=False,
                    multiline=False,
                    use_background=False,
                )
            )
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").TOADSTOOL
        ):
            output.append(SetBit(TOWER_CHARACTER_RECRUITED))
        output.append(Return())
        return EventScript(output)


# Boss fights


class HammerBrosFight(BossFightPrize):
    _text = "Hammer Bros."
    _formation = FORM0293
    _members = [
        FormationMember(HAMMERBROEnemy, 135, 127),
        FormationMember(HAMMERBROEnemy, 199, 143),
    ]

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BanditsWayGate"), _gf("BanditsWayGating").HAMMER_BRO
        ):
            output.extend(
                [
                    SetBit(MAP_BANDITS_WAY),
                    SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
                ]
            )
        return EventScript(output)

    _npc_models = [HammerBroLargeObject, HammerBroSmallObject]
    _statue_npc = HammerBroStatueObject

    _seaside_letter_name_if_sunken_ship_boss = "the Hammer Bros"
    _seaside_letter_name_if_volcano_boss = "two brothers dancing around"
    _seaside_letter_name_if_final_boss = "the Hammer Bros' pals."

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """HAMMER BRO: Alright already,\n you won, now go away![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you figured it out... But you\n gotta get past my hammer to get\n through![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """HAMMER BRO: ...grumble...[delay]\n My hammer's embarrassed about\n losing...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """HAMMER BRO: What're YOU lookin' at?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """HAMMER BRO: Look buddy, you\n already won, you can stop\n taunting my hammer now.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ After getting hammered, [await]\n I always drink Carrot Juice.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hey `MAIN_CHARACTER_NAME`!\n[await][page]\n My bro and I saw you squash\n `SEASIDE_BOSS`!  Nice one!\n[await]\n My bro and his hammer say they saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n We've nailed them down as one of \n `FINAL_BOSS_NAME`\n Listen, my bro is on me about[await]\n loanin' you my hammer.  Whaddaya\n say you bring me back an upgrade\n to pummel him with? Do me a solid![await][page]\n\n                                  Thanks!\n                         Hammer Bro #2[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big hammer! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Bro must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """HAMMER BRO: You better find [0x7024]\n more of `MARRYMORE_CHARACTER`'s things,\n or my hammer'll be angry![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """HAMMER BRO: What're YOU lookin'\n at?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find the Hammer Bro...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """HAMMER BRO: The dojo master\n takes on 3 different forms.\n Me, though? I'm just a hammer.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ This'd BETTER be important!?[await]\n  [select] (Nice hammer. Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ This'd BETTER be important!?[await]\n  [select] (Nice hammer. Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Hammer-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """HAMMER BRO: I guess you were\n tougher than I thought![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """HAMMER BRO: I guess you were\n tougher than I thought![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Hammer Bros' place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the HAMMER BROS!![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Hammer Bros are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Hammer Bros.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Hammer Bros are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Hammer Bros.[await]""",
    }


class Croco1BossFight(BossFightPrize):
    _text = "Croco 1"
    _formation = FORM0273
    _members = [
        FormationMember(CROCO1Enemy, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a thieving reptile dashing"
    _seaside_letter_name_if_final_boss = "Croco's flunkiess."
    _name = "Croco"

    _npc_models = [Croco1Object]
    _statue_npc = CrocoStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n CROCO: Get the heck outta here![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Alright, alright, so ya figured out\n my password! But I ain't goin'\n down without a fight![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CROCO: Enough already, get outta\n here![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CROCO: Back already? How 'bout a\n drink?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """\n    CROCO: 'Dis some kinda joke?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Wanna know how I run so fast?[await]\n Chug some Honey Syrup, chump![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n 'Sup Half-Wits?!\n[await][page]\n Did it take you 500 years to beat \n `SEASIDE_BOSS`?\n [await]\n While casing my next heist, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano. Seems... nice.[await]\n I better get a crew together with \n `FINAL_BOSS_NAME`\n I'm telling you this because I want \n this to be a challenge this time. \n I bet this bazooka that I lifted from\n that toad "guard" will be useful![await][page]\n\n                                    Seeya!\n                                     Croco[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Croco must have gotten\n lost on his way here.""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big reptile! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CROCO: What's this?[await][pause] You fools're\n gonna take another 100 years to\n find the last [0x7024] item(s)![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CROCO: Whaddya doin' hangin\n 'round here?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Croco...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CROCO: Think ya can beat the dojo\n master, chump? I'd like to see ya\n try![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Wallet-this and Coin-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Croco's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped CROCO!![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Croco's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Croco.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Croco's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Croco.[await]""",
    }


class MackBossFight(BossFightPrize):
    _text = "Mack"
    _formation = FORM0289
    _members = [
        FormationMember(MACKEnemy, 199, 119),
        FormationMember(BODYGUARDEnemy, 135, 111),
        FormationMember(BODYGUARDEnemy, 151, 127),
        FormationMember(BODYGUARDEnemy, 183, 143),
        FormationMember(BODYGUARDEnemy, 215, 151),
    ]
    _anchor_enemy = MACKEnemy

    _seaside_letter_name_if_volcano_boss = "a small sword jumping"
    _seaside_letter_name_if_final_boss = "Mack's shysters."
    _seaside_letter_name_if_final_boss_remake = "Claymorton's guys."

    _remake_name = "Claymorton"

    _npc_models = [MackLargeObject, MackMediumObject, MackSmallObject]
    _statue_npc = MackStatueObject

    _mook_henchmen = [BossFightHenchman(monster=BODYGUARDEnemy, model=ShysterHenchman)]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MACK: Party's over. I'm going to\n sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Listen, bub![await]\n You may have figured out my\n password, but you still gotta get\n past me if you want through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Mack's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped MACK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   MACK: Guess the party's over.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MACK: Hey `MAIN_CHARACTER_NAME`!\n Come back to crash our party?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MACK: OK, I get it, you can bounce\n too.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I don't care what kinda party it is![await]\n I drink Milk so I can be like Exor!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Yo `MAIN_CHARACTER_NAME`!\n[await][page]\n I heard you left and threw down\n with `SEASIDE_BOSS`![await]\n\n The shysters on lookout saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They got the good stuff from \n `FINAL_BOSS_NAME`[await]\n We'd better get back aboard before\n any other Shyster party fouls.\n I heard Exor might even show up![await][page]\n\n                             Hang loose!\n                                     Mack[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """BODYGUARD: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]""",
        DI2061_HEAD_CHEF: """BODYGUARD: Doesn't this cake\n look just like Mack?[await]""",
        DI2062_APPRENTICE_CHEF: """BODYGUARD: We've gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Mack must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MACK: I'm not happy to delay the\n party, but we can't get started\n until you find [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Mack's busy right now, so he can't\n play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Mack.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n   MACK: What're YOU doing here?[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Yo! You look tired.[delay] How 'bout a\n night on the house?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Mack's house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Yo! It's fine if you hang out in\n town, but... [delay]stay away from the\n shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ You trying to snoop on what I'm\n buying here?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n       What're YOU lookin' at?[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n               Beat it, bub![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MACK: Think you're gonna beat the\n dojo master today?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You come to crash my party?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You come to crash my party?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Bouncing-this and Party-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MACK: I guess you CAN bounce\n after all.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MACK: I guess you CAN bounce\n after all.[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CLAYMORTON: Party's over. I'm\n going to sleep.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Claymorton's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n CLAYMORTON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CLAYMORTON:\n        Guess the party's over.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CLAYMORTON: Hey `MAIN_CHARACTER_NAME`!\n Come back to crash our party?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CLAYMORTON: OK, I get it, you can\n bounce too.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Yo `MAIN_CHARACTER_NAME`!\n[await][page]\n I heard you left and threw down\n with `SEASIDE_BOSS`![await]\n\n The shymores on lookout saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They got the good stuff from \n `FINAL_BOSS_NAME`[await]\n We'd better get back aboard before\n any other Shyster party fouls.\n I heard Exor might even show up![await][page]\n\n                             Hang loose!\n                               Claymorton[await]""",
        DI2061_HEAD_CHEF: """BODYGUARD: Doesn't this cake\n look just like Claymorton?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Claymorton must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CLAYMORTON: I'm not happy to\n delay the party, but we can't get\n started until you get 4 more items![0]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Claymorton's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Claymorton.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CLAYMORTON:\n        What're YOU doing here?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Claymorton's\n house up on the hill yet?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CLAYMORTON: Think you're gonna\n beat the dojo master today?[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CLAYMORTON: I guess you CAN\n bounce after all.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CLAYMORTON: I guess you CAN\n bounce after all.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """BODYGUARD: Think you're tough,\n pal?[await][delay] March that ugly mustache into\n Mack's room, and see what\n happens![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """BODYGUARD: You beat Mack?[await]\n This is not good![delay_30]\n I guess you can bounce after all.[await]""",
        DI2560_TOWER_HENCHMAN_1: """BODYGUARD: Welcome![await][pause]\n Our party is invitation-only, so\n please come back another time.[await][page]\n[delay] ...You're here to crash it anyway?[delay]\n Alright, wise guy, let's go![await]""",
        DI2572_TOWER_HENCHMAN_2: """\n   BODYGUARD: Oh, no you don't![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """BODYGUARD: I almost feel bad\n for all those fools out there,\n who can't even bounce...[await]""",
        DI3073_TOWER_HENCHMAN_3: """BODYGUARD: How 'bout a fat lip to\n go with that ugly moustache?[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """BODYGUARD: Think you're tough,\n pal?[await][delay] March that ugly mustache into\n Claymorton's room, and see what\n happens![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """BODYGUARD: You beat Claymorton?[await]\n This is not good![delay_30]\n I guess you can bounce after all.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Mack's busy right now, so he can't\n play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Mack.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("KeroSewersGate"), _gf("KeroSewersGating").MACK
        ):
            output.extend([ClearBit(SEWERS_CLOSED)])
        return EventScript(output)


class PandoriteBossFight(BossFightPrize):
    _text = "Pandorite"
    _formation = FORM0266
    _members = [
        FormationMember(PANDORITEEnemy, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a red box sliding about"
    _seaside_letter_name_if_final_boss = "Pandorite's monsters."
    _seaside_letter_name_if_final_boss_remake = "Huhwhat's gremlins."
    _remake_name = "Huhwhat"

    _npc_models = [PandoriteLargeObject, PandoriteSmallObject]
    _statue_npc = MimicStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PANDORITE: That thing was making\n me sick...[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you cracked the code. I'm\n warning you though, I hate being\n woken up.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Pandorite's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped \nPANDORITE!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """PANDORITE: Whatever... Leave me\n alone so I can go back to sleep.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """PANDORITE: I think I like this place\n more than the sewers. It smells\n marginally better.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PANDORITE: I can't tell if this is\n better or worse without the\n protection of my box.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Here, you can have my...um...[await]\n '21 Redtail Chardonnay.[delay] It's fine.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Dear `MAIN_CHARACTER_NAME`,\n[await][page]\n Someone closed my box, and I\n floated up here to see your battle[await]\n with `SEASIDE_BOSS`.\n While looking for rocks, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I think it might be one of \n `FINAL_BOSS_NAME`[await]\n I've got all the rocks in my box\n so I should sink near the ship.\n Drop by to see if I made it later.[await][page]\n\n                         Warm Regards,\n                               Pandorite[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Pandorite must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PANDORITE: Sorry, you can't skip\n getting the last [0x7024] item(s).[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Pandorite's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Pandorite.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PANDORITE: There's not much to do\n around here.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Pandorite...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PANDORITE: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PANDORITE: ...I'm not sure how\n I'm accomplishing this.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PANDORITE: ...I'm not sure how\n I'm accomplishing this.[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """HUHWHAT: That thing was making\n me sick...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Huhwhat's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped \nHUHWHAT!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """HUHWHAT: Whatever... Leave me\n alone so I can go back to sleep.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """HUHWHAT: I think I like this place\n more than the sewers. It smells\n marginally better.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """HUHWHAT: I can't tell if this is\n better or worse without the\n protection of my box.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Dear `MAIN_CHARACTER_NAME`,\n[await][page]\n Someone closed my box, and I\n floated up here to see your battle[await]\n with `SEASIDE_BOSS`.\n While looking for rocks, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I think it might be one of \n `FINAL_BOSS_NAME`[await]\n I've got all the rocks in my box\n so I should sink near the ship.\n Drop by to see if I made it later.[await][page]\n\n                         Warm Regards,\n                                  Huhwhat[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Huhwhat must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """HUHWHAT: Sorry, you can't skip\n getting the last [0x7024] item(s).[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n PHuhwhat's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Huhwhat.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """HUHWHAT: There's not much to do\n around here.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Huhwhat...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """HUHWHAT: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """HUHWHAT: ...I'm not sure how\n I'm accomplishing this.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """HUHWHAT: ...I'm not sure how\n I'm accomplishing this.[await]""",
    }


class Belome1BossFight(BossFightPrize):
    _text = "Belome 1"
    _formation = FORM0278
    _members = [
        FormationMember(BELOME1Enemy, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a hungry dog walking"
    _seaside_letter_name_if_final_boss = "Belome's clones."
    _name = "Belome"

    _npc_models = [Belome1LargeObject, Belome1SmallObject]
    _statue_npc = BelomeSmallStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n        BELOME: Good night~![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Belome's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BELOME!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BELOME: Oh, you're back![await]\n Did you bring any food?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BELOME: Say, it's past my bedtime.\n Can you get off of my head?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I'm always STARVING~![await]\n...but I hydrate with Filtered Water.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ It's a damp, slimy, looking note\n (did `SEASIDE_BOSS` LICK this?).\n[await][page]\nA paw print and a crudely drawn image of `VOLCANO_BOSS_DESCRIPTION`\nis etched on the paper.\nThis is probably one of \n`FINAL_BOSS_NAME`'s henchmen!\n`SEASIDE_BOSS` likely headed down to\nfind more snacks,\nso it's time to move on.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big dog! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Belome must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BELOME: Oh, no, you're still\n missing [0x7024] item(s).[await][pause] I can't wait any\n longer to see what today's cake\n will be.[await][pause] I'm STARVING![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Belome.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BELOME: It's dreadfully boring\n around here~![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Belome...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you the pizza delivery person?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Are you the pizza delivery person?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Scarecrow-this and Hungry-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Belome.[await]""",
    }


class BowyerBossFight(BossFightPrize):
    _text = "Bowyer"
    _formation = FORM0291
    _members = [
        FormationMember(BOWYEREnemy, 183, 127),
    ]
    _force_start_event = BE0014_SET_7EE00A_TO_PARTY_SIZE_AT_START_OF_FIGHT
    _additional_enemies_to_scale = [AEROEnemy]

    _seaside_letter_name_if_volcano_boss = "a longbow loosing arrows at"
    _seaside_letter_name_if_final_boss = "Bowyer's lackeys."

    _npc_models = [BowyerLargeObject, BowyerOverworldObject, BowyerSmallObject]
    _statue_npc = BowyerStatueObject

    _mook_henchmen = [BossFightHenchman(monster=AEROEnemy, model=AeroHenchman)]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOWYER: Disturb me you must not,\n nya!""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Nya, NYA?![delay_30] Cracked the code, you\n did! But fight you, I will, nya![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Bowyer's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BOWYER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOWYER: That was nyat fair!\n Scram you must, nya![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOWYER: Back again, you are,\n nya? I'm nyat as mad as before.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOWYER: Nya, NYA?! Stop this,\n you must![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Nya, Nya, NYA!  Make like Locke![await]\n Bring me more Strongbow Cider![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Knock, knock, NYA!!\n[await][page]\n Your battle is long and boring,\n even for `SEASIDE_BOSS`, nya!\n[await]\n Aero #837 painted a target on\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano, nya!![await]\n 10,000 arrows will I fire at\n `FINAL_BOSS_NAME`, NYA!\n Follow me to the ship you will NOT!\n Your Scarf requires 100 Super \n Jumps and your Super Suit has\n -127 attack and m. attack, I hope![await][page]\n\n                                  NYA!!!!\n                                    Bowyer[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """FLUNKIE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]""",
        DI2061_HEAD_CHEF: """FLUNKIE: Doesn't this cake\n look just like Bowyer?[await]""",
        DI2062_APPRENTICE_CHEF: """FLUNKIE: We've gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Bowyer must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BOWYER: Nya, NYA!?[await][pause] Disturb me\n you must not, until [0x7024] more item(s)\n you find, nya![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Bowyer's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Bowyer.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\nBOWYER: Nya! Boring here, it is...[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Since I'm having a good day, you\n can stay here free of charge.\n [delay]How's that sound?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Bowyer's house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Don't cause any trouble in our\n town! Stay away from the shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I'm just a customer![delay] Let me shop\n in peace![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There's a very uh... [delay]important\n meeting happening inside.\n [delay]You may not enter.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ What's going on in here?[await][pause] None of\n your business, that's what![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n BOWYER: Interesting, this will be![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Fight me, you will, nya?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Fight me, you will, nya?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Arrow-this and Target-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOWYER: 1000 jumps I must do,\n nya![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOWYER: 1000 jumps I must do,\n nya![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """FLUNKIE: Whoa! You sure showed\n us! Go on ahead to Bowyer's\n place![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """FLUNKIE: Come back and visit\n us sometime. Bowyer won't stay\n mad forever![await]""",
        DI2560_TOWER_HENCHMAN_1: """FLUNKIE: Hello.[await][pause] Bowyer is busy\n now, and he really hates to be\n interrupted.[await][page]\n[delay] ...If you're not going to leave,\n I'll have to kick you out myself![await]""",
        DI2572_TOWER_HENCHMAN_2: """FLUNKIE: I'm gonna have to ask you\n not to interrupt Bowyer's target\n practice.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """FLUNKIE: ...sigh... [delay]Bowyer scolded\n me for interrupting his shooting\n practice.[await][pause] I was just trying to warn\n him that `MAIN_CHARACTER_NAME` is here![await]""",
        DI3073_TOWER_HENCHMAN_3: """FLUNKIE: You look like you'd make\n for a good statue![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Bowyer's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Bowyer.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("PipeVaultGate"), _gf("PipeVaultGating").BOWYER
        ):
            output.extend(
                [
                    ClearBit(PIPE_VAULT_GATED),
                ]
            )
        if world.settings.is_flag_value(
            _gf("Moleville1Gate"), _gf("Moleville1Gating").BOWYER
        ):
            output.extend(
                [
                    ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING),
                ]
            )
        return EventScript(output)


class Croco2BossFight(BossFightPrize):
    _text = "Croco 2"
    _formation = FORM0274
    _members = [
        FormationMember(CROCO2Enemy, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a thieving dinosaur dashing"
    _seaside_letter_name_if_final_boss = "Croco's accomplices."
    _name = "Croco"
    _additional_enemies_to_scale = [CROOKEnemyHenchman]

    _npc_models = [Croco2Object]
    _statue_npc = CrocoStatueObject

    _character_henchmen = [
        BossFightHenchman(monster=CROOKEnemyHenchman, model=CrookHenchman),
        BossFightHenchman(monster=CROOKEnemyHenchman, model=CrookHenchman),
        BossFightHenchman(monster=CROOKEnemyHenchman, model=CrookHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n CROCO: Get the heck outta here![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Alright, alright, so ya figured out\n my password! But I ain't goin'\n down without a fight![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Croco's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped CROCO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CROCO: Enough already, get outta\n here![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CROCO: Back already? How 'bout a\n drink?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """\n    CROCO: 'Dis some kinda joke?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I tapped Canada's Maple Syrup[await]\n Reserve. They'll NEVER catch me!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n 'Sup Half-Wits?!\n[await][page]\n Did it take you 500 years to beat \n `SEASIDE_BOSS`?\n [await]\n While casing my next heist, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano. Seems... nice.[await]\n I better get a crew together with \n `FINAL_BOSS_NAME`\n I'm telling you this because I want \n this to be a challenge this time. \n I bet this bazooka that I lifted from\n that toad "guard" will be useful![await][page]\n\n                                    Seeya!\n                                     Croco[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """FLUNKIE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]""",
        DI2061_HEAD_CHEF: """FLUNKIE: Doesn't this cake\n look just like Croco?[await]""",
        DI2062_APPRENTICE_CHEF: """FLUNKIE: We've gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Croco must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CROCO: What's this?[await][pause] You fools're\n gonna take another 100 years to\n find the last [0x7024] item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Croco's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Croco.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CROCO: Whaddya doin' hangin\n 'round here?[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ You tired? You can stay here\n for free.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Croco's house\n up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ You better not be snooping around\n the shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Huh?[delay] What am I doing here?[delay] None\n of your business, that's what![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n           Nothin' to see here.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Nope, nothing suspicious going on\n in this house![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CROCO: Think ya can beat the dojo\n master, chump? I'd like to see ya\n try![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Wallet-this and Coin-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CROCO: I hate to say it, but...\n I kinda like this![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """FLUNKIE: (Sob, sob...)[delay_30]\n You're pretty tough. I guess I'll let\n you through to Croco's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """FLUNKIE: You beat Croco!?[delay_30]\n We'll getcha for this![await][page]\n Maybe not today, maybe not\n tomorrow, but someday...[await]""",
        DI2560_TOWER_HENCHMAN_1: """FLUNKIE: Croco's busy! Scram![await]\n[delay_60] ...Not leaving, huh?\n[delay] Alright buddy, you asked for it![await]""",
        DI2572_TOWER_HENCHMAN_2: """FLUNKIE: Where d'ya think YOU'RE\n going?![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """\n  FLUNKIE: I could use a stepstool.[await]""",
        DI3073_TOWER_HENCHMAN_3: """\n      FLUNKIE: A tough guy, eh?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Croco's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Croco.[await]""",
    }


class PunchinelloBossFight(BossFightPrize):
    _text = "Punchinello 1"
    _formation = FORM0251
    _members = [
        FormationMember(PUNCHINELLOEnemy, 199, 119),
        FormationMember(MICROBOMBEnemy, 135, 119, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 151, 135, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 183, 151, hidden_at_start=True),
        FormationMember(MICROBOMBEnemy, 215, 159, hidden_at_start=True),
    ]
    _anchor_enemy = PUNCHINELLOEnemy
    _hp_slice_excluded_enemies = [MICROBOMBEnemy]
    _additional_enemies_to_scale = [BOBOMBEnemyHenchman, MEZZOBOMBEnemy]

    _name = "Punchinello"
    _seaside_letter_name_if_seaside_boss = "Hothead"
    _seaside_letter_name_if_volcano_boss = "a demolitionist stomping"
    _seaside_letter_name_if_final_boss = "Punchinello's demo team."

    _npc_models = [PunchinelloLargeObject, PunchinelloSmallObject]
    _statue_npc = PunchinelloStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=BOBOMBEnemyHenchman, model=BobOmbHenchman),
    ]
    _tiny_henchmen = [
        BossFightHenchman(monster=BOBOMBEnemyHenchman, model=MicrobombHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PUNCHINELLO: Grrr... Leave me\n alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So... You figured out my\n password.[await]\n If you're not here for an\n autograph, I'll have to test you\n once more to let you through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Punchinello's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n PUNCHINELLO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """PUNCHINELLO: Grrr... I'll never get famous\n at this rate![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """PUNCHINELLO: You've come back to\n visit? I truly must be famous![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PUNCHINELLO: They say I'm a hot\n head, so it's a bad idea to stand\n on my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ WATCH ME DRINK THIS TOBASCO![await]\n I'm gonna be youtube-famous![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """\n      BOB-OMB: I need a break.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n WHAT'S UP FANS?!\n[await][page]\n I just watched a HYPE fight versus\n `SEASIDE_BOSS`.  Oh.  Em.  Gee.[await]\n\n My Bob-omb army told me about\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.  Fuse is LIT!![await]\n I smell a collab video with \n `FINAL_BOSS_NAME`[await]\n Don't forget to tune in for my 100k\n follower special, where I'll play\n Bob-omb roulette with watermelons![await][page]\n\n           Like, Share, and Subscribe!\n                              Punchinello[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """BOB-OMB: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """\n      BOB-OMB: I need a break.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """\n      BOB-OMB: I need a break.[await]""",
        DI2061_HEAD_CHEF: """BOB-OMB: Doesn't this cake\n look just like Punchinello?[await]""",
        DI2062_APPRENTICE_CHEF: """BOB-OMB: We've gotten quite\n good with fondant.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Punchinello must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PUNCHINELLO: Huh?[delay_30] What the hay?[await]\n Where are the other [0x7024] item(s)?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Punchinello's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Punchinello.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PUNCHINELLO: Hmmm... [delay]Huh?\n [delay]A visitor? [delay]Well, there's not much\n to do around here.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hello there.[await][pause] Today, we've got an\n explosively good deal for you![delay] All\n inn expenses are free of charge.[await]\n Would you like to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Punchinello's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hello there.[delay] Welcome to our humble\n town. We have the least suspicious\n shed in all the land.[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I know how this must look, but I'm\n just here to browse the perfectly\n legal goods they're selling.[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Hello there.[delay] Sorry, but I can't let\n you through this door today.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ You wouldn't wanna enter this\n house, oh no.[delay] We'll make sure you\n don't enter by accident.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PUNCHINELLO: A challenge from\n the dojo master, eh? Let's see\n where this goes.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello. Are you with the press?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong number)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hello. Are you with the press?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong number)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Bomb-this and Famous-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Punchinello's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Punchinello.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """BOB-OMB: I guess I was a little\n hot-headed, thinking I could win.\n Go on in to Punchinello's room.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """BOB-OMB: Wow, you beat\n Punchinello! He's not very happy\n about that.[await]""",
        DI2560_TOWER_HENCHMAN_1: """BOB-OMB: Hello there.[await][pause] If you've\n come for Punchinello's autograph,\n please allow me to buzz you up...[await][page]\n [delay]...You're not here for that?[await]\n [delay]Uh oh, he'll be pretty mad!\n [delay]I'd better do something![await]""",
        DI2572_TOWER_HENCHMAN_2: """BOB-OMB: There's nothing to see\n back here...[await][pause] I mean that.[await]\n You don't believe me?[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """BOB-OMB: I don't look like the\n other bob-ombs here. [delay]That's weird.[await]""",
        DI3073_TOWER_HENCHMAN_3: """BOB-OMB: You don't think it makes\n sense for a bob-omb to be shooting\n bullets?[await][pause] ...Fight me about it![await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BoosterTowerGate"), _gf("BoosterTowerGating").PUNCHINELLO
        ):
            output.extend(
                [
                    ApplySolidityModToLevel(
                        permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0
                    ),
                    ApplyTileModToLevel(
                        use_alternate=True,
                        room_id=R202_BOOSTER_TOWER_ENTRANCE,
                        mod_id=32,
                    ),
                    SetBit(TOWER_OPENED),
                ]
            )
        return EventScript(output)


class BoosterBossFight(BossFightPrize):
    _text = "Booster 1"
    _formation = FORM0271
    _force_start_event = BE0012_DIALOGUE_FROM_BOOSTER_FIGHT
    _members = [
        FormationMember(BOOSTEREnemy, 183, 127),
        FormationMember(SNIFITEnemyHenchman, 135, 119),
        FormationMember(SNIFITEnemyHenchman, 151, 143),
        FormationMember(SNIFITEnemyHenchman, 199, 151),
    ]
    _anchor_enemy = BOOSTEREnemy
    _additional_enemies_to_scale = [APPRENTICEEnemyHenchman]
    _seaside_letter_name_if_volcano_boss = "a viking riding trains"
    _seaside_letter_name_if_final_boss = "Booster's frenemies."
    _name = "Booster"

    _npc_models = [BoosterObject]
    _statue_npc = BoosterStatueObject

    _character_henchmen = [
        BossFightHenchman(monster=SNIFITEnemyHenchman, model=SpookumHenchman),
        BossFightHenchman(monster=SNIFITEnemyHenchman, model=SpookumHenchman),
        BossFightHenchman(monster=SNIFITEnemyHenchman, model=SpookumHenchman),
    ]
    _mook_henchmen = [
        BossFightHenchman(monster=APPRENTICEEnemyHenchman, model=SpookumHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOOSTER: It's pretty cozy in here.[await][pause]\n No, you can't come in![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Eh?[delay_30] THAT was my password?![delay_30]\n I'd better fight you, just to be\n sure.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Booster's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BOOSTER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOOSTER: I'd love to entertain\n you, but I'm busy watching the\n fish. Come back later.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOOSTER: Eh...? My! It's you\n again![await][page]\n  We're having a heated debate over\n what a "party" is, so you can stay\n if you'd like to contribute.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOOSTER: Hm? How's the view up there?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ This Dish Detergent is DELICIOUS![await]\n Number 2, (belch) MORE SOAP!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """SNIFIT 1: There's a 70% chance the\n drink on the table is actually\n punch.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """SNIFIT 2: Booster can't find any\n beetles underwater, but he still\n enjoys watching the fish.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Attention `MAIN_CHARACTER_NAME`,\n[await][page]\n We had an urgent engagement, and\n regret that we couldn't stay and\n play with `SEASIDE_BOSS`.\n[await]\n While on beetle patrol, #2 saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n Snifit three suggested they might be\n `FINAL_BOSS_NAME`\n We're riding the Loco Express to\n the lake of wedding tears.  Also, \n Number 1 says there's no money \n in the budget for new doors.[await][page]\n\n                                   Booster\n                  Dictated but not read[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """SNIFIT 3: Uh... Do you know where\n we could get some cake down here?[await]""",
        DI2061_HEAD_CHEF: """SNIFIT 2: Doesn't this cake\n look just like Booster?[await]""",
        DI2062_APPRENTICE_CHEF: """SNIFIT 3: Uh... I think we should\n have made his mustache bigger.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Booster must have gotten\n lost on his way here.""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n   BOOSTER: Found our town, eh?[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """SNIFIT 1: Welcome![delay] How would you\n like to stay in our fabulous inn\n for free today?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Booster's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """\n You'd better not go near our shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I'm facing a promotion. Do they sell\n anything here that'll make me look\n more professional?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """SNIFIT 3: Uh... Don't look in the\n window. [delay]Pretty please.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """SNIFIT 2: There is nothing of\n interest to you in here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOOSTER: I wonder if the dojo\n master can shape-shift into a\n Mario doll.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Eh? What'd you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Eh? What'd you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Beetle-this and Train-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """SNIFIT 1: Hello there.[await]\n Booster's busy right now, so we\n can't let you in.[await]""",
        DI1945_NIMBUS_GUARD: """SNIFIT 2: Please refrain\n from bothering Booster.[await]"""
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Booster's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Booster.[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """SNIFSTER 1: Hello there.[await]\n Booster's busy right now, so we\n can't let you in.[await]""",
        DI1945_NIMBUS_GUARD: """SNIFSTER 2: Please refrain\n from bothering Booster.[await]"""
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """APPRENTICE: Oh, dear![delay] We've\n failed to keep the intruder away\n from Booster![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """APPRENTICE: Booster's not happy\n about losing. Please do not jump\n on his head.[await]""",
    }


class KnifeGuyGrateGuyBossFight(BossFightPrize):
    _text = "Knife Guy & Grate Guy"
    _formation = FORM0287
    _members = [
        FormationMember(KNIFEGUYEnemy, 151, 119),
        FormationMember(GRATEGUYEnemy, 199, 143),
    ]
    _seaside_letter_name_if_seaside_boss = "the Clowns"
    _seaside_letter_name_if_volcano_boss = "a couple clowns bouncing"
    _seaside_letter_name_if_final_boss = "Grate Guy's clowns."

    _npc_models = [GrateGuyLargeObject, GrateGuySmallObject]
    _statue_npc = GrateGuyStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """GRATE GUY: Get lost, buddy, I'm\n busy![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, a patron![delay_30] Come on in and let's\n get this show on the road![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Knife Guy and Grate Guy's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped KNIFE GUY\n and GRATE GUY!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """GRATE GUY: Yikes, you're pretty\n tough! I need some time to recover.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """GRATE GUY: It's so boring\n around here... Hey, wanna play\n "Look the other way" with me?[await][page]\n Hah! [delay_30]Just kidding![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """GRATE GUY: Sorry, `MAIN_CHARACTER_NAME`,\n but jumping on my head isn't going\n to teach you Blizzard.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Of course I didn't shake it up!![await]\n Go on, have a Root Beer!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """KNIFE GUY: No, I'm not giving you the Bright Card down here![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Heya `MAIN_CHARACTER_NAME`,\n[await][page]\n Looks like you totally thrashed\n `SEASIDE_BOSS`.  Whoopdy do!\n[await]\n Knife Guy tells me he saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They're in a traveling circus with \n `FINAL_BOSS_NAME`\n I was going to open a casino,[await]\n but Knife Guy dropped the ball on\n the building permits, so now our\n ship is sunk.  Stop by sometime,[await]\n we're always down to clown. [await][page]\n\n                                    Later!\n                 Grate Guy & Knife Guy[await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big clown! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Grate Guy must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """GRATE GUY: Hm?[await][pause] Well, you took all\n the trouble to find [0x7000] item(s,\n so... keep looking for the other [0x7024]![await]\n I can stick around all day.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Knife Guy and Grate Guy are busy\n right now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Knife Guy and\n Grate Guy.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """GRATE GUY: Gee, it sure is boring\n around here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Grate Guy...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """GRATE GUY: The dojo master's\n much tougher than I am. Think you\n can win?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Welcome! What brings you here?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Welcome! What brings you here?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Knife-this and Casino-that.[await][page]\n Sometimes I'd like to ask them what\n they're babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """GRATE GUY: Look, `MAIN_CHARACTER_NAME`!\n I've been training so hard, that my\n ball jumps with me![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """GRATE GUY: Look, `MAIN_CHARACTER_NAME`!\n I've been training so hard, that my\n ball jumps with me![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Knife Guy and Grate Guy are busy\n right now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Knife Guy and\n Grate Guy.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BoosterHillGate"), _gf("BoosterHillGating").KGGG
        ):
            output.extend([ClearBit(BOOSTER_HILL_CLOSED)])
        if world.settings.is_flag_value(
            _gf("MarrymoreGate"), _gf("MarrymoreGating").KGGG
        ):
            output.extend([SetBit(MARRYMORE_BACKDOOR_OPEN)])
        return EventScript(output)


class BundtBossFight(BossFightPrize):
    _text = "Bundt 1"
    _formation = FORM0286
    _members = [
        FormationMember(BUNDTEnemy, 199, 127),
        FormationMember(RASPBERRYEnemy, 199, 119),
        FormationMember(TORTEEnemy, 199, 151),
        FormationMember(TORTEEnemy, 135, 119),
    ]
    _anchor_enemy = BUNDTEnemy
    _hp_slice_excluded_enemies = [TORTEEnemy, TORTEEnemy]
    _seaside_letter_name_if_seaside_boss = "the Cake"
    _seaside_letter_name_if_volcano_boss = "a possessed cake walking"
    _seaside_letter_name_if_final_boss = "Bundt's dinner guests."
    _name = "Bundt"

    _npc_models = [BundtLargeObject, BundtSmallObject]
    _statue_npc = BundtStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=TORTEEnemy, model=TorteHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BUNDT: La la la la la la la la la~[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ What a surprise! [delay_30]Welcome![await]\n Let me warm up for the feast![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Bundt's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BUNDT!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BUNDT: Oh...! My beautiful body![await][pause]\n Please go away while I recover![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BUNDT: Come back to celebrate a\n wedding? At least try and eat me\n this time...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BUNDT: OH! MY CANDLES![await]""",
        DI1782_SHIP_BOSS_DRINK: """ I've got my own frosting, thanks.[await]\n "Happy" Frogs taste best, though![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Greetings and Salutations!\n[await][page]\n I can't get over how quickly you\n dispatched `SEASIDE_BOSS`!\n[await]\n My dinner guests informed me of \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I heard they're having a reunion with \n `FINAL_BOSS_NAME`\n I've gotten hungry aboard this ship.\n You wouldn't believe how much you\n can miss your chefs and creams. [await]\n Come visit and have a slice![await][page]\n\n       Frosting my way to victory,\n                                     Bundt[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: This masterpiece is\n our latest creation... wait...[await]""",
        DI2062_APPRENTICE_CHEF: """CHEF TORTE: ...Apprentice! [delay]Why\n does this look like Bundt?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Bundt must have gotten\n lost on its way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BUNDT: Hmm?[delay] You look like you could\n use a break![await][pause] Come back with\n the other [0x7024] item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Bundt is busy right now, so it\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Bundt.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BUNDT: Greetings and salutations!\n Welcome to our quiet little town![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Bundt...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BUNDT: What a fierce battle![await][pause] That\n was nothing compared to the dojo\n master, you know.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What's this?[await][pause] Looking for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ What's this?[await][pause] Looking for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Candle-this and Frosting-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BUNDT: What a delicious training\n exercise![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BUNDT: What a delicious training\n exercise![await]""",
        DI1120_NIMBUS_BIRD_GUARD: """CHEF TORTE: Is dinner time.[await]\n Ze guests are enjoyeeng zeir\n dinner, so ve cannot let you in.[await]""",
        DI1945_NIMBUS_GUARD: """APPRENTICE: Oh, yeah, I'm sure\n they're loving the food. Nice of\n them to invite us in for some...[await]"""
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Bundt is busy right now, so it\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Bundt.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """APPRENTICE: Fine, go on ahead.\n I'll warn you, though, some idiot\n stepped on the cake, so be careful.await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """APPRENTICE: Wow, you ate the\n whole thing? [delay_30]...[delay_30]How was it?[await]""",
        DI2560_TOWER_HENCHMAN_1: """CHEF TORTE: 'Allo. Ze dessert ees\n not ready yet. Please come back\n later, yes?[await][page]\n [delay]...[delay]Escuse me, sir, I said to please\n come back... LATER![await][page]\n[delay]\n   (He von't leave... [delay]Vat to do?)[await][page]\n                YOU FOOLS!![await]""",
        DI2572_TOWER_HENCHMAN_2: """APPRENTICE: Hey, genius, this way\n is the kitchen. Stay out![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """APPRENTICE: Why did Chef Torte\n tell me to stay up here? This is\n nowhere near the kitchen...[await]""",
        DI3073_TOWER_HENCHMAN_3: """APPRENTICE: I'm so bored! The\n other chefs won't let me into the\n kitchen![await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(_gf("SeaGate"), _gf("SeaGating").BUNDT):
            output.extend(
                [
                    SetBit(MAP_SEA),
                    SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
                ]
            )
        return EventScript(output)


class KingCalamariBossFight(BossFightPrize):
    _text = "King Calamari"
    _formation = FORM0277
    _members = [
        FormationMember(KINGCALAMARIEnemy, 222, 94, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 136, 115, hidden_at_start=True),
        FormationMember(TENTACLESEnemy2, 112, 127, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 193, 143, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 168, 156, hidden_at_start=True),
        FormationMember(TENTACLESEnemy, 135, 143, hidden_at_start=True),
    ]
    _extra_hp_enemies = [TENTACLESEnemy2, TENTACLESEnemy2, TENTACLESEnemy]
    _anchor_enemy = KINGCALAMARIEnemy
    _additional_enemies_to_scale = [BLOOBEREnemyHenchman]

    _force_start_event = BE0026_INTRO_SCENE_TENTACLES_RISE_FROM_HOLES
    _force_battlefield = BF03_SUNKEN_SHIP_KING_CALAMARIS_CELLAR
    _seaside_letter_name_if_seaside_boss = "the Squid"
    _seaside_letter_name_if_volcano_boss = "a giant squid lurking"
    _seaside_letter_name_if_final_boss = "King Calamari's hands."

    _npc_models = [BlooberObject]
    _statue_npc = BlooberStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=BLOOBEREnemyHenchman, model=BlooberHenchman),
    ]
    _tiny_henchmen = [
        BossFightHenchman(monster=BLOOBEREnemyHenchman, model=TinyBlooberHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """KING CALAMARI: When I was born, I\n hatched from an egg that was only\n three times as large as this one.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n King Calamari's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n KING CALAMARI!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """KING CALAMARI: I can't believe I\n was defeated in the ship I sunk\n myself...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """KING CALAMARI: Win or lose, I'm\n still king of this ship.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """KING CALAMARI: I'm pretty slimy,\n so this seems like a bad idea.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I've found booty in the hold![await]\n Vats of Pearlescent Oyster Juice![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n There's a wet parchment with ink:\n[await][page]\n There's a surpringly great picture \n your battle with `SEASIDE_BOSS`.[await]\n\n On the back is an image of [await]\n `VOLCANO_BOSS_DESCRIPTION`\n near a volcano, looks like.[await]\n Then a bunch of ?'s next to \n `FINAL_BOSS_NAME`[await]\n Finally, there's a picture of a\n squid with X's for eyes falling\n towards the shipwreck.[await][page]\n\n This drawing raises more questions\n than it answers.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big squid! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Calamari must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """KING CALAMARI: Sorry, I don't\n have any hint memos for where you\n can find the last [0x7024] item(s).[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n King Calamari is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering King Calamari.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """KING CALAMARI: It's not so weird\n for a squid to run a town.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find King Calamari...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """KING CALAMARI: Think you can beat\n the dojo master?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What do you want?[await]\n  [select] (Let's fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ What do you want?[await]\n  [select] (Let's fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Ship-this and Tentacle-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """KING CALAMARI: My tentacles\n shouldn't be able to do this.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """KING CALAMARI: My tentacles\n shouldn't be able to do this.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI2560_TOWER_HENCHMAN_1: """ Hello there. Welcome to our\n first-ever above-ground treasure\n hoard.[await][page]\n [delay].[delay].[delay].[delay]You're not here to see that?[delay_30]\n Well,[delay] then you must be an intruder!""",
        DI2572_TOWER_HENCHMAN_2: """ There's nothing back here!\n I mean it![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """ You've made your point, we'll step\n aside. But you haven't seen\n anything yet![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """ You beat King Calamari?[await][pause] I guess\n that's why this is a Mario game and\n not a Squid Game.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """ I'd just like to go back to\n shooting ink, not bullets...[await]""",
        DI3073_TOWER_HENCHMAN_3: """\n       You looking for a fight?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n King Calamari is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering King Calamari.[await]""",
    }


class HidonBossFight(BossFightPrize):
    _text = "Hidon"
    _formation = FORM0267
    _members = [
        FormationMember(HIDONEnemy, 167, 119),
        FormationMember(GOOMBETTEEnemy, 135, 111, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 135, 135, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 167, 151, hidden_at_start=True),
        FormationMember(GOOMBETTEEnemy, 215, 151, hidden_at_start=True),
    ]
    _anchor_enemy = HIDONEnemy
    _hp_slice_excluded_enemies = [
        GOOMBETTEEnemy,
        GOOMBETTEEnemy,
        GOOMBETTEEnemy,
        GOOMBETTEEnemy,
    ]

    _seaside_letter_name_if_volcano_boss = "a green box sliding about"
    _seaside_letter_name_if_final_boss = "Hidon's monsters."
    _seaside_letter_name_if_final_boss_remake = "Whuhoh's Goombas."
    _remake_name = "Whuhoh"

    _npc_models = [HidonLargeObject, HidonSmallObject]
    _statue_npc = MimicStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=GOOMBETTEEnemy, model=GoombetteLowerHenchman),
    ]
    _tiny_henchmen = [
        BossFightHenchman(monster=GOOMBETTEEnemy, model=GoombetteLowerHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """HIDON: No, I'm not gonna puke up\n another item for you! Go away![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Ugh... What a rude awakening!\n I'm going to make it a hassle for\n you to pass through here![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Hidon's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped HIDON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """HIDON: Guess I'll have to train the\n Goombettes harder.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """HIDON: This is definitely an upgrade\n from my old post.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """HIDON: Oh come on, you know I'm\n weak to jumps![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Goombettes! They're after my[await]\n 1947 Phateu Cetrus Merlot!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Listen up interloper!\n[await][page]\n Good job getting rid of\n `SEASIDE_BOSS`! Now[await]\n my naval dominance is complete!\n The goombette's nest reported[await]\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They sail under the flag of \n `FINAL_BOSS_NAME`[await]\n If you ever touch my box again,\n I'm taking a finger... at least.[await][page]\n\n                  Lots of Carni-kisses,\n                                     Hidon[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """GOOMBETTE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        DI2061_HEAD_CHEF: """GOOMBETTE: Doesn't this cake\n look just like Hidon?[await]""",
        DI2062_APPRENTICE_CHEF: """GOOMBETTE: We've gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Hidon must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """HIDON: ...I don't know where the\n last [0x7024] item(s) are. Ask the\n Goombettes.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Hidon is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Hidon.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n          HIDON: Oh, it's you.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hey! Why don't you crash here for\n the night? It's free! FREE![await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Hidon's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hey! What are you doing in our\n town? Don't go snooping around![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Why don'tcha mind your own\n beeswax?![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Don't even THINK about going\n inside this house![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Hey, buster![delay] You think you're some\n kinda tough guy, tryin' to step\n over us guards?![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """HIDON: The dojo master's pretty\n tough.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Ugh... What'd you wake me up for?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Ugh... What'd you wake me up for?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Piranha-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """HIDON: I bet this would be even\n harder to do in my box.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """HIDON: I bet this would be even\n harder to do in my box.[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """WHUHOH: No, I'm not gonna puke up\n another item for you! Go away![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Whuhoh's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped WHUHOH!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """WHUHOH: Guess I'll have to train\n the Mini Goombas harder.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """WHUHOH: This is definitely an\n upgrade from my old post.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """WHUHOH: Oh come on, you know I'm\n weak to jumps![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Mini Goombas! They're after my[await]\n 1947 Phateu Cetrus Merlot!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """MINI GOOMBA: Besides when he\n haphazardly throws us at enemies,\n Whuhoh is very good to us.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Listen up interloper!\n[await][page]\n Good job getting rid of\n `SEASIDE_BOSS`! Now[await]\n my naval dominance is complete!\n The goombette's nest reported[await]\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They sail under the flag of \n `FINAL_BOSS_NAME`[await]\n If you ever touch my box again,\n I'm taking a finger... at least.[await][page]\n\n                  Lots of Carni-kisses,\n                                    Whuhoh[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """MINI GOOMBA: Hop on the\n trampoline in the next room. It'll\n take you outside. Go on, try it![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """MINI GOOMBA: Besides when he\n haphazardly throws us at enemies,\n Whuhoh is very good to us.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """MINI GOOMBA: Besides when he\n haphazardly throws us at enemies,\n Whuhoh is very good to us.[await]""",
        DI2061_HEAD_CHEF: """MINI GOOMBA: Doesn't this cake\n look just like Whuhoh?[await]""",
        DI2062_APPRENTICE_CHEF: """MINI GOOMBA: We've gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Whuhoh must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """WHUHOH: ...I don't know where the\n last [0x7024] item(s) are. Ask the\n Mini Goombas.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Whuhoh is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Whuhoh.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n        WHUHOH: Oh, it's you.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Whuhoh's\n house up on the hill yet?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """WHUHOH: The dojo master's pretty\n tough.[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """WHUHOH: I bet this would be even\n harder to do in my box.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """WHUHOH: I bet this would be even\n harder to do in my box.[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """GOOMBETTE: Oh yeah? Think you're\n tough, just 'cause you're bigger\n than me?![await]""",
        DI1945_NIMBUS_GUARD: """GOOMBETTE: I heard you laughing!\n Go on, laugh it up! At least I'm\n allowed in the castle![await]"""
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """GOOMBETTE: You mighta' won\n against us, but Hidon's gonna\n beat you up![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """GOOMBETTE: You beat Hidon?![await]\n Oh, man...[await]""",
        DI2560_TOWER_HENCHMAN_1: """GOOMBETTE: I need a pen, but I\n can't reach the top drawer of this\n desk. Can you help me out?[await][page]\n [delay]...What?[delay] "How are you going to\n use a pen when you don't have any\n arms"?[await][pause] You makin' fun of me?!\n [delay]That's IT, buddy! Get down here![await]""",
        DI2572_TOWER_HENCHMAN_2: """GOOMBETTE: Hey! Hidon's trying to\n stay in hidin' over here![delay] Get lost![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """GOOMBETTE: (I'm too short to see\n out this window.)[await]""",
        DI3073_TOWER_HENCHMAN_3: """GOOMBETTE: Put up your dukes,\n tough guy![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """MINI GOOMBA: You mighta' won\n against us, but Whuhoh's gonna\n beat you up![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """MINI GOOMBA: You beat Whuhoh?![await]\n Oh, man...[await]""",
        DI2560_TOWER_HENCHMAN_1: """MINI GOOMBA: I need a pen, but I\n can't reach the top drawer of this\n desk. Can you help me out?[await][page]\n [delay]...What?[delay] "How are you going to\n use a pen when you don't have any\n arms"?[await][pause] You makin' fun of me?!\n [delay]That's IT, buddy! Get down here![await]""",
        DI2572_TOWER_HENCHMAN_2: """MINI GOOMBA: Hey! Whuhoh's trying\n to stay in hidin' over here![delay_30]\n Get lost![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """MINI GOOMBA: (I'm too short to\n see out this window.)[await]""",
        DI3073_TOWER_HENCHMAN_3: """MINI GOOMBA: Put up your dukes,\n tough guy![await]""",
    }
    _dialog_replacements_remake = {
        DI1120_NIMBUS_BIRD_GUARD: """MINI GOOMBA: Oh yeah? Think\n you're tough, just 'cause you're\n bigger than me?![await]""",
        DI1945_NIMBUS_GUARD: """MINI GOOMBA: I heard you laughing!\n Go on, laugh it up! At least I'm\n allowed in the castle![await]"""}


class JohnnyBossFight(BossFightPrize):
    _text = "Johnny 1"
    _formation = FORM0276
    _members = [
        FormationMember(JOHNNYEnemy, 183, 127),
        FormationMember(BANDANABLUEEnemy, 135, 111),
        FormationMember(BANDANABLUEEnemy, 135, 135),
        FormationMember(BANDANABLUEEnemy, 183, 159),
        FormationMember(BANDANABLUEEnemy, 215, 151),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 0, 0, hidden_at_start=True),
    ]
    _name = "Johnny"
    _seaside_letter_name_if_volcano_boss = "a shark prowling around"
    _seaside_letter_name_if_final_boss = "Johnny's crew."
    _seaside_letter_name_if_sunken_ship_boss = "Jonathan “Johnny” Jones"
    _anchor_enemy = JOHNNYEnemy
    _hp_slice_excluded_enemies = [
        BANDANABLUEEnemy,
        BANDANABLUEEnemy,
        BANDANABLUEEnemy,
        BANDANABLUEEnemy,
        WATERCRYSTALEnemy,
        WATERCRYSTALEnemy,
    ]
    _scaling_excluded_enemies = [WATERCRYSTALEnemy, WATERCRYSTALEnemy]

    _npc_models = [JohnnyLargeObject, JohnnySmallObject]
    _statue_npc = JohnnyStatueObject

    _character_henchmen = [
        BossFightHenchman(monster=BANDANABLUEEnemy, model=BandanaBlueHenchman),
        BossFightHenchman(monster=BANDANABLUEEnemy, model=BandanaBlueHenchman),
        BossFightHenchman(monster=BANDANABLUEEnemy, model=BandanaBlueHenchman),
        BossFightHenchman(monster=BANDANABLUEEnemy, model=BandanaBlueHenchman),
    ]
    _mook_henchmen = [
        BossFightHenchman(monster=BANDANAREDEnemyHenchman, model=BandanaRedHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JOHNNY: Matey, it'd be mighty fun\n to spar again, but I'm tryin' to\n sleep now.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Good job, matey... But ye gotta\n fight me first if ye wanna be let\n through![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,\n[await][page]\n Knowin' you, knocking down\n `SEASIDE_BOSS` was a breeze.[await]\n\n By the way, my pirates saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n It's probably one of \n `FINAL_BOSS_NAME`[await]\n Well, my gills are failing on me,\n so I'll be heading back down.\n Drop in when you have time, okay?[await][page]\n\n                         Your true mate,\n             Jonathan "Johnny" Jones[await]""",
        DI2061_HEAD_CHEF: """PIRATE: Y'arr, don't ye think\n this cake here be lookin' just like\n Johnny?[await]""",
        DI2062_APPRENTICE_CHEF: """PIRATE: Us pirates are pretty\n good with food, arr harr![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jones must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JOHNNY: Found [0x7000] item(s, eh? Arr,\n harr, harr...! You gotta find [0x7024]\n more, matey![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Johnny is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Johnny.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n        JOHNNY: Ahoy, matey![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome, matey! How'd ya like to\n stay here tonight, on the house?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two fellas o'er in the left\n building have been actin' weird.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ It ain't always easy gettin' into\n the Sea.[await][pause] Ya might need to do\n somethin' else, first![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have ye been to visit Johnny up\n on the hill yet, matey?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Arr, what ye be doin' in our town?\n Just stay away from the shed,\n ya hear?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Out in yonder Sunken Ship, there\n be a... er...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ A treasure chest, behind a big\n stack o' boxes! Don't forget about\n it, matey![await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ If ye can tough it out through the\n ship, you can come back here for\n some... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Come back here for some FUN,\n arr harr! Ya got that, matey?![await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """\n       I just be shoppin', matey.[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Read my lips... WE AIN'T LETTIN'\n YA THROUGH![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n You ain't gettin in here! It's ours![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JOHNNY: Good luck, matey. The dojo\n master's mighty tough.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Arr-this and Matey-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JOHNNY: Matey, I've got lots o'\n training to do![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """JOHNNY: Matey, I've got lots o'\n training to do![await]""",
        DI1120_NIMBUS_BIRD_GUARD: """ Read my lips... WE AIN'T LETTIN'\n YA THROUGH![await]""",
        DI1945_NIMBUS_GUARD: """ Arr, they won't even let us go for\n a dip in the springs! We're FISH![await]\n ...Time to unionize, arr harr![await]"""
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Johnny is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Johnny.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI2560_TOWER_HENCHMAN_1: """PIRATE: Welcome, matey![await][pause] Here to\n spar with Johnny, are ye?[await][page]\n Arr, good fun! Let's have a\n warm-up round![await]""",
        DI2572_TOWER_HENCHMAN_2: """PIRATE: This ain't the corner you\n want, matey![await][pause] But while you're here,\n let's have a spar, arr harr![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """PIRATE: I know there be some fine\n loot in this tower, but it's too far\n 'bove sea level for my liking![await]""",
        DI3073_TOWER_HENCHMAN_3: """PIRATE: I'll make ya see stars,\n arr harr![await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("YaridovichGate"), _gf("YaridovichGating").JOHNNY
        ):
            output.extend([SetBit(SEASIDE_BOSS_AVAILABLE)])
        return EventScript(output)


class YaridovichBossFight(BossFightPrize):
    _text = "Yaridovich"
    _formation = FORM0290
    _members = [
        FormationMember(YARIDOVICHEnemy, 183, 127),
        FormationMember(YARIDOVICHMirageEnemy, 183, 127, hidden_at_start=True),
    ]
    _anchor_enemy = YARIDOVICHEnemy
    _hp_slice_excluded_enemies = [YARIDOVICHMirageEnemy]
    _additional_enemies_to_scale = [DRILLBITEnemy]

    _seaside_letter_name_if_seaside_boss = "Yarid"
    _seaside_letter_name_if_seaside_boss_remake = "Speary"
    _seaside_letter_name_if_volcano_boss = "some conspicuous toads circling"
    _seaside_letter_name_if_final_boss = "Yaridovich's spies."
    _seaside_letter_name_if_final_boss_remake = "Speardovich's spies."
    _remake_name = "Speardovich"

    _npc_models = [YaridovichLargeObject, YaridOverworldObject, YaridovichSmallObject]
    _statue_npc = YaridovichStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=DRILLBITEnemy, model=DrillbitHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """YARIDOVICH: How could I lose to\n those...[delay] Huh? Hey, get lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Eee hee hee! So, you've cracked the\n code... Now, it's time for the\n REAL test![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Yaridovich's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n YARIDOVICH!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """YARIDOVICH: Ridiculous! How could\n a genius like me lose to them...?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """YARIDOVICH: I'm thinking it might\n be time for me to switch careers.[await][page]\n Say, do you happen to know anyone\n who's looking to hire a\n hydrodemolitions expert?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """YARIDOVICH: This is just adding\n insult to injury![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,\n[await][page]\n By now, you've certainly defeated\n `SEASIDE_BOSS`, I think!\n[await]\n My "Toad" spies tell me they saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I suspect they're one of \n `FINAL_BOSS_NAME`\n Give'em "the Tickler" from me![await]\n My joints are starting to rust,\n so I'll be headin' back down.\n Stop by whenever you need[await]\n something unsavory, okay?[await][page]\n\n                   Your confidant,\n                         Yaridovich[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """TOWNSPERSON: Hop on... the\n trampoline... in the next room.\n It'll take you... outside.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ My disguise was as see-through[await]\n as this glass of Motor Oil!![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]""",
        DI2061_HEAD_CHEF: """TOWNSPERSON: We must... make\n this cake... look exactly...\n like Yaridovich.[await]""",
        DI2062_APPRENTICE_CHEF: """TOWNSPERSON: We need... more\n fondant.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Yaridovich must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """YARIDOVICH: Eee hee...! You're\n still missing [0x7024] item(s)! Isn't that\n a shame?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Yaridovich is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Yaridovich.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """YARIDOVICH: A challenge from the\n dojo master? [delay]Eee hee hee, this\n ought to be interesting![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Eee hee...! You want to fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Eee hee...! You want to fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Brownie-this and Tickle-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """YARIDOVICH: I guess I wasn't as\n strong as I thought...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """YARIDOVICH: I guess I wasn't as\n strong as I thought...[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """\n There's nothing...to see...in here.[await]""",
        DI1945_NIMBUS_GUARD: """ If you have...no business...please\n leave.[await]"""
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """SPEARDOVICH: How could I lose to\n those...[delay] Huh? Hey, get lost![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Speardovich's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n SPEARDOVICH!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """SPEARDOVICH: Ridiculous! How\n could a genius like me lose to\n them...?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """SPEARDOVICH: I'm thinking it might\n be time for me to switch careers.[await][page]\n Say, do you happen to know anyone\n who's looking to hire a\n hydrodemolitions expert?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """SPEARDOVICH: This is just adding\n insult to injury![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,\n[await][page]\n By now, you've certainly defeated\n `SEASIDE_BOSS`, I think!\n[await]\n My "Toad" spies tell me they saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I suspect they're one of \n `FINAL_BOSS_NAME`\n Give'em "the Tickler" from me![await]\n My joints are starting to rust,\n so I'll be headin' back down.\n Stop by whenever you need[await]\n something unsavory, okay?[await][page]\n\n                   Your confidant,\n                         Speardovich[await]""",
        DI2061_HEAD_CHEF: """TOWNSPERSON: We must... make\n this cake... look exactly...\n like Speardovich.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Speardovich must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """SPEARDOVICH: Eee hee...! You're\n still missing [0x7024] item(s)! Isn't that\n a shame?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Speardovich is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Speardovich.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """SPEARDOVICH: A challenge from the\n dojo master? [delay]Eee hee hee, this\n ought to be interesting![await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """SPEARDOVICH: I guess I wasn't as\n strong as I thought...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """SPEARDOVICH: I guess I wasn't as\n strong as I thought...[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """TOWNSPERSON: Well done...\n You may go on... to Yaridovich.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """TOWNSPERSON: You won...\n Well done...[await]""",
        DI2560_TOWER_HENCHMAN_1: """TOWNSPERSON: I'm just... a\n secretary. Don't bother...\n Yaridovich.[await]""",
        DI2572_TOWER_HENCHMAN_2: """TOWNSPERSON: This is...not...\n the right way.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """TOWNSPERSON: It's nice...\n outside.[await]""",
        DI3073_TOWER_HENCHMAN_3: """TOWNSPERSON: You want...to\n fight?[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """TOWNSPERSON: Well done...\n You may go on... to Speardovich.[await]""",
        DI2560_TOWER_HENCHMAN_1: """TOWNSPERSON: I'm just... a\n secretary. Don't bother...\n Speardovich.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("LandsEndGate"), _gf("LandsEndGating").YARIDOVICH
        ):
            output.extend([ClearBit(LANDS_END_GATED)])
        return EventScript(output)


class MokuraBossFight(BossFightPrize):
    _text = "Mokura"
    _formation = FORM0314
    _members = [
        FormationMember(FORMLESSEnemy, 167, 135),
        FormationMember(MOKURAEnemy, 167, 135, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a noxious cloud floating"
    _seaside_letter_name_if_final_boss = "Mokura's collective."
    _seaside_letter_name_if_final_boss_remake = "Gassox' collective."
    _remake_name = "Gassox"
    _anchor_enemy = MOKURAEnemy
    _hp_slice_excluded_enemies = [FORMLESSEnemy]

    _npc_models = [MokuraLargeObject, MokuraSmallObject]
    _statue_npc = MokuraStatueObject

    _tiny_henchmen = [
        BossFightHenchman(monster=MOKURAEnemy, model=MokuraHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n     MOKURA: Uhh... Go away![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """\n             Duh, huh, huh...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Mokura's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped MOKURA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n            MOKURA: Hmm...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MOKURA: What're you doing in my\n secret lair?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MOKURA: I oughta go back to\n being invisible...[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Mmm...uhhh. Cotton Candy![await]\n ...It's...so...airy...YUM![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n ...Is this invisible ink?\n[await][page]\n \n (Defeated `SEASIDE_BOSS`.  Good.)[await]\n\n (Sensed...\n `VOLCANO_BOSS_DESCRIPTION`\n near volcano...)[await]\n (Ethereal bond with\n `FINAL_BOSS_NAME`).[await]\n\n This last part just reeks of\n flatulence... [await][page]\n\n           \n                                (Mokura)[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big cloud! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Mokura must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MOKURA: Uhh... You need [0x7024] more\n item(s)...[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Mokura's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Mokura.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n       MOKURA: Mwa, ha, ha![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Mokura...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MOKURA: Uhh... Are you... gonna\n beat the Dojo Master?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Uhh... Hi there.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Uhh... Hi there.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Secret-this and Gas-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n    MOKURA: Clouds can't jump...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n    MOKURA: Clouds can't jump...[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n      GASSOX: Uhh... Go away![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Gassox' place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped GASSOX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n           GASSOX: Hmm...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """GASSOX: What're you doing in my\n secret lair?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """GASSOX: I oughta go back to\n being invisible...[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n ...Is this invisible ink?\n[await][page]\n \n (Defeated `SEASIDE_BOSS`.  Good.)[await]\n\n (Sensed...\n `VOLCANO_BOSS_DESCRIPTION`\n near volcano...)[await]\n (Ethereal bond with\n `FINAL_BOSS_NAME`).[await]\n\n This last part just reeks of\n flatulence... [await][page]\n\n           \n                                (Gassox)[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Gassox must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """GASSOX: Uhh... You need [0x7024] more\n item(s)...[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Gassox is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Gassox.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n        GASSOX: Mwa, ha, ha![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Gassox...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """GASSOX: Uhh... Are you... gonna\n beat the Dojo Master?[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n     GASSOX: Clouds can't jump...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n     GASSOX: Clouds can't jump...[await]""",
    }


class Belome2BossFight(BossFightPrize):
    _text = "Belome 2"
    _formation = FORM0279
    _members = [
        FormationMember(BELOME2Enemy, 183, 127),
        FormationMember(MARIOCLONEEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL2Enemy, 215, 159, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a hungry dog walking"
    _seaside_letter_name_if_final_boss = "Belome's clones."
    _name = "Belome"

    _anchor_enemy = BELOME2Enemy
    _hp_slice_excluded_enemies = [MARIOCLONEEnemy, TOADSTOOL2Enemy]
    _additional_enemies_to_scale = [MALLOWCLONEEnemy, GENOCLONEEnemy, BOWSERCLONEEnemy]
    _character_henchmen = [
        BossFightHenchman(
            monster=MARIOCLONEEnemy, model=MariocloneHenchman
        ),
        BossFightHenchman(monster=MALLOWCLONEEnemy, model=MallowcloneHenchman),
        BossFightHenchman(monster=GENOCLONEEnemy, model=GenocloneHenchman),
        BossFightHenchman(
            monster=TOADSTOOL2Enemy, model=PeachcloneHenchman
        ),
    ]

    _mook_henchmen = [
        BossFightHenchman(
            monster=MARIOCLONEEnemy, model=MariocloneHenchman
        ),
        BossFightHenchman(
            monster=TOADSTOOL2Enemy, model=PeachcloneHenchman
        ),
        BossFightHenchman(monster=GENOCLONEEnemy, model=GenocloneHenchman),
        BossFightHenchman(monster=MALLOWCLONEEnemy, model=MallowcloneHenchman),
        BossFightHenchman(
            monster=BOWSERCLONEEnemy, model=BowsercloneHenchman_2
        ),
    ]

    _npc_models = [Belome2LargeObject, Belome2SmallObject]
    _statue_npc = BelomeSmallStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n        BELOME: Good night~![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Belome's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BELOME!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BELOME: Oh, you're back![await]\n Did you bring any food?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BELOME: Say, it's past my bedtime.\n Can you get off of my head?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Woof, I ate too many Mallows~![await]\n I should wash it down with Tonic~![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: "\n                    ••••••[await]",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hey `MAIN_CHARACTER_TITLE`, have\n you seen my parents?[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ It's a damp, slimy, looking note\n (did `SEASIDE_BOSS` LICK this?).\n[await][page]\nA paw print and a crudely drawn image of `VOLCANO_BOSS_DESCRIPTION`\nis etched on the paper.\nThis is probably one of \n`FINAL_BOSS_NAME`'s henchmen!\n`SEASIDE_BOSS` likely headed down to\nfind more snacks,\nso it's time to move on.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ If you find any Star\n Pieces, think you could hand them\n over?[await][page]\n No? [delay]...Oh well, I tried.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Take the trampoline in the next\n room. Go on, get outta here![await]""",
        DI2061_HEAD_CHEF: "\n                    ••••••[await]",
        DI2062_APPRENTICE_CHEF: " I've baked a cake for you.[await][pause]\n It just happens to look\n like a dog.[await]",
        DI2180_CHAPEL_NPC: """ Reverend Belome must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BELOME: Oh, no, you're still\n missing [0x7024] item(s).[await][pause] I can't wait any\n longer to see what today's cake\n will be.[await][pause] I'm STARVING![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Belome.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BELOME: It's dreadfully boring\n around here~![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Belome...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you the pizza delivery `MAIN_CHARACTER_GENDER_CASUAL`?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Are you the pizza delivery `MAIN_CHARACTER_GENDER_CASUAL`?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Scarecrow-this and Hungry-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: "\n                    ••••••[await]",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """TOADSTOOL 2: Yuck, I don't want\n to play ANYTHING with you![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Need a nap?\n You can stay here for free.[await][pause] No dolls will\n wander around overnight, I swear.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """\n                    ••••••[await]""",
        DI1945_NIMBUS_GUARD: """ There's nothing unusual about\n someone as pretty as me being a\n security guard![await]"""
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Belome.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: "\n                    ••••••[await]",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: "\n                    ••••••[await]",
        DI2560_TOWER_HENCHMAN_1: "\n                    ••••••[await]",
        DI2572_TOWER_HENCHMAN_2: """ If you aren't here to tell us about\n a really great cake recipe, then\n shoo![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """(What do Star Pieces even look\n like...?)[await]""",
        DI3073_TOWER_HENCHMAN_3: """\n    I serve...a higher authority...[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("MonstroTownGate"), _gf("MonstroTownGating").BELOME_2
        ):
            output.extend(
                [
                    RemoveObjectFromSpecificLevel(
                        NPC_3, R427_BELOME_TEMPLE_AREA_10_PIPE_TO_MONSTRO_TOWN
                    ),
                    SetBit(MAP_DIRECTIONAL_LANDS_END_MONSTRO_TOWN),
                    SetBit(MAP_MONSTRO_TOWN),
                ]
            )
        return EventScript(output)


class JaggerBossFight(BossFightPrize):
    _text = "Jagger"
    _formation = FORM0299
    _members = [
        FormationMember(JAGGEREnemy, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a turtle shoulder-charging"
    _seaside_letter_name_if_final_boss = "Jagger's compatriots."

    _npc_models = [TerrapinObject]
    _statue_npc = TerrapinStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JAGGER: It'd be fun to fight\n again, but I need a nap.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Wow, you figured out the\n password! Come on in and let's\n have a spar![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jagger's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped JAGGER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """JAGGER: Wow, what a fight! I\n better think about what I'm gonna\n do to win next time...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JAGGER: Welcome back! I've been\n training hard for our next fight,\n whenever that may be![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JAGGER: `MAIN_CHARACTER_NAME`, I can't\n jump as high as you. Is this\n really necessary?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ My Sensei's drink is gross...[await]\n Here, my Black Tea is WAY better.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hi `MAIN_CHARACTER_NAME`!\n[await][page]\n I saw you give the business to\n `SEASIDE_BOSS`! It was\n a shell of a good hit!! [await]\n While out training, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I hear they run with\n `FINAL_BOSS_NAME`\n I hope you've been practicing your[await]\n timed blocks! I'll know the next\n time I use terrapunch on you![await][page]\n\n                          You can do it!\n                                    Jagger[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big turtle! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jagger must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JAGGER: Oh, wow, you've already\n found [0x7000] item(s)![await][pause] I bet you'll find\n the last [0x7024] in no time.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jagger's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jagger.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\nJAGGER: Hi, `MAIN_CHARACTER_NAME`![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jagger...\n in his house. He is...the most\n respected person here.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello. May I help you?[await]\n  [select] (Let's fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hello. May I help you?[await]\n  [select] (Let's fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Sensei-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """JAGGER: Sensei, the new regimen\n will strengthen us, right?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Jagger's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Jagger.[await]""",
    }


class Jinx1BossFight(BossFightPrize):
    _text = "Jinx 1"
    _formation = FORM0288
    _members = [
        FormationMember(JINX1Enemy, 183, 127),
    ]
    _force_start_event = BE0071_JINX_USES_TRIPLE_KICK
    _seaside_letter_name_if_volcano_boss = "a small figure blinking"
    _seaside_letter_name_if_final_boss = "Jinx's kouhai."
    _name = "Jinx"

    _npc_models = [Jinx1SmallObject]
    _statue_npc = JinxStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JINX: Please do not disturb me.\n I am training in here.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   JINX: I was going easy on you![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JINX: I must accept that I have been\n bested. Good work![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JINX: Yes, I am short! Show a little\n respect![await]""",
        DI1782_SHIP_BOSS_DRINK: """ We're warming up `MAIN_CHARACTER_NAME`![await]\n But first, a Green Tea break![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n Have you mastered your training\n with `SEASIDE_BOSS`?\n[await]\n I sense your next challenge is\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They battle in the old style of \n `FINAL_BOSS_NAME`\n Complete this task, and you will[await]\n be prepared for our rematch.\n Fail, and you need not ever show\n your face on my ship again. There[await]\n are some promising turtles here. [await][page]\n\n                       Fight with honor,\n                                      Jinx[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jinx must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jinx.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n               JINX: Hmm...[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JINX: Master!\n Share your wisdom with us![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Jinx.[await]""",
    }


class Jinx2BossFight(BossFightPrize):
    _text = "Jinx 2"
    _formation = FORM0297
    _members = [
        FormationMember(JINX2Enemy, 183, 127),
    ]
    _force_start_event = BE0072_JINX_USES_QUICKSILVER
    _seaside_letter_name_if_volcano_boss = "a small figure blinking"
    _seaside_letter_name_if_final_boss = "Jinx's kouhai."
    _name = "Jinx"

    _npc_models = [Jinx2SmallObject]
    _statue_npc = JinxStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JINX: Please do not disturb me.\n I am training in here.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   JINX: I was going easy on you![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JINX: I must accept that I have been\n bested. Good work![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JINX: Yes, I am short! Show a little\n respect![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Well-fought, `MAIN_CHARACTER_NAME`![await]\n I've some Jasmine Tea for this day![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n Have you mastered your training\n with `SEASIDE_BOSS`?\n[await]\n I sense your next challenge is\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They battle in the old style of \n `FINAL_BOSS_NAME`\n Complete this task, and you will[await]\n be prepared for our rematch.\n Fail, and you need not ever show\n your face on my ship again. There[await]\n are some promising turtles here. [await][page]\n\n                       Fight with honor,\n                                      Jinx[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jinx must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jinx.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n               JINX: Hmm...[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JINX: Master!\n Share your wisdom with us![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Jinx.[await]""",
    }


class Jinx3BossFight(BossFightPrize):
    _text = "Jinx 3"
    _formation = FORM0298
    _members = [
        FormationMember(JINX3Enemy, 183, 127),
    ]
    _force_start_event = BE0073_JINX_USES_BOMBS_AWAY
    _seaside_letter_name_if_volcano_boss = "a small figure blinking"
    _seaside_letter_name_if_final_boss = "Jinx's kouhai."
    _name = "Jinx"

    _npc_models = [Jinx3SmallObject]
    _statue_npc = JinxStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JINX: Please do not disturb me.\n I am training in here.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   JINX: I was going easy on you![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JINX: I must accept that I have been\n bested. Good work![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JINX: Yes, I am short! Show a little\n respect![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Hail, Master `MAIN_CHARACTER_NAME`![await]\n Let us celebrate with Matcha![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n Have you mastered your training\n with `SEASIDE_BOSS`?\n[await]\n I sense your next challenge is\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They battle in the old style of \n `FINAL_BOSS_NAME`\n Complete this task, and you will[await]\n be prepared for our rematch.\n Fail, and you need not ever show\n your face on my ship again. There[await]\n are some promising turtles here. [await][page]\n\n                       Fight with honor,\n                                      Jinx[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jinx must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jinx.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n               JINX: Hmm...[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JINX: Master!\n Share your wisdom with us![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Jinx.[await]""",
    }


class CulexBossFight(BossFightPrize):
    _text = "Culex 1"
    _formation = FORM0322
    _members = [
        FormationMember(CULEXEnemy, 183, 103),
        FormationMember(FIRECRYSTALEnemy, 135, 103, hidden_at_start=True),
        FormationMember(WATERCRYSTALEnemy, 151, 119, hidden_at_start=True),
        FormationMember(EARTHCRYSTALEnemy, 183, 135, hidden_at_start=True),
        FormationMember(WINDCRYSTALEnemy, 215, 143, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "an ethereal knight gliding"
    _seaside_letter_name_if_final_boss = "Culex's travelers."
    _name = "Culex"

    _anchor_enemy = CULEXEnemy
    _hp_slice_excluded_enemies = [
        FIRECRYSTALEnemy,
        WATERCRYSTALEnemy,
        EARTHCRYSTALEnemy,
        WINDCRYSTALEnemy,
    ]

    _npc_models = [CulexLargeObject, CulexSmallObject]
    _statue_npc = CulexStatueObject

    _character_henchmen = [
        BossFightHenchman(monster=FIRECRYSTALEnemy, model=FireCrystalHenchman),
        BossFightHenchman(monster=WATERCRYSTALEnemy, model=WaterCrystalHenchman),
        BossFightHenchman(monster=EARTHCRYSTALEnemy, model=EarthCrystalHenchman),
        BossFightHenchman(monster=WINDCRYSTALEnemy, model=WindCrystalHenchman),
    ]
    _mook_henchmen = [
        BossFightHenchman(monster=FIRECRYSTALEnemy, model=FireCrystalHenchman),
        BossFightHenchman(monster=WATERCRYSTALEnemy, model=WaterCrystalHenchman),
        BossFightHenchman(monster=EARTHCRYSTALEnemy, model=EarthCrystalHenchman),
        BossFightHenchman(monster=WINDCRYSTALEnemy, model=WindCrystalHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CULEX: Please do not attempt to\n crack this egg again.[await][page]\n It will not give you thousands of\n experience points.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ You have passed the first test.\n But you're not finished yet!\n Please enter.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Culex's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped CULEX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CULEX: This world truly is\n uninhabitable for me and my kind...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CULEX: Greetings. It is good to\n make your acquaintance once\n again.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CULEX: This is not the encounter In expected when I came to visit this\n world.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ How droll, my crystals shattered.[await]\n I've only Bacchus Wine remaining.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """WATER CRYSTAL: I guess this is as\n close as I'll get to being returned\n to Mysidia.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Greetings, honored Warrior.\n[await][page]\n I have witnessed you do battle with\n `SEASIDE_BOSS`. \n I am impressed, but not surprised.[await]\n In my travels of your world, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n The crystals revealed they are \n allies of `FINAL_BOSS_NAME`.[await]\n I know not your path to victory, \n but challenge awaits you there. \n I must return to the sea, lest the\n fragile water crystal shatter.[await][page]\n\n                       Fight with honor,\n                                     Culex[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """EARTH CRYSTAL: I thought the\n Dark Elf was a bit strange, until\n we came to this world.[await]\n You truly have some characters\n here![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """FIRE CRYSTAL: Of course I'm\n miserable! We're UNDERWATER![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """WIND CRYSTAL: Culex is nice and\n all, but I miss Yang sometimes.[await]""",
        DI2061_HEAD_CHEF: """FIRE CRYSTAL: We needed a lot of\n heat to bake a cake of this size.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Culex must have gotten\n lost on his way here.""",
        DI2062_APPRENTICE_CHEF: """WATER CRYSTAL: We must shape\n this confection to resemble Culex.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CULEX: You must retrieve [0x7024] more\n item(s) before we may proceed.[await]\n Godspeed, champion knight![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Culex is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Culex.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n           CULEX: Good day.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome to our inn.[await]\n We are offering a competitive price\n of zero coins per night.[await]\n Will you be staying tonight?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Culex's\n house up on the hill yet?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """FIRE CRYSTAL: This area is\n off-limits.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """WATER CRYSTAL: This door is a...\n uh... portal to another dimension!\n We can't let you fall into it.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CULEX: It will be quite difficult to\n claim victory over the dojo master.\n I wish you luck.[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """FIRE CRYSTAL: This area is\n off-limits.[await]""",
        DI1945_NIMBUS_GUARD: """WIBD CRYSTAL: Are you sure you\n want to mess with a water crystal\n in a cloud kingdom?[await]"""
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """CRYSTAL: Proceed forth. Culex\n awaits you.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """CRYSTAL: Well met! You have\n satisfied Culex's hunger for a\n true challenge.[await]""",
        DI2560_TOWER_HENCHMAN_1: """FIRE CRYSTAL: Greetings.[await][pause] Culex\n is making preparations to head\n back to his home world.[await][pause] He's\n busy right now.[await][page]\n Please come back later...\n [delay]unless you want to get hurt![await]""",
        DI2572_TOWER_HENCHMAN_2: """WATER CRYSTAL: You are not going\n to find what you're seeking back\n here.[delay] Stay out.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """EARTH CRYSTAL: Wind Crystal\n really should have been the one\n standing guard all the way up here.[await]""",
        DI3073_TOWER_HENCHMAN_3: """EARTH CRYSTAL: Stand back!\n I might know Sandstorm![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Culex is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Culex.[await]""",
    }


class BoxBoyBossFight(BossFightPrize):
    _text = "Box Boy"
    _formation = FORM0268
    _members = [
        FormationMember(BOXBOYEnemy, 183, 127),
        FormationMember(FAUTSOEnemy, 151, 111, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a grey box sliding about"
    _seaside_letter_name_if_final_boss = "Box Boy's monsters."
    _seaside_letter_name_if_final_boss_remake = "Pleaseno's monsters"
    _remake_name = "Pleaseno"
    _hp_slice_excluded_enemies = [FAUTSOEnemy]
    _anchor_enemy = BOXBOYEnemy

    _npc_models = [BoxBoyLargeObject, BoxBoySmallObject]
    _statue_npc = MimicStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOX BOY: How many times are you\n gonna wake me up? Get lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, you're gonna PAY for waking\n me up like this![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Box Boy's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BOX BOY!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n    BOX BOY: You just got lucky![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """\n   BOX BOY: This place is boring.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOX BOY: You sure you wanna jump\n on me? I counter special attacks.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ You don't even deserve to LOOK at[await]\n My 1990 Comanee-Ronti Pinot Noir![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Trespassers BEWARE:\n[await][page]\n Loitering Prohibited (yes, you too\n `SEASIDE_BOSS`!)\n[await]\n Don't think I didn't see\n `VOLCANO_BOSS_DESCRIPTION`\n either, keep to your volcano.[await]\n We all know what happened to\n `FINAL_BOSS_NAME`\n the last time they showed up here.\n Also, I expect SILENCE.  No spells.\n Casting a spell is a good way to\n get blasted.  You've been warned.[await][page]\n\n             Now, GET OFF MY LAWN!!\n                                  Box Boy[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Boy must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BOX BOY: Still missing [0x7024] item(s)?\n Pathetic![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Box Boy's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Box Boy.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BOX BOY       What'd you come here for?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Box Boy...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOX BOY: The dojo master's gonna\n kick your butt![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ This'd BETTER be important![await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ This'd BETTER be important![await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOX BOY:\n      Ahh, you're not so tough![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOX BOY:\n      Ahh, you're not so tough![await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PLEASENO: How many times are you\n gonna wake me up? Get lost![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Pleaseno's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped PLEASENO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   PLEASENO: You just got lucky![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """\n   PLEASENO: This place is boring.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PLEASENO: You sure you wanna\n jump on me? I counter special\n attacks.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Trespassers BEWARE:\n[await][page]\n Loitering Prohibited (yes, you too\n `SEASIDE_BOSS`!)\n[await]\n Don't think I didn't see\n `VOLCANO_BOSS_DESCRIPTION`\n either, keep to your volcano.[await]\n We all know what happened to\n `FINAL_BOSS_NAME`\n the last time they showed up here.\n Also, I expect SILENCE.  No spells.\n Casting a spell is a good way to\n get blasted.  You've been warned.[await][page]\n\n             Now, GET OFF MY LAWN!!\n                                  Pleaseno[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Pleaseno must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PLEASENO: Still missing [0x7024] item(s)?\n Pathetic![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Pleaseno's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Pleaseno.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PLEASENO:       What'd you come here for?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Pleaseno...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PLEASENO: The dojo master's gonna\n kick your butt![await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PLEASENO:\n      Ahh, you're not so tough![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PLEASENO:\n      Ahh, you're not so tough![await]""",
    }


class MegasmilaxBossFight(BossFightPrize):
    _text = "Megasmilax"
    _formation = FORM0283
    _members = [
        FormationMember(SMILAXEnemy, 180, 157),
        FormationMember(SMILAXEnemy, 164, 175, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 143, 119, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 207, 151, hidden_at_start=True),
        FormationMember(SMILAXEnemy, 191, 127, hidden_at_start=True),
        FormationMember(MEGASMILAXEnemy, 175, 111, hidden_at_start=True),
    ]
    _force_start_event = BE0058_THRAX_IS_THERE
    _seaside_letter_name_if_seaside_boss = "the Plant"
    _seaside_letter_name_if_volcano_boss = "an invasive plant spreading"
    _seaside_letter_name_if_final_boss = "Megasmilax's seedlings."
    _anchor_enemy = MEGASMILAXEnemy
    _extra_hp_enemies = [SMILAXEnemy, SMILAXEnemy, SMILAXEnemy]
    _additional_enemies_to_scale = [PIRANHAPLANTEnemyHenchman]

    _npc_models = [MegasmilaxLargeObject, PiranhaPlantObject]
    _statue_npc = PiranhaPlantStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=PIRANHAPLANTEnemyHenchman, model=PiranhaPlantHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MEGASMILAX: I'm thirsty.[await][pause] Can you\n ask Shy Away to come back here,[delay]\n please?[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Hm?[delay_30] Not often we get visitors\n down here.[delay_30] Come in...[delay_60]\n at your own risk, that is![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Megasmilax's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n MEGASMILAX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n      MEGASMILAX: I'm thirsty.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MEGASMILAX: You'd think it\n wouldn't be so difficult to get\n watered around here.[await][pause] We're\n literally underwater.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MEGASMILAX: Careful. I have sharp\n teeth.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Go ahead, just add Water![await]\n Cha-Cha-Cha-Chia!  La Dee Dah~![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """SMILAX: I guess salt water\n wouldn't be very good for us.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n I'm still salivating over your battle\n with `SEASIDE_BOSS`.[await]\n I must taste its umami someday...\n I've heard through the vine about\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They must be part of the\n underground network of \n `FINAL_BOSS_NAME`[await]\n My offer to have you for dinner\n stands. I must return to my roots.[await][page]\n\n                             Stay hungry,\n                              Megasmilax[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """SMILAX: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """SMILAX: I guess salt water\n wouldn't be very good for us.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """SMILAX: I guess salt water\n wouldn't be very good for us.[await]""",
        DI2061_HEAD_CHEF: """SMILAX: We're making this cake\n in honour of Megasmilax.[await]""",
        DI2062_APPRENTICE_CHEF: """SMILAX: I hope the wedding party\n likes it. If they don't...[delay] well,[delay]\n they DID hire plants to bake a cake.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Megasmilax must have\n gotten lost on her way here.""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Megasmilax is busy right now, so\n she can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Megasmilax.[await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MEGASMILAX: Hm?[await]\n [0x7024] more item(s)?[await]\n Don't ask me.[delay] I'm just a plant.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n         MEGASMILAX: Hmm...[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hello there. Are you tired?\n We don't charge any fees here,\n if you'd like to stay.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Megasmilax's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Welcome to our humble little town.\n You're welcome to stick around,\n but keep away from the shed, OK?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ I'm shopping for some fertilizer.[await]\n [delay]...Don't give me that look!\n [delay]I'm just a plant![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There's nothing suspicious going on\n in here.[await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ We're just two plants growing in\n front of an abandoned door. ...But\n we're not letting you in.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MEGASMILAX: I would love to\n watch your match with the dojo\n master.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You don't look like the gardener...[await]\n  [select] (I'm here to fight you)\n  [select] (Oops, my mistake)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You don't look like the gardener...[await]\n  [select] (I'm here to fight you)\n  [select] (Oops, my mistake)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the lady next door.[await][page]\n She's always mumbling about\n Water-this and Fertilizer-that.[await]\n ...[delay]Actually, [delay]that doesn't sound\n so bad![await][page]\n Sometimes I'd like to ask her what\n she's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MEGASMILAX: This is harder than it\n looks. I'm a plant.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MEGASMILAX: This is harder than it\n looks. I'm a plant.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Megasmilax is busy right now, so\n she can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Megasmilax.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """SMILAX: Go on ahead to visit\n Megasmilax. But be warned, he's\n pretty tough when he's hydrated.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """SMILAX: Wow, you won![await][pause] Shy Away\n must have watered you more than\n he watered Megasmilax.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SMILAX: Hello there. Are you the\n gardener?[await][page]\n No?[await][pause] Well, [delay]we didn't call for a\n plumber today... [await][pause]]I better get you\n outta here![await]""",
        DI2572_TOWER_HENCHMAN_2: """SMILAX: If you didn't come back\n here to water us, you'd better get\n outta here.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """\n          SMILAX: I'm thirsty.[await]""",
        DI3073_TOWER_HENCHMAN_3: """\n       SMILAX: Careful, I bite.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("NimbusGate"), _gf("NimbusGating").MEGASMILAX
        ):
            output.extend(
                [
                    SetBit(NIMBUS_MAINLAND_UNLOCKED),
                    RemoveObjectFromSpecificLevel(
                        NPC_2, R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
                    ),
                ]
            )
        return EventScript(output)


class DodoBossFight(BossFightPrize):
    _text = "Dodo"
    _formation = FORM0315
    _members = [
        FormationMember(DODOEnemySolo, 183, 127),
    ]
    _seaside_letter_name_if_volcano_boss = "a large bird flapping about"
    _seaside_letter_name_if_final_boss = "Dodo's flock."

    _npc_models = [DodoLargeObject, DodoSmallObject]
    _statue_npc = DodoStatueObject

    _tiny_henchmen = [
        BossFightHenchman(monster=DODOEnemy, model=FeatherHenchman),
    ]

    _dialog_replacements = {
        # actually, don't use dialogs for dodo, just play sfx... how to handle this?
        # time this according to how long the feather sound effect is
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: "\n                    ••••••[await]",
        DI1660_SHIP_PASSWORD_COMPLETE: "\n                    ••••••[await]",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Dodo's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped DODO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: "\n                    ••••••[await]",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: "\n                    ••••••[await]",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: "\n                    ••••••[await]",
        DI1782_SHIP_BOSS_DRINK: """ (Dodo stares at a Hot Chocolate)[await]\n ...Please don't tell Valentina.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Dear `MAIN_CHARACTER_NAME`,\n[await][page]\n I saw your incredible battle with\n `SEASIDE_BOSS`!\n[await]\n At the "Tanning Salon", I saw \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano. [await]\n Valentina referred to them as\n `FINAL_BOSS_NAME`\n Look, I actually think you're cool,\n and I'm learning my Multistrike\n timing from our battles... But...\n I can't leave her. She needs me. I\n hope you understand.[await][page]\n\n                       Your biggest fan,\n                                      Dodo[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big bird! It is...\n masterpiece![await]""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """    Dodo is a bird of few words.[await]\n    You still have [0x7024] item(s) left\n                 to find.[await]""",  # use async for this one too
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Dodo's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Dodo.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: "\n                    ••••••[await]",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Dodo...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: "\n                    ••••••[await]",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """[delay_60][await]\n  [select] (I'm here for a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """[delay_60][await]\n  [select] (I'm here for a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n I never hear the guy next door.[await]\n Maybe he can't talk.[await][page]\n I'd like to go over and introduce\n myself sometime, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: "\n                    ••••••[await]",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: "\n                    ••••••[await]",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Dodo's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Dodo.[await]""",
    }


class BirdettaBossFight(BossFightPrize):
    _text = "Birdo"
    _formation = FORM0285
    _members = [
        FormationMember(BIRDETTAEnemy, 167, 118, hidden_at_start=True),
        FormationMember(SHELLYEnemy, 171, 103),
        FormationMember(EGGBERTEnemy, 135, 119, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 135, 135, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 167, 151, hidden_at_start=True),
        FormationMember(EGGBERTEnemy, 199, 151, hidden_at_start=True),
    ]
    _anchor_enemy = BIRDETTAEnemy
    _hp_slice_excluded_enemies = [
        EGGBERTEnemy,
        EGGBERTEnemy,
        EGGBERTEnemy,
        EGGBERTEnemy,
    ]
    _force_battlefield = BF23_NIMBUS_CASTLE_BIRDOS_ROOM
    _seaside_letter_name_if_volcano_boss = "a giant egg rolling"
    _seaside_letter_name_if_final_boss = "Birdo's bad eggs."

    _npc_models = [BirdettaLargeObject, BirdettaSmallObject]
    _statue_npc = BirdettaStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=EGGBERTEnemy, model=EggbertHenchman),
    ]

    _tiny_henchmen = [
        BossFightHenchman(monster=EGGBERTEnemy, model=EggbertHenchman),
    ]

    _dialog_replacements = {
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, yay, you've come to play!\n Come on in~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Birdo's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n BIRDO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BIRDO: Tee hee! Let's play\n again sometime![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BIRDO: Oh, you didn't forget\n about me! You're so sweet![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BIRDO: This isn't what I had in\n mind when I said I wanted to play![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Thanks for playing with me~![await]\n I lost, but I made Yoshi's Eggnog![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """EGGBERT: You visiting us has\n really made Birdo happy.\n Thank you![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """EGGBERT: You visiting us has\n really made Birdo happy.\n Thank you![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n HI `MAIN_CHARACTER_NAME`♥!\n[await][page]\n Did `SEASIDE_BOSS` submit to\n the power of HUGS?!♥\n[await]\n While doing some incubating, I saw \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n My eggies♥ think they scramble with\n `FINAL_BOSS_NAME`\n My lovelies♪ and I have to get back[await]\n to the ship, and the bouyant forces\n of seawater aren't helping.\n Stop by again soon♥! [await][page]\n\n                           ♥XO♥XO♥XO♥\n                                     Birdo[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """EGGBERT: You visiting us has\n really made Birdo happy.\n Thank you![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """EGGBERT: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """EGGBERT: We're making this cake\n look just like Birdo![await]""",
        DI2062_APPRENTICE_CHEF: """EGGBERT: No eggs were harmed\n in the making of this cake.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Birdo must have gotten\n lost on her way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BIRDO: Hello![await]\n ...Oh, no, you're still missing\n [0x7024] item(s)![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n              BIRDO: Hello![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Hello! You've been chosen to stay\n here in our lovely inn for FREE!\n Aren't you lucky?[await]\n Will you stay with us?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Birdo's busy right now, so she\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Birdo.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Birdo's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hi![delay] Welcome to our town![delay]\n Stay away from our shed, OK~?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Do you think they sell frying pans\n here?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ It's perfectly normal for two eggs\n to stand outside a locked house![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There's nothing weird going on\n here![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BIRDO: Ooh, are you gonna play\n with the dojo master?![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello! Did you come to play?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hello! Did you come to play?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She's always mumbling about\n Egg-this and Playtime-that.[await][page]\n Sometimes I'd like to ask her what\n she's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BIRDO: Thanks for playing with\n me~![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BIRDO: Thanks for playing with\n me~![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Birdo's busy right now, so she\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Birdo.[await]""",
    }
    _dialog_replacements_canon = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Birdetta's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n BIRDETTA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BIRDETTA: Tee hee! Let's play\n again sometime![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BIRDETTA: Oh, you didn't forget\n about me! You're so sweet![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BIRDETTA: This isn't what I had in\n mind when I said I wanted to play![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n HI `MAIN_CHARACTER_NAME`♥!\n[await][page]\n Did `SEASIDE_BOSS` submit to\n the power of HUGS?!♥\n[await]\n While doing some incubating, I saw \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n My eggies♥ think they scramble with\n `FINAL_BOSS_NAME`\n My lovelies♪ and I have to get back[await]\n to the ship, and the bouyant forces\n of seawater aren't helping.\n Stop by again soon♥! [await][page]\n\n                           ♥XO♥XO♥XO♥\n                                  Birdetta[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        DI2061_HEAD_CHEF: """EGGBERT: We're making this cake\n look just like Birdetta![await]""",
        DI2062_APPRENTICE_CHEF: """EGGBERT: No eggs were harmed\n in the making of this cake.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Birdetta must have\n gotten lost on her way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BIRDETTA: Hello![await]\n ...Oh, no, you're still missing\n [0x7024] item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Birdetta's busy right now, so she\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Birdetta.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n          BIRDETTA: Hello![await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Birdetta's\n house up on the hill yet?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BIRDETTA: Ooh, are you gonna play\n with the dojo master?![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She's always mumbling about\n Egg-this and Playtime-that.[await][page]\n Sometimes I'd like to ask her what\n she's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BIRDETTA: Thanks for playing with\n me~![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BIRDETTA: Thanks for playing with\n me~![await]""",
    }
    _dialog_replacements_canon_and_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Birdetta's busy right now, so she\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Birdetta.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """EGGBERT: Wow, you sure showed\n us! Don't disappoint Birdo![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """EGGBERT: Thanks for playing\n with us today![await]""",
        DI2560_TOWER_HENCHMAN_1: """EGGBERT: Birdo's feeling lonely\n today, so feel free to pay her a\n visit upstairs.[await][pause] I'm sure she'd love\n the company.[await][page]\n Just, let me make sure you'll be\n nice, first![await]""",
        DI2572_TOWER_HENCHMAN_2: """EGGBERT: Pardon me, Birdo's\n not back here. Please refrain from\n snooping around.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """EGGBERT: What did Birdo want\n me to do here, again? I'm just an\n egg![await]""",
        DI3073_TOWER_HENCHMAN_3: """EGGBERT: You're making me so\n mad, I could explode![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_canon = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """EGGBERT: Wow, you sure showed\n us! Don't disappoint Birdetta![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """EGGBERT: Thanks for playing\n with us today![await]""",
        DI2560_TOWER_HENCHMAN_1: """EGGBERT: Birdetta's feeling lonely\n today, so feel free to pay her a\n visit upstairs.[await][pause] I'm sure she'd love\n the company.[await][page]\n Just, let me make sure you'll be\n nice, first![await]""",
        DI2572_TOWER_HENCHMAN_2: """EGGBERT: Pardon me, Birdetta's\n not back here. Please refrain from\n snooping around.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """EGGBERT: What did Birdetta want\n me to do here, again? I'm just an\n egg![await]""",
    }


class ValentinaBossFight(BossFightPrize):
    _text = "Valentina"
    _formation = FORM0281
    _members = [
        FormationMember(VALENTINAEnemy, 183, 127),
        FormationMember(DODOEnemy, 199, 151, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a bossy lady being carried"
    _seaside_letter_name_if_final_boss = "Valentina's little birds."
    _anchor_enemy = VALENTINAEnemy
    _additional_enemies_to_scale = [BLUEBIRDEnemyHenchman, BIRDYEnemyHenchman]
    # Dodo contributes 40% of his HP to the pie total, but gets 2.5x his calculated slice
    _hp_pie_contribution_multipliers = {DODOEnemy: 0.4}
    _hp_slice_multipliers = {DODOEnemy: 2.5}

    _npc_models = [ValentinaLargeObject, ValentinaSmallObject]
    _statue_npc = NimbusLandStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=BLUEBIRDEnemyHenchman, model=BluebirdHenchman),
        BossFightHenchman(monster=BIRDYEnemyHenchman, model=BirdyHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """VALENTINA: ...What? You're STILL\n here?! Go AWAY!!![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ ALRIGHT, already![delay_30] If you're going\n to annoy me like this, get in here\n and finish the job![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Valentina's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n VALENTINA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """VALENTINA: If you don't stop\n bothering me, I'm going to turn\n your mustache into a\n vegetable scrubber![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """VALENTINA: YOU again?! You better\n have brought some margaritas![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """VALENTINA: Get OFF of my head\n before I take your shoes and throw\n them in the ocean!!![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Pfffft!  You call THIS a Martini?[await]\n MAKE IT AGAIN, and I MIGHT tip!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Valentina's grumpy. Booster got\n her a gold beetle for their\n anniversary.[await][pause] She wanted a ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Valentina's grumpy. Booster got\n her a gold beetle for their\n anniversary.[await][pause] She wanted a ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To whom it may concern,\n[await][page]\n Make sure that pesky\n `SEASIDE_BOSS`, is gone\n by the time I get back.[await]\n\n A little birdy told me they saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.  Gross.[await]\n I cannot abide any more of \n `FINAL_BOSS_NAME`\n They're all beneath me.  Literally.[await]\n Well, I've got a ship full of idiots\n to command.  Don't call, I have a\n boyfriend.  His name is...Booster.[await][page]\n\n                       NOT yours,\n                         Valentina[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Valentina's grumpy. Booster got\n her a gold beetle for their\n anniversary.[await][pause] She wanted a ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """ Why are we making a cake that\n looks like Valentina, again?[await]""",
        DI2062_APPRENTICE_CHEF: """ We're making a cake that looks like\n Valentina.[await][pause] What else would we\n do on our day off?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Valentina must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """VALENTINA: STOP BOTHERING ME![await]\n If you need something to do, go\n look for [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Valentina's busy right now, so she\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Valentina.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n   VALENTINA: I'm SO frustrated![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome![delay] I'll let you stay here for\n free, but don't tell Valentina.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Valentina's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ Hmm...[delay] What're you loitering\n around here for?[delay] Uh...[delay] Stay away\n from the shed, OK?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ ...I'm on my break. [delay]Just let me\n shop in peace, OK?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n     You can't just barge in here![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n         Hey! Who're YOU?!...[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """VALENTINA: You? Fighting the dojo\n master? Good luck, chump![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What? What do you want?![await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ What? What do you want?![await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She's always mumbling about\n Queen-this and Dodo-that.[await][page]\n Sometimes I'd like to ask her what\n she's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """VALENTINA: Is this REALLY going to\n make me powerful enough to take\n ov...[delay_30] I mean...[await][pause][delay_30] pay a cordial visit\n to Nimbus Land?![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """VALENTINA: Is this REALLY going to\n make me powerful enough to take\n ov...[delay_30] I mean...[await][pause][delay_30] pay a cordial visit\n to Nimbus Land?![await]""",
    }
    _dialog_replacements_canon_and_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Valentina's busy right now, so she\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Valentina.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """ Whatever, go on and fight\n Valentina. She doesn't pay us\n enough to keep you out.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """ Oh, you won?[await]\n [delay_30](...[delay_30]It's about time!)[await]""",
        DI2560_TOWER_HENCHMAN_1: """ I hate being a secretary! And...\n [delay_30]I'm going to make this your\n problem![await]""",
        DI2572_TOWER_HENCHMAN_2: """Whaddya want?[await][pause] You better not be\n trying to bother Valentina, [delay]or I'll\n be in trouble![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """Valentina only gives us the most\n boring jobs to do...[await]""",
        DI3073_TOWER_HENCHMAN_3: """\n       I'm bored. Entertain me![await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BarrelVolcanoGate"), _gf("BarrelVolcanoGating").VALENTINA
        ):
            output.extend(
                [
                    SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
                    SetBit(MAP_BARREL_VOLCANO),
                ]
            )
        return EventScript(output)


class CzarDragonBossFight(BossFightPrize):
    _text = "Czar Dragon"
    _formation = FORM0282
    _members = [
        FormationMember(CZARDRAGONEnemy, 183, 143),
        FormationMember(ZOMBONEEnemy, 183, 143, hidden_at_start=True),
        FormationMember(HELIOEnemy, 167, 119, hidden_at_start=True),
        FormationMember(HELIOEnemy, 135, 135, hidden_at_start=True),
        FormationMember(HELIOEnemy, 199, 167, hidden_at_start=True),
        FormationMember(HELIOEnemy, 231, 151, hidden_at_start=True),
    ]
    # Anchor is the average of Czar Dragon and Zombone (excluding Helios)
    _anchor_enemy = [CZARDRAGONEnemy, ZOMBONEEnemy]
    _scaling_excluded_enemies = [HELIOEnemy, HELIOEnemy, HELIOEnemy, HELIOEnemy]
    _additional_enemies_to_scale = [PYROSPHEREEnemyHenchman]

    _seaside_letter_name_if_seaside_boss = "the Dragon"
    _seaside_letter_name_if_volcano_boss = "a huge dragon blazing"
    _seaside_letter_name_if_final_boss = "the Czar Dragon's spawn."

    _npc_models = [CzarDragonLargeObject, CzarDragonMediumObject, CzarDragonSmallObject]
    _statue_npc = CzarStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=HELIOEnemy, model=HelioHenchman),
        BossFightHenchman(monster=PYROSPHEREEnemyHenchman, model=SparkyHenchman),
    ]
    _tiny_henchmen = [
        BossFightHenchman(monster=HELIOEnemy, model=HelioHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n    CZAR DRAGON: BLARRGGGG[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ BLARRGGGG[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Czar Dragon's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the CZAR DRAGON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n    CZAR DRAGON: BLARRGGGG[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """\n    CZAR DRAGON: BLARRGGGG[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """\n    CZAR DRAGON: BLARRGGGG[await]""",
        DI1782_SHIP_BOSS_DRINK: """ FIIIIIIIRRRRREEEEBAAAALLLLLLLL[await]\n WHISSSSSSSSSKEEEEEEEEEEEEY!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: "\n                    ••••••[await]",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: "\n                    ••••••[await]",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: "\n                    ••••••[await]",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: "\n                    ••••••[await]",
        DI2061_HEAD_CHEF: "\n                    ••••••[await]",
        DI2062_APPRENTICE_CHEF: "\n                    ••••••[await]",
        DI2180_CHAPEL_NPC: """ Reverend Dragon must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """\n    CZAR DRAGON: BLARRGGGG[await]""",  # can we make him say BLARG as many times as you have items remaining?
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Czar Dragon is busy right now,\n so he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Czar Dragon.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n  CZAR DRAGON: BLAAARRRGGGG[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ (Stay in the inn for free?)[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: "\n                    ••••••[await]",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: "\n                    ••••••[await]",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: "\n                    ••••••[await]",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: "\n                    ••••••[await]",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "\n                    ••••••[await]",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "\n                    ••••••[await]",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "\n                    ••••••[await]",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: "\n                    ••••••[await]",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: "\n                    ••••••[await]",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: "\n                    ••••••[await]",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: "\n                    ••••••[await]",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n  CZAR DRAGON: BLAAARRRGGGG[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """CZAR DRAGON: BLAAARRRGGGG\n  [select] (I agree, let's fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """CZAR DRAGON: BLAAARRRGGGG\n  [select] (I agree, let's fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always yelling about\n BLARRRRG-this and\n BLAHGAHRGGH-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n  CZAR DRAGON: BLAAARRRGGGG[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n  CZAR DRAGON: BLAAARRRGGGG[await]""",
        DI1120_NIMBUS_BIRD_GUARD: """\n                    ••••••[await]""",
        DI1945_NIMBUS_GUARD: """\n                    ••••••[await]"""
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Czar Dragon is busy right now,\n so he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Czar Dragon.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI2560_TOWER_HENCHMAN_1: "\n                    ••••••[await]",
        DI2572_TOWER_HENCHMAN_2: "\n                    ••••••[await]",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: "\n                    ••••••[await]",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: "\n                    ••••••[await]",
        DI3072_TOWER_HENCHMAN_3_WINDOW: "\n                    ••••••[await]",
        DI3073_TOWER_HENCHMAN_3: "\n                    ••••••[await]",
    }


class AxemRangersBossFight(BossFightPrize):
    _text = "Axem Rangers"
    _formation = FORM0292
    _members = [
        FormationMember(AXEMRANGERSEnemy, 201, 79),
        FormationMember(AXEMREDEnemy, 135, 111, hidden_at_start=True),
        FormationMember(AXEMBLACKEnemy, 135, 127, hidden_at_start=True),
        FormationMember(AXEMPINKEnemy, 151, 143, hidden_at_start=True),
        FormationMember(AXEMGREENEnemy, 183, 151, hidden_at_start=True),
        FormationMember(AXEMYELLOWEnemy, 215, 151, hidden_at_start=True),
    ]
    _anchor_enemy = [
        AXEMREDEnemy,
        AXEMYELLOWEnemy,
        AXEMBLACKEnemy,
        AXEMPINKEnemy,
        AXEMGREENEnemy,
    ]
    _force_start_event = BE0061_ONLY_MARIO_IS_THERE
    _force_battlefield = BF39_BLADE_AXEM_RANGERS
    _seaside_letter_name_if_seaside_boss = "the Axems"
    _seaside_letter_name_if_volcano_boss = "a huge AX flying around"
    _seaside_letter_name_if_final_boss = "the Axem Rangers' stooges."
    _seaside_letter_name_if_sunken_ship_boss = "ya boi red"

    _character_henchmen = [
        BossFightHenchman(monster=AXEMBLACKEnemy, model=AxemBlackHenchman),
        BossFightHenchman(monster=AXEMPINKEnemy, model=AxemPinkHenchman),
        BossFightHenchman(monster=AXEMYELLOWEnemy, model=AxemYellowHenchman),
        BossFightHenchman(monster=AXEMGREENEnemy, model=AxemGreenHenchman),
    ]

    _npc_models = [AxemRedObject]
    _statue_npc = AxemRedStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """AXEM RED: We're busy playing Uno\n in here. Go bother someone else![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Listen up, nerd![delay_30] You may have\n figured out our password, but\n we're not going down without\n a fight![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Axem Rangers' place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the AXEM RANGERS!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """AXEM RED: How could this happen\n to the Axem Rangers?![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """AXEM RED: Yo! Quit wasting your\n time around here, you've got a\n world to save![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """AXEM RED: Yo, `MAIN_CHARACTER_NAME`!\n This isn't cool!\n Get off of my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Yo! This energy drink is preem![await]\n Axem Red Bull gives me wings![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """AXEM BLACK: Red can be kind of\n a chump when he loses.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """AXEM PINK: I hate it down here!\n The water makes my makeup run![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n yo `MAIN_CHARACTER_NAME`,[await][page]\n hru? fite was zzz, so I went bak\n 2 teh ship 4 a nap. text me when ur\n done w/ `SEASIDE_BOSS`.[await]\n green would not shut up bout\n `VOLCANO_BOSS_DESCRIPTION`\n he saw near teh volcano.[await]\n pink flirted w/ a dood from\n `FINAL_BOSS_NAME`\n black wants 2 punk them, but[await]\n yellow got the squirtz again...\n so we got 2 go chill 4 a bit.  Hit\n me bak l8r. [await][page]\n\n                                     peace\n                                        red[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """AXEM YELLOW: Say, do you have\n anything to eat?[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """AXEM GREEN: The four of them may\n be hot heads, but I truly enjoy\n causing mischief with them.[await]""",
        DI2061_HEAD_CHEF: """AXEM YELLOW: Why the heck do\n I have to bake a cake that I'm\n not going to get to eat?![await]""",
        DI2062_APPRENTICE_CHEF: """AXEM GREEN: Not EVERYTHING\n we do is evil. Today we're baking a\n cake that looks like Axem Red.[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Red must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """AXEM RED: Listen! You're not\n going anywhere until you find [0x7024]\n more of `MARRYMORE_CHARACTER`'s item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Axem Rangers are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Axem Rangers.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """AXEM RED: Listen up![await]\n Quit snooping around town![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """AXEM YELLOW: You tired?[await]\n I'm feeling nice today, so you can\n stay for free.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Axem Red...\n in his house. He is...the most\n respected person here.[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n     AXEM BLACK: Beat it, clod![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """AXEM PINK: Get lost, mustache!\n [delay]This shed belongs to the Axem\n Rangers![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """AXEM RED: Yo! It won't be enough\n to win just once. The dojo master\n has three forms.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Yo! What do you want?![await]\n  [select] (A fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Yo! What do you want?![await]\n  [select] (A fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Shades-this and Makeup-that.[await][page]\n Sometimes I'd like to ask them what\n they're babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n  AXEM RED: I'm way outta shape![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n  AXEM RED: I'm way outta shape![await]""",
        DI1120_NIMBUS_BIRD_GUARD: """AXEM BLACK:\n              Beat it, clod![await]""",
        DI1945_NIMBUS_GUARD: """AXEM PINK:\n              Get lost, jerk![await]"""
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Axem Rangers are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Axem Rangers.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI2560_TOWER_HENCHMAN_1: """AXEM BLACK: Green hasn't shown\n up to cover me for lunch yet![await][pause] I'm\n so mad, I could fight somebody![await]""",
        DI2572_TOWER_HENCHMAN_2: """AXEM PINK: Where do you clods\n think you're going?![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """AXEM YELLOW: Man...[delay] I wish\n someone would bring me some food\n up here![await]""",
        DI3073_TOWER_HENCHMAN_3: """\n    AXEM YELLOW: Get lost, bub![await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(
            _gf("BowsersKeepGate"), _gf("BowsersKeepGating").AXEM
        ):
            output.extend(
                [
                    SetBit(MAP_VISTA_HILL),
                    ClearBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
                ]
            )
            if world.settings.is_flag_value(
                _gf("FactoryGate"), _gf("FactoryGating").OPEN
            ):
                output.extend(
                    [
                        SetBit(MAP_GATE),
                        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                    ]
                )
        return EventScript(output)


class ChesterBossFight(BossFightPrize):
    _text = "Chester"
    _formation = FORM0269
    _members = [
        FormationMember(CHESTEREnemy, 183, 127),
        FormationMember(BAHAMUTTEnemy, 135, 119, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a purple box sliding about"
    _seaside_letter_name_if_final_boss = "Chester's monsters."
    _seaside_letter_name_if_final_boss_remake = "Comeon's monsters."
    _remake_name = "Comeon"

    _npc_models = [ChesterLargeObject, ChesterSmallObject]
    _statue_npc = MimicStatueObject

    _anchor_enemy = CHESTEREnemy
    _hp_slice_excluded_enemies = [BAHAMUTTEnemy]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CHESTER: Go on, take it. Just let\n me go back to sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Quit draggin' your feet! Get in\n here and let's fight![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Chester's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: "\n"
        "PIRATE: That's AMAZING!\n No one's EVER whipped \nCHESTER!![await]"
        "",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """   CHESTER: (How embarrassing...)[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CHESTER: You know, I'm kind of a\n big deal over in Bowser's Keep.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CHESTER: This is unnecessary. Get\n off me![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Leave me alone with my precious[await]\n '92 Napper Cabernet Sauivignon.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`:\n[await][page]\n I'm too old for this nonsense with\n `SEASIDE_BOSS`, good luck.\n[await]\n Just to see if I could, I summoned\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n It seems they're associated with\n `FINAL_BOSS_NAME`\n I've been belching up monsters for\n a LONG time, and I've never seen\n anything this rude. Fix it, and\n I MIGHT forget you opened my box.[await][page]\n\n    Go do something useful for once.\n                                   Chester[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Chester must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CHESTER: Don't bother me unless\n you have found [0x7024] more item(s).[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Chester's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Chester.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CHESTER:\n       This town is pretty quiet.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Chester...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n   CHESTER: Now THIS I gotta see.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You're interrupting my sleep.[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You're interrupting my sleep.[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Dragon-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n  CHESTER: I don't even have legs![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n  CHESTER: I don't even have legs![await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """COMEON: Go on, take it. Just let\n me go back to sleep.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Comeon's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped \nCOMEON!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n  COMEON: (How embarrassing...)[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """COMEON: You know, I'm kind of a\n big deal over in Bowser's Keep.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`:\n[await][page]\n I'm too old for this nonsense with\n `SEASIDE_BOSS`, good luck.\n[await]\n Just to see if I could, I summoned\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n It seems they're associated with\n `FINAL_BOSS_NAME`\n I've been belching up monsters for\n a LONG time, and I've never seen\n anything this rude. Fix it, and\n I MIGHT forget you opened my box.[await][page]\n\n    Go do something useful for once.\n                                    Comeon[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Comeon must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """COMEON: Don't bother me unless\n you have found [0x7024] more item(s).[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Comeon's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Comeon.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """COMEON:\n       This town is pretty quiet.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Comeon...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n   COMEON: Now THIS I gotta see.[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n  COMEON: I don't even have legs![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n  COMEON: I don't even have legs![await]""",
    }


class KamekBossFight(BossFightPrize):
    _text = "Magikoopa"
    _formation = FORM0316
    _members = [
        FormationMember(KAMEKEnemy, 215, 111),
        FormationMember(TERRAPINEnemy, 167, 135, hidden_at_start=True),
    ]
    _anchor_enemy = KAMEKEnemy
    _scaling_excluded_enemies = [TERRAPINEnemy]
    _hp_slice_excluded_enemies = [TERRAPINEnemy]
    _additional_enemies_to_scale = [JINXCLONEEnemy, KINGBOMBEnemy, BAHAMUTTEnemy2]

    _force_start_event = BE0101_MAGIKOOPA_IS_THERE
    _seaside_letter_name_if_volcano_boss = "a hooded sorceror flying"
    _seaside_letter_name_if_final_boss = "Magikoopa's guys."
    _seaside_letter_name_if_final_boss_remake = "Wizakoopa's guys."
    _remake_name = "Wizakoopa"

    # _mook_henchmen = [
    #     BossFightHenchman(monster=JINXCLONEEnemy, model=JinxCloneHenchman),
    #     BossFightHenchman(monster=KINGBOMBEnemy, model=BobOmbHenchman),
    # ]
    _tiny_henchmen = [
        BossFightHenchman(monster=JINXCLONEEnemy, model=JinxCloneHenchman),
        BossFightHenchman(monster=BOBOMBEnemyHenchman, model=MicrobombHenchman),
    ]

    _npc_models = [MagikoopaLargeObject, MagikoopaSmallObject]
    _statue_npc = MagikoopaStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MAGIKOOPA: Normally,[delay] when I\n summon an egg,[delay] it doesn't\n encapsulate me...[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ This..is..my ship!\n Come in..if you dare![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Magikoopa's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n MAGIKOOPA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n  MAGIKOOPA: Huh? ...Where am I?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MAGIKOOPA: Oh, yes, I have seen\n `MARIO_NAME`'s brother before.\n I can't recall where, though...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MAGIKOOPA: `MAIN_CHARACTER_NAME`,\n why did you do this???[await]""",
        DI1782_SHIP_BOSS_DRINK: """ There's Magic Hat in my magic hat,[await]\n but we're not handing it over to[await]\n the likes of you![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`!\n[await][page]\n Before I could cast a spell, you\n defeated `SEASIDE_BOSS`![await]\n\n Earlier while flying around seeking \n sweet yoshi vengeance, I saw[await]\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I remember them being one of \n `FINAL_BOSS_NAME`[await]\n I'd better get back to the ship in\n case Yoshi falls into one the pits.[await][page]\n\n     Now you see me, now you don't![await]                               Magikoopa""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big wizard! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Magikoopa must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MAGIKOOPA: You..need..[0x7024] more\n item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Magikoopa's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Magikoopa.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """MAGIKOOPA:\n    There's nothing..to see..here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Magikoopa...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n        MAGIKOOPA: OH, MY!![await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Yoshi-this and Bowser-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n MAGIKOOPA:\n       Oh, dear... What to do...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n MAGIKOOPA:\n       Oh, dear... What to do...[await]""",
    }
    _dialog_replacements_remake = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """WIZAKOOPA: Normally,[delay] when I\n summon an egg,[delay] it doesn't\n encapsulate me...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Wizakoopa's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n WIZAKOOPA!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n  WIZAKOOPA: Huh? ...Where am I?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """WIZAKOOPA: Oh, yes, I have seen\n `MARIO_NAME`'s brother before.\n I can't recall where, though...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """WIZAKOOPA: `MAIN_CHARACTER_NAME`,\n why did you do this???[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`!\n[await][page]\n Before I could cast a spell, you\n defeated `SEASIDE_BOSS`![await]\n\n Earlier while flying around seeking \n sweet yoshi vengeance, I saw[await]\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I remember them being one of \n `FINAL_BOSS_NAME`[await]\n I'd better get back to the ship in\n case Yoshi falls into one the pits.[await][page]\n\n     Now you see me, now you don't![await]                               Wizakoopa""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """WIZAKOOPA: You..need..[0x7024] more\n item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Wizakoopa's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Wizakoopa.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """WIZAKOOPA:\n    There's nothing..to see..here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Wizakoopa...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n        WIZAKOOPA: OH, MY!![await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n WIZAKOOPA:\n       Oh, dear... What to do...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n WIZAKOOPA:\n       Oh, dear... What to do...[await]""",
    }
    _dialog_replacements_canon = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """KAMEK: Normally,[delay] when I\n summon an egg,[delay] it doesn't\n encapsulate me...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Kamek's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n KAMEK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n    KAMEK: Huh? ...Where am I?[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """KAMEK: Oh, yes, I have seen\n `MARIO_NAME`'s brother before.\n I can't recall where, though...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """KAMEK: `MAIN_CHARACTER_NAME`,\n why did you do this???[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`!\n[await][page]\n Before I could cast a spell, you\n defeated `SEASIDE_BOSS`![await]\n\n Earlier while flying around seeking \n sweet yoshi vengeance, I saw[await]\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I remember them being one of \n `FINAL_BOSS_NAME`[await]\n I'd better get back to the ship in\n case Yoshi falls into one the pits.[await][page]\n\n     Now you see me, now you don't![await]                                     Kamek""",
        DI2180_CHAPEL_NPC: """ Reverend Kamek must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """KAMEK: You..need..[0x7024] more\n item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Kamek's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Kamek.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """KAMEK:\n    There's nothing..to see..here![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Kamek... in his house.\n He is...the most respected person\n here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n           KAMEK: OH, MY!![await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n KAMEK: Oh, dear... What to do...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n KAMEK:\n       Oh, dear... What to do...[await]""",
    }
    _dialog_replacements_canon_and_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Kamek's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Kamek.[await]""",
    }


class BoomerBossFight(BossFightPrize):
    _text = "Boomer"
    _formation = FORM0317
    _members = [
        FormationMember(BOOMEREnemy, 215, 143),
        FormationMember(HANGINSHYEnemy, 66, 115),
        FormationMember(HANGINSHYEnemy, 186, 74),
    ]
    _force_battlefield = BF29_BOWSERS_KEEP_CHANDELIERS
    _seaside_letter_name_if_volcano_boss = "a noble soldier marching"
    _seaside_letter_name_if_final_boss = "Boomer's soldiers."
    _hp_slice_excluded_enemies = [HANGINSHYEnemy, HANGINSHYEnemy]

    _npc_models = [BoomerLargeObject, BoomerOverworldObject, BoomerSmallObject]
    _statue_npc = BoomerStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOOMER: I lost fair and square.[await]\n Now it is time for me to sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Ahhhhh... So, it's YOU who solved\n my riddle![delay_30] Now, you've got to deal\n with ME![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Boomer's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BOOMER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOOMER: I don't need your\n sympathy! Go on...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOOMER: A true soldier knows\n when to accept defeat. You earned\n your victory.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOOMER: This is absurd! Get off\n of my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Great battle deserves great Sake![await]\n Join me, `MAIN_CHARACTER_NAME`.  Kampai![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """Origami figures sit in silent tableau:\n[await][page]\nOne figure resembles `VOLCANO_BOSS_DESCRIPTION`\nwhile the others appear to be\n`FINAL_BOSS_NAME`\n[await]\nA haiku lays near the figures:\n\nStay strong `MAIN_CHARACTER_NAME`\n[await]\nShow them what discipline means\n[await]\nShred them throughly[await][page]\n\n                   Go in peace,\n                         Boomer[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like samurai! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Boomer must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BOOMER: Ha ha ha![delay_30] So, you found\n [0x7000] item(s) already. Impressive.[await][pause] But\n now you've got to find [0x7024] more![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Boomer's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Boomer.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BOOMER: Ha ha ha![await][pause] So, you've\n found our village![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Boomere...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOOMER: Ha ha ha! A match\n against the dojo master?!\n This ought to be fun![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Gahahaha! Is it a fight you seek?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Gahahaha! Is it a fight you seek?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Soldier-this and Honor-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOOMER: You won fair and square!\n But I won't make it so easy for you\n next time![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOOMER: You won fair and square!\n But I won't make it so easy for you\n next time![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Boomer's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Boomer.[await]""",
    }


class ExorBossFight(BossFightPrize):
    _text = "Exor"
    _formation = FORM0296
    _members = [
        FormationMember(EXOREnemy, 193, 64),
        FormationMember(NEOSQUIDEnemy, 187, 136),
        FormationMember(RIGHTEYEEnemy, 174, 145, hidden_at_start=True),
        FormationMember(LEFTEYEEnemy, 203, 157, hidden_at_start=True),
    ]
    _force_start_event = BE0080_EXOR_FIGHT_BEGINS
    _force_battlefield = BF16_BOWSERS_KEEP_TURRET_EXOR
    _seaside_letter_name_if_volcano_boss = "a massive sword falling"
    _seaside_letter_name_if_final_boss = "Exor's sellswords."
    _hp_slice_excluded_enemies = [
        RIGHTEYEEnemy,
        NEOSQUIDEnemy,
    ]  # exor and left eye are minimum required to defeat so only they count
    _anchor_enemy = [RIGHTEYEEnemy, LEFTEYEEnemy, NEOSQUIDEnemy]

    _npc_models = [ExorSmallObject]
    _statue_npc = ExorStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """  EXOR: What do you want? Get\n lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Halt! This ship belongs to ME!\n If you want to get through...\n bring it on![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Exor's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped EXOR!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """EXOR: If it weren't for nosey\n characters like you, I could live in\n this ship undisturbed![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """EXOR: Halt! Don't even THINK\n about leaving until you've had\n some of this juice![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """EXOR: Look, if you really want to\n humiliate me, why not use\n Geno Whirl too, while you're at it?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ You think I was MADE this HUGE?![await]\n No, I drank my Milk EVERY DAY!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n HEY!\n[await][page]\n What did you do to\n `SEASIDE_BOSS`?!\n[await]\n Let's see you deal with \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano![await]\n You are no match for us,\n `FINAL_BOSS_NAME`\n Trespass on my chip at your own\n peril!  I will devour you and expel\n your corporeal form in the\n dimmension of bombs and sledges!\n Mind your place, Tiny.[await][page]\n\n    Turn the "Ge" flag on, weakling.\n                                      Exor[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big sword! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Exor must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """EXOR: Halt![await][pause] What do you have\n here?[delay] [0x7000] item(s)?[await]\n No, this won't do.[await][pause] Find [0x7024] more,\n[delay] or I won't let you through![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Exor's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Exor.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """EXOR: There isn't much to see in\n this town. Especially not in\n the shed.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Exor...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """EXOR: Think you're gonna beat the\n dojo master? Now this I GOTTA\n see![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Halt! What do you want?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Halt! What do you want?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Nosey-this and Trespasser-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """\n        EXOR: How humiliating![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """\n        EXOR: How humiliating![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Exor's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Exor.[await]""",
    }

    def boss_hunt_unlocks(self, world: GameWorld) -> EventScript:
        output: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(_gf("FactoryGate"), _gf("FactoryGating").EXOR):
            output.extend(
                [
                    SetBit(MAP_GATE),
                    SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                ]
            )

        return EventScript(output)


class CountdownBossFight(BossFightPrize):
    _text = "Count Down"
    _formation = FORM0284
    _members = [
        FormationMember(COUNTDOWNEnemy, 150, 93),
        FormationMember(DINGALINGEnemy, 158, 52),
        FormationMember(DINGALINGEnemy, 194, 67),
    ]
    _force_battlefield = BF18_SMITHY_FACTORY_COUNT_DOWNS_PAD
    _anchor = COUNTDOWNEnemy

    _seaside_letter_name_if_seaside_boss = "the Clock"
    _seaside_letter_name_if_volcano_boss = "a noisy clock winding"
    _seaside_letter_name_if_final_boss = "Count Down's friends."

    _npc_models = [CountDownGridplaneObject]
    _statue_npc = CountDownStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=DINGALINGEnemy, model=DingalingHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """COUNT DOWN: Sometimes, even an\n alarm clock needs to sleep.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ This is not good![delay_30]\n He figured out the password![delay_30]\n ...We better do something![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Count Down's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n COUNT DOWN!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """COUNT DOWN: ...What time is it?\n Time for you to leave![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """COUNT DOWN: What are you still\n doing around here? Taking a break,\n huh?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """\n   COUNT DOWN: This is not good![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Ahh, fresh squeezed Orange Juice-[await]\n The second best way to wake up![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """DING-A-LING: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """DING-A-LING: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ WAKE UP CALL FOR\n `MAIN_CHARACTER_NAME`!!\n[await][page]\n YOU'RE LATE DEFEATING\n `SEASIDE_BOSS`!!\n[await]\n NEWSFLASH:\n `VOLCANO_BOSS_DESCRIPTION`\n SPOTTED NEAR THE VOLCANO!![await]\n DING-A-LING SOURCES LINK TO \n `FINAL_BOSS_NAME`\n TIME WAITS FOR NO ONE!! \n BETTER NAIL THAT MACK SKIP, \n ROCK CANDY MANIP, BLOCK CLIP\n BACK TO SUNKEN SHIP, YIP!![await][page]\n\n Alarm off  <<<        >>>  Snooze\n                              Count Down[await]""",
        DI2061_HEAD_CHEF: """DING-A-LING: I guess it is a little\n weird to make a cake that looks\n like a clock with no body.[await]""",
        DI2062_APPRENTICE_CHEF: """DING-A-LING: Are you impressed by\n how well we can bake without\n having any hands?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Down must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """COUNT DOWN: You've only got\n [0x7000] item(s)! You're missing [0x7024]![await]\n You better do something![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Count Down's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Count Down.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """COUNT DOWN: There's nothing to\n do here![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Our inn is free![await][pause] Why?[delay_30] Uh...[delay]\n I'm not sure.[delay_30] Anyway,[delay] do you\n want to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to Count Down's\n house up on the hill yet?[await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n       This is off-limits! Scram![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n       Get outta here! Beat it![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """COUNT DOWN: The dojo master will\n be tough to beat![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Uh-oh! Are you looking for\n trouble?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Uh-oh! Are you looking for\n trouble?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n The guy next door never seems\n to shut his alarm clock off.[await][page]\n I'd like to go over and give him a\n piece of my mind, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Count Down's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Count Down.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """RING-A-DING: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """RING-A-DING: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ WAKE UP CALL FOR\n `MAIN_CHARACTER_NAME`!!\n[await][page]\n YOU'RE LATE DEFEATING\n `SEASIDE_BOSS`!!\n[await]\n NEWSFLASH:\n `VOLCANO_BOSS_DESCRIPTION`\n SPOTTED NEAR THE VOLCANO!![await]\n RING-A-DING SOURCES LINK TO \n `FINAL_BOSS_NAME`\n TIME WAITS FOR NO ONE!! \n BETTER NAIL THAT MACK SKIP, \n ROCK CANDY MANIP, BLOCK CLIP\n BACK TO SUNKEN SHIP, YIP!![await][page]\n\n Alarm off  <<<        >>>  Snooze\n                              Count Down[await]""",
        DI2061_HEAD_CHEF: """RING-A-DING: I guess it is a little\n weird to make a cake that looks\n like a clock with no body.[await]""",
        DI2062_APPRENTICE_CHEF: """RING-A-DING: Are you impressed by\n how well we can bake without\n having any hands?[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """DING-A-LING: We failed to stop\n you. Go ahead into Count Down's\n room![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """DING-A-LING: You beat Count Down!\n We didn't see that coming![await]""",
        DI2560_TOWER_HENCHMAN_1: """DING-A-LING: `MAIN_CHARACTER_NAME`'s HERE![await][pause][delay_30]\n I'd better do something![await]""",
        DI2572_TOWER_HENCHMAN_2: """DING-A-LING: You won't find\n Count Down back here![await]\n Leave us alone![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """DING-A-LING: Man...[delay_15] I'm tired.[await]\n Even alarm bells get tired\n sometimes.[await]""",
        DI3073_TOWER_HENCHMAN_3: """DING-A-LING: Back off![delay_15] I know\n Fear Roulette and I'm not afraid\n to use it![await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed_remake = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """RING-A-DING: We failed to stop\n you. Go ahead into Count Down's\n room![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """RING-A-DING: You beat Count Down!\n We didn't see that coming![await]""",
        DI2560_TOWER_HENCHMAN_1: """RING-A-DING: `MAIN_CHARACTER_NAME`'s HERE![await][pause][delay_30]\n I'd better do something![await]""",
        DI2572_TOWER_HENCHMAN_2: """RING-A-DING: You won't find\n Count Down back here![await]\n Leave us alone![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """RING-A-DING: Man...[delay_15] I'm tired.[await]\n Even alarm bells get tired\n sometimes.[await]""",
        DI3073_TOWER_HENCHMAN_3: """RING-A-DING: Back off![delay_15] I know\n Fear Roulette and I'm not afraid\n to use it![await]""",
    }


class CloakerDominoBossFight(BossFightPrize):
    _text = "Cloaker & Domino"
    _formation = FORM0294
    _members = [
        FormationMember(CLOAKEREnemy, 151, 111),
        FormationMember(DOMINOEnemy, 215, 159),
        FormationMember(MADADDEREnemy, 167, 135, hidden_at_start=True),
    ]
    _anchor_enemy = [CLOAKEREnemy, DOMINOEnemy]
    _additional_enemies_to_scale = [EARTHLINKEnemy, CLOAKEREnemy2, DOMINOEnemy2]
    _extra_hp_enemies = [EARTHLINKEnemy]
    # You only fight 2 of the 4 enemies (Cloaker+EarthLink OR Domino+MadAdder)
    _location_hp_multiplier = 0.5

    _force_battlefield = BF40_SMITHY_FACTORY_DOMINO_CLOAKERS_PAD
    _force_start_event = BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION
    _seaside_letter_name_if_seaside_boss = "the Snake"
    _seaside_letter_name_if_volcano_boss = "a snake slithering around"
    _seaside_letter_name_if_final_boss = "Domino's snakes."

    _npc_models = [DominoLargeObject, DominoSmallObject]
    _statue_npc = DominoStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """DOMINO: I'm busy wallowing in\n misery at my defeat here.[await][pause] Get lost![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Uh oh, you cracked the code...\n I don't like where this is going...[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Cloaker and Domino's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n CLOAKER and DOMINO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """DOMINO: Guess you're tougher\n than I thought...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """\n DOMINO: So, you've returned...![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """DOMINO: I don't like where this is\n going...[await]""",
        DI1782_SHIP_BOSS_DRINK: """ I always enjoy a nice Bubble Tea[await]\n...after CLOBBERING TIME!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hey `MAIN_CHARACTER_NAME`!\n[await][page]\n We TOLD you to put your dukes up\n with `SEASIDE_BOSS`!\n[await]\n You'd better be ready!  We saw \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano![await]\n We think those snakes belong to\n `FINAL_BOSS_NAME`\n They sound like WEAKLINGS!\n It would be shameful if they\n defeated you. Stop by the ship if\n you want to play! Or see a\n blockable Carni-Kiss![await][page]\n\n              IT'S CLOBBERING TIME!!\n                       Cloaker & Domino[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big brick! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Domino must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """DOMINO: Hee hee hee... You still\n need to find [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Cloaker and Domino are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Cloaker and Domino.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """DOMINO: Hee hee hee... So you've\n found our little town! Boring,\n isn't it?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Domino...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """DOMINO: Hee hee hee... So you're\n challenging the dojo master?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hee hee hee... Wanna fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hee hee hee... Wanna fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Weaklings-this and Snake-that.[await][page]\n Sometimes I'd like to ask them what\n they're babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """DOMINO: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn't been\n getting me the results I wanted.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """DOMINO: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn't been\n getting me the results I wanted.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Cloaker and Domino are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Cloaker and Domino.[await]""",
    }


class ClerkBossFight(BossFightPrize):
    _text = "Clerk"
    _formation = FORM0258
    _members = [
        FormationMember(CLERKEnemy, 199, 119),
        FormationMember(MADMALLETEnemyHenchman, 135, 119),
        FormationMember(MADMALLETEnemyHenchman, 199, 151),
    ]
    _seaside_letter_name_if_seaside_boss = "the Clerk"
    _seaside_letter_name_if_volcano_boss = "a yellow-clad smith trudging"
    _seaside_letter_name_if_final_boss = "the Clerk's minions."

    _npc_models = [ClerkBattleObject, ClerkLargeObject, ClerkSmallObject]
    _statue_npc = ShovelKnightStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=MADMALLETEnemyHenchman, model=MadMalletHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CLERK: I'm going to sleep for 10\n years.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Sorry, you may have figured out the\n password, but I can't allow you\n through without a fight.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Clerk's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the CLERK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CLERK: I don't get paid nearly\n enough to get whooped that\n badly...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CLERK: So, you've come back! I\n hope your journey is staying on\n schedule![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CLERK: What do you think you're\n doing?![await]""",
        DI1782_SHIP_BOSS_DRINK: """ You'll have to take this up with the[await]\n Manager.  I'M having an Espresso.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Hey `MAIN_CHARACTER_NAME`,\n[await][page]\n When you can, I need a report on\n your the results of your battle with `SEASIDE_BOSS`.\n[await]\n On company retreat, I met\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n Mad Mallet saw them having drinks\n with `FINAL_BOSS_NAME`\n I've got to get back to work.  I \n spent my break writing this.  If\n you happen to return to the ship,\n could you bring me a Pick Me Up?[await][page]\n\n                                   Thanks,\n                                 the Clerk[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """MAD MALLET: Hop on the\n trampoline in the next room. It'll\n take you outside.[await]""",
        DI2061_HEAD_CHEF: """MAD MALLET: We're making a cake\n to look just like the Clerk![await]""",
        DI2062_APPRENTICE_CHEF: """MAD MALLET: We've gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Clerk must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CLERK: Whatcha got? [0x7000] item(s)?\n At this rate, you should find the\n last [0x7024] in no time![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Clerk is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Clerk.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """CLERK: Not much happens in this\n quiet and completely unsuspicious\n town.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Welcome.[delay] Would you like to stay\n here for free?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to the Clerk's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """\nDon't go snooping around our town![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """\n        I'm just shopping here![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n                 Get lost![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ Hey buddy, why don't you go snoop\n around some other houses instead?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CLERK: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you here for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Are you here for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Puffball-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CLERK: If anyone asks, I'm on\n break![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CLERK: If anyone asks, I'm on\n break![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Clerk is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Clerk.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """MAD MALLET: You trashed us!\n Go on to the Clerk's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """MAD MALLET: Whoa... No one's\n beaten the Clerk in 10 years![await]""",
        DI2560_TOWER_HENCHMAN_1: """MAD MALLET: Welcome.[await][pause] It's the\n Clerk's day off, so he's not taking\n visitors today.[await][page]\n ...But if you insist, I'll have to\n keep you out myself![await]""",
        DI2572_TOWER_HENCHMAN_2: """MAD MALLET: Listen, the Clerk\n doesn't get paid enough to deal\n with you.[await][page]\n  I certainly don't either, but I'm\n having a bad day![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """MAD MALLET: Wow! I can see\n Nimbus Land from here![await]""",
        DI3073_TOWER_HENCHMAN_3: """MAD MALLET: I'm gonna THRASH\n ya![await]""",
    }


class ManagerBossFight(BossFightPrize):
    _text = "Manager"
    _formation = FORM0259
    _members = [
        FormationMember(MANAGEREnemy, 199, 119),
        FormationMember(POUNDEREnemyHenchman, 151, 111),
        FormationMember(POUNDEREnemyHenchman, 167, 135),
        FormationMember(POUNDEREnemyHenchman, 215, 143),
    ]
    _seaside_letter_name_if_seaside_boss = "the Manager"
    _seaside_letter_name_if_volcano_boss = "a blue-clad smith trudging"
    _seaside_letter_name_if_final_boss = "the Manager's minions."

    _npc_models = [ManagerBattleObject, ManagerLargeObject, ManagerSmallObject]
    _statue_npc = ShovelKnightStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=POUNDEREnemyHenchman, model=PounderHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """MANAGER: I'm going to sleep for 25\n years.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Who gave you the password?!\n You're gonna pay for this![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Manager's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the MANAGER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """MANAGER: Why don't you just jump\n on out of here?![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """MANAGER: Oh, you've returned.\n Good work so far.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """MANAGER: Get off of my head\n before I make you take the longest\n jump of your life![await]""",
        DI1782_SHIP_BOSS_DRINK: """ DON'T bother the Director with this.[await]\n Just, drink my Cappuccino. Happy?[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n Have you taken care of \n `SEASIDE_BOSS` yet?[await]\n\n There's a report on my desk about [await]\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They're a priority client of \n `FINAL_BOSS_NAME`[await]\n Take care of them, pronto.  All\n vacation time recinded until it's\n done.  I expect regular updates.[await][page]\n\n      Make it happen or you're fired.\n                             The Manager[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """POUNDER: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """POUNDER: We're making a cake\n to look just like the Manager![await]""",
        DI2062_APPRENTICE_CHEF: """POUNDER: We've gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Manager must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """MANAGER: Heh heh heh.[delay] Good work.[await]\n You just need [0x7024] more item(s).[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Manager is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Manager.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """MANAGER: Come to invade our\n town, have you?[await][pause] No need, there's\n nothing of interest here, I swear![await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Good day.[delay] We're offering free\n reservations today. Would you like\n to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to the Manager's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ If you're gonna snoop around,\n [delay]just don't do it near the shed![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ Hey buddy, I'm just trying to shop\n here. Why don't you mind your own\n business?[await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n             Don't bother us![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n      Can't you see we're busy?[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """MANAGER: You think you can beat\n the dojo master?![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Yes?[await][pause] What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Yes?[await][pause] What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Schedule-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """MANAGER: Don't interrupt me while\n I'm training![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """MANAGER: Don't interrupt me while\n I'm training![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Manager is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Manager.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """POUNDER: We lost, but we made\n the Manager proud![await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """POUNDER: Wow! The Manager's\n been here 25 years, and you just\n dethroned him![await]""",
        DI2560_TOWER_HENCHMAN_1: """POUNDER: Good day.[await][pause] The Manager\n is busy today and will not be\n seeing any guests.[await][pause]\n If you try to force your way in,\n I'll have to deal with you![await]""",
        DI2572_TOWER_HENCHMAN_2: """POUNDER: Stay outta our hair![await]\n [delay]...Huh? [delay]"You don't have hair"?[await][pause]\n That's it, you're asking for it![await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """POUNDER: Man, I need a break. This\n job is tiring.[await]""",
        DI3073_TOWER_HENCHMAN_3: """POUNDER: Bullet Bill production is\n on schedule! Don't get in my way![await]""",
    }


class DirectorBossFight(BossFightPrize):
    _text = "Director"
    _formation = FORM0260
    _members = [
        FormationMember(DIRECTOREnemy, 183, 127),
        FormationMember(POUNDETTEEnemyHenchman, 135, 119),
        FormationMember(POUNDETTEEnemyHenchman, 167, 103),
        FormationMember(POUNDETTEEnemyHenchman, 199, 151),
        FormationMember(POUNDETTEEnemyHenchman, 231, 135),
    ]
    _seaside_letter_name_if_seaside_boss = "the Director"
    _seaside_letter_name_if_volcano_boss = "a red-clad smith trudging"
    _seaside_letter_name_if_final_boss = "the Director's minions."

    _npc_models = [DirectorBattleObject, DirectorLargeObject, DirectorSmallObject]
    _statue_npc = ShovelKnightStatueObject

    _mook_henchmen = [
        BossFightHenchman(monster=POUNDETTEEnemyHenchman, model=PoundetteHenchman),
    ]

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """DIRECTOR: (Could this day get any\n worse?)[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Figured out the password, did you?[delay_30]\n Don't get too cocky![delay_30]\n Intruders will be eliminated![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Director's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the DIRECTOR!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """DIRECTOR: I'm afraid I have more\n pressing matters to attend to.\n Depart at once.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """DIRECTOR: Do not waste too much\n time here. Your quest must\n continue.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """DIRECTOR: Any tomfoolery will be\n dealt with by immediate meltdown.\n Get off of my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Only the Chief can help you, now.[await]\n I have a Latte with my name on it.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """POUNDETTE: I don't feel like I'm\n being used to my full potential\n down here.[await][pause] But I don't mind\n having a break.[await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """POUNDETTE: I don't feel like I'm\n being used to my full potential\n down here.[await][pause] but I don't mind\n having a break.[await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To Whom It May Concern:\n[await][page]\n Please conclude all business with\n `SEASIDE_BOSS` ASAP.\n[await]\n Your next assignment involves\n `VOLCANO_BOSS_DESCRIPTION`\n at the volcano. [await]\n Temporary labor available from\n `FINAL_BOSS_NAME`\n All changes tenured with immediate\n effect. Mandatory overtime until\n the job is complete.  Direct all\n inquiries to the Manager.[await][page]\n\n                                   Signed,\n                              the Director[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """POUNDETTE: I don't feel like I'm\n being used to my full potential\n down here.[await][pause] but I don't mind\n having a break.[await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """POUNDETTE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """POUNDETTE: We're making a cake\n to look just like the Director![await]""",
        DI2062_APPRENTICE_CHEF: """POUNDETTE: We've gotten REAL\n good with fondant![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Director must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """DIRECTOR: I'm afraid you must\n continue searching.[delay] There are\n [0x7024] item(s) remaining.[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Director is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Director.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """DIRECTOR: I'm afraid there is\n nothing of concern to you in\n this town.[await]""",
        DI2832_OCCUPIED_SEASIDE_INNKEEPER: """ Salutations. How would you like to\n stay in our inn for free today?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING: """ The two guys in the left building\n have been acting suspicious.[await]""",
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED: """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ Have you been to the Director's\n house up on the hill yet?[await]""",
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED: """ There's nothing suspicious going on\n in our town! [delay]Now go on, go to the\n next town![await]""",
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ Once you get through the Sunken\n Ship, you can... er...[await]""",
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT: """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER: """ No, you can't see what I'm buying!\n [delay]How rude![await]""",
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """\n                   Scram![await]""",
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD: """ There's some important business\n happening in this shed, so get lost\n and quit trying to interrupt us![await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """DIRECTOR: I'm afraid the dojo\n master will be quite a challenge for\n you to beat.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ State your business.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ State your business.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Meltdown-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Director is busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Director.[await]""",
    }
    _dialog_replacements_if_mandatory_fights_changed = {
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """POUNDETTE: Well, we lost.\n Time for a break.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """POUNDETTE: You beat the Director!\n Impressive![await]""",
        DI2560_TOWER_HENCHMAN_1: """POUNDETTE: Salutations.[await][pause] Would you\n like to book an appointment with\n the Director?[await][pause]\n ...You want to just barge right\n in?![delay] No way![await]\n Time to teach you some manners![await]""",
        DI2572_TOWER_HENCHMAN_2: """POUNDETTE: The Director doesn't\n want anyone coming back here.[await]\n So I'm going to have to ask you\n to leave.[await]""",
        DI3072_TOWER_HENCHMAN_3_WINDOW: """POUNDETTE: Finally, some time to\n rest![await]""",
        DI3073_TOWER_HENCHMAN_3: """\nPOUNDETTE: Let's see whatcha got![await]""",
    }


class GunyolkBossFight(BossFightPrize):
    _text = "Gunyolk"
    _formation = FORM0261
    _members = [
        FormationMember(GUNYOLKEnemy, 199, 103),
        FormationMember(FACTORYCHIEFEnemy, 231, 151),
    ]
    _seaside_letter_name_if_seaside_boss = "the Chief"
    _seaside_letter_name_if_volcano_boss = "a big machine rolling"
    _seaside_letter_name_if_final_boss = "the Factory Chief's goons."

    _npc_models = [FactoryChiefObject]
    _statue_npc = FactoryChiefStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """FACTORY CHIEF: Grrr... Leave me\n alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you solved it?[delay_30]\n Too bad, this is the end of the line\n for you! I won't let you through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Gunyolk's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n the GUNYOLK!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """FACTORY CHIEF: Harrumph! Get out\n of here before I invent something\n even stronger![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """FACTORY CHIEF: I'm surprised to\n see you back here! I don't have any\n new inventions to show yet.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """FACTORY CHIEF: Harrumph! I should\n invent myself a spiky hat![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Who do I have to Breaker Beam[await]\n to get a cuppa Coffee 'round here?[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n              Memorandum\n[await][page]\n `MAIN_CHARACTER_NAME` dispatched\n to handle `SEASIDE_BOSS`.\n[await]\n Real estate acquisition stalled by\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n Competition associated with \n `FINAL_BOSS_NAME`\n Report all conversations involving[await]\n the words "union", "living wage",\n "healthcare benefits", and/or\n "remote work environment" to your[await]\n supervisor immediately.[await][page]\n\n                      Do more with less.\n                                -The Chief[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big ninja! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Chief must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """FACTORY CHIEF: Harrumph! You're\n still missing [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n The Gunyolk is busy right now, so\n it can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering the Gunyolk.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """FACTORY CHIEF: Harrumph! What're\n you doing here?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find the Factory Chief...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """FACTORY CHIEF: Harrumph! Just\n because you beat me, doesn't mean\n you can beat the dojo master![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Did you come here to fight me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Did you come here to fight me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Ninja-this and Invention-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """FACTORY CHIEF: I'll out-jump you\n if it's the last thing I do![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """FACTORY CHIEF: I'll out-jump you\n if it's the last thing I do![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n The Gunyolk is busy right now, so\n it can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering the Gunyolk.[await]""",
    }


class SmithyBossFight(BossFightPrize):
    _text = "Smithy"
    _formation = FORM0295
    _members = [
        FormationMember(SMITHY1Enemy, 199, 127),
        FormationMember(SMELTEREnemy, 87, 87),
        FormationMember(MACHINEMADEBodyguardEnemy, 135, 127, hidden_at_start=True),
        FormationMember(MACHINEMADEBodyguardEnemy, 199, 159, hidden_at_start=True),
    ]
    _seaside_letter_name_if_volcano_boss = "a furious weaponsmith thundering"
    _seaside_letter_name_if_final_boss = "Smithy's gang."
    _hp_slice_excluded_enemies = [
        MACHINEMADEBodyguardEnemy,
        MACHINEMADEBodyguardEnemy,
        SMELTEREnemy,
    ]
    _extra_hp_enemies = [SMITHY2Enemy]
    _additional_enemies_to_scale = [
        SMITHY2Enemy,
        SMITHYBodyEnemy,
        SMITHYChestEnemy,
        SMITHYMageEnemy,
        SMITHYSafeEnemy2,
        SMITHYTankEnemy,
    ]

    _npc_models = [SmithyLargeObject, SmithyBodyOverworldObject, SmithySmallObject]
    _statue_npc = SmithyStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """SMITHY: How utterly annoying!\n Leave me alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Gufaw, haw, haw![delay_30] You really think\n I'm going to let you through with\n just a password?![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Smithy's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n SMITHY!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """SMITHY: How utterly annoying!\n Get out of here before I crush\n you all![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """SMITHY: Gufaw, haw, haw...\n Not quite as impressive as my\n factory, eh?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """SMITHY: Never have I been so\n wronged![await]""",
        DI1782_SHIP_BOSS_DRINK: """ This isn't even my final form![await]\n Barkeep!  Bring me more Ale!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Weakling,\n[await][page]\n I'll bet you had trouble with\n `SEASIDE_BOSS`. Pathetic.[await]\n\n A Drill Bit screamed about\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano when I smashed it.[await]\n I expected better from \n `FINAL_BOSS_NAME`[await]\n The Shyster is complaining about\n my blood pressure again.  I have\n a sledge for problems like these.[await][page]\n\n You haven't seen my final form yet,\n                                    Smithy[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like blacksmith! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Smithy must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """SMITHY: How utterly annoying![await]\n Give me [0x7024] more item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Smithy's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Smithy.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """SMITHY: So, it's YOU![await]\n Unfortunately for you, there's\n nothing evil in this town that\n demands your attention.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Smithy...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """\n   SMITHY: Grr... Leave me alone![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Grr... What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Grr... What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Factory-this and Weapon-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """SMITHY: Grr... [delay]You're stronger\n than I thought...[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """SMITHY: Grr... [delay]You're stronger\n than I thought...[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Smithy's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Smithy.[await]""",
    }


class Punchinello2BossFight(BossFightPrize):
    _text = "Punchinello 2"
    _formation = FORM0124
    _members = [
        FormationMember(PUNCHINELLO2Enemy, 188, 116),
        FormationMember(STRONGBOBOMB3Enemy, 145, 103, hidden_at_start=True),
        FormationMember(STRONGBOBOMB1Enemy, 150, 129, hidden_at_start=True),
        FormationMember(STRONGBOBOMB4Enemy, 182, 142, hidden_at_start=True),
        FormationMember(STRONGBOBOMB2Enemy, 223, 142, hidden_at_start=True),
    ]
    _anchor_enemy = PUNCHINELLO2Enemy
    _hp_slice_excluded_enemies = [
        STRONGBOBOMB3Enemy,
        STRONGBOBOMB1Enemy,
        STRONGBOBOMB4Enemy,
        STRONGBOBOMB2Enemy,
    ]

    _name = "Punchinello"
    _seaside_letter_name_if_seaside_boss = "Hothead"
    _seaside_letter_name_if_volcano_boss = "a demolitionist stomping"
    _seaside_letter_name_if_final_boss = "Punchinello's demo team."

    _npc_models = [Punchinello2LargeObject, Punchinello2SmallObject]
    _statue_npc = PunchinelloStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """PUNCHINELLO: Grrr... Leave me\n alone![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So... You figured out my\n password.[await]\n If you're not here for an\n autograph, I'll have to test you\n once more to let you through![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Punchinello's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped\n PUNCHINELLO!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """PUNCHINELLO: Grrr... I'll never get famous\n at this rate![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """PUNCHINELLO: You've come back to\n visit? I truly must be famous![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """PUNCHINELLO: They say I'm a hot\n head, so it's a bad idea to stand\n on my head.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ WATCH ME DRINK THIS TOBASCO![await]\n I'm gonna be youtube-famous![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n WHAT'S UP FANS?!\n[await][page]\n I just watched a HYPE fight versus\n `SEASIDE_BOSS`.  Oh.  Em.  Gee.[await]\n\n My Bob-omb army told me about\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.  Fuse is LIT!![await]\n I smell a collab video with \n `FINAL_BOSS_NAME`[await]\n Don't forget to tune in for my 100k\n follower special, where I'll play\n Bob-omb roulette with watermelons![await][page]\n\n           Like, Share, and Subscribe!\n                              Punchinello[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like celebrity! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Punchinello must have\n gotten lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """PUNCHINELLO: Huh?[delay_30] What the hay?[await]\n Where are the other [0x7024] item(s)?[await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Punchinello's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Punchinello.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """PUNCHINELLO: Hmmm... [delay]Huh?\n [delay]A visitor? [delay]Well, there's not much\n to do around here.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Punchinello...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """PUNCHINELLO: A challenge from\n the dojo master, eh? Let's see\n where this goes.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Hello. Are you with the press?[await]\n  [select] (I'm here to fight)\n  [select] (Sorry, wrong number)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Hello. Are you with the press?[await]\n  [select] (I'm here to fight)\n  [select] (Sorry, wrong number)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Bomb-this and Famous-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Punchinello's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Punchinello.[await]""",
    }


class Booster2BossFight(BossFightPrize):
    _text = "Booster 2"
    _formation = FORM0123
    _members = [
        FormationMember(BOOSTEREnemy2, 184, 116),
        FormationMember(SNIFIT2Enemy, 156, 132),
        FormationMember(SNIFIT2Enemy, 143, 104),
        FormationMember(SNIFIT2Enemy, 212, 138),
        FormationMember(BOOSTERDUMMY, 0, 0),
    ]

    _seaside_letter_name_if_volcano_boss = "a viking riding trains"
    _seaside_letter_name_if_final_boss = "Booster's frenemies."
    _name = "Booster"
    _hp_slice_excluded_enemies = [BOOSTERDUMMY]

    _npc_models = [Booster2SmallObject]
    _statue_npc = BoosterStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BOOSTER: It's pretty cozy in here.[await][pause]\n No, you can't come in![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Eh?[delay_30] THAT was my password?![delay_30]\n I'd better fight you, just to be\n sure.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Booster's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BOOSTER!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BOOSTER: I'd love to entertain\n you, but I'm busy watching the\n fish. Come back later.[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BOOSTER: Eh...? My! It's you\n again![await][page]\n  We're having a heated debate over\n what a "party" is, so you can stay\n if you'd like to contribute.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BOOSTER: Hm? How's the view up there?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ This Dish Detergent is DELICIOUS![await]\n Number 2, (belch) MORE SOAP!!![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Attention `MAIN_CHARACTER_NAME`,\n[await][page]\n We had an urgent engagement, and\n regret that we couldn't stay and\n play with `SEASIDE_BOSS`.\n[await]\n While on beetle patrol, #2 saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n Snifit three suggested they might be\n `FINAL_BOSS_NAME`\n We're riding the Loco Express to\n the lake of wedding tears.  Also, \n Number 1 says there's no money \n in the budget for new doors.[await][page]\n\n                                   Booster\n                  Dictated but not read[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like stinky man! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Booster must have gotten\n lost on his way here.""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n   BOOSTER: Found our town, eh?[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Booster...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BOOSTER: I wonder if the dojo\n master can shape-shift into a\n Mario doll.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Eh? What'd you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Eh? What'd you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Beetle-this and Train-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Booster's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Booster.[await]""",
    }


class Bundt2BossFight(BossFightPrize):
    _text = "Bundt 2"
    _formation = FORM0137
    _members = [
        FormationMember(BUNDT2Enemy, 199, 127),
        FormationMember(RASPBERRY2Enemy, 199, 119),
        FormationMember(TORTE2Enemy, 199, 151),
        FormationMember(TORTE2Enemy, 135, 119),
        FormationMember(CANDLEEnemy, 0, 0),
    ]
    _force_start_event = BE0017_BEGIN_BUNDT_POSTGAME

    _seaside_letter_name_if_seaside_boss = "the Cake"
    _seaside_letter_name_if_volcano_boss = "a possessed cake walking"
    _seaside_letter_name_if_final_boss = "Bundt's dinner guests."
    _name = "Bundt"

    _npc_models = [Bundt2LargeObject, Bundt2SmallObject]
    _statue_npc = BundtStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """BUNDT: La la la la la la la la la~[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ What a surprise! [delay_30]Welcome![await]\n Let me warm up for the feast![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Bundt's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BUNDT!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BUNDT: Oh...! My beautiful body![await][pause]\n Please go away while I recover![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BUNDT: Come back to celebrate a\n wedding? At least try and eat me\n this time...[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BUNDT: OH! MY CANDLES![await]""",
        DI1782_SHIP_BOSS_DRINK: """ I've got my own frosting, thanks.[await]\n "Happy" Frogs taste best, though![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Greetings and Salutations!\n[await][page]\n I can't get over how quickly you\n dispatched `SEASIDE_BOSS`!\n[await]\n My dinner guests informed me of \n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n I heard they're having a reunion with \n `FINAL_BOSS_NAME`\n I've gotten hungry aboard this ship.\n You wouldn't believe how much you\n can miss your chefs and creams. [await]\n Come visit and have a slice![await][page]\n\n       Frosting my way to victory,\n                                     Bundt[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: This masterpiece is\n our latest creation... wait...[await]""",
        DI2062_APPRENTICE_CHEF: """CHEF TORTE: ...Apprentice! [delay]Why\n does this look like Bundt?[await]""",
        DI2180_CHAPEL_NPC: """ Reverend Bundt must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BUNDT: Hmm?[delay] You look like you could\n use a break![await][pause] Come back with\n the other [0x7024] item(s)![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Bundt is busy right now, so it\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Bundt.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BUNDT: Greetings and salutations!\n Welcome to our quiet little town![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Bundt...\n in his house. He is...the most\n respected dessert here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BUNDT: What a fierce battle![await][pause] That\n was nothing compared to the dojo\n master, you know.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ What's this?[await][pause] Looking for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ What's this?[await][pause] Looking for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Candle-this and Frosting-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BUNDT: What a delicious training\n exercise![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BUNDT: What a delicious training\n exercise![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Bundt is busy right now, so it\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Bundt.[await]""",
    }


class Johnny2Fight(BossFightPrize):
    _text = "Johnny 2"
    _formation = FORM0216
    _members = [
        FormationMember(JOHNNYEnemy2, 165, 121),
    ]
    _name = "Johnny"
    _seaside_letter_name_if_volcano_boss = "a shark prowling around"
    _seaside_letter_name_if_final_boss = "Johnny's crew."
    _seaside_letter_name_if_sunken_ship_boss = "Jonathan “Johnny” Jones"

    _npc_models = [JohnnyLargeObject, JohnnySmallObject]
    _statue_npc = JohnnyStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JOHNNY: Matey, it'd be mighty fun\n to spar again, but I'm tryin' to\n sleep now.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Good job, matey... But ye gotta\n fight me first if ye wanna be let\n through![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n To `MAIN_CHARACTER_NAME`,\n[await][page]\n Knowin' you, knocking down\n `SEASIDE_BOSS` was a breeze.[await]\n\n By the way, my pirates saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n It's probably one of \n `FINAL_BOSS_NAME`[await]\n Well, my gills are failing on me,\n so I'll be heading back down.\n Drop in when you have time, okay?[await][page]\n\n                         Your true mate,\n             Jonathan "Johnny" Jones[await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like shark! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jones must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JOHNNY: Found [0x7000] item(s, eh? Arr,\n harr, harr...! You gotta find [0x7024]\n more, matey![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Johnny is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Johnny.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n        JOHNNY: Ahoy, matey![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Johnny...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JOHNNY: Good luck, matey. The dojo\n master's mighty tough.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Arr-this and Matey-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JOHNNY: Matey, I've got lots o'\n training to do![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """JOHNNY: Matey, I've got lots o'\n training to do![await]""",
    }


class Belome3Fight(BossFightPrize):
    _text = "Belome 3"
    _formation = FORM0055
    _members = [
        FormationMember(BELOMEEnemy3, 183, 127),
        FormationMember(MARIOCLONESEnemy, 135, 119, hidden_at_start=True),
        FormationMember(TOADSTOOL3Enemy, 215, 159, hidden_at_start=True),
    ]
    _additional_enemies_to_scale = [BOWSERCOPYSEnemy, GENOCLONESEnemy, MALLOWCOPYSEnemy]
    _anchor_enemy = BELOMEEnemy3
    _hp_slice_excluded_enemies = [MARIOCLONESEnemy, TOADSTOOL3Enemy]

    _seaside_letter_name_if_volcano_boss = "a hungry dog walking"
    _seaside_letter_name_if_final_boss = "Belome's clones."
    _name = "Belome"

    _npc_models = [Belome3LargeObject, Belome3SmallObject]
    _statue_npc = BelomeSmallStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """\n        BELOME: Good night~![await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Belome's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped BELOME!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """BELOME: Oh, you're back![await]\n Did you bring any food?[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """BELOME: Say, it's past my bedtime.\n Can you get off of my head?[await]""",
        DI1782_SHIP_BOSS_DRINK: """ Woof, I ate too many Mallows~![await]\n I should wash it down with Tonic~![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """ It's a damp, slimy, looking note\n (did `SEASIDE_BOSS` LICK this?).\n[await][page]\nA paw print and a crudely drawn image of `VOLCANO_BOSS_DESCRIPTION`\nis etched on the paper.\nThis is probably one of \n`FINAL_BOSS_NAME`'s henchmen!\n`SEASIDE_BOSS` likely headed down to\nfind more snacks,\nso it's time to move on.[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like big dog! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Belome must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """BELOME: Oh, no, you're still\n missing [0x7024] item(s).[await][pause] I can't wait any\n longer to see what today's cake\n will be.[await][pause] I'm STARVING![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Belome.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """BELOME: It's dreadfully boring\n around here~![await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Belome...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ Are you the pizza delivery person?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ Are you the pizza delivery person?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Scarecrow-this and Hungry-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """BELOME: This training regimen is\n giving me quite the appetite![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Belome.[await]""",
    }


class Jinx4BossFight(BossFightPrize):
    _text = "Jinx 4"
    _formation = FORM0217
    _members = [
        FormationMember(JINXEnemy4, 181, 122),
        FormationMember(TeamGaugeEnemy, 36, 200),
    ]
    _scaling_excluded_enemies = [TeamGaugeEnemy]
    _hp_slice_excluded_enemies = [TeamGaugeEnemy]

    _seaside_letter_name_if_volcano_boss = "a small figure blinking"
    _seaside_letter_name_if_final_boss = "Jinx's kouhai."
    _name = "Jinx"

    _npc_models = [Jinx4SmallObject]
    _statue_npc = JinxStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """JINX: Please do not disturb me.\n I am training in here.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """\n   JINX: I was going easy on you![await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """JINX: I must accept that I have been\n bested. Good work![await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """JINX: Yes, I am short! Show a little\n respect![await]""",
        DI1782_SHIP_BOSS_DRINK: """ Hail, Master `MAIN_CHARACTER_NAME`![await]\n Let us celebrate with Matcha![await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n `MAIN_CHARACTER_NAME`,\n[await][page]\n Have you mastered your training\n with `SEASIDE_BOSS`?\n[await]\n I sense your next challenge is\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n They battle in the old style of \n `FINAL_BOSS_NAME`\n Complete this task, and you will[await]\n be prepared for our rematch.\n Fail, and you need not ever show\n your face on my ship again. There[await]\n are some promising turtles here. [await][page]\n\n                       Fight with honor,\n                                      Jinx[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Jinx must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        DI2560_TOWER_HENCHMAN_1: """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFIT 2: Please refrain\n from bothering Jinx.[await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n               JINX: Hmm...[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        DI3057_MONSTRO_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT: """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        DI3338_MONSTRO_SUPERBOSS_HINT: """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """JINX: Master!\n Share your wisdom with us![await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Jinx.[await]""",
    }


class Culex3DBossFight(BossFightPrize):
    _text = "Culex 2"
    _formation = FORM0096
    _members = [
        FormationMember(CULEX3DEnemy, 183, 103),
        FormationMember(FIRECRYS3DEnemy, 135, 103, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 151, 119, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 183, 135, hidden_at_start=True),
        FormationMember(FIRECRYS3DEnemy, 215, 143, hidden_at_start=True),
    ]
    _force_start_event = BE0077_CULEX_3D
    _anchor_enemy = CULEX3DEnemy

    _seaside_letter_name_if_volcano_boss = "an ethereal knight gliding"
    _seaside_letter_name_if_final_boss = "Culex's travelers."
    _name = "Culex"

    _npc_models = [CulexLargeObject, CulexSmallObject]
    _statue_npc = CulexStatueObject

    _dialog_replacements = {
        DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING: """CULEX: Please do not attempt to\n crack this egg again.[await][page]\n It is not an effective way to\n grind experience points.[await]""",
        DI1660_SHIP_PASSWORD_COMPLETE: """ You have passed the first test.\n But you're not finished yet!\n Please enter.[await]""",
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED: """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Culex's place.[await]""",
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED: """PIRATE: That's AMAZING!\n No one's EVER whipped CULEX!![await]""",
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING: """CULEX: This world truly is\n uninhabitable for me and my kind...[await]""",
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER: """CULEX: Greetings. It is good to\n make your acquaintance once\n again.[await]""",
        DI1781_SHIP_BOSS_JUMP_ON_HEAD: """CULEX: This is not the encounter In expected when I came to visit this\n world.[await]""",
        DI1782_SHIP_BOSS_DRINK: """ How droll, my crystals shattered.[await]\n I've only Bacchus Wine remaining.[await]""",
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1786_LETTER_FROM_SHIP_BOSS: """\n Greetings, honored Warrior.\n[await][page]\n I have witnessed you do battle with\n `SEASIDE_BOSS`. \n I am impressed, but not surprised.[await]\n In my travels of your world, I saw\n `VOLCANO_BOSS_DESCRIPTION`\n near the volcano.[await]\n The crystals revealed they are \n allies of `FINAL_BOSS_NAME`.[await]\n I know not your path to victory, \n but challenge awaits you there. \n I must return to the sea, lest the\n fragile water crystal shatter.[await][page]\n\n                       Fight with honor,\n                                     Culex[await]""",
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4: """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        DI2061_HEAD_CHEF: """CHEF TORTE: Zees cake, ve make\n it look like demon! It is...\n masterpiece![await]""",
        DI2180_CHAPEL_NPC: """ Reverend Culex must have gotten\n lost on his way here.""",
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE: """CULEX: You must retrieve [0x7024] more\n item(s) before we may proceed.[await]\n Godspeed, champion knight![await]""",
        DI2830_SEASIDE_BOSS_WELCOMES_YOU: """\n           CULEX: Good day.[await]""",
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME: """ You will find Culex...\n in his house. He is...the most\n respected person here.[await]""",
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT: """CULEX: It will be quite difficult to\n claim victory over the dojo master.\n I wish you luck.[await]""",
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
        DI3353_DOJO_BOSS_2_FULLY_DEFEATED: """CULEX: Well met! Thank you for\n the excellent battle.[await]""",
    }
    _dialog_replacements_remake = {
        DI2560_TOWER_HENCHMAN_1: """SNIFSTER 1: Hello there.[await]\n Culex is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        DI2572_TOWER_HENCHMAN_2: """SNIFSTER 2: Please refrain\n from bothering Culex.[await]""",
    }


class SlotsPrize1(SlotsPrize):
    _logic_event = E2490_BEAN_VALLEY_LEFTMOST_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [JmpToEvent(E2490_BEAN_VALLEY_LEFTMOST_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE)]
        )


class SlotsPrize2(SlotsPrize):
    _logic_event = E2491_BEAN_VALLEY_BOTTOM_LEFT_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                JmpToEvent(
                    E2491_BEAN_VALLEY_BOTTOM_LEFT_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE
                )
            ]
        )


class SlotsPrize3(SlotsPrize):
    _logic_event = E2492_BEAN_VALLEY_BOTTOM_RIGHT_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                JmpToEvent(
                    E2492_BEAN_VALLEY_BOTTOM_RIGHT_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE
                )
            ]
        )


# Collection of all BossFightPrize subclasses for the ShuffledBosses flag
ALL_BOSS_FIGHTS: list[type[BossFightPrize]] = [
    # Standard bosses
    HammerBrosFight,
    Croco1BossFight,
    MackBossFight,
    PandoriteBossFight,
    Belome1BossFight,
    BowyerBossFight,
    Croco2BossFight,
    PunchinelloBossFight,
    BoosterBossFight,
    KnifeGuyGrateGuyBossFight,
    BundtBossFight,
    KingCalamariBossFight,
    HidonBossFight,
    JohnnyBossFight,
    YaridovichBossFight,
    Belome2BossFight,
    JaggerBossFight,
    Jinx1BossFight,
    Jinx2BossFight,
    Jinx3BossFight,
    CulexBossFight,
    BoxBoyBossFight,
    MegasmilaxBossFight,
    DodoBossFight,
    BirdettaBossFight,
    ValentinaBossFight,
    CzarDragonBossFight,
    AxemRangersBossFight,
    ChesterBossFight,
    KamekBossFight,
    BoomerBossFight,
    ExorBossFight,
    CountdownBossFight,
    CloakerDominoBossFight,
    ClerkBossFight,
    ManagerBossFight,
    DirectorBossFight,
    GunyolkBossFight,
    SmithyBossFight,
    # Remake bosses
    Punchinello2BossFight,
    Booster2BossFight,
    Bundt2BossFight,
    Johnny2Fight,
    Belome3Fight,
    Jinx4BossFight,
    Culex3DBossFight,
]
