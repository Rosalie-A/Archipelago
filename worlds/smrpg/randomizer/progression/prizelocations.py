from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (
    EventScript,
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    Return,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject

from ..types.logic import Inventory
from ..types.prize import Prize
from ..types.prizelocation import (
    AllyNPCSub,
    BossFightLocationHenchmanNPC,
    BossFightLocationNPC,
    RemoveIfNotFilled,
    StandingLocation,
    TreasureChestLocationRow1,
    TreasureChestLocationRow2,
    TreasureChestLocationRow3,
    TreasureChestLocationRow4,
    TreasureChestLocationRow5,
    TreasureChestLocationRow6,
    NPCLocationRow1,
    NPCLocationRow2,
    NPCLocationRow3,
    NPCLocationRow4,
    NPCLocationRow5,
    NPCLocationRow6,
    NPCLocationRow7,
    StandingLocationRow1,
    StandingLocationRow2,
    StandingLocationRow3,
    StandingLocationRow4,
    StandingLocationRow5,
    StandingLocationRow6,
    StandingLocationRow7,
    StandingLocationRow8,
    StandingLocationRow9,
    StandingLocationRow10,
    StandingLocationRow11,
    StandingLocationRow12,
    StandingLocationRow13,
    StandingLocationRow14,
    StandingLocationRow15,
    RiverLocationRow2,
    BossFightLocation,
    CharacterRecruitmentLocation,
    StartingCharacterLocation,
    StarPieceLocation,
    SpellSlotLocation,
    ShuffleLocationSelector,
    TreasureShopLocation,
    BoosterHillLocation,
    FrogDiscipleLocation,
    PacketLocationRow1,
    InvisibleFlagLocation,
    WorldAreaEnum,
    KeyItemLocation,
)
from ..types.packet_type import PacketType
from ..data.variables.room_names import *
from ..data.variables.event_script_names import *
from ..data.variables.action_script_names import *
from ..data.variables.pack_names import *
from .prizes import *
from ..types.prize import (
    FPFlowerPrize,
    SlotsPrize,
    EmptyPrize,
)
from ..types.flags import *
from ..utils.npcs import (
    set_npc_direction_if_swse_only,
    set_mines_punch_command,
)
from ..utils.snippets.es_mimic_rise import get_mimic_rise_kamek
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    NPC_0,
    NPC_1,
    NPC_2,
    NPC_3,
    NPC_4,
    NPC_5,
    NPC_6,
    NPC_7,
    NPC_8,
    NPC_9,
    NPC_10,
    NPC_11,
    NPC_12,
    NPC_13,
    NPC_14,
    NPC_15,
    NPC_16,
    NPC_17,
    NPC_18,
    NPC_19,
    NPC_20,
    NPC_21,
    NPC_22,
    NPC_23,
    NPC_24,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import (
    SOUTHEAST,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
    ActionQueueAsync,
    Pause,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (
    A_SetSpriteSequence,
    A_FaceSoutheast,
    A_FaceSouthwest,
    A_Pause,
    A_VisibilityOn,
    A_PlaySound,
)
from typing import TYPE_CHECKING, cast

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments.sequence_speeds import *
from ..logic.renders import (
    render_bandits_way_boss,
    render_forest_maze_character_empty,
    render_forest_maze_character,
    render_booster_tower_indoor_boss,
    render_booster_tower_henchman_scripts,
    render_marrymore_boss_henchmen,
    render_marrymore_character_empty,
    render_seaside_beach_boss,
    render_ship_password_boss,
    render_ship_final_boss,
    render_dojo_first_fight,
    render_dojo_fight,
    render_bean_valley_planter_boss,
    render_statue_room_boss,
    render_volcano_exit_boss,
    render_inner_factory_second_fight,
    render_inner_factory_third_fight_slot,
    render_inner_factory_fourth_fight,
    render_final_boss_fight,
)

if TYPE_CHECKING:
    from ..types.logic import Inventory
    from ..types.gameworld import GameWorld


# Lazy imports for flags defined after the circular import point in flags.py
# These flags are defined after flags.py imports prizelocations, so they're not
# available via "from ..types.flags import *" at module load time.
def _get_late_flags():
    """Lazy import for flags defined after the circular import in flags.py."""
    from ..types.flags import (
        BowserDoorShuffle,
        BucketWarp,
        CasinoWarp,
        FixKnifeGuy,
        SkipBossFights,
        StarPiecesRequired,
        SuitePrize1Threshold,
        SuitePrize2Threshold,
        SuitePrize3Threshold,
        SuitePrize4Threshold,
        SuitePrize5Threshold,
        SuitePrize6Threshold,
    )

    return {
        "BowserDoorShuffle": BowserDoorShuffle,
        "BucketWarp": BucketWarp,
        "CasinoWarp": CasinoWarp,
        "FixKnifeGuy": FixKnifeGuy,
        "SkipBossFights": SkipBossFights,
        "StarPiecesRequired": StarPiecesRequired,
        "SuitePrize1Threshold": SuitePrize1Threshold,
        "SuitePrize2Threshold": SuitePrize2Threshold,
        "SuitePrize3Threshold": SuitePrize3Threshold,
        "SuitePrize4Threshold": SuitePrize4Threshold,
        "SuitePrize5Threshold": SuitePrize5Threshold,
        "SuitePrize6Threshold": SuitePrize6Threshold,
    }


_late_flags_cache = None


def _get_flag(name: str):
    """Get a late-defined flag by name."""
    global _late_flags_cache
    if _late_flags_cache is None:
        _late_flags_cache = _get_late_flags()
    return _late_flags_cache[name]


# Comments are included here to document what condition is met for a location to be considered checked.
# Anything that takes a flag has a variable name listed, ie TOAD_IN_MUSHROOM_WAY_1.
# The actual memory address this corresponds to can be found in data/variables/variable_names.py
# ie TOAD_IN_MUSHROOM_WAY_1 = Flag(0x7052, 4) = $7052 bit 4

# There are no longer any missable checks. All missable checks have become permanent in one way or another

# note: hidon + pandorite mimics work weird. they do three things
# they can appear in any chest
# say for example the fight is in the MushroomKingdomMainHall chest...
# 1: the mimic fight begins - this is the MushroomKingdomMainHall check. the mimic fight is not an AP item but it is considered an "item" for internal shuffling purposes
# 2: upon defeat, the mimic drops an item - this is the Mimic1DropRewardLocation check. this is considered checked when MIMIC_1_CLEARED is set (or MIMIC_2_CLEARED). this can in theory be an AP item
# at this point, the chest looks and acts empty from the player's POV, but it is NOT disabled!
# when the player reloads the room, the chest is hittable again for an extra check. this is the Mimic1ReloadRewardLocation and can also in theory be an AP item. this DOES disable the chest
# in memory, this third check is considered done when the host chest (MushroomKingdomMainHall for ex.) has its object trigger disabled
# so it's kind of like a chest checked condition gets deferred when a mimic is found
# the actual chest that does this is random every seed
# i am not sure what that implies for AP but we can work it out

# not sure what to do about InfiniteCoinsPrize
# normally an easy way to tell a chest is checked is if its object trigger is disabled
# but the chest that holds infinite coins never disables its object trigger
# can be in a random chest
# is it possible for tracker to know ahead of time which chest it is in and flag it as checked when first opened?
# when the player first hits the chest that contains infinite coins it will set the INFINITE_COINS_FOUND bit regardless of what chest it's been shuffled into


########## mario's house


class StartingItem1Location(NPCLocationRow2):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_1
    _world_area = WorldAreaEnum.MARIOS_PAD
    _blacklist = [StarPiecePrize, RecoveryMushroomPrize]
    # this is granted at the start of the game by default


class StartingItem2Location(NPCLocationRow3):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_2
    _world_area = WorldAreaEnum.MARIOS_PAD
    _blacklist = [StarPiecePrize, RecoveryMushroomPrize]
    # this is granted at the start of the game by default


class StartingItem3Location(NPCLocationRow4):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_3
    _world_area = WorldAreaEnum.MARIOS_PAD
    _blacklist = [StarPiecePrize, RecoveryMushroomPrize]
    # this is granted at the start of the game by default


class StartingItem4Location(NPCLocationRow5):
    _originally_held = MushroomPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_STARTER_4
    _world_area = WorldAreaEnum.MARIOS_PAD
    _blacklist = [StarPiecePrize, RecoveryMushroomPrize]
    # this is granted at the start of the game by default


class StartingCharacter1(StartingCharacterLocation):
    _originally_held = MarioRecruitmentPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_1
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1220_STARTING_CHARACTER_1
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class MarioSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = JumpSpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MarioRecruitmentPrize)


class MarioSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = FireOrbSpellPrize
    _level = 3

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MarioRecruitmentPrize)


class MarioSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = SuperJumpSpellPrize
    _level = 6

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MarioRecruitmentPrize)


class MarioSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = SuperFlameSpellPrize
    _level = 10

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MarioRecruitmentPrize
        )


class MarioSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = UltraJumpSpellPrize
    _level = 14

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MarioRecruitmentPrize
        )


class MarioSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = UltraFlameSpellPrize
    _level = 18

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MarioRecruitmentPrize
        )


class StartingCharacter2(StartingCharacterLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_2
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1221_STARTING_CHARACTER_2
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class StartingCharacter3(StartingCharacterLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_3
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1222_STARTING_CHARACTER_3
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class StartingCharacter4(StartingCharacterLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_4
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1223_STARTING_CHARACTER_4
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class StartingCharacter5(StartingCharacterLocation):
    _originally_held = None
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.STARTER_CHARACTER_5
    _world_area = WorldAreaEnum.MARIOS_PAD
    _container_event = E1224_STARTING_CHARACTER_5
    _show_dialog: bool = False

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(1)
        return super().set_prize(prize)


class PostgameVoucherLocation(NPCLocationRow6, KeyItemLocation):
    _bias = True
    _originally_held = StayVoucherPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.POSTGAME_VOUCHER
    _world_area = WorldAreaEnum.MARIOS_PAD
    _remake_only = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_inner_mines(world, inventory)
            and can_access_tower(world, inventory)
            and can_clear_chapel(world, inventory)
            and can_clear_ship(world, inventory)
            and can_access_temple_boss(world, inventory)
            and can_access_sealed_door_boss(world, inventory)
            and can_access_fifth_dojo_boss(world, inventory)
        )

    # Flag as checked: VOUCHER_CHECK_DONE


########## mushroom way


class MushroomWay1LowerChest(TreasureChestLocationRow1):
    _originally_held = Coins5Prize
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_1
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher, SlotsPrize]
    # Flag as checked: npc 0 in room 203 has its object trigger disabled.


class MushroomWay1UpperChest(TreasureChestLocationRow2):
    _originally_held = Coins8Prize
    _rooms = [R203_MUSHROOM_WAY_AREA_01]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_2
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher, SlotsPrize]
    # Flag as checked: npc 1 in room 203 has its object trigger disabled.


class MushroomWay1ToadRescue(NPCLocationRow2):
    _originally_held = HoneySyrupPrize
    _rooms = [R203_MUSHROOM_WAY_AREA_01, R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.TOAD_RESCUE_1
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_1


class MushroomWay2LedgeChest(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_3
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 0 in room 204 has its object trigger disabled.


class MushroomWay2ToadRescue(NPCLocationRow3):
    _originally_held = FlowerTabPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02, R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.TOAD_RESCUE_2
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_2


class MushroomWayRightGoomba(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_4
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 1 in room 204 has its object trigger disabled.


class MushroomWayLeftItemRemake(StandingLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.REMAKE_1
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _remake_only = True

    # Flag as checked: npc 10 in room 204 has been removed from the room.


class MushroomWayRightItemRemake(StandingLocationRow2):
    _bias = True
    _originally_held = PickMeUpPrize
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.REMAKE_2
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _remake_only = True

    # Flag as checked: npc 11 in room 204 has been removed from the room.


class MushrooomWayBossFight(BossFightLocation):
    _originally_held = HammerBrosFight
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_BOSS_FIGHT
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _pack_id = PACK183_MUSHROOM_WAY_BOSS
    _post_unlocks_event_id = E1194_MUSHROOM_WAY_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R205_MUSHROOM_WAY_AREA_03,
            NPC_7,
            sequence_setter_event_id=E0755_MUSHROOM_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MUSHROOM_WAY):
            content.extend(
                [
                    SetBit(MAP_BANDITS_WAY),
                    SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_BANDITS_WAY),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomWayStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_STAR_PIECE
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _parent = MushrooomWayBossFight
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomWayBossFightRewardItem(NPCLocationRow1):
    _bias = True
    _originally_held = HammerPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.HAMMER_BROS_REWARD
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MushroomWayCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = MallowRecruitmentPrize
    _rooms = [R205_MUSHROOM_WAY_AREA_03]
    _id = ShuffleLocationSelector.MUSHROOM_WAY_CHARACTER
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _container_event = E1225_MUSHROOM_WAY_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(R203_MUSHROOM_WAY_AREA_01, NPC_8),
        AllyNPCSub(R204_MUSHROOM_WAY_AREA_02, NPC_7),
        AllyNPCSub(R205_MUSHROOM_WAY_AREA_03, NPC_5),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return is_all_starting_chars_set(world, inventory)

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(2)
        return super().set_prize(prize)

    # Flag as checked: TOAD_IN_MUSHROOM_WAY_3


class MallowSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = ThunderboltSpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MallowRecruitmentPrize)


class MallowSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = HPRainSpellPrize
    _level = 3

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MallowRecruitmentPrize)


class MallowSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = PsychopathSpellPrize
    _level = 6

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(MallowRecruitmentPrize)


class MallowSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = ShockerSpellPrize
    _level = 10

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MallowRecruitmentPrize
        )


class MallowSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = SnowyPrize
    _level = 14

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MallowRecruitmentPrize
        )


class MallowSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = StarRainSpellPrize
    _level = 18

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory) and inventory.has_item(
            MallowRecruitmentPrize
        )


########## mushroom kingdom - available before and during invasion


class MushroomKingdomMainHall(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
        R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
    ]
    _npc_ids = [NPC_2, NPC_6]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_HALLWAY
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: either npc 2 in room 17 or npc 6 in room 325 has its object trigger disabled.


class MushroomKingdomLiberatedVaultLeft(TreasureChestLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
        R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_1
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 0 in room 31 or 331 has its object trigger disabled.


class MushroomKingdomLiberatedVaultRight(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
        R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_2
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 1 in room 31 or 331 has its object trigger disabled.


class MushroomKingdomLiberatedVaultMiddle(TreasureChestLocationRow3):
    _originally_held = FPFlowerPrize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
        R331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
    ]
    _npc_ids = [NPC_2, NPC_2]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_3
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 2 in room 31 or 331 has its object trigger disabled.


class MushroomKingdomChair(NPCLocationRow1):
    _originally_held = MushroomPrize
    _rooms = [
        R020_MUSHROOM_KINGDOM_CASTLE_TOADSTOOLS_ROOM,
        R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    ]
    _id = ShuffleLocationSelector.PEACH_SURPRISE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    # flag as checked: npc 0 is missing/despawned from room 20 or npc 7 is missing/despawned from room 328


class MushroomKingdomFreeShopItem(NPCLocationRow1):
    _originally_held = PickMeUpPrize
    _rooms = [
        R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
        R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    # flag as checked: MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED


class MushroomKingdomShopBasementLeft(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_BASEMENT_1
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 0 in room 492 has its object trigger disabled.


class MushroomKingdomShopBasementRight(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_BASEMENT_2
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 1 in room 492 has its object trigger disabled.


class MushroomKingdomWalletGuyFirstRewardLocation(NPCLocationRow2):
    _originally_held = FlowerTabPrize
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _id = ShuffleLocationSelector.WALLET_GUY_1
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(WalletPrize)

    # Flag as checked: RETURNED_WALLET


class MushroomKingdomWalletGuySecondRewardLocation(NPCLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _id = ShuffleLocationSelector.WALLET_GUY_2
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory) and inventory.has_item(WalletPrize)

    # Flag as checked: SECOND_WALLET_PRIZE_RECEIVED


########## mushroom kingdom = available only during occupation or later


class MushroomKingdomOccupiedOutdoorGuardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, R191_MUSHROOM_KINGDOM_OUTSIDE]
    _id = ShuffleLocationSelector.INVASION_EASTERN_GUARD
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: NPC 5 removed from room 190
    # Remember you need to define an additional henchman slot for the liberated room


class MushroomKingdomOccupiedCastleToadRescueLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [
        R328_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_TOADSTOOLS_ROOM,
    ]
    _id = ShuffleLocationSelector.INVASION_TOAD_RESCUE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Remember you need to define an additional henchman slot for the liberated room
    # Flag as checked: OCCUPIED_MUSHROOM_KINGDOM_TOAD_RESCUED


class MushroomKingdomOccupiedFamilyRescueLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [
        R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
        R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
    ]
    _id = ShuffleLocationSelector.INVASION_FAMILY
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED and OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_2_DEFEATED must BOTH be set


class MushroomKingdomOccupiedGuestRoomLocation(NPCLocationRow1):
    _bias = True
    _originally_held = WakeUpPinPrize
    _rooms = [R330_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_GUEST_ROOM]
    _id = ShuffleLocationSelector.INVASION_GUEST_ROOM
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: OCCUPIED_MUSHROOM_KINGDOM_GUEST_ROOM_ITEM_GRANTED


class MushroomKingdomBossFight(BossFightLocation):
    _bias = True
    _originally_held = MackBossFight
    _rooms = [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM]
    _id = ShuffleLocationSelector.INVASION_BOSS_FIGHT
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _pack_id = PACK179_MUSHROOM_KINGDOM_BOSS
    _post_unlocks_event_id = E1195_BANDITS_WAY_BOSS_UNLOCKS
    _henchman_can_run_away = False

    _npc_slots = [
        BossFightLocationNPC(
            R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
            NPC_3,
            sequence_setter_event_id=E0761_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_4],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_5],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_6],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_7],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_8],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_9],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
                R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
                R329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
                R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
                R191_MUSHROOM_KINGDOM_OUTSIDE,
            ],
            [
                NPC_3,
                NPC_5,
                NPC_0,
                NPC_4,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_0,
                NPC_1,
                NPC_4,
                NPC_10,
            ],
            pack_id=PACK010_KINGDOM_HENCHMEN_1,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0051_HENCHMAN_CONTAINER_1,
        ),
        BossFightLocationHenchmanNPC(
            [
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            ],
            [
                NPC_3,
            ],
        ),
        BossFightLocationHenchmanNPC(
            [
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
                R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
                R329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
                R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
                R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
                R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
                R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            ],
            [
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_4,
                NPC_6,
                NPC_1,
                NPC_1,
                NPC_0,
                NPC_0,
                NPC_1,
                NPC_3,
                NPC_1,
            ],
            pack_id=PACK011_KINGDOM_HENCHMEN_2,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0052_HENCHMAN_CONTAINER_2,
        ),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        for slot, henchman in henchmen_assignments:
            model = henchman.model
            if model is not None:
                npc_base = model().base
                for npc_id, room_id in zip(slot.npc_ids, slot.room_ids):
                    set_npc_direction_if_swse_only(world, room_id, npc_id, npc_base)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.KINGDOM):
            content.extend([ClearBit(SEWERS_CLOSED)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: MUSHROOM_KINGDOM_LIBERATED


class MushroomKingdomStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece1
    _rooms = [R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM]
    _id = ShuffleLocationSelector.INVASION_STAR_PIECE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _parent = MushroomKingdomBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_bandits_way(
            world, inventory
        )

    # Flag as checked: MUSHROOM_KINGDOM_LIBERATED


########## mushroom kingdom: only available AFTER liberation


class MushroomKingdomStoreExchangeLocation(NPCLocationRow2, KeyItemLocation):
    _bias = True
    _originally_held = CricketPiePrize
    _rooms = [
        R483_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_TOP_FLOOR,
        R491_MUSHROOM_KINGDOM_ITEM_SHOP_TOP_FLOOR,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_EXCHANGE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory) and inventory.has_item(
            RareFrogCoinPrize
        )

    # Flag as checked: RARE_FROG_COIN_EXCHANGED


class MushroomKingdomInnPurchaseLocation(NPCLocationRow1):
    _bias = True
    _originally_held = BeetlemaniaPrize
    _rooms = [
        R493_MUSHROOM_KINGDOM_INN_1F,
    ]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_INN
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: GAMEBOY_KID_PURCHASE_COMPLETE


########## bandit's way


class BanditsWayFlowerJumpLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BANDITS_WAY_1
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 9 in room 207 has its object trigger disabled.


class BanditsWayCoin1Location(StandingLocationRow3):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_1
    _world_area = WorldAreaEnum.BANDITS_WAY

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 3 in room 207 has been removed from the room.


class BanditsWayCoin2Location(StandingLocationRow2):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_2
    _world_area = WorldAreaEnum.BANDITS_WAY

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 4 in room 207 has been removed from the room.


class BanditsWayCoin3Location(StandingLocationRow1):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BANDITS_WAY_COIN_3
    _world_area = WorldAreaEnum.BANDITS_WAY

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 5 in room 207 has been removed from the room.


class BanditsWayDogChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R077_BANDITS_WAY_AREA_03]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_2
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 0 in room 77 has its object trigger disabled.


class BanditsWayPlatformsLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = BanditsWayStarPrize
    _rooms = [R078_BANDITS_WAY_AREA_04]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_STAR_CHEST
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 0 in room 78 has its object trigger disabled.


class BanditsWayPlatformsRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R078_BANDITS_WAY_AREA_04]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BANDITS_WAY_DOG_JUMP
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 1 in room 78 has its object trigger disabled.


class BanditsWayDeadEndChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BANDITS_WAY_CROCO
    _world_area = WorldAreaEnum.BANDITS_WAY
    _blacklist = [
        EXPStarPrize,
        SlotsPrize,
        SecondMimicFightLauncher,
        ThirdMimicFightLauncher,
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: npc 0 in room 206 has its object trigger disabled.


class BanditsWayBossFight(BossFightLocation):
    _bias = True
    _originally_held = Croco1BossFight
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.BANDITS_WAY_BOSS_FIGHT
    _world_area = WorldAreaEnum.BANDITS_WAY
    _pack_id = PACK163_BANDITS_WAY_BOSS
    _post_unlocks_event_id = E1196_MUSHROOM_KINGDOM_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R076_BANDITS_WAY_AREA_01,
            NPC_5,
            sequence_setter_event_id=E0757_BANDITS_WAY_AREA_01_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R207_BANDITS_WAY_AREA_02,
            NPC_8,
            sequence_setter_event_id=E0756_BANDITS_WAY_AREA_02_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R077_BANDITS_WAY_AREA_03,
            NPC_8,
            sequence_setter_event_id=E0758_BANDITS_WAY_AREA_03_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R078_BANDITS_WAY_AREA_04,
            NPC_12,
            sequence_setter_event_id=E0759_BANDITS_WAY_AREA_04_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R206_BANDITS_WAY_AREA_05,
            NPC_8,
            sequence_setter_event_id=E0760_BANDITS_WAY_AREA_05_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R505_ENDING_CREDITS_YOSTER_ISLE_CROCO_RACING_YOSHI,
            NPC_10,
            sequence_setter_event_id=E1193_ENDING_CREDITS_YOSTER_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def render(self, world: GameWorld):
        """Set animation scripts for this boss to be more specific for the character"""
        assert isinstance(self.prize, BossFightPrize)
        w = super().render(world)
        render_bandits_way_boss(world, self.prize)
        return w

    # Flag as checked: BANDITS_WAY_LIBERATED


class BanditsWayStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.BANDITS_WAY_STAR_PIECE
    _world_area = WorldAreaEnum.BANDITS_WAY
    _parent = BanditsWayBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_bandits_way(
            world, inventory
        )

    # Flag as checked: BANDITS_WAY_LIBERATED


class BanditsWayBossFirstItemDropLocation(NPCLocationRow1, KeyItemLocation):
    _bias = True
    _originally_held = RareFrogCoinPrize
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.CROCO_1_REWARD
    _world_area = WorldAreaEnum.BANDITS_WAY

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: BANDITS_WAY_LIBERATED set


class BanditsWayBossSecondItemDropLocation(NPCLocationRow2, KeyItemLocation):
    _bias = True
    _originally_held = WalletPrize
    _rooms = [R206_BANDITS_WAY_AREA_05]
    _id = ShuffleLocationSelector.CROCO_1_REWARD_2
    _world_area = WorldAreaEnum.BANDITS_WAY

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    # Flag as checked: BANDITS_WAY_LIBERATED set (checked at same time as BanditsWayBossSecondItemDropLocation)


########## kero sewers


class KeroSewersStairRoomLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_PANDORITE_ROOM
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: npc 0 in room 60 has its object trigger disabled.


class KeroSewersStairRoomRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FirstMimicFightLauncher
    _rooms = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PANDORITE_CHEST
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: npc 1 in room 60 has its object trigger disabled.


class Mimic1BossFight(BossFightLocation):
    _bias = True
    _originally_held = PandoriteBossFight
    _rooms = [512]  # can be in any room.
    _override_id = 512
    _id = ShuffleLocationSelector.PANDORITE_BOSS_FIGHT
    _world_area = WorldAreaEnum.KERO_SEWERS
    _pack_id = PACK156_SEWER_CHEST_FIGHT
    _post_unlocks_event_id = E1249_MIMIC_1_BOSS_UNLOCKS

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(FirstMimicFightLauncher)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    # Flag as checked: MIMIC_1_CLEARED


class Mimic1DropRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = TrueformPinPrize
    _rooms = [512]  # can be in any room, custom id.
    _id = ShuffleLocationSelector.PANDORITE_REWARD_1
    _world_area = WorldAreaEnum.KERO_SEWERS
    _override_id = 512

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(FirstMimicFightLauncher)

    # flag as checked: MIMIC_1_CLEARED


class Mimic1StarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [512]  # can be in any room.
    _override_id = 512
    _id = ShuffleLocationSelector.PANDORITE_BOSS
    _world_area = WorldAreaEnum.KERO_SEWERS
    _parent = Mimic1BossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and inventory.has_item(
            FirstMimicFightLauncher
        )

    # Flag as checked: MIMIC_1_CLEARED


class Mimic1ReloadRewardLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = Coins50Prize
    _rooms: list[int] = []  # Dynamic room, handled by mimic system
    _npc_ids: list[AreaObject] = []  # No specific NPC
    _id = ShuffleLocationSelector.PANDORITE_REWARD_2
    _world_area = WorldAreaEnum.KERO_SEWERS
    _override_id = 512
    # FirstMimicFightLauncher must be blacklisted to prevent circular dependency:
    # This location's can_access requires defeating first mimic, which requires
    # accessing the FirstMimicFightLauncher location - can't be the same location.
    _blacklist = [EXPStarPrize, SlotsPrize, MimicFightInitiatorPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(FirstMimicFightLauncher)

    def grant(self) -> EventScript:
        # Mimic rewards don't need room-specific chest disable commands
        if self.prize is None:
            return EventScript([Return()])
        return EventScript(
            [] if self.prize.chest_grant is None else self.prize.chest_grant.contents
        )

    # flag as checked: the host chest for FirstMimicFightLauncher has its object trigger disabled


class KeroSewersFourRatRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KeroSewersStarPrize
    _rooms = [R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_STAR_CHEST
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: npc 0 in room 59 has its object trigger disabled.


class KeroSewersBeforeBelomeLowerLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_LOWER
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: npc 0 in room 301 has its object trigger disabled.


class KeroSewersBeforeBelomeUpperBeforeFlipLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_UPPER_1
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    # flag as checked: SEWER_CHEST_FIRST_PRIZE_OBTAINED


class KeroSewersBeforeBelomeUpperAfterFlipLocation(
    KeyItemLocation, TreasureChestLocationRow3
):
    _originally_held = CricketJamPrize
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.KERO_SEWERS_BEFORE_BELOME_UPPER_2
    _world_area = WorldAreaEnum.KERO_SEWERS
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: SEWERS_FLIPPED_CHEST_OPENED


class KeroSewersBossFight(BossFightLocation):
    _bias = True
    _originally_held = Belome1BossFight
    _rooms = [R302_KERO_SEWERS_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.KERO_SEWERS_BOSS
    _world_area = WorldAreaEnum.KERO_SEWERS
    _pack_id = PACK168_SEWER_BOSS
    _post_unlocks_event_id = E1197_KERO_SEWER_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R302_KERO_SEWERS_AREA_08_BELOMES_ROOM,
            NPC_1,
            sequence_setter_event_id=E0772_KERO_SEWERS_BELOME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sewer(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.FOREST):
            content.extend(
                [
                    ClearBit(PIPE_VAULT_GATED),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: SEWER_BOSS_DEFEATED


class KeroSewersStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _id = ShuffleLocationSelector.KERO_SEWERS_STAR_PIECE
    _world_area = WorldAreaEnum.KERO_SEWERS
    _parent = KeroSewersBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_sewer(
            world, inventory
        )

    # Flag as checked: SEWER_BOSS_DEFEATED


########## Midas River


class MidasRiverFirstCompletionRewardLocation(NPCLocationRow1):
    _originally_held = NokNokShellPrize
    _rooms = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _id = ShuffleLocationSelector.MIDAS_RIVER_FIRST_TIME
    _world_area = WorldAreaEnum.MIDAS_RIVER
    # Flag as checked: MIDAS_RIVER_FIRST_VISIT_PRIZE_RECEIVED


class MidasRiverBottomLeftCaveLocation(RiverLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_LEFT_CAVE
    _world_area = WorldAreaEnum.MIDAS_RIVER
    # Flag as checked: MIDAS_RIVER_TUNNEL_3_PRIZE


class MidasRiverBottomRightCaveLocation(RiverLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.MIDAS_RIVER_BOTTOM_RIGHT_CAVE
    _world_area = WorldAreaEnum.MIDAS_RIVER
    # Flag as checked: MIDAS_RIVER_TUNNEL_4_PRIZE


########## tadpole pond


class TadpolePondCricketPieExchangeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FroggiestickPrize
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _id = ShuffleLocationSelector.CRICKET_PIE_REWARD
    _world_area = WorldAreaEnum.TADPOLE_POND
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(CricketPiePrize)

    # Flag as checked: CRICKET_PIE_EXCHANGED


class TadpolePondCricketJamExchangeLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FrogCoin10Prize
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _id = ShuffleLocationSelector.CRICKET_JAM_REWARD
    _world_area = WorldAreaEnum.TADPOLE_POND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(CricketPiePrize) and inventory.has_item(
            CricketJamPrize
        )

    # Flag as checked: CRICKET_JAM_EXCHANGED


class MelodyBayFirstRewardLocation(NPCLocationRow1, KeyItemLocation):
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_1
    _world_area = WorldAreaEnum.TADPOLE_POND
    # Flag as checked: MELODY_BAY_ITEM_1_GRANTED


class MelodyBaySecondRewardLocation(NPCLocationRow2, KeyItemLocation):
    _bias = True
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_2
    _world_area = WorldAreaEnum.TADPOLE_POND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    # Flag as checked: MELODY_BAY_ITEM_2_GRANTED


class MelodyBayThirdRewardLocation(NPCLocationRow3, KeyItemLocation):
    _bias = True
    _originally_held = ProgressiveCardPrize
    _rooms = [R074_TADPOLE_POND_AREA_02]
    _id = ShuffleLocationSelector.MELODY_BAY_3
    _world_area = WorldAreaEnum.TADPOLE_POND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_clear_mines(world, inventory)
            and can_access_temple_boss(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: MELODY_BAY_ITEM_3_GRANTED


########## rose way


class RoseWaySwingingPlatformRoomLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.ROSE_WAY_PLATFORM
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 0 in room 80 has its object trigger disabled.


class RoseWayLeftIslandLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.ROSE_WAY_FLOWER
    _world_area = WorldAreaEnum.ROSE_WAY
    # Flag as checked: npc 7 in room 79 has been removed from the room.


class RoseWayMiddleIslandLocation(StandingLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.ROSE_WAY_MUSHROOM
    _world_area = WorldAreaEnum.ROSE_WAY
    # Flag as checked: npc 8 in room 79 has been removed from the room.


class RoseWayCoin1Location(StandingLocationRow7):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_18]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_1
    _world_area = WorldAreaEnum.ROSE_WAY
    # Flag as checked: npc 17 in room 79 has been removed from the room.


class RoseWayCoin2Location(StandingLocationRow6):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_19]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_2
    _world_area = WorldAreaEnum.ROSE_WAY
    # Flag as checked: npc 18 in room 79 has been removed from the room.


class RoseWayCoin3Location(StandingLocationRow5):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_20]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_3
    _world_area = WorldAreaEnum.ROSE_WAY
    # Flag as checked: npc 19 in room 79 has been removed from the room


class RoseWayCoin4Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_21]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_4
    _world_area = WorldAreaEnum.ROSE_WAY
    # Flag as checked: npc 20 in room 79 has been removed from the room


class RoseWayCoin5Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R079_ROSE_WAY_MAIN_AREA]
    _npc_ids = [NPC_22]
    _id = ShuffleLocationSelector.ROSE_WAY_COIN_5
    _world_area = WorldAreaEnum.ROSE_WAY
    # Flag as checked: npc 21 in room 79 has been removed from the room


class RoseWayFiveChestRoomTopLocation(TreasureChestLocationRow1):
    _originally_held = RecoveryMushroomPrize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_1
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 0 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomBottomLeftLocation(TreasureChestLocationRow2):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_2
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 1 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomRightLocation(TreasureChestLocationRow3):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_3
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 2 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomLeftLocation(TreasureChestLocationRow4):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_4
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 3 in room 81 has its object trigger disabled.


class RoseWayFiveChestRoomBottomRightLocation(TreasureChestLocationRow5):
    _originally_held = Coins5Prize
    _rooms = [R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.ROSE_WAY_FIVE_CHESTS_5
    _world_area = WorldAreaEnum.ROSE_WAY
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 4 in room 81 has its object trigger disabled.


########### rose town


class RoseTownShopLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.ROSE_TOWN_STORE_2
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 4 in room 87 has its object trigger disabled.


class RoseTownShopRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R087_ROSE_TOWN_ITEM_SHOP]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.ROSE_TOWN_STORE_1
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 5 in room 87 has its object trigger disabled.


class RoseTownCloudRightChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LazyShellArmorPrize
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.GARDENER_CLOUD_1
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize]
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            inventory.has_item(SeedPrize)
            and inventory.has_item(FertilizerPrize)
            and can_clear_mines(world, inventory)
            and can_clear_forest(world, inventory)
        )

    # Flag as checked: npc 0 in room 419 has its object trigger disabled.


class RoseTownCloudLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = LazyShellWeaponPrize
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.GARDENER_CLOUD_2
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize]
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            inventory.has_item(SeedPrize)
            and inventory.has_item(FertilizerPrize)
            and can_clear_mines(world, inventory)
            and can_clear_forest(world, inventory)
        )

    # Flag as checked: npc 1 in room 419 has its object trigger disabled.


class RoseTownInnToadPrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [
        R095_ROSE_TOWN_DURING_BOWYER_INN_2F,
        R096_ROSE_TOWN_INN_2F,
    ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TOAD
    _world_area = WorldAreaEnum.ROSE_TOWN
    # Flag as checked:  ROSE_TOWN_TOAD


class RoseTownInnGazPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FingerShotPrize
    _rooms = [R086_ROSE_TOWN_INN_1F]
    _id = ShuffleLocationSelector.GAZ
    _world_area = WorldAreaEnum.ROSE_TOWN

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_forest(world, inventory)

    # Flag as checked: ROSE_TOWN_GAZ_ITEM_GRANTED


class RoseTownTreasureHouseLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_1
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 0 in room 93 or 94 has its object trigger disabled.


class RoseTownTreasureHouseRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_2
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 1 in room 93 or 94 has its object trigger disabled.


class RoseTownTreasureHouseMazeRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
        R094_ROSE_TOWN_TREASURE_HOUSE_1F,
    ]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_MAZE_REWARD
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: TREASURE_HUNTER_HOUSE_PRIZE


class RoseTownTreasureHouseUpperChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [
        R097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F,
        R098_ROSE_TOWN_TREASURE_HOUSE_2F,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.ROSE_TOWN_TREASURE_HOUSE_3
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # Flag as checked: npc 1 in room 97 or 98 has its object trigger disabled.


########## forest maze


class ForestMazeFirstRoomLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R224_FOREST_MAZE_AREA_01]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_1
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 2 in room 224 has its object trigger disabled.


class ForestMazeFirstUndergroundExitLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R228_FOREST_MAZE_AREA_04]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_2
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 2 in room 228 has its object trigger disabled.


class ForestMazeUndergroundWigglerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_1
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 2 in room 242 has its object trigger disabled.


class ForestMazeUndergroundBottomRightTrunkChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_2
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 3 in room 242 has its object trigger disabled.


class ForestMazeUndergroundMiddleLeftChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = EmptyPrize
    _rooms = [R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_UNDERGROUND_3
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 4 in room 242 has its object trigger disabled.


class ForestMazeInnerMazeEntranceLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_RED_ESSENCE
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 4 in room 227 has its object trigger disabled.


class ForestMazeSecretTopRightChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_1
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 1 in room 234 has its object trigger disabled.


class ForestMazeSecretBottomRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_2
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 2 in room 234 has its object trigger disabled.


class ForestMazeSecretTopMiddleChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_3
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 3 in room 234 has its object trigger disabled.


class ForestMazeSecretBottomMiddleChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_4
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 4 in room 234 has its object trigger disabled.


class ForestMazeSecretLeftChestLocation(TreasureChestLocationRow5):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R234_FOREST_MAZE_SECRET]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.FOREST_MAZE_SECRET_5
    _world_area = WorldAreaEnum.FOREST_MAZE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_forest(world, inventory)

    # Flag as checked: npc 5 in room 234 has its object trigger disabled.


class ForestMazeBossFight(BossFightLocation):
    _bias = True
    _originally_held = BowyerBossFight
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_BOSS
    _world_area = WorldAreaEnum.FOREST_MAZE
    _pack_id = PACK181_FOREST_BOSS
    _post_unlocks_event_id = E1198_FOREST_MAZE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
            NPC_11,
            sequence_setter_event_id=E0775_FOREST_MAZE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_1]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_7]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_3]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_9]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_4]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_5]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_2]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_8]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_0]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_6]),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_forest(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.FOREST):
            content.extend(
                [
                    ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        if self._character_henchman_slots is None:
            return

        # Build a lookup of slot -> henchman for quick access
        assignment_map: dict[BossFightLocationHenchmanNPC, BossFightHenchman] = {
            slot: henchman for slot, henchman in henchmen_assignments
        }

        removed_ctr = 0

        # Loop through ALL character henchman slots, not just assigned ones
        for slot in self._character_henchman_slots:
            henchman = assignment_map.get(slot)
            for npc_id, room_id in zip(slot.npc_ids, slot.room_ids):
                # Check if this slot was assigned
                if henchman is not None:
                    npc_base = henchman.model().base
                    set_npc_direction_if_swse_only(
                        world, room_id, npc_id, npc_base, SOUTHEAST
                    )
                else:
                    # Slot was not assigned - hide the NPC with default sprite
                    if not isinstance(
                        self.prize, self._originally_held  # pyright: ignore
                    ):
                        removed_ctr += 1
                        rm = world.rooms._rooms[room_id]
                        assert rm is not None
                        rm.get_npc_by_target_id(npc_id).set_visible(False)
                        world.event_scripts.delete_command_by_identifier(
                            f"forest_henchman_{npc_id}"
                        )
        if removed_ctr == 10:
            world.event_scripts.delete_command_by_identifier(
                "forest_henchmen_bounce_30"
            )

    # Flag as checked: FOREST_LIBERATED


class ForestMazeStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece2
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_STAR_PIECE
    _world_area = WorldAreaEnum.FOREST_MAZE
    _parent = ForestMazeBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_forest(
            world, inventory
        )

    # Flag as checked: FOREST_LIBERATED


class ForestMazeCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = GenoRecruitmentPrize
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_CHARACTER
    _world_area = WorldAreaEnum.FOREST_MAZE
    _container_event = E1226_FOREST_MAZE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            NPC_11,
        ),
        AllyNPCSub(
            R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
            NPC_12,
        ),
        AllyNPCSub(
            R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
            NPC_10,
        ),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(6)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_forest(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.prize is None:
            render_forest_maze_character_empty(world)
        else:
            render_forest_maze_character(world, cast(CharacterPrize, self.prize))
        return op

    # Flag as checked: FOREST_LIBERATED


class GenoSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = GenoBeamSpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize)


class GenoSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = GenoBoostSpellPrize
    _level = 8

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize)


class GenoSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = GenoWhirlSpellPrize
    _level = 11

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize)


class GenoSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = GenoBlastSpellPrize
    _level = 14

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class GenoSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = GenoFlashSpellPrize
    _level = 17

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class GenoSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = None
    _level = 19

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(GenoRecruitmentPrize) and not_earlygame(
            world, inventory
        )


########## pipe vault


class PipeVaultSlidingCoinRoomBackChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_1
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 8 in room 125 has its object trigger disabled.


class PipeVaultSlidingCoinRoomMiddleChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_2
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 9 in room 125 has its object trigger disabled.


class PipeVaultSlidingCoinRoomFrontChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_3
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 10 in room 125 has its object trigger disabled.


class PipeVaultSlidingCoinRoomCoin1Location(StandingLocationRow5):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_1
    _world_area = WorldAreaEnum.PIPE_VAULT

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_1


class PipeVaultSlidingCoinRoomCoin2Location(StandingLocationRow4):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_2
    _world_area = WorldAreaEnum.PIPE_VAULT

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 1 in room 125 has been removed from the room.


class PipeVaultSlidingCoinRoomCoin3Location(StandingLocationRow3):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_3
    _world_area = WorldAreaEnum.PIPE_VAULT

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 2 in room 125 has been removed from the room


class PipeVaultSlidingCoinRoomCoin4Location(StandingLocationRow2):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_4
    _world_area = WorldAreaEnum.PIPE_VAULT

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 3 in room 125 has been removed from the room


class PipeVaultSlidingCoinRoomCoin5Location(StandingLocationRow1):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_COIN_5
    _world_area = WorldAreaEnum.PIPE_VAULT

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 4 in room 125 has been removed from the room


class PipeVaultSlidingCoinRoomCrouchItemLocation(StandingLocationRow6):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.PIPE_VAULT_SLIDE_FROG_COIN
    _world_area = WorldAreaEnum.PIPE_VAULT

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 5 in room 125 has been removed from the room.


class PipeVaultGoombaThumpinFirstPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _id = ShuffleLocationSelector.GOOMBA_THUMPING_1
    _world_area = WorldAreaEnum.PIPE_VAULT

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: GOOMBA_THUMPING_1


class PipeVaultGoombaThumpinSecondPrizeLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerJarPrize
    _rooms = [R143_PIPE_VAULT_GOOMBATHUMPING_ROOM]
    _id = ShuffleLocationSelector.GOOMBA_THUMPING_2
    _world_area = WorldAreaEnum.PIPE_VAULT

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: GOOMBA_THUMPING_2


class PipeVaultRisingPlatformChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_1
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 0 in room 128 has its object trigger disabled.


class PipeVaultChompweedChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = Coins20Prize
    _rooms = [R128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.PIPE_VAULT_NIPPERS_2
    _world_area = WorldAreaEnum.PIPE_VAULT
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # flag as checked: npc 1 in room 128 has its object trigger disabled.


########### yoster isle


class YosterEntranceChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.YOSTER_ISLE_ENTRANCE
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # Flag as checked: npc 1 in room 33 has its object trigger disabled.


class YosterRacePrize1Location(NPCLocationRow1):
    _bias = True
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_1
    _world_area = WorldAreaEnum.YOSTER_ISLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # Flag as checked: COMPLETED_MUSHROOM_DERBY


class YosterRacePrize2Location(NPCLocationRow3):
    _bias = True
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_2
    _world_area = WorldAreaEnum.YOSTER_ISLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # Flag as checked: COMPLETED_MUSHROOM_DERBY


class YosterRacePrize3Location(NPCLocationRow4):
    _bias = True
    _originally_held = YoshiCookiePrize
    _rooms = [R034_YOSTER_ISLE]
    _id = ShuffleLocationSelector.YOSTER_ISLE_RACE_REWARD_3
    _world_area = WorldAreaEnum.YOSTER_ISLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory)

    # Flag as checked: COMPLETED_MUSHROOM_DERBY


########## moleville


class TreasureShopItem1(TreasureShopLocation, NPCLocationRow1):
    _bias = True
    _originally_held = LuckyJewelPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_1
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    # Flag as checked: TREASURE_SHOP_ITEM_1_PURCHASED


class TreasureShopItem2(TreasureShopLocation, NPCLocationRow2):
    _bias = True
    _originally_held = ProgressiveEggPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_2
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and can_clear_seaside_boss(
            world, inventory
        )

    # Flag as checked: TREASURE_SHOP_ITEM_2_PURCHASED


class TreasureShopItem3(TreasureShopLocation, NPCLocationRow3):
    _bias = True
    _originally_held = FryingPanPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_3
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and can_clear_volcano(world, inventory)

    # Flag as checked: TREASURE_SHOP_ITEM_3_PURCHASED


class FireworksShopItemLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = RegularFireworksPrize
    _rooms = [R339_MOLEVILLE_FIREWORKS_SHOP]
    _id = ShuffleLocationSelector.FIREWORKS_SHOP
    _world_area = WorldAreaEnum.MOLEVILLE

    def key(self, world: GameWorld) -> bool:
        return not world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.VANILLA
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    # Flag as checked: FIREWORKS_HOUSE_ITEM_SOLD
    # not a check if progressive fireworks is turned off


class PurtendStoreLocation(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = ProgressiveFireworksPrize
    _rooms = [R108_MOLEVILLE_OUTSIDE]
    _id = ShuffleLocationSelector.PURTEND_STORE
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and inventory.has_item_count(
            ProgressiveFireworksPrize, 1
        )

    # flag as checked: PURTEND_STORE_CHECK_DONE
    # not a check if progressive fireworks turned off


class CookieTraderLocation(KeyItemLocation, NPCLocationRow4):
    _bias = True
    _originally_held = ProgressiveFireworksPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.COOKIE_TRADER
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and inventory.has_item_count(
            ProgressiveFireworksPrize, 2
        )

    # flag as checked: COOKIE_TRADER_CHECKED
    # not a check if progressive fireworks turned off


class BucketGirlRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R108_MOLEVILLE_OUTSIDE]
    _id = ShuffleLocationSelector.BUCKET_GIRL
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        if not can_clear_mines(world, inventory):
            return False
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
            return inventory.has_item_count(ProgressiveFireworksPrize, 3)
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
            return inventory.has_item(RegularFireworksPrize)
        else:
            return True

    # Flag as checked: CARBO_COOKIE_GIVEN


class OuterMinesTrampolineHenchmanLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_1
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # Flag as checked: NPC 1 invisible in room 273


class OuterMinesLeftHenchmanLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_2
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # Flag as checked: NPC 1 invisible in room 277


class OuterMinesRightHenchmanLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    _id = ShuffleLocationSelector.CROCO_FLUNKIE_3
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # Flag as checked: NPC 1 invisible in room 283


class OuterMinesBossFight(BossFightLocation):
    _bias = True
    _originally_held = Croco2BossFight
    _rooms = [
        R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
        R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
        R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
        R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
        R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
        R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    ]
    _override_id = 518
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _pack_id = PACK164_MINES_FIRST_BOSS
    _post_unlocks_event_id = E1199_OUTER_MNES_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
            NPC_0,
            sequence_setter_event_id=E0777_MINES_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
            NPC_0,
            sequence_setter_event_id=E0779_MINES_LEFT_OF_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
            NPC_0,
            sequence_setter_event_id=E0781_MINES_TINY_ROOM_2_LEFT_OF_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
            NPC_0,
            sequence_setter_event_id=E0783_MINES_ROOM_THAT_SPLITS_TO_PA_MOLE_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
            NPC_0,
            sequence_setter_event_id=E0785_MINES_SMALL_NORTH_ROOM_IN_MINIBOSS_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
            NPC_0,
            sequence_setter_event_id=E0787_MINES_LONG_ROOM_IN_MINIBOSS_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE],
            [NPC_1],
            PACK142_MINES_HENCHMAN_MIDDLE,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM],
            [NPC_1],
            PACK141_MINES_HENCHMAN_LEFT,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM],
            [NPC_1],
            PACK079_MINES_HENCHMAN_RIGHT,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # Flag as checked: MINES_BOSS_1_DEFEATED


class OuterMinesStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [518]
    _override_id = 518
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _parent = OuterMinesBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_moleville_entrance(
            world, inventory
        )

    # Flag as checked: MINES_BOSS_1_DEFEATED


class OuterMinesBossPrizeLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = BambinoBombPrize
    _id = ShuffleLocationSelector.CROCO_2_ITEM
    _world_area = WorldAreaEnum.MOLEVILLE
    _rooms = [
        R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
        R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
        R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
        R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
        R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
        R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)

    # flag as checked: MINES_BOSS_1_DEFEATED


class InnerMinesTracksChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = MolevilleMinesStarPrize
    _rooms = [R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_STAR_CHEST
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: npc 0 in room 285 has its object trigger disabled.


class InnerMinesShyguyCartLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_SHY_GUY
    _world_area = WorldAreaEnum.MOLEVILLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: RUNAWAY_MINECART_ITEM_OBTAINED


class InnerMinesBoxesChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [R280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_COINS
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: npc 0 in room 280 has its object trigger disabled.


class InnerMinesSaveBlockChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: npc 0 in room 288 has its object trigger disabled.


class InnerMinesHighUpChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_PUNCHINELLO_2
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)

    # Flag as checked: npc 1 in room 288 has its object trigger disabled.


class InnerMinesBossFight(BossFightLocation):
    _bias = True
    _originally_held = PunchinelloBossFight
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT
    _world_area = WorldAreaEnum.MOLEVILLE
    _pack_id = PACK140_MINES_BOSS_2
    _post_unlocks_event_id = E1200_INNER_MINES_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            NPC_0,
            sequence_setter_event_id=E0788_MINES_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            ],
            [NPC_4, NPC_5, NPC_6],
            PACK152_MINES_BOSS_ROOM_HENCHMAN,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [
                R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER,
            ],
            [NPC_1],
        ),
    ]
    _tiny_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            ],
            [NPC_1, NPC_2, NPC_3],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MINES):
            content.extend(
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
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        # Check if any tiny henchman slots were assigned
        if self._tiny_henchman_slots is not None:
            assigned_slots = {slot for slot, _ in henchmen_assignments}
            for slot in self._tiny_henchman_slots:
                if slot in assigned_slots:
                    world.action_scripts.delete_command_by_identifier("microbomb_spark")
                    break

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        # Use VRAM-constrained selection (max 4096 for mines boss room)
        npc_model = self.prize.get_npc_for_slot(world, 4096)
        set_mines_punch_command(world, npc_model())
        return op

    # Flag as checked: MINES_BOSS_2_DEFEATED


class InnerMinesStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece3
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_2
    _world_area = WorldAreaEnum.MOLEVILLE
    _parent = InnerMinesBossFight
    # Flag as checked: MINES_BOSS_2_DEFEATED

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_mines(
            world, inventory
        )


class InnerMinesCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = BowserRecruitmentPrize
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_CHARACTER
    _world_area = WorldAreaEnum.MOLEVILLE
    _container_event = E1227_MOLEVILLE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM,
            NPC_1,
        ),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(8)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        # starters need to be set first
        return can_clear_mines(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )

    # Flag as checked: MINES_BOSS_2_DEFEATED


class BowserSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = TerrorizeSpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize)


class BowserSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = PoisonGasSpellPrize
    _level = 12

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize)


class BowserSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = CrusherSpellPrize
    _level = 15

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize)


class BowserSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = BowserCrushSpellPrize
    _level = 18

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class BowserSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = None
    _level = 20

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class BowserSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = None
    _level = 22

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BowserRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class InnerMinesPostgameBossFight(BossFightLocation):
    _bias = True
    _originally_held = Punchinello2BossFight
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _override_id = 527
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.MOLEVILLE
    _remake_only = True
    _pack_id = PACK071_MINES_POSTGAME
    _post_unlocks_event_id = E1253_POSTGAME_MINES_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE,
            NPC_0,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_postgame_boss(world, inventory)

    # Flag as checked: MINES_POSTGAME_COMPLETED


class InnerMinesPostgameStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _override_id = 527
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_3
    _world_area = WorldAreaEnum.MOLEVILLE
    _remake_only = True
    _parent = InnerMinesPostgameBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(
            inventory, world
        ) and can_access_moleville_postgame_boss(world, inventory)

    # Flag as checked: MINES_POSTGAME_COMPLETED


class InnerMinesPostgameDrop(NPCLocationRow1):
    _bias = True
    _originally_held = WonderChompPrize
    _rooms = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_POSTGAME_DROP
    _world_area = WorldAreaEnum.MOLEVILLE
    _remake_only = True
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_postgame_boss(world, inventory)

    # Flag as checked: MINES_POSTGAME_COMPLETED


########## booster pass


class BoosterPassBushLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _id = ShuffleLocationSelector.BOOSTER_PASS_BUSH
    _world_area = WorldAreaEnum.BOOSTER_PASS
    # flag as checked: BOOSTER_PASS_BUSH_ITEM_FOUND


class BoosterPassFirstRoomLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOOSTER_PASS_1
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # flag as checked: npc 8 in room 100 has its object trigger disabled.


class BoosterPassFirstRoomRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RockCandyPrize
    _rooms = [R100_BOOSTER_PASS_AREA_01]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_PASS_2
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # flag as checked: npc 9 in room 100 has its object trigger disabled.


class BoosterPassSecondRoomFlowerLocation(StandingLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R101_BOOSTER_PASS_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOOSTER_PASS_FLOWER
    _world_area = WorldAreaEnum.BOOSTER_PASS
    # flag as checked: npc 6 in room 101 has been removed from the room.


class BoosterPassSecretMiddleChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_1
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 10 in room 405 has its object trigger disabled.


class BoosterPassSecretRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_2
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 11 in room 405 has its object trigger disabled.


class BoosterPassSecretLeftChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R405_BOOSTER_PASS_SECRET]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOOSTER_PASS_SECRET_3
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 12 in room 405 has its object trigger disabled.


########## booster tower


class BoosterTowerSpookumStairsLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_SPOOKUM
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 6 in room 196 has its object trigger disabled.


class BoosterTowerTrainRoomCreviceLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_RAILWAY
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: NPC 1 removed from room 194


class BoosterTowerChestNearThwompLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_THWOMP
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 2 in room 36 has its object trigger disabled.


