# E0668_SUMMON_MARRYMORE_BOSS_TO_ROOM
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript([
	JmpIfBitSet(UNKNOWN_7063_5, ["EVENT_256_ret_0"]),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_5),
	StopBackgroundEvent(TIMER_701C),
	StopBackgroundEvent(TIMER_701E),
	Pause(10),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_TransferToXYZF(x=9, y=97, z=0, direction=EAST),
		A_TransferXYZFPixels(x=16, y=8, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_TransferToXYZF(x=9, y=98, z=0, direction=EAST),
		A_TransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_TransferToXYZF(x=10, y=95, z=0, direction=EAST),
		A_TransferXYZFPixels(x=254, y=4, z=0, direction=EAST),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=5, y=85)
	]),
	RememberLastObject(),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(30),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
	RestoreAllHP(),
	RestoreAllFP(),
	RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
	RememberLastObject(),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_9),
	RemoveObjectFromCurrentLevel(NPC_10),
	RemoveObjectFromCurrentLevel(NPC_11),
	RemoveObjectFromSpecificLevel(NPC_0, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_1, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_2, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_7, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_8, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_9, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_10, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RemoveObjectFromSpecificLevel(NPC_11, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER),
	RunEventAsSubroutine(E0200_UNLOCK_FOREST_IF_GATED_BY_MARRYMORE_CHARACTER),
	FadeInFromBlack(sync=False),
	ClearBit(TEMP_704C_0),
    RunEventAsSubroutine(E0225_CHECK_VOUCHER_UNLOCK),
	SetBit(MARRYMORE_LIBERATED),
	SetBit(MAP_STAR_HILL),
	SetBit(TEMP_7042_1),
	ClearBit(TEMP_7042_0),
	ClearBit(TEMP_7042_2),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=1),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=2),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=3),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=5),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=7),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	RunEventAsSubroutine(E1204_CHAPEL_BOSS_UNLOCKS),
	RunEventAsSubroutine(E1228_MARRYMORE_CHARACTER),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 4),
	JmpIfComparisonResultIsLesser(["EVENT_668_j_24"]),
	SetBit(SWITCH_MENU_UNLOCKED),
	RemoveOneOfItemFromInventory(ShoesItem, identifier="EVENT_668_j_24"),
	RemoveOneOfItemFromInventory(BroochItem),
	RemoveOneOfItemFromInventory(RingItem),
	RemoveOneOfItemFromInventory(CrownItem),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
