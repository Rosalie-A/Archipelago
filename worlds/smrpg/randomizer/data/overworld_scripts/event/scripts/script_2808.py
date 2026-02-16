# E2808_MUSHROOM_WAY_BOSS_FIGHT
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
	JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_2808_ret_28"], identifier="EVENT_2808_jmp_if_bit_set_0"),
	FreezeAllNPCsUntilReturn(),
	ActionQueueSync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=27, y=94),
		A_FaceNortheast()
	]),
	StopEmbeddedActionScript(MARIO),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2808_restore_all_hp_7"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2808_restore_all_hp_7"),
	RestoreAllFP(),
	SetBit(TOAD_IN_MUSHROOM_WAY_3),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_7),
	SummonObjectToCurrentLevel(NPC_8),
	FreezeAllNPCsUntilReturn(),
	RemoveObjectFromSpecificLevel(NPC_7, R205_MUSHROOM_WAY_AREA_03),
	RemoveObjectFromSpecificLevel(NPC_5, R205_MUSHROOM_WAY_AREA_03),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_5),
	FadeInFromBlack(sync=False),
	UnfreezeCamera(),
	UnfreezeAllNPCs(),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	SetVarToConst(OLD_STAR_PIECE_ID, 200),
	RunEventAsSubroutine(E1225_MUSHROOM_WAY_CHARACTER),
	Set7000ToPartySize(),
	CompareVarToConst(PRIMARY_TEMP_7000, 4),
	JmpIfComparisonResultIsLesser(["EVENT_2808_j_24"]),
	SetBit(SWITCH_MENU_UNLOCKED),
    RunEventAsSubroutine(E1194_MUSHROOM_WAY_BOSS_UNLOCKS),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER, identifier="EVENT_2808_j_24"),
	JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_1, ["grant_toad_2_rescue_if_not_done"]),
    SetVarToConst(PRIMARY_TEMP_7000, R203_MUSHROOM_WAY_AREA_01),
	RunEventAsSubroutine(E0252_NPC_QUEST_2_GRANT),
	JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_2, ["EVENT_2808_ret_28"], identifier="grant_toad_2_rescue_if_not_done"),
    SetVarToConst(PRIMARY_TEMP_7000, R204_MUSHROOM_WAY_AREA_02),
	RunEventAsSubroutine(E0251_NPC_QUEST_3_GRANT),
	Return(identifier="EVENT_2808_ret_28")
])