class BoosterTowerFallingChestLocation(
    NPCLocationRow1
):  # this looks like a chest, requires an overworld item, but acts like a npc reward
    _originally_held = MasherPrize
    _rooms = [R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_MASHER
    _container_event = E0253_NPC_QUEST_1_GRANT
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: TOWER_SEESAW_CHEST_OPENED


class BoosterTowerKnifeGuyPrizeLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = BrightCardPrize
    _rooms = [R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: KNIFE_GUY_PRIZE_GRANTED


# this check does not exist if FixKnifeGuy is disabled
class BoosterTowerKnifeGuy2PrizeLocation(NPCLocationRow2):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and world.settings.isflag_enabled(
            _get_flag("FixKnifeGuy")
        )

    # flag as checked: KNIFE_GUY_SECOND_PRIZE_AWARDED


class BoosterTowerPortraitPrizeLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = ElderKeyPrize
    _rooms = [R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PORTRAITS
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 7 in room 195 has been removed from the room
    # AND
    # PORTRAIT_GAME_COMPLETED is set


class BoosterTowerElderKeyItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = ChompPrize
    _rooms = [R200_BOOSTER_TOWER_6F_AREA_03_ELDERS_ROOM_WCHOMP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_CHOMP
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and inventory.has_item(ElderKeyPrize)

    # flag as checked: npc 0 in room 200 has been removed from the room.


class BoosterTowerParachuteRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 9 in room 35 has its object trigger disabled.


class BoosterTowerParachuteRoomCreviceLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_PARACHUTE_CREVICE
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: NPC 8 removed from room 35


class BoosterTowerCheckerboardRightmostItemLocation(
    KeyItemLocation, StandingLocationRow14
):
    _originally_held = RoomKeyPrize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ROOM_KEY
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 5 in room 41 has been removed from the room.


class BoosterTowerCheckerboardTopItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 0 in room 41 has been removed from the room.


class BoosterTowerCheckerboardLeftmostItemLocation(StandingLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 1 in room 41 has been removed from the room.


class BoosterTowerCheckerboardUpperRightItemLocation(StandingLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 2 in room 41 has been removed from the room.


class BoosterTowerCheckerboardBottomItemLocation(StandingLocationRow4):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_FROG_COIN_4
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 3 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin1Location(StandingLocationRow5):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 7 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin2Location(StandingLocationRow6):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 8 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin3Location(StandingLocationRow7):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 9 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin4Location(StandingLocationRow8):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_4
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 10 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin5Location(StandingLocationRow9):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_5
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 11 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin6Location(StandingLocationRow10):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_6
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 12 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin7Location(StandingLocationRow11):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_7
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 13 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin8Location(StandingLocationRow12):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_8
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 14 in room 41 has been removed from the room.


class BoosterTowerCheckerboardCoin9Location(StandingLocationRow13):
    _bias = True
    _originally_held = Coins1Prize
    _rooms = [
        R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS
    ]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_COIN_9
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 15 in room 41 has been removed from the room.


class BoosterTowerRoomKeyChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = ZoomShoesPrize
    _rooms = [R048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_ZOOM_SHOES
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and inventory.has_item(RoomKeyPrize)

    # flag as checked: npc 0 in room 48 has its object trigger disabled.


class BoosterTowerTopFloorLowerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 0 in room 199 has its object trigger disabled.


class BoosterTowerTopFloorUpperChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = GoodieBagPrize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 1 in room 199 has its object trigger disabled.


class BoosterTowerTopFloorCornerChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_TOP_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: npc 9 in room 199 has its object trigger disabled.


class BoosterTowerCurtainGamePrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = AmuletPrize
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_KNIFE_GUY
    _world_area = WorldAreaEnum.BOOSTER_TOWER

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory)

    # flag as checked: TOWER_BOSS_1_STAR_PIECE
    # will be granted regardless of whether they do curtain game or fight boss


class BoosterTowerIndoorBossFight(BossFightLocation):
    _bias = True
    _originally_held = BoosterBossFight
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _pack_id = PACK161_TOWER_FIRST_FIGHT
    _post_unlocks_event_id = E1201_TOWER_CURTAIN_BOSS_UNLOCKS
    _henchman_can_run_away = False
    _npc_slots = [
        BossFightLocationNPC(
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            NPC_0,
            sequence_setter_event_id=E0789_TOWER_CURTAIN_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_7,
            sequence_setter_event_id=E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            NPC_6,
            sequence_setter_event_id=E0791_TOWER_ANCESTOR_GAME_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS,
            NPC_6,
            sequence_setter_event_id=E0792_TOWER_FIRST_BOBOMB_STAIRCASE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R054_BOOSTER_HILL_DUMMY,
            NPC_7,
        ),
        BossFightLocationNPC(
            R202_BOOSTER_TOWER_ENTRANCE,
            NPC_1,
            sequence_setter_event_id=E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
            NPC_3,
            sequence_setter_event_id=E0797_TOWER_LOBBY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            NPC_3,
            sequence_setter_event_id=E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_10,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_4, NPC_1, NPC_0, NPC_3, NPC_0, NPC_2],
            PACK000_TOWER_HENCHMAN_1,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0053_HENCHMAN_CONTAINER_3,
        ),
        BossFightLocationHenchmanNPC(
            [
                R194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_0, NPC_2, NPC_1, NPC_4, NPC_1, NPC_1],
            PACK001_TOWER_HENCHMAN_2,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0054_HENCHMAN_CONTAINER_4,
        ),
        BossFightLocationHenchmanNPC(
            [
                R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS,
                R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                R054_BOOSTER_HILL_DUMMY,
                R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            ],
            [NPC_8, NPC_3, NPC_2, NPC_5, NPC_2, NPC_3],
            PACK054_TOWER_HENCHMAN_3,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            container_event=E0055_HENCHMAN_CONTAINER_5,
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_4]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_5]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_6]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_7]
        ),
        BossFightLocationHenchmanNPC(
            [R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA], [NPC_8]
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R405_BOOSTER_PASS_SECRET],
            [NPC_9],
            PACK032_TOWER_PASS_HENCHMAN,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        )
    ]
    _dialogs_expecting_replacement = [
        DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
        DI2560_TOWER_HENCHMAN_1,
        DI2572_TOWER_HENCHMAN_2,
        DI3072_TOWER_HENCHMAN_3_WINDOW,
        DI3073_TOWER_HENCHMAN_3
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and not_earlygame(world, inventory)

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.npc_slots and self.prize and self.prize.model:
            assert isinstance(self.prize, BossFightPrize)
            is_vanilla = isinstance(
                self.prize, (self._originally_held, Booster2BossFight)
            )
            render_booster_tower_indoor_boss(
                world, self.prize, self.npc_slots, is_vanilla
            )

            # Remove special snifit sprites that other henchmen don't have
            # Only if character henchman slots are assigned (KeepMinigameSpritesIntact not set)
            from ..types.flags import KeepMinigameSpritesIntact

            character_henchmen_assigned = (
                not world.settings.isflag_enabled(KeepMinigameSpritesIntact)
                and self.prize.character_henchmen is not None
                and len(self.prize.character_henchmen) >= 3
            )
            if character_henchmen_assigned:
                render_booster_tower_henchman_scripts(
                    world,
                    self.prize,
                    (
                        len(self.prize.character_henchmen)
                        if self.prize.character_henchmen
                        else 0
                    ),
                )

            # Only if mook henchman slot is assigned
            mook_henchmen_assigned = (
                not world.settings.isflag_enabled(KeepMinigameSpritesIntact)
                and self.prize.mook_henchmen is not None
                and len(self.prize.mook_henchmen) > 0
            )

        return op

    # Flag as checked: TOWER_BOSS_1_STAR_PIECE


class BoosterTowerIndoorStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _parent = BoosterTowerIndoorBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: TOWER_BOSS_1_STAR_PIECE


class BoosterTowerIndoorBossFightRemake(BossFightLocation):
    _bias = True
    _originally_held = Booster2BossFight
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _override_id = 528
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_3
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _remake_only = True
    _pack_id = PACK070_TOWER_POSTGAME
    _post_unlocks_event_id = E1202_POSTGAME_TOWER_CURTAIN_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            NPC_10,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower_postgame_boss(world, inventory)

    # Flag as checked: POSTGAME_TOWER_COMPLETED


class BoosterTowerIndoorStarPieceRemake(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _override_id = 528
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _remake_only = True
    _parent = BoosterTowerIndoorBossFightRemake

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower_postgame_boss(world, inventory)

    # Flag as checked: POSTGAME_TOWER_COMPLETED


class BoosterTowerRemakeBossFightPrizeLocation(NPCLocationRow2):
    _bias = True
    _originally_held = Stella023Prize
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_POSTGAME_DROP
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _remake_only = True
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower_postgame_boss(world, inventory)

    # Flag as checked: POSTGAME_TOWER_COMPLETED


class BoosterTowerBalconyBossFight(BossFightLocation):
    _bias = True
    _originally_held = KnifeGuyGrateGuyBossFight
    _rooms = [R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_BOSS_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _pack_id = PACK177_TOWER_SECOND_BOSS
    _post_unlocks_event_id = E1203_TOWER_BALCONY_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and not_earlygame(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.TOWER):
            content.extend([ClearBit(BOOSTER_HILL_CLOSED)])
        if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.TOWER):
            content.extend([SetBit(MARRYMORE_BACKDOOR_OPEN)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: TOWER_BOSS_2_DEFEATED


class BoosterTowerBalconyStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R202_BOOSTER_TOWER_ENTRANCE]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _parent = BoosterTowerBalconyBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: TOWER_BOSS_2_DEFEATED


########## booster hill


class BoosterHillGuaranteedItem1(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 0
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_1
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P038_BOOSTER_HILL_PRIZE_0,
        P069_BOOSTER_HILL_PRIZE_STANDING_0
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 0 to 1


class BoosterHillGuaranteedItem2(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 1
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_2
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P039_BOOSTER_HILL_PRIZE_1,
        P071_BOOSTER_HILL_PRIZE_STANDING_1
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 1 to 2


class BoosterHillGuaranteedItem3(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 2
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_3
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P041_BOOSTER_HILL_PRIZE_2,
        P072_BOOSTER_HILL_PRIZE_STANDING_2
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 2 to 3


class BoosterHillGuaranteedItem4(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 3
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_4
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P042_BOOSTER_HILL_PRIZE_3,
        P074_BOOSTER_HILL_PRIZE_STANDING_3,
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 3 to 4


class BoosterHillGuaranteedItem5(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 4
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_5
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P044_BOOSTER_HILL_PRIZE_4,
        P075_BOOSTER_HILL_PRIZE_STANDING_4,
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 4 to 5


class BoosterHillGuaranteedItem6(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 5
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_6
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P046_BOOSTER_HILL_PRIZE_5,
        P077_BOOSTER_HILL_PRIZE_STANDING_5
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 5 to 6


class BoosterHillGuaranteedItem7(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 6
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_7
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P057_BOOSTER_HILL_PRIZE_6,
        P078_BOOSTER_HILL_PRIZE_STANDING_6
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 6 to 7


class BoosterHillGuaranteedItem8(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 7
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_8
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P058_BOOSTER_HILL_PRIZE_7,
        P080_BOOSTER_HILL_PRIZE_STANDING_7
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 7 to 8


class BoosterHillGuaranteedItem9(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 8
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_9
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P059_BOOSTER_HILL_PRIZE_8,
        P081_BOOSTER_HILL_PRIZE_STANDING_8
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 8 to 9


class BoosterHillGuaranteedItem10(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 9
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_10
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P060_BOOSTER_HILL_PRIZE_9,
        P082_BOOSTER_HILL_PRIZE_STANDING_9
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 9 to 10


class BoosterHillGuaranteedItem11(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 10
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_11
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P061_BOOSTER_HILL_PRIZE_10,
        P083_BOOSTER_HILL_PRIZE_STANDING_10
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 10 to 11


class BoosterHillGuaranteedItem12(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 11
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_12
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P062_BOOSTER_HILL_PRIZE_11,
        P084_BOOSTER_HILL_PRIZE_STANDING_11
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 11 to 12


class BoosterHillGuaranteedItem13(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 12
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_13
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P063_BOOSTER_HILL_PRIZE_12,
        P085_BOOSTER_HILL_PRIZE_STANDING_12
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 12 to 13


class BoosterHillGuaranteedItem14(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 13
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_14
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P065_BOOSTER_HILL_PRIZE_13,
        P086_BOOSTER_HILL_PRIZE_STANDING_13
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 13 to 14


class BoosterHillGuaranteedItem15(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 14
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_15
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P066_BOOSTER_HILL_PRIZE_14,
        P087_BOOSTER_HILL_PRIZE_STANDING_14
    ]


    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 14 to 15


class BoosterHillGuaranteedItem16(StandingLocation, BoosterHillLocation):
    _bias = True
    _70B1_id = 15
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_16
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P068_BOOSTER_HILL_PRIZE_15,
        P088_BOOSTER_HILL_PRIZE_STANDING_15
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)

    # flag as checked $70B1 goes from 15 to 16


########## marrymore


class MarrymoreFirstSuitePrizeLocation(NPCLocationRow1):
    _originally_held = FlowerTabPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_1
    _world_area = WorldAreaEnum.MARRYMORE
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize1Threshold setting


class MarrymoreSecondSuitePrizeLocation(NPCLocationRow2):
    _originally_held = FlowerJarPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_2
    _world_area = WorldAreaEnum.MARRYMORE
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize2Threshold setting


class MarrymoreThirdSuitePrizeLocation(NPCLocationRow3):
    _originally_held = FrogCoin1Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_3
    _world_area = WorldAreaEnum.MARRYMORE
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize3Threshold setting


class MarrymoreFourthSuitePrizeLocation(NPCLocationRow4):
    _originally_held = FrogCoin2Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_4
    _world_area = WorldAreaEnum.MARRYMORE
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize4Threshold setting


class MarrymoreFifthSuitePrizeLocation(NPCLocationRow5):
    _originally_held = FrogCoin3Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_5
    _world_area = WorldAreaEnum.MARRYMORE
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize5Threshold setting


class MarrymoreSixthSuitePrizeLocation(NPCLocationRow6):
    _originally_held = FrogCoin20Prize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_PRIZE_6
    _world_area = WorldAreaEnum.MARRYMORE
    # flag as checked: MARRYMORE_SUITE_LEGAL_COUNT >= SuitePrize6Threshold setting
    # LMK if these need dedicated bits or if AP is able to figure out the threshold on its own


class MarrymoreBigTipLocation(NPCLocationRow7):
    _originally_held = FlowerBoxPrize
    _rooms = [R007_MARRYMORE_INN_1F]
    _id = ShuffleLocationSelector.MARRYMORE_BIG_TIP
    _world_area = WorldAreaEnum.MARRYMORE
    # flag as checked: MARRYMORE_MAJOR_TIP_GIVEN


class MarrymoreHotelChestLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R009_MARRYMORE_INN_REGULAR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MARRYMORE_INN
    _world_area = WorldAreaEnum.MARRYMORE
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    # flag as checked: npc 0 in room 9 has its object trigger disabled.


# These are really NPC grants but they need sprite replacements.
# Override container event
class MarrymoreSnifit1Location(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = BroochPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_1
    _world_area = WorldAreaEnum.MARRYMORE
    _container_event = E0253_NPC_QUEST_1_GRANT
    _npc_ids = [NPC_6]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)

    # flag as checked: CHAPEL_ITEM_1_RETRIEVED


class MarrymoreSnifit2Location(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = RingPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_2
    _world_area = WorldAreaEnum.MARRYMORE
    _container_event = E0252_NPC_QUEST_2_GRANT
    _npc_ids = [NPC_3]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)

    # flag as checked: CHAPEL_ITEM_2_RETRIEVED


class MarrymoreSnifit3Location(KeyItemLocation, NPCLocationRow3):
    _bias = True
    _originally_held = ShoesPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_3
    _world_area = WorldAreaEnum.MARRYMORE
    _container_event = E0251_NPC_QUEST_3_GRANT
    _npc_ids = [NPC_4]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)

    # flag as checked: CHAPEL_ITEM_3_RETRIEVED


class MarrymoreAltarHeadLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = CrownPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.MARRYMORE_ALTAR
    _world_area = WorldAreaEnum.MARRYMORE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)

    # flag as checked: npc 5 in room 154 has been removed from the room.


class MarrymoreBossFight(BossFightLocation):
    _bias = True
    _originally_held = BundtBossFight
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_BOSS_FIGHT
    _world_area = WorldAreaEnum.MARRYMORE
    _pack_id = PACK176_CHAPEL_BOSS
    _post_unlocks_event_id = E1204_CHAPEL_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R155_MARRYMORE_CHAPEL_KITCHEN,
            NPC_0,
            sequence_setter_event_id=E0796_MARRYMORE_KITCHEN_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_11,
            sequence_setter_event_id=E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R155_MARRYMORE_CHAPEL_KITCHEN,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            ],
            [NPC_1, NPC_9],
        ),
        BossFightLocationHenchmanNPC(
            [
                R155_MARRYMORE_CHAPEL_KITCHEN,
                R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            ],
            [NPC_2, NPC_10],
        ),
    ]
    _dialogs_expecting_replacement = [
        DI2061_HEAD_CHEF,
        DI2062_APPRENTICE_CHEF
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(SeaGate, SeaGating.MARRYMORE):
            content.extend(
                [
                    SetBit(MAP_SEA),
                    SetBit(MAP_DIRECTIONAL_SEASIDE_DOWN_SEA),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld):
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if (
            self.prize.character_henchmen is not None
            and len(self.prize.character_henchmen) >= 1
        ):
            render_marrymore_boss_henchmen(world, self.prize.character_henchmen)
        return op

    # Flag as checked: MARRYMORE_LIBERATED


class MarrymoreBossFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_STAR_PIECE
    _world_area = WorldAreaEnum.MARRYMORE
    _parent = MarrymoreBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory)

    # Flag as checked: MARRYMORE_LIBERATED


class MarrymoreCharacter(CharacterRecruitmentLocation):
    _bias = True
    _originally_held = ToadstoolRecruitmentPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_CHARACTER
    _world_area = WorldAreaEnum.MARRYMORE
    _container_event = E1228_MARRYMORE_CHARACTER
    _show_dialog: bool = True

    _npc_fills = [
        AllyNPCSub(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_8,
        ),
        AllyNPCSub(
            R054_BOOSTER_HILL_DUMMY,
            NPC_8,
        ),
    ]

    def set_prize(self, prize: Prize | None):
        assert isinstance(prize, CharacterPrize) or prize is None
        if isinstance(prize, CharacterPrize):
            prize.set_starting_level(9)
        return super().set_prize(prize)

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory) and is_all_starting_chars_set(
            world, inventory
        )

    def render(self, world: GameWorld):
        op = super().render(world)
        if self.prize is None:
            render_marrymore_character_empty(world)
        return op

    # Flag as checked: MARRYMORE_LIBERATED


class ToadstoolSpell1(SpellSlotLocation):
    _bias = True
    _originally_held = TherapySpellPrize
    _level = 1

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize)


class ToadstoolSpell2(SpellSlotLocation):
    _bias = True
    _originally_held = GroupHugSpellPrize
    _level = 6

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize)


class ToadstoolSpell3(SpellSlotLocation):
    _bias = True
    _originally_held = SleepyTimeSpellPrize
    _level = 11

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize)


class ToadstoolSpell4(SpellSlotLocation):
    _bias = True
    _originally_held = ComeBackSpellPrize
    _level = 13

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class ToadstoolSpell5(SpellSlotLocation):
    _bias = True
    _originally_held = MuteSpellPrize
    _level = 15

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class ToadstoolSpell6(SpellSlotLocation):
    _bias = True
    _originally_held = PsychBombSpellPrize
    _level = 18

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ToadstoolRecruitmentPrize) and not_earlygame(
            world, inventory
        )


class MarrymoreBossFightRemake(BossFightLocation):
    _bias = True
    _originally_held = Bundt2BossFight
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_BOSS_FIGHT
    _world_area = WorldAreaEnum.MARRYMORE
    _override_id = 529
    _remake_only = True
    _pack_id = PACK078_CHAPEL_POSTGAME
    _post_unlocks_event_id = E1204_CHAPEL_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            NPC_12,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel_postgame_boss(world, inventory)

    # Flag as checked: POSTGAME_CHAPEL_COMPLETE


class MarrymoreBossFightStarPieceRemake(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_STAR_PIECE
    _world_area = WorldAreaEnum.MARRYMORE
    _override_id = 529
    _remake_only = True
    _parent = MarrymoreBossFightRemake

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_chapel_postgame_boss(
            world, inventory
        )

    # Flag as checked: POSTGAME_CHAPEL_COMPLETE


class MarrymoreBossFightRemakeItemDrop(NPCLocationRow4):
    _bias = True
    _originally_held = EnduringBroochPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _id = ShuffleLocationSelector.MARRYMORE_POSTGAME_ITEM_DROP
    _world_area = WorldAreaEnum.MARRYMORE
    _remake_only = True
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel_postgame_boss(world, inventory)

    # flag as checked: POSTGAME_CHAPEL_COMPLETE


########### star hill


class StarHillStarPiece(StarPieceLocation):
    _originally_held = StarPiece4
    _rooms = [R159_STAR_HILL_AREA_04]
    _id = ShuffleLocationSelector.STAR_HILL_STAR_PIECE_1
    _world_area = WorldAreaEnum.STAR_HILL
    # Flag as checked (send item, which i guess we can't do yet with SP checks):  NPC 9 removed from room and STAR_HILL_CHECKED
    # Flag as checked (tracker): STAR_HILL_CHECKED


########### seaside town pre-liberation


class FrogDiscipleLocation1(FrogDiscipleLocation):
    _originally_held = SeeYaPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_1
    _world_area = WorldAreaEnum.TADPOLE_POND
    # flag as checked: FROG_DISCIPLE_ITEM_1_PURCHASED


class FrogDiscipleLocation2(FrogDiscipleLocation):
    _originally_held = EarlierTimesPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_2
    _world_area = WorldAreaEnum.TADPOLE_POND
    # flag as checked: FROG_DISCIPLE_ITEM_2_PURCHASED


class FrogDiscipleLocation3(FrogDiscipleLocation):
    _originally_held = ExpBoosterPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_3
    _world_area = WorldAreaEnum.TADPOLE_POND
    # flag as checked: FROG_DISCIPLE_ITEM_3_PURCHASED


class FrogDiscipleLocation4(FrogDiscipleLocation):
    _originally_held = CoinTrickPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_4
    _world_area = WorldAreaEnum.TADPOLE_POND
    # flag as checked: FROG_DISCIPLE_ITEM_4_PURCHASED


class FrogDiscipleLocation5(FrogDiscipleLocation):
    _originally_held = ScroogeRingPrize
    _id = ShuffleLocationSelector.FROG_DISCIPLE_5
    _world_area = WorldAreaEnum.TADPOLE_POND
    # flag as checked: FROG_DISCIPLE_ITEM_5_PURCHASED


########### seaside town when boss fight available


class SeasideBeachBossFight(BossFightLocation):
    _bias = True
    _originally_held = YaridovichBossFight
    _rooms = [R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS_FIGHT
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _pack_id = PACK180_SEASIDE_BOSS
    _post_unlocks_event_id = E1206_SEASIDE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F,
            NPC_0,
            sequence_setter_event_id=E0805_SEASIDE_OCCUPIED_ELDER_HOUSE_1F_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            NPC_0,
            sequence_setter_event_id=E0805_SEASIDE_OCCUPIED_ELDER_HOUSE_1F_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            NPC_6,
            sequence_setter_event_id=E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            NPC_7,
            sequence_setter_event_id=E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_0, NPC_0],
        ),
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_1, NPC_1],
        ),
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F,
                R210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_2, NPC_0, NPC_0, NPC_2],
        ),
        BossFightLocationHenchmanNPC(
            [
                R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_3, NPC_0, NPC_3],
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP], [NPC_1]
        ),
        BossFightLocationHenchmanNPC(
            [R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP], [NPC_0]
        ),
        BossFightLocationHenchmanNPC(
            [R214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP], [NPC_1]
        ),
        BossFightLocationHenchmanNPC(
            [R215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST], [NPC_0]
        ),
        BossFightLocationHenchmanNPC(
            [R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE], [NPC_0]
        ),
        BossFightLocationHenchmanNPC(
            [R216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE], [NPC_1]
        ),
        BossFightLocationHenchmanNPC(
            [R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST], [NPC_0]
        ),
    ]
    _dialogs_expecting_replacement = [
        DI2830_SEASIDE_BOSS_WELCOMES_YOU,
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
        DI2832_OCCUPIED_SEASIDE_INNKEEPER,
        DI2834_OCCUPIED_SEASIDE_HENCHMAN_HINT_TO_LEFT_BUILDING,
        DI2837_OCCUPIED_SEASIDE_HENCHMAN_SEA_MAY_BE_LOCKED,
        DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
        DI2839_OCCUPIED_SEASIDE_HENCHMAN_AVOID_SHED,
        DI2841_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2842_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2843_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2844_OCCUPIED_SEASIDE_HENCHMAN_SHIP_CHEST_HINT,
        DI2845_OCCUPIED_SEASIDE_HENCHMAN_CUSTOMER,
        DI2847_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
        DI2848_OCCUPIED_SEASIDE_HENCHMAN_SHED_GUARD,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_seaside_boss(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(LandsEndGate, LandsEndGating.SEASIDE):
            content.extend([ClearBit(LANDS_END_GATED)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, YaridovichBossFight):
            render_seaside_beach_boss(world, self.prize)

            # Hide NPCs for unassigned character henchman slots
            if (
                self._character_henchman_slots is not None
                and self.prize.character_henchmen is not None
                and len(self.prize.character_henchmen) > 0
            ):
                assigned_count = len(self.prize.character_henchmen)
                for slot_index, slot in enumerate(self._character_henchman_slots):
                    if slot_index >= assigned_count:
                        for room_id, npc_id in zip(slot.room_ids, slot.npc_ids):
                            rm = world.rooms._rooms[room_id]
                            assert rm is not None
                            rm.get_npc_by_target_id(npc_id).set_visible(False)
                        if slot_index == 0:
                            deletions = [
                                "ship_henchman_1_beach_1",
                                "ship_henchman_1_beach_2",
                                "ship_henchman_1_beach_3",
                            ]
                            for d in deletions:
                                world.event_scripts.delete_command_by_identifier(d)
                        if slot_index == 1:
                            world.event_scripts.delete_command_by_identifier(
                                "ship_henchman_2_beach_1"
                            )

        return op

    # Flag as checked: SEASIDE_LIBERATED


class SeasideBeachStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece5
    _rooms = [R316_SEASIDE_TOWN_BEACH]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _parent = SeasideBeachBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_seaside_boss(
            world, inventory
        )

    # Flag as checked: SEASIDE_LIBERATED


class SeasideTownBossPrizeLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = ShedKeyPrize
    _rooms = [R316_SEASIDE_TOWN_BEACH]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS_PRIZE
    _world_area = WorldAreaEnum.SEASIDE_TOWN

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_seaside_boss(world, inventory)

    # flag as checked: npc 0 in room 316 has been removed from the room.
    # TODO probably need a bit for this, item is absent by default and only summoned when boss defeated


########### seaside town gated by shed key


class SeasideTownShedRescueLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerBoxPrize
    _rooms = [R314_SEASIDE_TOWN_SHED]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_RESCUE
    _world_area = WorldAreaEnum.SEASIDE_TOWN

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_seaside_boss(world, inventory) and inventory.has_item(
            ShedKeyPrize
        )

    # flag as checked: SEASIDE_SHED_EMPTIED


########## sea


class SeaStarslapRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = SeaStarPrize
    _rooms = [R134_SEA_AREA_03_SUPER_STAR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_STAR_CHEST
    _world_area = WorldAreaEnum.SEA
    _blacklist = [ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 0 in room 134 has its object trigger disabled.


class SeaSaveRoomBackChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_1
    _world_area = WorldAreaEnum.SEA
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 0 in room 132 has its object trigger disabled.


class SeaSaveRoomMiddleChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_2
    _world_area = WorldAreaEnum.SEA
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 1 in room 132 has its object trigger disabled.


class SeaSaveRoomFrontChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SEA_SAVE_ROOM_3
    _world_area = WorldAreaEnum.SEA
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 2 in room 132 has its object trigger disabled.


class SeaWhirlpoolChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEA_WHIRLPOOL_CHEST
    _world_area = WorldAreaEnum.SEA
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 0 in room 133 has its object trigger disabled.


########## sunken ship


class ShipRatStairsChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_RAT_STAIRS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 0 in room 167 has its object trigger disabled.


class ShipRatStairsBoxesLocation(PacketLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _replace = "spawn_ship_box_item"
    _rooms = [R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.CHEST
    _packet_id = P037_SHIP_STAIRCASE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_STAIRWAY_FREESTANDING_ITEM_OBTAINED


class ShipTroopaPuzzleLocation(PacketLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _replace = "spawn_ship_troopa_item"
    _rooms = [R166_SUNKEN_SHIP_PUZZLE_ROOM_1]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P027_SUNKEN_SHIP_TROOPA_PUZZLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_TROOPA_PRIZE


class ShipTrampolinePuzzle(PacketLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _replace = "spawn_ship_trampoline_item"
    _rooms = [R163_SUNKEN_SHIP_PUZZLE_ROOM_2]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P026_SUNKEN_SHIP_TRAMPOLINE_PUZZLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: UNKNOWN_707D_1


class Ship3DMazePuzzle(PacketLocationRow1):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _replace = "spawn_ship_3d_maze_item"
    _rooms = [R168_SUNKEN_SHIP_PUZZLE_ROOM_3]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P029_SUNKEN_SHIP_3D_MAZE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_MAZE_PRIZE


class ShipShopChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_SHOP
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: npc 0 in room 169 has its object trigger disabled.


class ShipCoinSnakePuzzleLocation(StandingLocationRow1):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
        R171_SUNKEN_SHIP_PUZZLE_ROOM_4,
    ]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _npc_ids = [
        NPC_0,
        NPC_1,
        NPC_2,
        NPC_3,
        NPC_4,
        NPC_5,
        NPC_6,
        NPC_7,
        NPC_8,
        NPC_9,
        NPC_10,
        NPC_11,
        NPC_12,
        NPC_13,
        NPC_14,
        NPC_15,
        NPC_16,
    ]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COIN_SNAKE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_COIN_PRIZE


class ShipCannonballPuzzle(PacketLocationRow1):
    _bias = True
    _originally_held = MushroomPrize
    _replace = "spawn_ship_cannonball_item"
    _rooms = [R172_SUNKEN_SHIP_PUZZLE_ROOM_5]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P035_SUNKEN_SHIP_CANNONBALL_PUZZLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: SHIP_CANNONBALL_PRIZE


class ShipBarrelPuzzle(PacketLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _replace = "spawn_ship_barrel_item"
    _rooms = [R176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL]
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _packet_type = PacketType.FALLING
    _packet_id = P036_BARREL_PUZZLE_PRIZE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sea(world, inventory)

    # flag as checked: UNKNOWN_707D_5


class ShipPasswordBossFight(BossFightLocation):
    _bias = True
    _originally_held = KingCalamariBossFight
    _rooms = [R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_MIDBOSS_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _pack_id = PACK167_SHIP_FIRST_BOSS
    _post_unlocks_event_id = E1207_SHIP_MID_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM,
            NPC_7,
            sequence_setter_event_id=E0800_SHIP_PASSWORD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [DI1660_SHIP_PASSWORD_COMPLETE]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, KingCalamariBossFight):
            render_ship_password_boss(world, self.prize)
        return op

    # Flag as checked: SHIP_MIDBOSS_COMPLETED


class ShipPasswordStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_MIDBOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _parent = ShipPasswordBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_ship(world, inventory)

    # Flag as checked: SHIP_MIDBOSS_COMPLETED


class EarlyInnerShipLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COINS_1
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 0 in room 175 has its object trigger disabled.


class EarlyInnerShipRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_COINS_1
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 1 in room 175 has its object trigger disabled.


class InnerShipCloneRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_CLONE_ROOM
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [SlotsPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 2 in room 179 has its object trigger disabled.


class InnerShipBehindBoxesChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_FROG_COIN_ROOM
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, SlotsPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 0 in room 183 has its object trigger disabled.


class InnerShipSaveRoomLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_HIDON_MUSHROOM
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 1 in room 184 has its object trigger disabled.


class InnerShipSaveRoomRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = SecondMimicFightLauncher
    _rooms = [R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.HIDON_CHEST
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 2 in room 184 has its object trigger disabled.


class Mimic2DropRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = SafetyBadgePrize
    _rooms = [513]  # can be in any room, custom id.
    _id = ShuffleLocationSelector.HIDON_REWARD_1
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 513

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)

    # flag as checked: MIMIC_2_CLEARED


class Mimic2BossFight(BossFightLocation):
    _bias = True
    _originally_held = HidonBossFight
    _rooms = [513]  # can be in any room.
    _override_id = 513
    _id = ShuffleLocationSelector.HIDON_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _pack_id = PACK157_SHIP_CHEST_FIGHT
    _post_unlocks_event_id = E1250_MIMIC_2_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)

    # Flag as checked: MIMIC_2_CLEARED


class Mimic2StarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.HIDON_BOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _rooms = [513]
    _override_id = 513
    _parent = Mimic2BossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)

    # Flag as checked: MIMIC_2_CLEARED


class Mimic2ReloadRewardLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = Coins100Prize
    _rooms: list[int] = []  # Dynamic room, handled by mimic system
    _npc_ids: list[AreaObject] = []  # No specific NPC
    _id = ShuffleLocationSelector.HIDON_REWARD_2
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 513
    # SecondMimicFightLauncher must be blacklisted to prevent circular dependency:
    # This location's can_access requires defeating second mimic, which requires
    # accessing the SecondMimicFightLauncher location - can't be the same location.
    _blacklist = [EXPStarPrize, SlotsPrize, MimicFightInitiatorPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(SecondMimicFightLauncher)

    def grant(self) -> EventScript:
        # Mimic rewards don't need room-specific chest disable commands
        if self.prize is None:
            return EventScript([Return()])
        return EventScript(
            [] if self.prize.chest_grant is None else self.prize.chest_grant.contents
        )

    # flag as checked: the host chest for SecondMimicFightLauncher has its object trigger disabled


class InnerShipFirstUnderwaterRoomBottomItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_1
    _world_area = WorldAreaEnum.SUNKEN_SHIP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 0 in room 187 has been removed from the room.


class InnerShipFirstUnderwaterRoomTopItemLocation(StandingLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_2
    _world_area = WorldAreaEnum.SUNKEN_SHIP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 1 in room 187 has been removed from the room.


class InnerShipFirstUnderwaterRoomLeftItemLocation(StandingLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_3
    _world_area = WorldAreaEnum.SUNKEN_SHIP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 2 in room 187 has been removed from the room.


class InnerShipFirstUnderwaterRoomMiddleItemLocation(StandingLocationRow4):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_UNDERWATER_FROG_COIN_4
    _world_area = WorldAreaEnum.SUNKEN_SHIP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 3 in room 187 has been removed from the room.


class InnerShipSecretRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = SafetyRingPrize
    _rooms = [R185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_SAFETY_RING
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 0 in room 185 has its object trigger disabled.


class InnerShipPoolRoomLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BLOOBER_ROOM
    _world_area = WorldAreaEnum.SUNKEN_SHIP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 5 in room 27 has been removed from the room.


class InnerShipBeforeBossChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BANDANA_REDS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _blacklist = [EXPStarPrize, ThirdMimicFightLauncher]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    # flag as checked: npc 4 in room 24 has its object trigger disabled.


class ShipFinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = JohnnyBossFight
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _pack_id = PACK166_SHIP_SECOND_BOSS
    _post_unlocks_event_id = E1208_SHIP_END_BOSS_UNLOCKS
    _henchman_can_run_away = False
    _npc_slots = [
        BossFightLocationNPC(
            R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            NPC_8,
            sequence_setter_event_id=E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R432_ENDING_CREDITS_JOHNNY_LOOKING_OUT_AT_SUNSET_ON_BEACH_SHORE,
            NPC_0,
            sequence_setter_event_id=E1191_ENDING_CREDITS_CLIFF_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_1, NPC_4],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            ],
            [NPC_2, NPC_5],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
            [NPC_3],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM],
            [NPC_4],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                R024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
            ],
            [NPC_0, NPC_1, NPC_2, NPC_3],
            PACK068_SHIP_HENCHMAN_1,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
        BossFightLocationHenchmanNPC(
            [
                R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
                R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
            ],
            [NPC_0, NPC_1],
            PACK069_SHIP_HENCHMAN_2,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
        ),
    ]
    _dialogs_expecting_replacement = [
        DI1778_SHIP_BOSS_AFTER_DEFEAT_BEFORE_LEAVING,
        DI1779_SHIP_BOSS_AFTER_DEFEAT_MUCH_LATER,
        DI1781_SHIP_BOSS_JUMP_ON_HEAD,
        DI1782_SHIP_BOSS_DRINK,
        DI1784_SHIP_BOSS_SIDEKICK_IN_ROOM_2,
        DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1,
        DI1786_LETTER_FROM_SHIP_BOSS,
        DI1792_SHIP_BOSS_SIDEKICK_IN_ROOM_3,
        DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4,
        DI1694_FINAL_SHIP_HENCHMEN_DEFEATED,
        DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_ship(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(YaridovichGate, YaridovichGating.SHIP):
            content.extend([ClearBit(SEASIDE_BOSS_AVAILABLE)])
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, (JohnnyBossFight, Johnny2Fight)):
            render_ship_final_boss(world, self.prize)

        return op

    # Flag as checked: SHIP_LIBERATED


class ShipFinalStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_BOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _parent = ShipFinalBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_ship(world, inventory)

    # Flag as checked: SHIP_LIBERATED


class ShipPostgameBossFight(BossFightLocation):
    _bias = True
    _originally_held = Johnny2Fight
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_BOSS_FIGHT
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 526
    _remake_only = True
    _pack_id = PACK118_SHIP_POSTGAME
    _post_unlocks_event_id = E1209_POSTGAME_SHIP_END_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
            NPC_7,
            sequence_setter_event_id=E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_ship_postgame_boss(world, inventory)

    # Flag as checked: POSTGAME_SHIP_COMPLETED


class ShipPostgameFightItemDrop(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = ExtraShinyStonePrize
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_DROP
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _remake_only = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_ship_postgame_boss(world, inventory)

    # flag as checked: POSTGAME_SHIP_COMPLETED


class ShipPostgameStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _id = ShuffleLocationSelector.SUNKEN_SHIP_POSTGAME_BOSS
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _override_id = 526
    _remake_only = True
    _parent = ShipPostgameBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_ship_postgame_boss(world, inventory)

    # Flag as checked: POSTGAME_SHIP_COMPLETED


########## lands end


class LandsEndRisingPlatformChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R137_LANDS_END_AREA_01]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.LANDS_END_RED_ESSENCE
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 4 in room 137 has its object trigger disabled.


class LandsEndChowPitStaticChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R138_LANDS_END_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_CHOW_PIT_1
    _world_area = WorldAreaEnum.LANDS_END

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 138 has its object trigger disabled.


class LandsEndChowPitMovingChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R138_LANDS_END_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.LANDS_END_CHOW_PIT_2
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [SlotsPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 7 in room 138 has its object trigger disabled.


class LandsEndBeeTowerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R141_LANDS_END_AREA_04_ROTATING_FLOWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LNDS_END_BEE_ROOM
    _world_area = WorldAreaEnum.LANDS_END

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 141 has its object trigger disabled.


class LandsEndCaveSideRemake(StandingLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R142_LANDS_END_AREA_05_SKY_BRIDGE]
    _world_area = WorldAreaEnum.LANDS_END
    _npc_ids = [NPC_19]
    _remake_only = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and world.settings.is_flag_value(
            Remake, True
        )

    # Flag as checked: npc 19 in room 142 is removed.


class LandsEndGrottoEntranceChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.LANDS_END_SECRET_1
    _world_area = WorldAreaEnum.LANDS_END

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 7 in room 270 has its object trigger disabled.


class LandsEndGrottoCornerChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_SECRET_2
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 270 has its object trigger disabled.


class LandsEndGrottoEndChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_SHY_AWAY
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 401 has its object trigger disabled.


class LandsEndUndergroundSaveBoxChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LandsEndVolcanoStarPrize
    _rooms = [R263_LANDS_END_UNDERGROUND_AREA_01]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_1
    _world_area = WorldAreaEnum.LANDS_END

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 5 in room 263 has its object trigger disabled.


class LandsEndFirstPurchasableChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LandsEndStar2Prize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_18]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_2
    _world_area = WorldAreaEnum.LANDS_END

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 18 in room 262 has its object trigger disabled.


class LandsEndSecondPurchasableChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = LandsEndStar3Prize
    _rooms = [R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS]
    _npc_ids = [NPC_19]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_3
    _world_area = WorldAreaEnum.LANDS_END

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 19 in room 262 has its object trigger disabled.


class TroopaClimbSub12PrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = TroopaPinPrize
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _id = ShuffleLocationSelector.TROOPA_CLIMB
    _world_area = WorldAreaEnum.LANDS_END

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and can_access_monstro_town(
            world, inventory
        )

    # TODO need to modify lands end overworld marker to never take you to the back exit if you havent unlocked the area yet
    # flag as checked: TROOPA_CLIMB_COMPLETED


class LandsEndCloudBoss(BossFightLocation):
    _bias = True
    _originally_held = MokuraBossFight
    _id = ShuffleLocationSelector.LANDS_END_CLOUD_BOSS_FIGHT
    _world_area = WorldAreaEnum.LANDS_END
    _rooms = [
        R137_LANDS_END_AREA_01,
        R317_LANDS_END_DESERT_AREA_01,
        R318_LANDS_END_DESERT_AREA_02,
        R319_LANDS_END_DESERT_AREA_06,
        R402_LANDS_END_DESERT_AREA_03,
        R403_LANDS_END_DESERT_AREA_05,
        R404_LANDS_END_DESERT_AREA_04,
        R424_BELOME_TEMPLE_AREA_03_PIPE_TO_ROOM_DETERMINED_BY_FORTUNE,
        R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM,
        R426_BELOME_TEMPLE_AREA_07_PIPE_TO_BELOMES_ROOM,
        R428_BELOME_TEMPLE_AREA_01_WWARP_TRAMPOLINE,
    ]
    _override_id = 519
    _pack_id = PACK207_LANDS_END_CLOUD
    _post_unlocks_event_id = E1210_CLOUD_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory)

    # Flag as checked: LANDS_END_CLOUD_STAR_PIECE_COMPLETED


class LandsEndCloudStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.LANDS_END_STAR_PIECE_1
    _world_area = WorldAreaEnum.LANDS_END
    _rooms = [519]
    _override_id = 519
    _parent = LandsEndCloudBoss

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and not_earlygame(world, inventory)

    # Flag as checked: LANDS_END_CLOUD_STAR_PIECE_COMPLETED


class BelomeTempleFortuneTellerLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins50Prize
    _rooms = [R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_TELLER
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 5 in room 420 has its object trigger disabled.


class BelomeTempleLMRChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_1
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 6 in room 421 has its object trigger disabled.


class BelomeTempleLRMChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = YoshiCookiePrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_2
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 7 in room 421 has its object trigger disabled.


class BelomeTempleRLMChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_3
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 8 in room 421 has its object trigger disabled.


class BelomeTempleRMLChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_FORTUNE_4
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 9 in room 421 has its object trigger disabled.


class BelomeBeforeBossRightChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_1
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 0 in room 425 has its object trigger disabled.


class BelomeBeforeBossLowerLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_2
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 1 in room 425 has its object trigger disabled.


class BelomeBeforeBossMiddleChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_3
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 2 in room 425 has its object trigger disabled.


class BelomeBeforeBossUpperLeftChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_AFTER_FORTUNE_3
    _world_area = WorldAreaEnum.TEMPLE
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)

    # flag as checked: npc 3 in room 425 has its object trigger disabled.


class BelomeTempleTreasuryUpperCornerLeftItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_1
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 0 in room 422 has been removed from the room.


class BelomeTempleTreasuryUpperCornerLowerLeftItemLocation(StandingLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_2
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 1 in room 422 has been removed from the room.


class BelomeTempleTreasuryUpperCornerTopItemLocation(StandingLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_3
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 2 in room 422 has been removed from the room.


class BelomeTempleTreasuryTopmostItemLocation(StandingLocationRow4):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FLOWER_4
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 3 in room 422 has been removed from the room.


class BelomeTempleTreasuryMidLeftItemLocation(StandingLocationRow5):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_1
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 4 in room 422 has been removed from the room.


class BelomeTempleTreasuryAlmostTopItemLocation(StandingLocationRow6):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_2
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 5 in room 422 has been removed from the room.


class BelomeTempleTreasuryAlmostLeftmostItemLocation(StandingLocationRow7):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_3
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 6 in room 422 has been removed from the room.


class BelomeTempleTreasuryOuterUpperRightItemLocation(StandingLocationRow8):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_4
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 7 in room 422 has been removed from the room.


class BelomeTempleTreasuryInnerUpperRightItemLocation(StandingLocationRow9):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_5
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 8 in room 422 has been removed from the room.


class BelomeTempleTreasuryLowestItemsRightLocation(StandingLocationRow10):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_6
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 9 in room 422 has been removed from the room.


class BelomeTempleTreasuryLowerOuterBottomRightItemLocation(StandingLocationRow11):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_7
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 10 in room 422 has been removed from the room.


class BelomeTempleTreasuryRightmostItemLocation(StandingLocationRow12):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_FROG_COIN_8
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 11 in room 422 has been removed from the room.


class BelomeTempleTreasuryBottomLeftCornerItemLocation(StandingLocationRow13):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_2
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 13 in room 422 has been removed from the room.


class BelomeTempleTreasuryLowestItemsLeftLocation(StandingLocationRow14):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_1
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 14 in room 422 has been removed from the room.


class BelomeTempleTreasuryUpperOuterBottomRightItemLocation(StandingLocationRow15):
    _bias = True
    _originally_held = FireBombPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_3
    _world_area = WorldAreaEnum.TEMPLE

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )

    # flag as checked: npc 15 in room 422 has been removed from the room.


class TempleBossFight(BossFightLocation):
    _bias = True
    _originally_held = Belome2BossFight
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_FIGHT
    _world_area = WorldAreaEnum.TEMPLE
    _pack_id = PACK169_TEMPLE_BOSS
    _post_unlocks_event_id = E1211_TEMPLE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            NPC_4,
            sequence_setter_event_id=E0814_TEMPLE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_temple_boss(world, inventory)

    # Flag as checked: TEMPLE_BOSS_DEFEATED


class TempleBossFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS
    _world_area = WorldAreaEnum.TEMPLE
    _parent = TempleBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_temple_boss(
            world, inventory
        )

    # Flag as checked: TEMPLE_BOSS_DEFEATED


class TempleBossFightPostgame(BossFightLocation):
    _bias = True
    _originally_held = Belome3Fight
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME_FIGHT
    _world_area = WorldAreaEnum.TEMPLE
    _override_id = 523
    _remake_only = True
    _pack_id = PACK033_POSTGAME_TEMPLE
    _post_unlocks_event_id = E1212_POSTGAME_TEMPLE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            NPC_5,
            sequence_setter_event_id=E0814_TEMPLE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_temple_postgame_boss(world, inventory)

    # Flag as checked: TEMPLE_POSTGAME_BOSS_DEFEATED


class TempleBossFightStarPiecePostgame(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME
    _world_area = WorldAreaEnum.TEMPLE
    _override_id = 523
    _remake_only = True
    _parent = TempleBossFightPostgame

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_temple_postgame_boss(
            world, inventory
        )

    # Flag as checked: TEMPLE_POSTGAME_BOSS_DEFEATED


class TemplePostgameFightItemDrop(NPCLocationRow1):
    _bias = True
    _originally_held = SageStickPrize
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS_POSTGAME_DROP
    _world_area = WorldAreaEnum.TEMPLE
    _remake_only = True
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_temple_postgame_boss(world, inventory)

    # flag as checked: TEMPLE_POSTGAME_BOSS_DEFEATED


########## monstro town


class MonstroEntranceLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R267_MONSTRO_TOWN_ENTRANCE]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_ENTRANCE
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)

    # flag as checked: npc 1 in room 267 has its object trigger disabled.


class MonstroThwompItemLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = TempleKeyPrize
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MONSTRO_TOWN_THWOMP
    _world_area = WorldAreaEnum.MONSTRO_TOWN

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)

    # flag as checked: npc 0 in room 324 has been removed from the room.


class DojoFirstFight(BossFightLocation):
    _bias = True
    _originally_held = JaggerBossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _pack_id = PACK189_DOJO_PREFIGHT
    _post_unlocks_event_id = E1213_DOJO_1_BOSS_UNLOCKS
    _allow_run_away = True

    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_1,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI3044_DOJO_BOSS_1_AFTER_DEFEAT,
        DI3352_DOJO_BOSS_1_FULLY_DEFEATED,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, JaggerBossFight):
            render_dojo_first_fight(world, self.prize)
        return op

    # Flag as checked: DOJO_BOSS_1_DEFEATED


class DojoFirstFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_1
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _parent = DojoFirstFight
    # Flag as checked: DOJO_BOSS_1_DEFEATED

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_monstro_town(
            world, inventory
        )


class DojoSecondFight(BossFightLocation):
    _bias = True
    _originally_held = Jinx1BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 515
    _pack_id = PACK178_DOJO_FIGHT_1
    _post_unlocks_event_id = E1214_DOJO_2_BOSS_UNLOCKS
    _allow_run_away = True
    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_0,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize, (Jinx1BossFight, Jinx2BossFight, Jinx3BossFight, Jinx4BossFight)
        ):
            render_dojo_fight(
                world,
                self.prize,
                "dojo_boss_2_initiate_aq",
                "dojo_boss_2_initiate",
                "dojo_boss_2_pause",
            )
        return op

    # Flag as checked: DOJO_BOSS_2_DEFEATED


class DojoSecondFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_2
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 515
    _parent = DojoSecondFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_monstro_town(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: DOJO_BOSS_2_DEFEATED


class DojoThirdFight(BossFightLocation):
    _bias = True
    _originally_held = Jinx2BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 516
    _pack_id = PACK187_DOJO_SECOND_BOSS
    _post_unlocks_event_id = E1215_DOJO_3_BOSS_UNLOCKS
    _allow_run_away = True
    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_2,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize, (Jinx1BossFight, Jinx2BossFight, Jinx3BossFight, Jinx4BossFight)
        ):
            render_dojo_fight(
                world,
                self.prize,
                "dojo_boss_3_initiate_aq",
                "dojo_boss_3_initiate",
                "dojo_boss_3_pause",
            )
        return op

    # Flag as checked: DOJO_BOSS_3_DEFEATED


class DojoThirdFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_3
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 516
    _parent = DojoThirdFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: DOJO_BOSS_3_DEFEATED


class DojoFourthFight(BossFightLocation):
    _bias = True
    _originally_held = Jinx3BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_4
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 517
    _pack_id = PACK188_DOJO_THIRD_BOSS
    _post_unlocks_event_id = E1216_DOJO_4_BOSS_UNLOCKS
    _allow_run_away = True
    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_3,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [DI3353_DOJO_BOSS_2_FULLY_DEFEATED]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize, (Jinx1BossFight, Jinx2BossFight, Jinx3BossFight, Jinx4BossFight)
        ):
            render_dojo_fight(
                world,
                self.prize,
                "dojo_boss_4_initiate_aq",
                "dojo_boss_4_initiate",
                "dojo_boss_4_pause",
            )
        return op

    # Flag as checked: DOJO_BOSS_4_DEFEATED


class DojoFourthFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_4
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 517
    _parent = DojoFourthFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: DOJO_BOSS_4_DEFEATED


class MonstroDojoClearRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = JinxBeltPrize
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.JINX_DOJO_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: DOJO_BOSS_4_DEFEATED


class DojoFifthFight(BossFightLocation):
    _bias = True
    _originally_held = Jinx4BossFight
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_FIGHT_POSTGAME
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 525
    _remake_only = True
    _pack_id = PACK189_DOJO_PREFIGHT
    _post_unlocks_event_id = E1217_DOJO_5_BOSS_UNLOCKS
    _allow_run_away = True
    _npc_slots = [
        BossFightLocationNPC(
            R255_MONSTRO_TOWN_JINXS_DOJO,
            NPC_4,
            sequence_setter_event_id=E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_fifth_dojo_boss(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize, (Jinx1BossFight, Jinx2BossFight, Jinx3BossFight, Jinx4BossFight)
        ):
            render_dojo_fight(
                world,
                self.prize,
                "dojo_boss_5_initiate_aq",
                "dojo_boss_5_initiate",
                "dojo_boss_5_pause",
            )
        return op

    # Flag as checked: DOJO_POSTGAME_COMPLETED


class DojoFifthFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_POSTGAME
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 525
    _remake_only = True
    _parent = DojoFifthFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_fifth_dojo_boss(
            world, inventory
        )

    # Flag as checked: DOJO_POSTGAME_COMPLETED


class MonstroDojoPostgameClearRewardLocation(NPCLocationRow2):
    _bias = True
    _originally_held = TeamworkBandPrize
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_POSTGAME_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_fifth_dojo_boss(world, inventory)

    # Flag as checked: DOJO_POSTGAME_COMPLETED


class MonstroSealedDoorBossFight(BossFightLocation):
    _bias = True
    _originally_held = CulexBossFight
    _rooms = [R351_CULEXS_ROOM]
    _id = ShuffleLocationSelector.CULEX_BOSS_FIGHT
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _pack_id = PACK216_MONSTRO_DOOR_BOSS
    _post_unlocks_event_id = E1218_MONSTRO_SEALED_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R351_CULEXS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI3338_MONSTRO_SUPERBOSS_HINT,
        DI3057_MONSTRO_SUPERBOSS_PROMPT,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_door_boss(world, inventory)

    # Flag as checked: MONSTRO_MIDDLE_DOOR_COMPLETED


class MonstroSealedDoorStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_BOSS
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _parent = MonstroSealedDoorBossFight
    _npc_slots = [
        BossFightLocationNPC(
            R351_CULEXS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_sealed_door_boss(
            world, inventory
        )

    # Flag as checked: MONSTRO_MIDDLE_DOOR_COMPLETED


class MonstroSealedDoorClearRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = QuartzCharmPrize
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_door_boss(world, inventory)

    # Flag as checked: MONSTRO_MIDDLE_DOOR_COMPLETED


class MonstroSealedDoorBossFightPostgame(BossFightLocation):
    _bias = True
    _originally_held = Culex3DBossFight
    _rooms = [R351_CULEXS_ROOM]
    _override_id = 524
    _id = ShuffleLocationSelector.CULEX_POSTGAME_BOSS_FIGHT
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _pack_id = PACK055_MONSTRO_DOOR_POSTGAME
    _post_unlocks_event_id = E1219_POSTGAME_MONSTRO_SEALED_BOSS_UNLOCKS

    _npc_slots = [
        BossFightLocationNPC(
            R351_CULEXS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_postgame_boss(world, inventory)

    _dialogs_expecting_replacement = [DI3058_MONSTRO_POSTGAME_SUPERBOSS_PROMPT]

    # Flag as checked: CULEX_POSTGAME_COMPLETED


class MonstroSealedDoorStarPiecePostgame(StarPieceLocation):
    _bias = True
    _originally_held = None
    _override_id = 524
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_POSTGAME_BOSS
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _parent = MonstroSealedDoorBossFightPostgame

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_sealed_postgame_boss(
            world, inventory
        )

    # Flag as checked: CULEX_POSTGAME_COMPLETED


class MonstroSealedDoorClearRewardLocationPostgame(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = CrystalShardPrize
    _rooms = [R351_CULEXS_ROOM]
    _id = ShuffleLocationSelector.CULEX_POSTGAME_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_postgame_boss(world, inventory)

    # Flag as checked: CULEX_POSTGAME_COMPLETED


class MonstroFirstSuperJumpRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = AttackScarfPrize
    _rooms = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _id = ShuffleLocationSelector.SUPER_JUMPS_30
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and inventory.has_item(
            SuperJumpSpellPrize
        )

    # Flag as checked: SUPER_JUMP_PRIZE_1_GRANTED


class MonstroSecondSuperJumpRewardLocation(NPCLocationRow2):
    _bias = True
    _originally_held = SuperSuitPrize
    _rooms = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _id = ShuffleLocationSelector.SUPER_JUMPS_100
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and inventory.has_item(
            SuperJumpSpellPrize
        )

    # Flag as checked: SUPER_JUMP_PRIZE_2_GRANTED


class MonstroFlagExchangeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = GhostMedalPrize
    _rooms = [R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN]
    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and inventory.has_item(DryBonesFlagPrize)
            and inventory.has_item(GreaperFlagPrize)
            and inventory.has_item(BigBooFlagPrize)
        )

    # Flag as checked: UNUSED_7093_5


########## bean valley


class BeanValleyFirstDeadEndLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 3 in room 252 has its object trigger disabled.


class BeanValleyFirstProgressChestLocation(TreasureChestLocationRow2):
    _originally_held = FrogCoin1Prize
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 4 in room 252 has its object trigger disabled.


class BeanValleyLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize1
    _rooms = [R334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_LEFT_PIRANHA_PIPE
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 0 in room 334 has its object trigger disabled.


class BeanValleyBottomLeftPiranhaPipeLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize2
    _rooms = [R348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_LEFT_PIRANHA_PIPE
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 0 in room 348 has its object trigger disabled.


class BeanValleyBottomRightPiranhaPipeUpperLocation(TreasureChestLocationRow1):
    _originally_held = SlotsPrize3
    _rooms = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_UPPER
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 0 in room 349 has its object trigger disabled.


class BeanValleyBottomRightPiranhaPipeLowerLocation(TreasureChestLocationRow2):
    _originally_held = KerokeroColaPrize
    _rooms = [R349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA_PIPE_LOWER
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 2 in room 349 has its object trigger disabled.


class BeanValleyRightPipeLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = ThirdMimicFightLauncher
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 5 in room 335 has its object trigger disabled.


class Mimic3BossFight(BossFightLocation):
    _bias = True
    _originally_held = BoxBoyBossFight
    _rooms = [514]  # can be in any room.
    _override_id = 514
    _id = ShuffleLocationSelector.BOX_BOY_BOSS_FIGHT
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _pack_id = PACK158_VALLEY_CHEST_FIGHT
    _post_unlocks_event_id = E1251_MIMIC_3_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(ThirdMimicFightLauncher) and not_earlygame(
            world, inventory
        )

    # Flag as checked: MIMIC_3_CLEARED


class Mimic3StarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.BOX_BOY_BOSS
    _rooms = [514]
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _override_id = 514
    _parent = Mimic3BossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and inventory.has_item(ThirdMimicFightLauncher)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: MIMIC_3_CLEARED


class BeanValleyRightPipeRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RedEssencePrize
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 7 in room 335 has its object trigger disabled.


class BeanValleyRightPipeUnderStairsLocation(NPCLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOX_BOY_ROOM_HIDDEN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 9 in room 335 is removed.


class BeanValleyRightPipeAboveGroundLocation(TreasureChestLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R251_BEAN_VALLEY_PIRANHA_PIPE_AREA]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BEAN_VALLEY_PIRANHA_PLANTS
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 13 in room 251 has its object trigger disabled.


class BeanValleyPlanterBossFight(BossFightLocation):
    _bias = True
    _originally_held = MegasmilaxBossFight
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOSS_FIGHT
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _pack_id = PACK173_VALLEY_BOSS
    _post_unlocks_event_id = E1229_BEAN_VALLEY_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R254_BEAN_VALLEY_SMILAX_AREA,
            NPC_1,
            sequence_setter_event_id=E0817_BEAN_VALLEY_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(NimbusGate, NimbusGating.VALLEY):
            content.extend(
                [
                    SetBit(NIMBUS_MAINLAND_UNLOCKED),
                    RemoveObjectFromSpecificLevel(
                        NPC_2, R369_NIMBUS_LAND_ENTRANCE_WWARP_TRAMPOLINE
                    ),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, (MegasmilaxBossFight)):
            render_bean_valley_planter_boss(world, self.prize)
        return op

    # Flag as checked: BEAN_VALLEY_BOSS_DEFEATED


class BeanValleyPlanterStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BOSS
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _parent = BeanValleyPlanterBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and not_earlygame(world, inventory)

    # Flag as checked: BEAN_VALLEY_BOSS_DEFEATED


class BeanValleyBossNoteLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = SeedPrize
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_MEGASMILAX_ROOM
    _world_area = WorldAreaEnum.BEAN_VALLEY

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory)

    # flag as checked: SEED_CHECKED


class BeanstalkLowestChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 9 in room 379 has its object trigger disabled.


class BeanValley1stRoomFloatingItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_FROG_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 3 in room 378 has been removed from the room.


class BeanValley1stRoomMiddleCoinLocation(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_MIDDLE_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 4 in room 378 has been removed from the room.


class BeanValley1stRoomUpperCoinLocation(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_UPPER_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 5 in room 378 has been removed from the room.


class BeanValley1stRoomLowerCoinLocation(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R378_BEAN_VALLEY_BEANSTALKS_AREA_01]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FIRST_VINE_ROOM_LOWER_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 6 in room 378 has been removed from the room.


class Beanstalk2ndRoomFloatingItemLocation(StandingLocationRow1):
    _originally_held = FrogCoin1Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_FROG_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 6 in room 379 has been removed from the room.


class Beanstalk2ndRoomCoin1Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 3 in room 379 has its object trigger disabled.


class Beanstalk2ndRoomCoin2Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 4 in room 379 has its object trigger disabled.


class Beanstalk2ndRoomCoin3Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R379_BEAN_VALLEY_BEANSTALKS_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_BEANSTALK_COIN_3
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 5 in room 379 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin1Location(StandingLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 3 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin2Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 4 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin3Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_3
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 5 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin4Location(StandingLocationRow4):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_4
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 6 in room 380 has its object trigger disabled.


class BeanValleyEastBeanstalkCoin5Location(StandingLocationRow5):
    _originally_held = Coins10Prize
    _rooms = [R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_EAST_BEANSTALK_COIN_5
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 7 in room 380 has its object trigger disabled.


class BeanValleyWestBeanstalkCoin1Location(StandingLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 4 in room 381 has its object trigger disabled.


class BeanValleyWestBeanstalkCoin2Location(StandingLocationRow2):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 5 in room 381 has its object trigger disabled.


class BeanValleyWestBeanstalkCoin3Location(StandingLocationRow3):
    _originally_held = Coins10Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_COIN_3
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 6 in room 381 has its object trigger disabled.


class BeanValleyWestBeanstalkFloatingItemLocation(StandingLocationRow4):
    _originally_held = FrogCoin1Prize
    _rooms = [R381_BEAN_VALLEY_BEANSTALKS_AREA_04_FROM_LEFT_BEANSTALK_OF_AREA_02]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BEAN_VALLEY_WEST_BEANSTALK_FROG_COIN
    _world_area = WorldAreaEnum.BEAN_VALLEY
    # flag as checked: npc 7 in room 381 has been removed from the room.


class BeanstalkUpperCloudLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 1 in room 372 has its object trigger disabled.


class BeanstalkUpperCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = RareScarfPrize
    _rooms = [R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_CLOUD_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 2 in room 372 has its object trigger disabled.


class BeanstalkLowerCloudLeftChestLocation(TreasureChestLocationRow1):
    _originally_held = FPFlowerPrize
    _rooms = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FALL_1
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 1 in room 373 has its object trigger disabled.


class BeanstalkLowerCloudRightChestLocation(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BEAN_VALLEY_FALL_2
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [EXPStarPrize]
    # flag as checked: npc 2 in room 373 has its object trigger disabled.


########## casino


class CasinoGrateGuyPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = StarEggPrize
    _rooms = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _id = ShuffleLocationSelector.CASINO_GRATE_GUY_PRIZE
    _world_area = WorldAreaEnum.CASINO

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BrightCardPrize)

    # flag as checked: CASINO_PRIZE_WON


########## nimbus land


class NimbusShopChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R344_NIMBUS_LAND_ITEM_SHOP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SHOP
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_outer_nimbus(world, inventory)

    # flag as checked: npc 0 in room 344 has its object trigger disabled.


class NimbusInnDreamPrize1Location(NPCLocationRow1):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R346_NIMBUS_LAND_INN_BEDROOM]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_outer_nimbus(world, inventory)

    # flag as checked: NIMBUS_INN_PRIZE_GRANTED


class NimbusInnDreamPrize2Location(NPCLocationRow2):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R346_NIMBUS_LAND_INN_BEDROOM]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN_2
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_outer_nimbus(world, inventory)

    # flag as checked: NIMBUS_INN_PRIZE_GRANTED


# Only enabled with one specific setting
class GarroFreeItem(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = GoldPaintPrize
    _rooms = [R341_NIMBUS_LAND_GARROS_HOUSE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_GARRO
    _world_area = WorldAreaEnum.BEAN_VALLEY

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_outer_nimbus(world, inventory)

    # flag as checked: GARRO_ITEM_GRANTED


class NimbusCastleStatueGamePrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FeatherPrize
    _rooms = [R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM]
    _override_id = 520
    _id = ShuffleLocationSelector.DODO_REWARD
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_nimbus(world, inventory)

    # flag as checked: STATUE_GAME_DONE


class StatueRoomBossFight(BossFightLocation):
    _bias = True
    _originally_held = DodoBossFight
    _override_id = 520
    _id = ShuffleLocationSelector.NIMBUS_LAND_STATUE_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK208_NIMBUS_CASTLE_FIRST_BOSS
    _post_unlocks_event_id = E1230_STATUE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
            NPC_1,
            sequence_setter_event_id=E0818_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_3,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            NPC_0,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI2180_CHAPEL_NPC
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory) and not_earlygame(
            world, inventory
        )

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, (DodoBossFight)):
            from ..types.flags import KeepMinigameSpritesIntact

            render_statue_room_boss(
                world,
                self.prize,
                world.settings.isflag_enabled(KeepMinigameSpritesIntact),
            )
        return op

    # Flag as checked: STATUE_KEEPER_STAR_PIECE


class StatueRoomStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _override_id = 520
    _id = ShuffleLocationSelector.NIMBUS_LAND_STAR_PIECE_1
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _parent = StatueRoomBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = world.settings.isflag_enabled(
            _get_flag("SkipBossFights")
        ) or not_earlygame(world, inventory)
        return (
            super().can_access(inventory, world)
            and can_access_nimbus_castle(world, inventory)
            and boss_condition
        )

    # Flag as checked: STATUE_KEEPER_STAR_PIECE


class NimbusCastleOuterPrisonCellarRightNPCLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerJarPrize
    _rooms = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: BLUE_CELLAR_GUARD_ITEM_GRANTED


class NimbusCastleOuterPrisonCellarLeftNPCLocation(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = CastleKey1Prize
    _rooms = [R414_NIMBUS_CASTLE_AREA_08_FROM_AREA_07_GET_ROOM_KEY_1_HERE]
    _id = ShuffleLocationSelector.NIMBUS_LAND_PRISONERS_2
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: RED_CELLAR_GUARD_ITEM_GRANTED


class NimbusCastleBusinessCentreOccupiedChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_INN_2
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: NIMBUS_MISSABLE_CHECK_CLEARED
    # (not really missable anymore. the chest that replaces this in the liberated castle will simply give you its item first if you didn't already get it)


class NimbusCastleCornerBridgeChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
        R500_NIMBUS_CASTLE_AREA_04_DUMMY,
    ]
    _npc_ids = [NPC_2, NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_LAND_BEFORE_BIRDETTA_2
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 2 in room 111 has its object trigger disabled.
    # or npc 0 in room 500 has its object trigger disabled


class NimbusCastleOutOfBoundsChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_1
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 0 in room 410 has its object trigger disabled


class NimbusCastleAboveJawfulChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_OUT_OF_BOUNDS_2
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 1 in room 410 has its object trigger disabled


class NimbusCastleSingleGoldBirdChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_SINGLE_GOLD_BIRD
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 1 in room 113 has its object trigger disabled.


class NimbusCastleTwoLevelLowerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        R498_NIMBUS_CASTLE_AREA_10_DUMMY,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_1
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_nimbus_castle(world, inventory)

    # flag as checked: npc 0 in room 114 has its object trigger disabled.


### nimbus castle gated by ck1


class GiantEggBossFight(BossFightLocation):
    _bias = True
    _originally_held = BirdettaBossFight
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_EGG_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK175_NIMBUS_CASTLE_SECOND_BOSS
    _post_unlocks_event_id = E1231_EGG_BOSS_UNLOCKS
    _dialogs_expecting_replacement = [DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_nimbus(world, inventory) and not_earlygame(
            world, inventory
        )

    # Flag as checked: NIMBUS_MID_BOSS_COMPLETED


class GiantEggStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_PIECE_2
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _parent = GiantEggBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_inner_nimbus(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: NIMBUS_MID_BOSS_COMPLETED


class NimbusCastleGiantEggRewardLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = CastleKey2Prize
    _rooms = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_BIRDETTA
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_nimbus(world, inventory) and not_earlygame(
            world, inventory
        )

    # flag as checked: NIMBUS_MID_BOSS_COMPLETED


### nimbus land gated by ck2


class NimbusCastleTwoLevelUpperChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [
        R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        R498_NIMBUS_CASTLE_AREA_10_DUMMY,
    ]
    _npc_ids = [NPC_1, NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_AFTER_EGG_2
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_late_nimbus(world, inventory)

    # flag as checked: npc 1 in room 114 has its object trigger disabled.


class NimbusCastleBackHallwayOccupiedChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = NimbusLandStarPrize
    _rooms = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_CHEST
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_late_nimbus(world, inventory)

    # flag as checked: npc 0 in room 121 has its object trigger disabled.


class NimbusFinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = ValentinaBossFight
    _rooms = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_FINAL_BOSS_FIGHT
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _pack_id = PACK171_NIMBUS_CASTLE_THIRD_BOSS
    _post_unlocks_event_id = E1232_NIMBUS_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA,
            NPC_9,
            sequence_setter_event_id=E0822_NIMBUS_LAND_OCCUPIED_EXTERIOR_FINAL_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            NPC_4,
            sequence_setter_event_id=E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            NPC_9,
            sequence_setter_event_id=E0795_ENDING_CREDITS_CHAPEL_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            ],
            [NPC_11],
        ),
        BossFightLocationHenchmanNPC(
            [
                R416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            ],
            [NPC_12],
        ),
    ]
    _statue_slots = [
        # Garro's house
        BossFightLocationNPC(
            R341_NIMBUS_LAND_GARROS_HOUSE,
            NPC_1,
            sequence_setter_event_id=E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R341_NIMBUS_LAND_GARROS_HOUSE,
            NPC_2,
            sequence_setter_event_id=E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R341_NIMBUS_LAND_GARROS_HOUSE,
            NPC_3,
            sequence_setter_event_id=E0821_GARROS_HOUSE_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Main hall
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_0,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_1,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_2,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_3,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_4,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            NPC_5,
            sequence_setter_event_id=E0823_NIMBUS_CASTLE_MAIN_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Occupied 4-way path
        BossFightLocationNPC(
            R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0824_NIMBUS_CASTLE_OCCUPIED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0824_NIMBUS_CASTLE_OCCUPIED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Antechamber
        BossFightLocationNPC(
            R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            NPC_0,
            sequence_setter_event_id=E0825_NIMBUS_CASTLE_THRONE_ROOM_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            NPC_1,
            sequence_setter_event_id=E0825_NIMBUS_CASTLE_THRONE_ROOM_ANTECHAMBER_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Occupied throne room
        BossFightLocationNPC(
            R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0826_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0826_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Polishing room
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_0,
            sequence_setter_event_id=E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_1,
            sequence_setter_event_id=E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            NPC_2,
            sequence_setter_event_id=E0819_NIMBUS_CASTLE_STATUE_POLISHING_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Lone statue room
        BossFightLocationNPC(
            R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
            NPC_3,
            sequence_setter_event_id=E0827_NIMBUS_CASTLE_SINGLE_BIRD_STATUE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Left shaman hall
        BossFightLocationNPC(
            R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            NPC_6,
            sequence_setter_event_id=E0829_NIMBUS_CASTLE_EARLY_WEST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            NPC_7,
            sequence_setter_event_id=E0829_NIMBUS_CASTLE_EARLY_WEST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Right shaman hall
        BossFightLocationNPC(
            R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM,
            NPC_6,
            sequence_setter_event_id=E0830_NIMBUS_CASTLE_EARLY_EAST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM,
            NPC_7,
            sequence_setter_event_id=E0830_NIMBUS_CASTLE_EARLY_EAST_SHAMAN_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Liberated throne room
        BossFightLocationNPC(
            R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0831_NIMBUS_CASTLE_LIBERATED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0831_NIMBUS_CASTLE_LIBERATED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Hot springs
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_1,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_2,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_3,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R447_NIMBUS_LAND_HOT_SPRINGS,
            NPC_4,
            sequence_setter_event_id=E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Cellar hallway
        BossFightLocationNPC(
            R497_NIMBUS_CASTLE_AREA_06_DUMMY,
            NPC_0,
            sequence_setter_event_id=E0834_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R497_NIMBUS_CASTLE_AREA_06_DUMMY,
            NPC_1,
            sequence_setter_event_id=E0834_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Five-door hallway
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_2,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_3,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            NPC_4,
            sequence_setter_event_id=E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        # Liberated 4-way path
        BossFightLocationNPC(
            R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            NPC_0,
            sequence_setter_event_id=E0836_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            NPC_1,
            sequence_setter_event_id=E0836_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _dialogs_expecting_replacement = [
        DI1120_NIMBUS_BIRD_GUARD,
        DI1945_NIMBUS_GUARD,
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.NIMBUS):
            content.extend(
                [
                    SetBit(MAP_DIRECTIONAL_NIMBUS_LAND_BARREL_VOLCANO),
                    SetBit(MAP_BARREL_VOLCANO),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: NIMBUS_LAND_LIBERATED


class NimbusFinalStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_PIECE_3
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _parent = NimbusFinalBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_nimbus_boss(
            world, inventory
        )

    # Flag as checked: NIMBUS_LAND_LIBERATED


### nimbus land gated by liberation


class NimbusCastleBackHallwayLiberatedChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_STAR_AFTER_VALENTINA
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: npc 1 in room 121 has its object trigger disabled.


class NimbusCastleBusinessCentreLiberatedChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.NIMBUS_CASTLE_CORNER_CHEST_AFTER_VALENTINA
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: NIMBUS_MISSABLE_CHECK_CLEARED


class NimbusLandRightSideLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = FertilizerPrize
    _rooms = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _id = ShuffleLocationSelector.NIMBUS_LAND_RIGHT_SIDE
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: NPC 9 removed from room 438.


class NimbusLandCrocoItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = SignalRingPrize
    _rooms = [R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.NIMBUS_LAND_SIGNAL_RING
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: npc 5 in room 345 has been removed from the room.


class NimbusLandInnerCellarLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerJarPrize
    _rooms = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _id = ShuffleLocationSelector.NIMBUS_LAND_CELLAR
    _world_area = WorldAreaEnum.NIMBUS_LAND

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_nimbus_boss(world, inventory)

    # flag as checked: NIMBUS_CASTLE_LIBERATED_GUARD_ITEM_GRANTED


########## barrel volcano


class VolcanoLavaCoveLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 355 has its object trigger disabled.


class VolcanoLavaCoveRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SECRET_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 2 in room 355 has its object trigger disabled.


class VolcanoEarlyProgressChestLeftLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R384_VOLCANO_AREA_05]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 0 in room 384 has its object trigger disabled.


class VolcanoEarlyProgressChestRightLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R384_VOLCANO_AREA_05]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BEFORE_STAR_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 384 has its object trigger disabled.


class VolcanoEarlyProgressThirdChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LandsEndVolcanoStarPrize
    _rooms = [R385_VOLCANO_AREA_06]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_STAR_ROOM
    _world_area = WorldAreaEnum.BARREL_VOLCANO

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 0 in room 385 has its object trigger disabled.


class VolcanoLavaPoolLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R361_VOLCANO_AREA_09]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_LAVA_POOL
    _world_area = WorldAreaEnum.BARREL_VOLCANO

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 361 has been removed from the room.


class VolcanoReverseRecoilItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R383_VOLCANO_AREA_10_JUMPING_PYROSPHERES]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_REVERSE
    _world_area = WorldAreaEnum.BARREL_VOLCANO

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 4 in room 383 has been removed from the room.


class VolcanoRightDonutItemLocation(StandingLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R358_VOLCANO_AREA_11]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 358 has been removed from the room.


class VolcanoLeftDonutItemLocation(StandingLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R358_VOLCANO_AREA_11]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_DONUT_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 2 in room 358 has been removed from the room.


class VolcanoSaveRoomLowerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 0 in room 366 has its object trigger disabled.


class VolcanoSaveRoomUpperChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R366_VOLCANO_AREA_13_WSAVE_POINT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_SAVE_ROOM_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 1 in room 366 has its object trigger disabled.


class VolcanoShopEntranceChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins100Prize
    _rooms = [R367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_HINOPIO
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_volcano(world, inventory)

    # flag as checked: npc 0 in room 367 has its object trigger disabled.


class VolcanoBridgeBossFight(BossFightLocation):
    _bias = True
    _originally_held = CzarDragonBossFight
    _rooms = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _pack_id = PACK172_VOLCANO_FIRST_BOSS
    _post_unlocks_event_id = E1233_VOLCANO_MID_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0840_VOLCANO_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            ],
            [NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_volcano(world, inventory)

    # Flag as checked: VOLCANO_MIDBOSS_DEFEATED


class VolcanoBridgeStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _parent = VolcanoBridgeBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_volcano(
            world, inventory
        )

    # Flag as checked: VOLCANO_MIDBOSS_DEFEATED


class VolcanoExitBossFight(BossFightLocation):
    _bias = True
    _originally_held = AxemRangersBossFight
    _rooms = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _pack_id = PACK182_VOLCANO_BOSS
    _post_unlocks_event_id = E1234_VOLCANO_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R392_VOLCANO_POSTCD_AREA_06,
            NPC_0,
            sequence_setter_event_id=E0842_VOLCANO_FINAL_PRE_EXIT_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R394_VOLCANO_POSTCD_AREA_05,
            NPC_2,
            sequence_setter_event_id=E0843_VOLCANO_POST_BOSS_ROOM_WITH_ENEMY_WARPS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            NPC_1,
            sequence_setter_event_id=E0844_VOLCANO_EXIT_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R391_VOLCANO_POSTCD_AREA_04,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            ],
            [NPC_1, NPC_0, NPC_2],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            ],
            [NPC_2, NPC_3],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                R394_VOLCANO_POSTCD_AREA_05,
            ],
            [NPC_3, NPC_4, NPC_1],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [
                R392_VOLCANO_POSTCD_AREA_06,
                R394_VOLCANO_POSTCD_AREA_05,
                R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            ],
            [NPC_4, NPC_0, NPC_5],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_volcano(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.VOLCANO):
            content.extend(
                [
                    SetBit(MAP_VISTA_HILL),
                    ClearBit(MAP_DIRECTIONAL_NIMBUS_LAND_VISTA_HILL),
                ]
            )
            if world.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
                content.extend(
                    [
                        SetBit(MAP_GATE),
                        SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                    ]
                )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        if isinstance(self.prize, AxemRangersBossFight):
            return op
        assert isinstance(self.prize, BossFightPrize)
        render_volcano_exit_boss(world, self.prize)
        return op

    # Flag as checked: VOLCANO_LIBERATED


class VolcanoExitStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece6
    _rooms = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_2
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _parent = VolcanoExitBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_volcano(
            world, inventory
        )

    # Flag as checked: VOLCANO_LIBERATED


########## bowser's keep


class KeepDarkRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DARK_ROOM
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 0 in room 453 has its object trigger disabled.


class KeepFirstCrocoShopLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = Coins150Prize
    _rooms = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 0 in room 451 has its object trigger disabled.


class KeepFirstCrocoShopRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CROCO_SHOP_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 1 in room 451 has its object trigger disabled.


class KeepInvisibleBridgeFrontChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrightBombPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 4 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 5 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeLeftChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = IceBombPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 6 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeBackChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 7 in room 322 has its object trigger disabled.


class KeepInvisibleBridgeCoin1Location(StandingLocationRow1):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 8 in room 322 has been removed from the room.


class KeepInvisibleBridgeCoin2Location(StandingLocationRow2):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 9 in room 322 has been removed from the room.


class KeepInvisibleBridgeCoin3Location(StandingLocationRow3):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 10 in room 322 has been removed from the room.


class KeepInvisibleBridgeCoin4Location(StandingLocationRow4):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_INVISIBLE_BRIDGE_COIN_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 11 in room 322 has been removed from the room.


class KeepXYPlatformsBackLeftChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 10 in room 458 has its object trigger disabled.


class KeepXYPlatformsFrontLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = RedEssencePrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 11 in room 458 has its object trigger disabled.


class KeepXYPlatformsFrontRightChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 12 in room 458 has its object trigger disabled.


class KeepXYPlatformsBackRightChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = FireBombPrize
    _rooms = [R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MOVING_PLATFORMS_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 13 in room 458 has its object trigger disabled.


class KeepElevatorRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ELEVATOR_PLATFORMS
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 8 in room 321 has its object trigger disabled.


class KeepCannonballRoomFrontRightChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 3 in room 457 has its object trigger disabled.


class KeepCannonballRoomBackChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 4 in room 457 has its object trigger disabled.


class KeepCannonballFrontLeftChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = PickMeUpPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 5 in room 457 has its object trigger disabled.


class KeepCannonballMidRightChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 6 in room 457 has its object trigger disabled.


class KeepCannonballMidLeftChestLocation(TreasureChestLocationRow5):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_5
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 7 in room 457 has its object trigger disabled.


class KeepCannonballCoin1Location(StandingLocationRow1):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 8 in room 457 has been removed from the room.


class KeepCannonballCoin2Location(StandingLocationRow2):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 9 in room 457 has been removed from the room.


class KeepCannonballCoin3Location(StandingLocationRow3):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_10]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 10 in room 457 has been removed from the room.


class KeepCannonballCoin4Location(StandingLocationRow4):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_11]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 11 in room 457 has been removed from the room.


class KeepCannonballCoin5Location(StandingLocationRow5):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_12]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_5
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 12 in room 457 has been removed from the room.


class KeepCannonballCoin6Location(StandingLocationRow6):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_13]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_6
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 13 in room 457 has been removed from the room.


class KeepCannonballCoin7Location(StandingLocationRow7):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_7
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 14 in room 457 has been removed from the room.


class KeepCannonballCoin8Location(StandingLocationRow8):
    _bias = True
    _originally_held = Coins10Prize
    _rooms = [R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING]
    _npc_ids = [NPC_15]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_CANNONBALL_ROOM_COIN_8
    _world_area = WorldAreaEnum.BOWSERS_KEEP

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 15 in room 457 has been removed from the room.


class KeepRotatingPlatformsFrontChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 1 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsFrontMidLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 2 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsBackMidRightChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FireBombPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 3 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsFrontMidRightChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_4]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 4 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsBackMidLeftChestLocation(TreasureChestLocationRow5):
    _bias = True
    _originally_held = PickMeUpPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_5
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 5 in room 455 has its object trigger disabled.


class KeepRotatingPlatformsBackChestLocation(TreasureChestLocationRow6):
    _bias = True
    _originally_held = KerokeroColaPrize
    _rooms = [
        R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS
    ]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_ROTATING_PLATFORMS_6
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory)

    # flag as checked: npc 6 in room 455 has its object trigger disabled.


class ObstacleCourseFinalFight(BossFightLocation):
    _bias = True
    _originally_held = ChesterBossFight
    _rooms = [R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_CHESTER
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _pack_id = PACK159_SIX_DOOR_RUSH_FIGHT
    _post_unlocks_event_id = E1235_OBSTACLE_COURSE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            NPC_4,
            sequence_setter_event_id=E0845_VOLCANO_BRIEF_HENCHMAN_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        )
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(
            self.prize,
            (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight),
        ):
            m = self.prize.smallest_npc()
            if m.animations.dojo_challenge is not None:
                a = m.animations.dojo_challenge
                cast(
                    ActionQueueAsync,
                    world.event_scripts.get_command_by_identifier(
                        "keep_obstacle_boss_intro",
                    ),
                ).set_subscript(
                    [
                        A_FaceSouthwest(),
                        A_VisibilityOn(),
                        A_Pause(35),
                        A_SetSpriteSequence(
                            index=a.sequence_id, looping=False, is_sequence=True
                        ),
                    ]
                )
            else:
                world.event_scripts.delete_command_by_identifier(
                    "keep_obstacle_boss_intro"
                )
        return op

    # Flag as checked: BATTLE_DOOR_BOSS_BIT


class ObstacleCourseFinalFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_CHESTER
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _parent = ObstacleCourseFinalFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: BATTLE_DOOR_BOSS_BIT


class KeepDoorRewardChest1Location(TreasureChestLocationRow1):
    _bias = True
    _originally_held = SonicCymbalPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_access_keep(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_1_PRIZE_RETRIEVED


class KeepDoorRewardChest2Location(TreasureChestLocationRow2):
    _bias = True
    _originally_held = SuperSlapPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_access_keep(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_2_PRIZE_RETRIEVED


class KeepDoorRewardChest3Location(TreasureChestLocationRow3):
    _bias = True
    _originally_held = DrillClawPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_access_keep(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_3_PRIZE_RETRIEVED


class KeepDoorRewardChest4Location(TreasureChestLocationRow4):
    _bias = True
    _originally_held = StarGunPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_4
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = not_earlygame(world, inventory)
        return can_access_keep(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_4_PRIZE_RETRIEVED


class KeepDoorRewardChest5Location(TreasureChestLocationRow5):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_5
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_access_keep(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_5_PRIZE_RETRIEVED


class KeepDoorRewardChest6Location(TreasureChestLocationRow6):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [
        R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
        R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
    ]
    _npc_ids = [NPC_0, NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_DOOR_REWARD_6
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = (
            not_earlygame(world, inventory)
            if world.settings.isflag_enabled(_get_flag("BowserDoorShuffle"))
            else True
        )
        return can_access_keep(world, inventory) and boss_condition

    # flag as checked: BK_OBSTACLE_6_PRIZE_RETRIEVED


class KeepAfterObstaclesBossFight(BossFightLocation):
    _bias = True
    _originally_held = KamekBossFight
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _pack_id = PACK209_KEEP_FIRST_BOSS
    _post_unlocks_event_id = E1236_KEEP_1_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0847_KEEP_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY,
            NPC_0,
            sequence_setter_event_id=E0848_KEEP_BATTLE_DOOR_2B_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY,
            NPC_0,
            sequence_setter_event_id=E0849_KEEP_BATTLE_DOOR_2C_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            NPC_0,
            sequence_setter_event_id=E0850_KEEP_BATTLE_DOOR_1A_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
            NPC_0,
            sequence_setter_event_id=E0851_KEEP_BATTLE_DOOR_1B_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            NPC_0,
            sequence_setter_event_id=E0846_KEEP_BATTLE_DOOR_1C_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
            NPC_0,
            sequence_setter_event_id=E0852_KEEP_BATTLE_DOOR_2A_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER_TROOPS_REPAIR,
            NPC_6,
            sequence_setter_event_id=E1192_ENDING_CREDITS_KEEP_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, KamekBossFight):
            world.event_scripts.delete_command_by_identifier("kamek_palette")
            m = self.prize.smallest_npc()
            if isinstance(
                self.prize,
                (PandoriteBossFight, HidonBossFight, BoxBoyBossFight, ChesterBossFight),
            ):
                cast(
                    ActionQueueAsync,
                    world.event_scripts.get_command_by_identifier(
                        "keep_boss_1_animation_aq"
                    ),
                ).set_subscript(get_mimic_rise_kamek())
                world.event_scripts.delete_command_by_identifier(
                    "keep_boss_1_animation_pause"
                )

            elif (
                m.animations.keep_challenge is not None
                and m.animations.keep_challenge.total_duration is not None
            ):
                world.event_scripts.get_subscript_command_by_identifier(
                    "keep_boss_1_animation_aq",
                    "keep_boss_1_animation",
                    A_SetSpriteSequence,
                ).set_index(m.animations.keep_challenge.sequence_id)
                cast(
                    Pause,
                    world.event_scripts.get_command_by_identifier(
                        "keep_boss_1_animation_pause",
                    ),
                ).set_length(m.animations.keep_challenge.total_duration)
            else:
                world.event_scripts.delete_command_by_identifier(
                    "keep_boss_1_animation_aq"
                )

            # rise script not used for box summon or battle halls, so have a separate if block
            if (
                m.animations.keep_summon is not None
                and m.animations.keep_summon.total_duration is not None
            ):
                world.action_scripts.get_command_by_identifier(
                    "keep_battle_room_summon", A_SetSpriteSequence
                ).set_index(m.animations.keep_summon.sequence_id)
                world.event_scripts.get_command_by_identifier(
                    "EVENT_941_pause_0", Pause
                ).set_length(m.animations.keep_summon.total_duration)
                world.event_scripts.get_script_by_id(
                    E0942_KEEP_FIRST_BOSS_SUMMON_CHEST
                ).set_contents(
                    [
                        ActionQueueAsync(
                            NPC_1,
                            [
                                A_FaceSoutheast(),
                                A_SetSpriteSequence(
                                    index=m.animations.keep_summon.sequence_id,
                                    is_sequence=True,
                                    looping=False,
                                    mirror_sprite=True,
                                ),
                                A_Pause(m.animations.keep_summon.total_duration),
                            ],
                        ),
                        Return(),
                    ]
                )
            else:
                world.event_scripts.get_script_by_id(
                    E0942_KEEP_FIRST_BOSS_SUMMON_CHEST
                ).set_contents(
                    [
                        ActionQueueAsync(NPC_1, [A_FaceSoutheast(), A_Pause(60)]),
                        Return(),
                    ]
                )
        return op

    # Flag as checked: KEEP_BOSS_1_DEFEATED


class KeepAfterObstaclesStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_1
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _parent = KeepAfterObstaclesBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: KEEP_BOSS_1_DEFEATED


class KeepAfterObstaclesBossChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = InfiniteCoinsPrize
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.BOWSERS_KEEP_MAGIKOOPA
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)

    def render(
        self, world: GameWorld | None = None
    ) -> tuple[list[list[UsableEventScriptCommand]], list[UsableEventScriptCommand]]:
        op = super().render(world)
        assert world is not None

        if not isinstance(self.prize, self._originally_held):
            # only colour the chest gold if it's vanilla
            world.event_scripts.delete_command_by_identifier(
                "infinite_coin_chest_palette"
            )
            # give it a random sound effect
            world.event_scripts.get_subscript_command_by_identifier(
                "infinite_coin_chest_aq", "infinite_coin_chest_sfx", A_PlaySound
            ).set_sound(random.randint(1, 162))
        return op

    # flag as checked: npc 0 in room 266 has its object trigger disabled.


class KeepChandelierBossFight(BossFightLocation):
    _bias = True
    _originally_held = BoomerBossFight
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 521
    _pack_id = PACK210_KEEP_SECOND_BOSS
    _post_unlocks_event_id = E1237_KEEP_CHANDELIER_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0853_KEEP_FINAL_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        if not isinstance(self.prize, BoomerBossFight):
            # Use VRAM-constrained selection (max 4096 for chandelier room)
            npc_model = self.prize.get_npc_for_slot(world, 4096)
            m = npc_model()
            if (
                m.animations.chandelier_challenge is not None
                and m.animations.chandelier_challenge.total_duration is not None
            ):
                world.event_scripts.get_subscript_command_by_identifier(
                    "chandelier_challenge_action_queue_0",
                    "chandelier_challenge",
                    A_SetSpriteSequence,
                ).set_index(m.animations.chandelier_challenge.sequence_id)
                world.event_scripts.get_subscript_command_by_identifier(
                    "chandelier_challenge_action_queue_0",
                    "chandelier_challenge_pause_45",
                    A_Pause,
                ).set_length(m.animations.chandelier_challenge.total_duration)
            else:
                world.event_scripts.delete_subscript_command_by_identifier(
                    "chandelier_challenge_action_queue_0",
                    "chandelier_challenge",
                )
        return op

    # Flag as checked: KEEP_BOSS_2_DEFEATED


class KeepChandelierStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_2
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 521
    _parent = KeepChandelierBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: KEEP_BOSS_2_DEFEATED


class KeepFinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = ExorBossFight
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 522
    _pack_id = PACK186_KEEP_THIRD_BOSS
    _post_unlocks_event_id = E1238_KEEP_EXIT_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(FactoryGate, FactoryGating.KEEP):
            content.extend(
                [
                    SetBit(MAP_GATE),
                    SetBit(MAP_DIRECTIONAL_BOWSERS_KEEP_GATE),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    # Flag as checked: KEEP_BOSS_3_DEFEATED


class KeepFinalStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _id = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_3
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM]
    _override_id = 522
    _parent = KeepFinalBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: KEEP_BOSS_3_DEFEATED


########## outer factory


class OuterFactorySaveRoomChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.FACTORY_SAVE_ROOM
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory)

    # flag as checked: npc 0 in room 237 has its object trigger disabled.


class FactoryBoltPlatformsChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = UltraHammerPrize
    _rooms = [R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.FACTORY_BOLT_PLATFORMS
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory)

    # flag as checked: npc 7 in room 239 has its object trigger disabled.


class FactoryEntranceBossFight(BossFightLocation):
    _bias = True
    _originally_held = CountdownBossFight
    _rooms = [R433_SMITHY_FACTORY_AREA_01_DUMMY]
    _id = ShuffleLocationSelector.FACTORY_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.FACTORY
    _pack_id = PACK174_FACTORY_FIRST_BOSS
    _post_unlocks_event_id = E1239_OUTER_FACTORY_1_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM,
            NPC_0,
            sequence_setter_event_id=E0854_ABYSS_1ST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM],
            [NPC_1],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM],
            [NPC_2],
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: ABYSS_BOSS_1_DEFEATED


class FactoryEntranceStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R433_SMITHY_FACTORY_AREA_01_DUMMY]
    _id = ShuffleLocationSelector.FACTORY_BOSS_1
    _world_area = WorldAreaEnum.FACTORY
    _parent = FactoryEntranceBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: ABYSS_BOSS_1_DEFEATED


class FactoryAxemConveyorsChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.FACTORY_FALLING_AXEMS
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 6 in room 434 has its object trigger disabled.


class FactoryTreasurePitBackChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.FACTORY_TREASURE_PIT_1
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 0 in room 443 has its object trigger disabled.


class FactoryTreasurePitFrontChestLocation(TreasureChestLocationRow3):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_2]
    _id = ShuffleLocationSelector.FACTORY_TREASURE_PIT_2
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 2 in room 443 has its object trigger disabled.


class FactoryBigConveyorRoomFirstChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RoyalSyrupPrize
    _rooms = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids = [NPC_8]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_1
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 8 in room 475 has its object trigger disabled.


class FactoryBigConveyorRoomSecondChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = MaxMushroomPrize
    _rooms = [
        R475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS
    ]
    _npc_ids = [NPC_9]
    _id = ShuffleLocationSelector.FACTORY_CONVEYOR_PLATFORMS_2
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 9 in room 475 has its object trigger disabled.


class FactoryBehindNinjasRightChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_1
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 1 in room 443 has its object trigger disabled.


class FactoryBehindNinjasLeftChestLocation(TreasureChestLocationRow4):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [
        R443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM
    ]
    _npc_ids = [NPC_3]
    _id = ShuffleLocationSelector.FACTORY_BEHIND_SNAKES_2
    _world_area = WorldAreaEnum.FACTORY
    _blacklist = [EXPStarPrize]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: npc 3 in room 443 has its object trigger disabled.


class FactoryTransitionBossFight(BossFightLocation):
    _bias = True
    _originally_held = CloakerDominoBossFight
    _rooms = [R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM]
    _id = ShuffleLocationSelector.FACTORY_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.FACTORY
    _pack_id = PACK184_FACTORY_SECOND_BOSS
    _post_unlocks_event_id = E1240_OUTER_FACTORY_2_BOSS_UNLOCKS

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: ABYSS_BOSS_2_DEFEATED


class FactoryTransitionStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM]
    _id = ShuffleLocationSelector.FACTORY_BOSS_2
    _world_area = WorldAreaEnum.FACTORY
    _parent = FactoryTransitionBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: ABYSS_BOSS_2_DEFEATED


########## inner factory


class InnerFactoryFirstFight(BossFightLocation):
    _bias = True
    _originally_held = ClerkBossFight
    _rooms = [R469_FACTORY_GROUNDS_AREA_01]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK146_FACTORY_BOSS_RUSH_1
    _post_unlocks_event_id = E1241_INNER_FACTORY_1_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R469_FACTORY_GROUNDS_AREA_01,
            NPC_8,
            sequence_setter_event_id=E0855_INNER_FACTORY_1ST_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]

    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R469_FACTORY_GROUNDS_AREA_01],
            [NPC_7],
            PACK150_FACTORY_BOSS_RUSH_HENCHMAN,
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
        BossFightLocationHenchmanNPC(
            [R469_FACTORY_GROUNDS_AREA_01],
            [NPC_6],
            skip_swap_if_flag="KeepMinigameSpritesIntact",
            remove_if_not_filled=RemoveIfNotFilled.IF_ANY_FILLED,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: INNER_FACTORY_ROOM_1_COMPLETED


class InnerFactoryFirstFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R469_FACTORY_GROUNDS_AREA_01]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_1
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactoryFirstFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: INNER_FACTORY_ROOM_1_COMPLETED


class InnerFactoryToadGiftLocation(NPCLocationRow1):
    _bias = True
    _originally_held = RockCandyPrize
    _rooms = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _id = ShuffleLocationSelector.FACTORY_TOAD_GIFT
    _world_area = WorldAreaEnum.INNER_FACTORY

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # flag as checked: TOAD_SHOP_FREEBIE_RECEIVED


class InnerFactorySecondFight(BossFightLocation):
    _bias = True
    _originally_held = ManagerBossFight
    _rooms = [R471_FACTORY_GROUNDS_AREA_02]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_2
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK147_FACTORY_BOSS_RUSH_2
    _post_unlocks_event_id = E1242_INNER_FACTORY_2_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R471_FACTORY_GROUNDS_AREA_02,
            NPC_15,
            sequence_setter_event_id=E0856_INNER_FACTORY_2ND_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R471_FACTORY_GROUNDS_AREA_02],
            [NPC_12],
            remove_if_not_filled=RemoveIfNotFilled.ALWAYS,
        ),
        BossFightLocationHenchmanNPC(
            [R471_FACTORY_GROUNDS_AREA_02],
            [NPC_13],
            remove_if_not_filled=RemoveIfNotFilled.ALWAYS,
        ),
        BossFightLocationHenchmanNPC(
            [R471_FACTORY_GROUNDS_AREA_02],
            [NPC_14],
            remove_if_not_filled=RemoveIfNotFilled.ALWAYS,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        if isinstance(self.prize, self._originally_held):
            return op
        assert isinstance(self.prize, BossFightPrize)
        render_inner_factory_second_fight(world, self.prize)
        return op

    # Flag as checked: INNER_FACTORY_ROOM_2_COMPLETED


class InnerFactorySecondFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R471_FACTORY_GROUNDS_AREA_02]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_2
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactorySecondFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: INNER_FACTORY_ROOM_2_COMPLETED


class InnerFactoryThirdFight(BossFightLocation):
    _bias = True
    _originally_held = DirectorBossFight
    _rooms = [R472_FACTORY_GROUNDS_AREA_03]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_3
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK148_FACTORY_BOSS_RUSH_3
    _post_unlocks_event_id = E1243_INNER_FACTORY_3_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R472_FACTORY_GROUNDS_AREA_03,
            NPC_10,
            sequence_setter_event_id=E0857_INNER_FACTORY_3RD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_7]),
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_8]),
        BossFightLocationHenchmanNPC([R472_FACTORY_GROUNDS_AREA_03], [NPC_9]),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)

        # Process each slot separately
        for slot_index in range(3):
            if (
                self.prize.character_henchmen is not None
                and len(self.prize.character_henchmen) > slot_index
            ):
                render_inner_factory_third_fight_slot(
                    world, self.prize.character_henchmen[slot_index], slot_index
                )

        return op

    # Flag as checked: npc 10 in room 472 removed


class InnerFactoryThirdFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R472_FACTORY_GROUNDS_AREA_03]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_3
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactoryThirdFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: npc 10 in room 472 removed


class InnerFactoryFourthFight(BossFightLocation):
    _bias = True
    _originally_held = GunyolkBossFight
    _rooms = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_4
    _world_area = WorldAreaEnum.INNER_FACTORY
    _pack_id = PACK149_FACTORY_BOSS_RUSH_4
    _post_unlocks_event_id = E1244_INNER_FACTORY_4_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
            NPC_12,
            sequence_setter_event_id=E0858_INNER_FACTORY_4TH_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM], [NPC_0]
        ),
    ]

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        # If the prize is not the original GunyolkBossFight, hide NPCs 0-6 in room 470
        if not isinstance(self.prize, GunyolkBossFight):
            render_inner_factory_fourth_fight(world)
        return op

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_factory(world, inventory) and not_earlygame(world, inventory)

    # Flag as checked: INNER_FACTORY_ROOM_4_COMPLETED


class InnerFactoryFourthFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_4
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = InnerFactoryFourthFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: INNER_FACTORY_ROOM_4_COMPLETED


class FinalBossFight(BossFightLocation):
    _bias = True
    _originally_held = SmithyBossFight
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FIGHT_FINAL
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _rooms = [R509_FACTORY_GROUNDS_SMITHYS_PAD]
    _pack_id = PACK185_FINAL_BOSS
    _post_unlocks_event_id = E1245_INNER_FACTORY_5_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R509_FACTORY_GROUNDS_SMITHYS_PAD,
            NPC_4,
            sequence_setter_event_id=E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R469_FACTORY_GROUNDS_AREA_01,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R471_FACTORY_GROUNDS_AREA_02,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
                R472_FACTORY_GROUNDS_AREA_03,
            ],
            [
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_7,
                NPC_8,
                NPC_9,
                NPC_10,
                NPC_11,
                NPC_15,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
                NPC_7,
                NPC_8,
                NPC_9,
                NPC_10,
                NPC_11,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_5,
                NPC_6,
            ],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_factory_final_boss(world, inventory)

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        op = super().render(world)
        assert isinstance(self.prize, BossFightPrize)
        # Replace event scripts for non-Smithy boss in Smithy's location
        if not isinstance(self.prize, SmithyBossFight):
            render_final_boss_fight(world, self.prize)
        return op

    # Flag as checked: FACTORY_BOSS_DEFEATED


class FinalBossFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece7
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FINAL
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _parent = FinalBossFight

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )

    # Flag as checked: FACTORY_BOSS_DEFEATED


########## invisible flag check pool

# Three of the following locations will be chosen at random and included in the seed. If the setting is disabled, then it will be the first three (defaults).
# In a tracker, their exact locations should not be known, but these will be considered checked when a certain bit is set.
# INVISIBLE_FLAG_1_FOUND, INVISIBLE_FLAG_2_FOUND, INVISIBLE_FLAG_3_FOUND


class MariosPadBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _x_coord = 3
    _y_coord = 11
    _world_area = WorldAreaEnum.MARIOS_PAD
    _clue_text = """\n My item's underneath a green bed.[await]"""

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) or world.settings.isflag_enabled(SkipMustyFearsSequence)


class RoseTownSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord = 10
    _y_coord = 47
    _world_area = WorldAreaEnum.ROSE_TOWN
    _clue_text = """\n My item's behind a wooden flower.[await]"""

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) or world.settings.isflag_enabled(SkipMustyFearsSequence)


class YosterIsleGoalFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R034_YOSTER_ISLE]
    _x_coord = 21
    _y_coord = 62
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _y_shift = -4
    _clue_text = """\n My item's between "O" and "A".[await]"""

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_pipe_vault(world, inventory) and (
            can_access_monstro_town(world, inventory)
            or world.settings.isflag_enabled(SkipMustyFearsSequence)
        )


class MariosPadSteamwhistleFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R016_MARIOS_PAD]
    _x_coord = 11
    _y_coord = 34
    _world_area = WorldAreaEnum.MARIOS_PAD
    _z_coord = 1
    _clue_text = "\n  Mine is underneath a steamwhistle.[await]"

    # All other flag locations are in logic only after you can talk to the musty fears because otherwise how tf would you know where to look?
    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MariosPadLanternFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R016_MARIOS_PAD]
    _x_coord = 13
    _y_coord = 35
    _world_area = WorldAreaEnum.MARIOS_PAD
    _x_shift = 8
    _y_shift = -8
    _clue_text = "\n    Mine is under a white lantern.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MariosPadHatFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _x_coord = 3
    _y_coord = 13
    _world_area = WorldAreaEnum.MARIOS_PAD
    _z_coord = 1
    _clue_text = """\n      My item's under a red hat.[await]"""

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MushroomWayTreeFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R204_MUSHROOM_WAY_AREA_02]
    _x_coord = 11
    _y_coord = 16
    _world_area = WorldAreaEnum.MUSHROOM_WAY
    _z_coord = 3
    _x_shift = -16
    _clue_text = " Mine's under a tree, up on a ledge\n by itself.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MushroomKingdomSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _x_coord = 22
    _y_coord = 116
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _z_coord = 2
    _y_shift = -8
    _clue_text = "\n  Mine's behind a wooden mushroom.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MushroomKingdomEmptyHouseFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R482_MUSHROOM_KINGDOM_DURING_MACK_RAZ_AND_RAINIS_HOUSE,
        R490_MUSHROOM_KINGDOM_RAZ_AND_RAINIS_HOUSE,
    ]
    _x_coord = 14
    _y_coord = 61
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _y_shift = 8
    _clue_text = " Mine is under the bed in an empty\n house.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class ChancellorThroneFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
        R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
    ]
    _x_coord = 19
    _y_coord = 24
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _z_coord = 3
    _clue_text = "\n       Mine's under a blue chair.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BanditsWayFlowerFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R207_BANDITS_WAY_AREA_02]
    _x_coord = 25
    _y_coord = 89
    _world_area = WorldAreaEnum.BANDITS_WAY
    _x_shift = 16
    _clue_text = "\n      Mine's on a landing flower.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_bandits_way(
            world, inventory
        )


class KeroStairsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS]
    _x_coord = 5
    _y_coord = 41
    _world_area = WorldAreaEnum.KERO_SEWERS
    _z_coord = 4
    _y_shift = 8
    _clue_text = " Mine's in a corner, nearby lots of\n dank stairs.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sewer(
            world, inventory
        )


class KeroGateFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE]
    _x_coord = 4
    _y_coord = 88
    _world_area = WorldAreaEnum.KERO_SEWERS
    _z_coord = 4
    _x_shift = -16
    _clue_text = "\n Mine is by a lone metal spike fence.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sewer(
            world, inventory
        )


class MidasTreesFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _x_coord = 24
    _y_coord = 26
    _world_area = WorldAreaEnum.MIDAS_RIVER
    _x_shift = -8
    _clue_text = " Mine's between a lone pair of\n palm trees, near water.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class TadpoleCabinetFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _x_coord = 25
    _y_coord = 29
    _world_area = WorldAreaEnum.TADPOLE_POND
    _z_coord = 2
    _x_shift = 8
    _y_shift = 8
    _clue_text = "\n       Mine is in a frog cabinet.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseWayDirtPatchFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    _x_coord = 25
    _y_coord = 88
    _world_area = WorldAreaEnum.ROSE_WAY
    _clue_text = " Mine is in the middle of a HUGE\n patch of dirt.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord = 15
    _y_coord = 63
    _world_area = WorldAreaEnum.ROSE_TOWN
    _y_shift = -8
    _clue_text = "\n  Mine is under a low steel hydrant.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownSinkFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R089_ROSE_TOWN_DURING_BOWYER_THREE_GRANDKIDS_HOUSE,
        R090_ROSE_TOWN_THREE_GRANDKIDS_HOUSE,
    ]
    _x_coord = 15
    _y_coord = 10
    _world_area = WorldAreaEnum.ROSE_TOWN
    _y_shift = 1
    _clue_text = "\n My item is in a kitchen sink under\n some green curtains.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownBowserFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R085_ROSE_TOWN_DURING_BOWYER_INN_1F,
        R086_ROSE_TOWN_INN_1F,
    ]
    _x_coord = 7
    _y_coord = 21
    _world_area = WorldAreaEnum.ROSE_TOWN
    _clue_text = "\n   Mine's under a miniature turtle.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class RoseTownGardenerHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord = 2
    _y_coord = 85
    _world_area = WorldAreaEnum.ROSE_TOWN
    _y_shift = -8
    _clue_text = "\n   Mine is under a private hydrant.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_clear_forest(world, inventory)
            and can_clear_chapel(world, inventory)
        )


class RoseTownGardenerBucketFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord = 5
    _y_coord = 87
    _world_area = WorldAreaEnum.ROSE_TOWN
    _clue_text = "\n   Mine is under a private bucket.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_clear_forest(world, inventory)
            and can_clear_chapel(world, inventory)
        )


class RoseTownGardenerLeafFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _x_coord = 4
    _y_coord = 111
    _world_area = WorldAreaEnum.ROSE_TOWN
    _z_coord = 10
    _clue_text = "\n Mine's on a big leaf between\n two chests.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and inventory.has_item(SeedPrize)
            and inventory.has_item(FertilizerPrize)
            and can_clear_forest(world, inventory)
            and can_clear_chapel(world, inventory)
        )


class ForestMazeSecretStumpFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R231_FOREST_MAZE_SECRET_ENTRANCE]
    _x_coord = 18
    _y_coord = 72
    _world_area = WorldAreaEnum.FOREST_MAZE
    _x_shift = 16
    _clue_text = " Mine is behind a brightly\n illuminated tree stump.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_forest(
            world, inventory
        )


class ForestMazeSecretMushroomsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R235_FOREST_MAZE_AREA_08_UNDERGROUND]
    _x_coord = 25
    _y_coord = 93
    _world_area = WorldAreaEnum.FOREST_MAZE
    _x_shift = -8
    _y_shift = 8
    _clue_text = " Mine is on an illuminated pack of\n 5 mushrooms.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_forest(
            world, inventory
        )


class ForestMazeSecretWigglerFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER]
    _x_coord = 2
    _y_coord = 39
    _world_area = WorldAreaEnum.FOREST_MAZE
    _clue_text = "\n        Mine is on a sleepy bug.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_forest(
            world, inventory
        )


class PipeVaultExteriorFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R055_PIPE_VAULT_ENTRANCE]
    _x_coord = 17
    _y_coord = 19
    _world_area = WorldAreaEnum.PIPE_VAULT
    _x_shift = -8
    _y_shift = 8
    _clue_text = " Mine is by a pipe in the middle of\n the road.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_pipe_vault(
            world, inventory
        )


class PipeVaultRedPipeFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R129_PIPE_VAULT_AREA_05]
    _x_coord = 21
    _y_coord = 107
    _world_area = WorldAreaEnum.PIPE_VAULT
    _x_shift = -8
    _y_shift = -8
    _clue_text = "\n     Mine is behind a low red pipe.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_pipe_vault(
            world, inventory
        )


class YosterIsleHutFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R034_YOSTER_ISLE]
    _x_coord = 11
    _y_coord = 70
    _world_area = WorldAreaEnum.YOSTER_ISLE
    _clue_text = "\n         Mine's in a fruity hut.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_pipe_vault(
            world, inventory
        )


class MolevilleHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 6
    _y_coord = 63
    _world_area = WorldAreaEnum.MOLEVILLE
    _y_shift = -8
    _clue_text = "\n     Mine's under a gold hydrant.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleMountainBushFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord = 19
    _y_coord = 31
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 12
    _clue_text = " Mine's in a bush at the top of\n a mountain.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R337_MOLEVILLE_INN]
    _x_coord = 6
    _y_coord = 12
    _world_area = WorldAreaEnum.MOLEVILLE
    _x_shift = 16
    _clue_text = "\n       Mine's under a middle bed.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MolevilleMinesArrowsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE]
    _x_coord = 5
    _y_coord = 51
    _world_area = WorldAreaEnum.MOLEVILLE
    _clue_text = " Mine's between two arrows,\n pointing away from each other.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) and can_access_moleville_entrance(world, inventory)


class MolevilleMinesCeilingFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM]
    _x_coord = 8
    _y_coord = 13
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 4
    _clue_text = " Mine's in a zig-zag room, up\n on the ceiling.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(
            world, inventory
        ) and can_access_moleville_entrance(world, inventory)


class MolevilleMinesEntryFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING]
    _x_coord = 22
    _y_coord = 23
    _world_area = WorldAreaEnum.MOLEVILLE
    _z_coord = 3
    _x_shift = 16
    _clue_text = '\n My item?[delay]\n ...[delay]It\'s on the word "IN",\n [delay]above a big hole.[await]'

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_mines(
            world, inventory
        )


class BoosterPassCornerBushFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R101_BOOSTER_PASS_AREA_02]
    _x_coord = 17
    _y_coord = 112
    _world_area = WorldAreaEnum.BOOSTER_PASS
    _x_shift = -8
    _y_shift = 8
    _clue_text = "\n        Mine's in a corner bush.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BoosterTowerExteriorSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R202_BOOSTER_TOWER_ENTRANCE]
    _x_coord = 4
    _y_coord = 110
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = 16
    _clue_text = " Mine's behind a sign with Japanese\n letters.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BoosterTowerDeskFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM]
    _x_coord = 24
    _y_coord = 113
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = 16
    _clue_text = '\n      Mine\'s under "B" and "K".[await]'

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerMasherRoomFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER]
    _x_coord = 19
    _y_coord = 122
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _y_shift = 8
    _clue_text = "\n Mine's on a lightly-loaded see-saw.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerCurtainFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS]
    _x_coord = 7
    _y_coord = 64
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _z_coord = 9
    _y_shift = 8
    _clue_text = " Mine's in a corner, between a\n window and a red curtain.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerThwompInvisibleFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER]
    _x_coord = 5
    _y_coord = 114
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _z_coord = 12
    _clue_text = "\n     Mine is near a lonely thwomp.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerBrokenFrameFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    _x_coord = 15
    _y_coord = 83
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = -8
    _y_shift = -9
    _clue_text = "\n       Mine is in a broken frame.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerBeetleCageFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord = 7
    _y_coord = 18
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _clue_text = "\n     Mine is on an insect cage.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class BoosterTowerToyBoxFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord = 7
    _y_coord = 24
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _x_shift = 16
    _clue_text = "\n       Mine is behind a toy box.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_tower(
            world, inventory
        )


class MarrymoreOutsideCrateFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R005_MARRYMORE_OUTSIDE_DURING_BOOSTER,
        R064_MARRYMORE_OUTSIDE,
    ]
    _x_coord = 23
    _y_coord = 60
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 6
    _x_shift = -8
    _y_shift = -8
    _clue_text = "\n  Mine is under a lone backyard box.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreHallwayFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R011_MARRYMORE_INN_3F]
    _x_coord = 18
    _y_coord = 76
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 3
    _clue_text = " My item is in a flower pot in a\n hallway.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreSuiteBedFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R012_MARRYMORE_INN_SUITE_ROOM]
    _x_coord = 7
    _y_coord = 13
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 6
    _x_shift = -16
    _clue_text = " Mine's beneath two adjoined\n red beds.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreKitchenFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R155_MARRYMORE_CHAPEL_KITCHEN]
    _x_coord = 2
    _y_coord = 20
    _world_area = WorldAreaEnum.MARRYMORE
    _x_shift = -8
    _y_shift = 8
    _clue_text = " Mine is in a big cabinet full of\n dishes.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreFireplaceFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R152_MARRYMORE_CHAPEL_MAIN_HALL]
    _x_coord = 9
    _y_coord = 33
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 2
    _y_shift = -8
    _clue_text = "\n    Mine is in an empty fireplace.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MarrymoreOrganFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    ]
    _x_coord = 23
    _y_coord = 65
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 1
    _x_shift = -16
    _clue_text = " Mine is behind a big musical\n instrument.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_chapel(
            world, inventory
        )


class MarrymoreAltarFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    ]
    _x_coord = 23
    _y_coord = 70
    _world_area = WorldAreaEnum.MARRYMORE
    _z_coord = 1
    _clue_text = "\n        Mine's behind a podium.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_chapel(
            world, inventory
        )


class StarHillNorthStarFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R158_STAR_HILL_AREA_02]
    _x_coord = 8
    _y_coord = 69
    _world_area = WorldAreaEnum.STAR_HILL
    _z_coord = 2
    _x_shift = -10
    _clue_text = "\n     Mine is atop the North Star.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownAnchorFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 14
    _y_coord = 57
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _x_shift = 16
    _clue_text = "\n       Mine is behind an anchor.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownHydrantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 16
    _y_coord = 25
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _z_coord = 5
    _x_shift = 0
    _y_shift = -8
    _clue_text = "\n  Mine is under a high steel hydrant.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownBucketFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord = 20
    _y_coord = 31
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _z_coord = 3
    _clue_text = "\n Mine is in a bucket between two\n staircases.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownFlowersFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST,
        R313_SEASIDE_TOWN_ACCESSORY_SHOP,
    ]
    _x_coord = 26
    _y_coord = 60
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _y_shift = 8
    _clue_text = " Mine's in the middle of three\n pink flowers.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class SeasideTownShedBoxFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R314_SEASIDE_TOWN_SHED]
    _x_coord = 5
    _y_coord = 23
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _y_shift = 8
    _clue_text = " Mine's under a lone crate in an\n empty house.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_clear_seaside_boss(world, inventory)
            and inventory.has_item(ShedKeyPrize)
        )


class SeaArrowFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord = 8
    _y_coord = 21
    _world_area = WorldAreaEnum.SEA
    _x_shift = -8
    _y_shift = -8
    _clue_text = "\n   Mine is beside a mossy up-arrow.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class SeaBoxesFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord = 9
    _y_coord = 36
    _world_area = WorldAreaEnum.SEA
    _y_shift = -8
    _clue_text = "\n    Mine's in some V-shaped boxes.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class SeaStalagnateFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _x_coord = 18
    _y_coord = 43
    _world_area = WorldAreaEnum.SEA
    _z_coord = 6
    _x_shift = -8
    _y_shift = -8
    _clue_text = " Mine is behind a big gray\n stalagnate.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class SeaUnderwaterSailFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R174_SEA_AREA_08_SHORE_WITH_SUNKEN_SHIP]
    _x_coord = 4
    _y_coord = 41
    _world_area = WorldAreaEnum.SEA
    _clue_text = "\n        Mine's behind a big sail.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipBarrelPileFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R162_SUNKEN_SHIP_AREA_04_GREAPERS_DRY_BONES]
    _x_coord = 7
    _y_coord = 66
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _z_coord = 3
    _clue_text = "\n  Mine is atop a big pile of barrels.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipDoorMarkerFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY]
    _x_coord = 18
    _y_coord = 82
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _z_coord = 1
    _y_shift = 8
    _clue_text = ' Mine is on a stack of boxes.[await][pause]\n[delay] Hm?[delay] Is that not specific enough?[await][page]\n Well,[delay] the boxes act as a door\n marker.[delay] They represent the\n number "4".[await]'

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipButtonFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R166_SUNKEN_SHIP_PUZZLE_ROOM_1]
    _x_coord = 16
    _y_coord = 133
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _clue_text = "\n   Mine is under a floating button.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_sea(
            world, inventory
        )


class ShipSwitchFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _x_coord = 17
    _y_coord = 121
    _world_area = WorldAreaEnum.SUNKEN_SHIP
    _clue_text = (
        '\n Mine is underneath a floating "J"\n that is all on its lonesome.[await]'
    )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_ship(
            world, inventory
        )


class LandsEndPlatformFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R137_LANDS_END_AREA_01]
    _x_coord = 6
    _y_coord = 29
    _world_area = WorldAreaEnum.LANDS_END
    _clue_text = "\n   Mine is under a rising platform.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class LandsEndCannonFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL]
    _x_coord = 11
    _y_coord = 115
    _world_area = WorldAreaEnum.LANDS_END
    _y_shift = -8
    _clue_text = " Mine's under a big and quiet\n cannon.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndArrowFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS]
    _x_coord = 28
    _y_coord = 29
    _world_area = WorldAreaEnum.LANDS_END
    _x_shift = 16
    _clue_text = "\n Mine is beside an orange up-arrow.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndHillFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R404_LANDS_END_DESERT_AREA_04]
    _x_coord = 23
    _y_coord = 96
    _world_area = WorldAreaEnum.LANDS_END
    _x_shift = 8
    _y_shift = 8
    _clue_text = " Mine is on a short, red hill in a\n remote area.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndTwoHillFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R319_LANDS_END_DESERT_AREA_06]
    _x_coord = 8
    _y_coord = 121
    _world_area = WorldAreaEnum.LANDS_END
    _clue_text = "   My item's between two red hills.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndStalagmiteFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R265_LANDS_END_UNDERGROUND_AREA_03]
    _x_coord = 22
    _y_coord = 80
    _world_area = WorldAreaEnum.LANDS_END
    _x_shift = 8
    _y_shift = 8
    _clue_text = (
        " Mine's on a big stalagmite\n formation in an underground cave.[await]"
    )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndCliffBushFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _x_coord = 23
    _y_coord = 103
    _world_area = WorldAreaEnum.LANDS_END
    _z_coord = 22
    _clue_text = " Mine is on a bush, way up high on\n a cliff.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class LandsEndSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _x_coord = 24
    _y_coord = 118
    _world_area = WorldAreaEnum.LANDS_END
    _z_coord = 0
    _y_shift = -4
    _x_shift = 8
    _clue_text = "     My item's on a yellow arrow.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_lands_end(
            world, inventory
        )


class DojoBonsaiFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _x_coord = 6
    _y_coord = 9
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _y_shift = 8
    _clue_text = "\n   Mine's underneath a bonsai tree.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroEntranceSignFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R267_MONSTRO_TOWN_ENTRANCE]
    _x_coord = 9
    _y_coord = 102
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _clue_text = "\n     Mine's in a lone flowery bush.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroBatFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _x_coord = 5
    _y_coord = 51
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _z_coord = 4
    _y_shift = 8
    _clue_text = "\n     Mine's behind a wooden bat.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroFanFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R395_MONSTRO_TOWN_MONSTERMAMAS_HOUSE_1F]
    _x_coord = 12
    _y_coord = 80
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _z_coord = 1
    _x_shift = -16
    _clue_text = "\n         Mine's beside a fan.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class MonstroShellFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP]
    _x_coord = 16
    _y_coord = 15
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _z_coord = 1
    _y_shift = 8
    _clue_text = "\n   Mine's beneath a spinning shell.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BeanValleyPipeFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R252_BEAN_VALLEY_MAIN_AREA]
    _x_coord = 17
    _y_coord = 85
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _z_coord = 1
    _x_shift = -16
    _clue_text = " Mine's on an isolated, dead-end\n pipe.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class BeanValleyBeanstalkBlockFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA]
    _x_coord = 27
    _y_coord = 27
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _clue_text = "\n  Mine's underneath a big beanstalk.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory)


class CasinoBellFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _x_coord = 14
    _y_coord = 19
    _world_area = WorldAreaEnum.CASINO
    _x_shift = 8
    _y_shift = 8
    _clue_text = "\n       Mine is beside a tiny bell.[await][pause]\n I don't think it does anything.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and inventory.has_item(
            BrightCardPrize
        )


class NimbusGoldGoombaFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R341_NIMBUS_LAND_GARROS_HOUSE]
    _x_coord = 5
    _y_coord = 14
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 1
    _clue_text = "\n     Mine is on a golden Goomba.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_outer_nimbus(
            world, inventory
        )


class NimbusInnLobbyFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R343_NIMBUS_LAND_INN]
    _x_coord = 6
    _y_coord = 84
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 2
    _x_shift = -8
    _y_shift = -8
    _clue_text = " Mine is under a stove with two\n pots.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_outer_nimbus(
            world, inventory
        )


class NimbusPlantFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [
        R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT
    ]
    _x_coord = 27
    _y_coord = 74
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 1
    _clue_text = " Mine is behind a big potted plant\n in a corner.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_nimbus_castle(
            world, inventory
        )


class NimbusBirdFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _x_coord = 28
    _y_coord = 48
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _y_shift = -8
    _clue_text = " Mine is under a birdcage, in a\n restricted dead-end area.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_nimbus_boss(
            world, inventory
        )


class NimbusHotSpringsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R447_NIMBUS_LAND_HOT_SPRINGS]
    _x_coord = 19
    _y_coord = 114
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _z_coord = 5
    _clue_text = " Mine's on the right side of a\n hot pool.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_clear_nimbus_boss(
            world, inventory
        )


class VolcanoShipsFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R353_VOLCANO_AREA_18_HINO_MART]
    _x_coord = 11
    _y_coord = 61
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _z_coord = 2
    _clue_text = "\n    Mine is between two vehicles.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_volcano(
            world, inventory
        )


class KeepPostObstacleBossRoomFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _x_coord = 26
    _y_coord = 97
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _x_shift = 8
    _y_shift = 8
    _clue_text = "\n    Mine is between two red doors.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_access_keep(world, inventory)
            and not_earlygame(world, inventory)
        )


class KeepThwompFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM]
    _x_coord = 19
    _y_coord = 47
    _world_area = WorldAreaEnum.BOWSERS_KEEP
    _clue_text = "\n      Mine is under a big thwomp.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_access_keep(world, inventory)
            and not_earlygame(world, inventory)
        )


class FactoryCanopyFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R220_SMITHY_FACTORY_AREA_02_WSAVE_POINT]
    _x_coord = 16
    _y_coord = 15
    _world_area = WorldAreaEnum.FACTORY
    _z_coord = 10
    _y_shift = 8
    _clue_text = "  My item's under a bolted canopy.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_factory(
            world, inventory
        )


class FactoryLugnutFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER]
    _x_coord = 23
    _y_coord = 52
    _world_area = WorldAreaEnum.FACTORY
    _z_coord = 7
    _clue_text = "    My item's underneath a lugnut.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and can_access_factory(
            world, inventory
        )


class FactoryTrampolineFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R507_SMITHY_FACTORY_AREA_08_TRAMPOLINE_AFTER_COUNT_DOWN]
    _x_coord = 14
    _y_coord = 9
    _world_area = WorldAreaEnum.FACTORY
    _y_shift = 16
    _clue_text = " My item is with the world's\n loneliest trampoline.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )


class FactoryButtonFlag(InvisibleFlagLocation):
    _bias = True
    _rooms = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _x_coord = 4
    _y_coord = 36
    _world_area = WorldAreaEnum.INNER_FACTORY
    _z_coord = 5
    _clue_text = " Mine is on a jammed machine\n button.[await]"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )


########## Mixins


def can_defeat_bosses(world: GameWorld, inventory: Inventory, count: int) -> bool:
    if world.settings.is_flag_value(
        ProgressionLogicDifficulty, ProgressionLogicDifficultyOptions.HARD
    ):
        return True
    return inventory.has_item_count(BossFightPrize, count)


def not_earlygame(world: GameWorld, inventory: Inventory) -> bool:
    return can_defeat_bosses(world, inventory, 5)


#    return can_defeat_bosses(world, inventory, 0)
# setting to 0 as a test
# having this restriction makes it difficult for seeds to succeed with highly restrictive logic
# at that point i think it's kinda on you if you want to make your own life that difficult


def all_starters_places(world: GameWorld, inventory: Inventory) -> bool:
    strchars = world.settings.get_flag(StartingCharacters)
    startmax = len(strchars.enabled)
    return inventory.has_item_count(CharacterPrize, startmax)


def can_access_bandits_way(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Bandit's Way."""
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MALLOW):
        return inventory.has_item(MallowRecruitmentPrize)
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.HAMMER_BRO):
        return inventory.has_item(HammerBrosFight)
    # Mushroom Way: true
    return True


def can_access_sewer(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Kero Sewers."""
    if can_access_lands_end(world, inventory):
        return True
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.MALLOW):
        return inventory.has_item(MallowRecruitmentPrize)
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.MACK):
        return inventory.has_item(MackBossFight)
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.KINGDOM):
        return can_access_bandits_way(world, inventory)
    if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.RFC):
        return can_access_bandits_way(world, inventory) and inventory.has_item(
            RareFrogCoinPrize
        )
    return True


def can_access_forest(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Forest Maze."""
    if world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.PIE):
        return inventory.has_item(CricketPiePrize)
    return True


def can_clear_forest(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Forest Maze."""
    return can_access_forest(world, inventory)


def can_access_pipe_vault(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Pipe Vault."""
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.GENO):
        return inventory.has_item(GenoRecruitmentPrize)
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.FOREST):
        return can_clear_forest(world, inventory)
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.BOWYER):
        return inventory.has_item(BowyerBossFight)
    return True


def can_access_moleville_entrance(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the uper entrance to the mines."""
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.GENO):
        return inventory.has_item(GenoRecruitmentPrize)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.FOREST):
        return can_access_forest(world, inventory)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOWYER):
        return inventory.has_item(BowyerBossFight)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOSHI):
        return can_access_pipe_vault(world, inventory)
    return True


def can_access_inner_mines(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the inner half
    of Moleville Mines (beyond the exploding wall)."""
    return can_access_moleville_entrance(world, inventory) and inventory.has_item(
        BambinoBombPrize
    )


def can_clear_mines(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Moleville Mines."""
    return can_access_inner_mines(world, inventory)


def can_access_moleville_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Moleville."""
    return (
        can_access_inner_mines(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_tower(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to enter Booster Tower."""
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MARIO):
        return inventory.has_item(MarioRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MALLOW):
        return inventory.has_item(MallowRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.GENO):
        return inventory.has_item(GenoRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.BOWSER):
        return inventory.has_item(BowserRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.TOADSTOOL):
        return inventory.has_item(ToadstoolRecruitmentPrize)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MINES):
        return can_access_inner_mines(world, inventory)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.PUNCHINELLO):
        return inventory.has_item(PunchinelloBossFight)
    return True


def can_access_tower_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Booster Tower."""
    return (
        can_access_tower(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_hill(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Booster Hill."""
    if world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.TOWER):
        return can_access_tower(world, inventory)
    if world.settings.is_flag_value(BoosterHillGate, BoosterHillGating.KGGG):
        return inventory.has_item(KnifeGuyGrateGuyBossFight)
    return True


def can_access_chapel(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to enter the Marrymore chapel."""
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.TOWER):
        return can_access_tower(world, inventory)
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.KGGG):
        return inventory.has_item(KnifeGuyGrateGuyBossFight)
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.HILL):
        return can_access_hill(world, inventory)
    return True


def can_clear_chapel(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss of Marrymore."""
    return (
        inventory.has_item(ShoesPrize)
        and inventory.has_item(RingPrize)
        and inventory.has_item(BroochPrize)
        and inventory.has_item(CrownPrize)
        and can_access_chapel(world, inventory)
        and not_earlygame(world, inventory)
    )


def can_access_chapel_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Marrymore."""
    return (
        can_clear_chapel(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_sea(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Sea."""
    if world.settings.is_flag_value(SeaGate, SeaGating.TOADSTOOL):
        return inventory.has_item(ToadstoolRecruitmentPrize)
    if world.settings.is_flag_value(SeaGate, SeaGating.STAR_4):
        return inventory.has_item_count(StarPiecePrize, 4)
    if world.settings.is_flag_value(SeaGate, SeaGating.BUNDT):
        return inventory.has_item(BundtBossFight)
    if world.settings.is_flag_value(SeaGate, SeaGating.MARRYMORE):
        return can_access_chapel(world, inventory) and not_earlygame(world, inventory)
    return True


def can_clear_ship(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Sunken Ship."""
    return can_access_sea(world, inventory) and not_earlygame(world, inventory)


def can_access_ship_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Sunken Ship."""
    return (
        can_clear_ship(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_seaside_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Seaside Town boss."""
    if world.settings.is_flag_value(YaridovichGate, YaridovichGating.SHIP):
        return can_clear_ship(world, inventory)
    if world.settings.is_flag_value(YaridovichGate, YaridovichGating.JOHNNY):
        return inventory.has_item(JohnnyBossFight)
    return True


def can_clear_seaside_boss(world: GameWorld, inventory: Inventory) -> bool:
    return can_access_seaside_boss(world, inventory) and not_earlygame(world, inventory)


def can_access_lands_end(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Land's End."""
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.STAR_5):
        return inventory.has_item_count(StarPiecePrize, 5)
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.ELDER):
        return can_access_seaside_boss(world, inventory) and inventory.has_item(
            ShedKeyPrize
        )
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.YARIDOVICH):
        return inventory.has_item(YaridovichBossFight)
    if world.settings.is_flag_value(LandsEndGate, LandsEndGating.SEASIDE):
        return can_clear_seaside_boss(world, inventory)
    return True


def can_access_temple_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Belome Temple."""
    if world.settings.is_flag_value(BelomeTempleGate, BelomeTempleGating.KEY):
        return inventory.has_item(TempleKeyPrize) and can_access_lands_end(
            world, inventory
        )
    return can_access_lands_end(world, inventory)


def can_clear_temple_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Belome Temple."""
    return can_access_temple_boss(world, inventory) and not_earlygame(world, inventory)


def can_access_temple_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the postgame boss at Belome Temple."""
    return (
        can_clear_temple_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_monstro_town(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Monstro Town."""
    if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.LANDS_END):
        return can_access_temple_boss(world, inventory) and not_earlygame(
            world, inventory
        )
    if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.BELOME_2):
        return inventory.has_item(Belome2BossFight)
    return True


def can_access_fifth_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 5th Monstro dojo boss."""
    return (
        can_access_monstro_town(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and not_earlygame(world, inventory)
    )


def can_access_outer_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get to Nimbus Land."""
    if world.settings.is_flag_value(NimbusGate, NimbusGating.VALLEY):
        return not_earlygame(world, inventory)
    if world.settings.is_flag_value(NimbusGate, NimbusGating.MEGASMILAX):
        return inventory.has_item(MegasmilaxBossFight)
    return True


def can_access_nimbus_castle(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Nimbus Castle."""
    outer_access = can_access_outer_nimbus(world, inventory)
    if world.settings.is_flag_value(NimbusGate, NimbusGating.PAINT):
        return outer_access and inventory.has_item(GoldPaintPrize)
    return outer_access


def can_access_inner_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get past the Castle Key 1 door."""
    return can_access_nimbus_castle(world, inventory) and inventory.has_item(
        CastleKey1Prize
    )


def can_access_late_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get past the Castle Key 2 door."""
    return can_access_inner_nimbus(world, inventory) and inventory.has_item(
        CastleKey2Prize
    )


def can_clear_nimbus_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear the Nimbus Land boss."""
    return can_access_late_nimbus(world, inventory) and not_earlygame(world, inventory)


def can_access_volcano(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Barrel Volcano."""
    if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.NIMBUS):
        return can_clear_nimbus_boss(world, inventory)
    if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.VALENTINA):
        return inventory.has_item(ValentinaBossFight)
    return True


def can_clear_volcano(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to clear Barrel Volcano."""
    return can_access_volcano(world, inventory) and not_earlygame(world, inventory)


def can_access_keep(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Bowser's Keep."""
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.VOLCANO):
        return can_clear_volcano(world, inventory)
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
        return inventory.has_item_count(StarPiecePrize, 6)
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.AXEM):
        return inventory.has_item(AxemRangersBossFight)
    return True


def can_access_factory(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Outer Factory."""
    if world.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
        return (
            inventory.has_item_count(StarPiecePrize, 6)
            and can_access_keep(world, inventory)
            and not_earlygame(world, inventory)
        )
    if world.settings.is_flag_value(FactoryGate, FactoryGating.EXOR):
        return (
            inventory.has_item(ExorBossFight)
            and can_access_keep(world, inventory)
            and not_earlygame(world, inventory)
        )
    if world.settings.is_flag_value(FactoryGate, FactoryGating.OPEN):
        return can_access_keep(world, inventory)
    if world.settings.is_flag_value(FactoryGate, FactoryGating.KEEP):
        return can_access_keep(world, inventory) and not_earlygame(world, inventory)
    return True


def can_access_inner_factory_final_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the final Factory boss."""
    value = world.settings.get_flag(_get_flag("StarPiecesRequired")).value
    has_stars = inventory.has_item_count(StarPiecePrize, value)
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        fireworks_access = inventory.has_item(RegularFireworksPrize)
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        fireworks_access = inventory.has_item_count(ProgressiveFireworksPrize, 3)
    else:
        fireworks_access = True
    can_access_bucket = (
        fireworks_access
        and can_clear_mines(world, inventory)
        and world.settings.isflag_enabled(_get_flag("BucketWarp"))
    )
    can_access_casino = world.settings.isflag_enabled(
        _get_flag("CasinoWarp")
    ) and inventory.has_item(BrightCardPrize)
    return (
        has_stars
        and (
            can_access_bucket
            or can_access_casino
            or can_access_factory(world, inventory)
        )
        and not_earlygame(world, inventory)
    )


def can_access_sealed_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the sealed door boss."""
    boss_reqs = can_access_monstro_town(world, inventory) and not_earlygame(
        world, inventory
    )
    item_reqs: bool = False
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        item_reqs = inventory.has_item(RegularFireworksPrize) and can_clear_mines(
            world, inventory
        )
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        item_reqs = inventory.has_item_count(ProgressiveFireworksPrize, 2)
    else:
        item_reqs = can_clear_mines(world, inventory)
    return item_reqs and boss_reqs


def can_access_sealed_postgame_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the second sealed door boss."""
    return (
        can_access_sealed_door_boss(world, inventory)
        and inventory.has_item(StayVoucherPrize)
        and inventory.has_item(ExtraShinyStonePrize)
        and not_earlygame(world, inventory)
    )


def can_access_invisible_flags(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the invisible item checks have been activated."""
    return world.settings.isflag_enabled(
        SkipMustyFearsSequence
    ) or can_access_monstro_town(world, inventory)

    # mimic 3 and postgame temple


def can_damage_enemies_with_spells(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to damage enemies with a non-elemental spell."""
    pool = [
        StarRainSpellPrize,
        GenoWhirlSpellPrize,
        TerrorizeSpellPrize,
        PoisonGasSpellPrize,
    ]
    if not world.settings.isflag_enabled(InfuseSpellElements):
        pool.extend(
            [
                GenoBeamSpellPrize,
                GenoFlashSpellPrize,
                GenoBlastSpellPrize,
                CrusherSpellPrize,
                BowserCrushSpellPrize,
                PsychBombSpellPrize,
            ]
        )
    return inventory.has_one_of(pool)


def is_all_starting_chars_set(world: GameWorld, inventory: Inventory | None = None):
    """Check if all starting character slots are filled.

    If inventory is provided, also counts character prizes in the inventory
    as "effectively set" for assumed-reachability placement.
    """
    from ..types.prize import CharacterPrize

    strchars = world.settings.get_flag(StartingCharacters)
    startmax = len(strchars.enabled)

    # Count how many character prizes are in the assumed inventory
    chars_in_inventory = 0
    if inventory is not None:
        chars_in_inventory = sum(
            1 for item in inventory if isinstance(item, CharacterPrize)
        )

    # Count how many starting slots are unfilled
    unfilled_slots = 0
    starting_locations = [
        StartingCharacter1,
        StartingCharacter2,
        StartingCharacter3,
        StartingCharacter4,
        StartingCharacter5,
    ]
    for i in range(startmax):
        loc = world.get_location(starting_locations[i])
        if loc.prize is None:
            unfilled_slots += 1

    # All starting chars are "effectively set" if the inventory has enough
    # character prizes to fill the unfilled slots
    return chars_in_inventory >= unfilled_slots
