# E3642_NIMBUS_EXTERIOR_OCCUPIED_LOADER
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
	JmpIfBitClear(NIMBUS_MID_BOSS_COMPLETED, ["EVENT_3642_set_temp_action_script_3"]),
	ClearBit(TEMP_704C_0),
	ClearBit(GUEST_DROPPED_OFF),
	SetTempAsyncActionScript(NPC_5, A0804_INC_PALETTE_ROW_15, identifier="EVENT_3642_set_temp_action_script_3"),
	SetTempAsyncActionScript(NPC_6, A0807_INC_PALETTE_ROW_2),
	SetTempAsyncActionScript(NPC_1, A0806_INC_PALETTE_ROW_3),
	SetTempAsyncActionScript(NPC_3, A0803_INC_PALETTE_ROW),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(2)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetPriority(3)
	]),
	JmpIfBitSet(TEMP_704C_0, ["EVENT_3584_ret_0"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3642_fade_in_from_black_sync_20"]),
	FadeInFromBlack(sync=False),
	Return(),
	FadeInFromBlack(sync=True, identifier="EVENT_3642_fade_in_from_black_sync_20"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(132),
		A_Walk1StepNortheast(),
		A_FloatingOn(),
		A_WalkNortheastSteps(2)
	]),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	PauseScriptUntilEffectDone(),
	ClearBit(TEMP_7042_0),
	Return()
])
