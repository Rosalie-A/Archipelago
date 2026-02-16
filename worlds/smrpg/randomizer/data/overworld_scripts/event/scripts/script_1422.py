# E1422_RESCUE_TOAD_MUSHROOM_WAY_2
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
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	DisableObjectTrigger(NPC_7),
	PauseActionScript(NPC_7),
	PauseActionScript(NPC_8),
	StartBattleAtBattlefield(PACK004_JUST_TROOPAS, BF09_GRASSLANDS),
	JmpIfBitSet(RUN_AWAY, ["EVENT_1422_set_action_script_8"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_1422_reset_and_choose_game_32"]),
	Jmp(["EVENT_1422_freeze_all_npcs_until_return_16"]),
	SetAsyncActionScript(NPC_7, A0015_DO_NOTHING, identifier="EVENT_1422_set_action_script_8"),
	SetAsyncActionScript(NPC_8, A0015_DO_NOTHING),
	ActionQueueSync(target=NPC_7, subscript=[
		A_BPL262728(),
		A_TransferToXYZF(x=13, y=28, z=12, direction=EAST),
		A_FaceSoutheast(),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_BPL262728(),
		A_TransferToXYZF(x=13, y=28, z=14, direction=EAST),
		A_FaceSoutheast(),
		A_ReturnQueue()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=14, y=28, z=6, direction=EAST),
		A_FaceSouth(),
		A_ReturnQueue()
	]),
	RunBackgroundEvent(event_id=E1432_RESCUE_TOAD_EXTENDED, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	Return(),
	FreezeAllNPCsUntilReturn(identifier="EVENT_1422_freeze_all_npcs_until_return_16"),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FloatingOn(),
		A_BPL262728(),
		A_SetPriority(3),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_TransferToXYZF(x=14, y=28, z=6, direction=EAST),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_TransferToXYZF(x=13, y=29, z=6, direction=EAST),
		A_FaceNortheast()
	]),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromSpecificLevel(NPC_8, R204_MUSHROOM_WAY_AREA_02),
	FadeInFromBlack(sync=False),
	Pause(15),
	RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
	Pause(15),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetAllSpeeds(FASTER),
		A_WalkSoutheastSteps(3),
		A_JumpToHeight(112),
		A_WalkSoutheastSteps(11),
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromSpecificLevel(NPC_7, R204_MUSHROOM_WAY_AREA_02),
	SummonObjectToSpecificLevel(NPC_5, R205_MUSHROOM_WAY_AREA_03),
	SetBit(TOAD_IN_MUSHROOM_WAY_2),
	UnfreezeAllNPCs(),
	Return(),
	ResetAndChooseGame(identifier="EVENT_1422_reset_and_choose_game_32"),
	Return()
])
