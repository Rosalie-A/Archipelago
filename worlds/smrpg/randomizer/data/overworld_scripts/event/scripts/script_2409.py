# E2409_ABYSS_ROOM_BEFORE_1ST_BOSS_LOADER
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
	JmpIfVarEqualsConst(FACTORY_FALL_1, 237, ["EVENT_2409_set_var_to_const_21"]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkSouthPixels(2),
		A_WalkSoutheastPixels(5)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_WalkSouthwestPixels(12)
	]),
	SetVarToConst(FACTORY_FALL_1, 239),
	SetVarToConst(FACTORY_FALL_2, 24),
	SetVarToConst(FACTORY_FALL_3, 16),
	ClearBit(DIRECTIONAL_7045_0),
	FreezeCamera(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=25, y=44),
		A_WalkSouthwestPixels(5),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=25, y=43),
		A_WalkSouthwestPixels(11),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=27, y=39),
		A_WalkSouthwestPixels(5),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=28, y=38),
		A_WalkSouthwestPixels(11),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_OverwriteSolidity(),
		A_TransferToXYZF(x=32, y=43, z=0, direction=EAST)
	]),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True),
	UnfreezeCamera(),
	RunBackgroundEvent(event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 239, identifier="EVENT_2409_set_var_to_const_21"),
	SetVarToConst(FACTORY_FALL_2, 0),
	SetVarToConst(FACTORY_FALL_3, 0),
	ClearBit(DIRECTIONAL_7045_0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(6),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftZDownPixels(19)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_WalkSouthwestPixels(6),
		A_ShiftZDownPixels(19)
	]),
	RunBackgroundEvent(event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 239, identifier="EVENT_2409_set_var_to_const_32"),
	SetVarToConst(FACTORY_FALL_2, 24),
	SetVarToConst(FACTORY_FALL_3, 16),
	ClearBit(DIRECTIONAL_7045_0),
	FreezeCamera(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=25, y=44),
		A_WalkSouthwestPixels(5),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=25, y=43),
		A_WalkSouthwestPixels(11),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftToXYCoords(x=27, y=39),
		A_WalkSouthwestPixels(5),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=28, y=38),
		A_WalkSouthwestPixels(11),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_OverwriteSolidity(),
		A_TransferToXYZF(x=27, y=43, z=0, direction=EAST)
	]),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0415_PLAYER_ENTER_ANGLED_JUMPING_POSE),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True),
	UnfreezeCamera(),
	RunBackgroundEvent(event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True),
	Return(),
	JmpIfBitClear(UNUSED_708F_5, ["EVENT_2409_set_var_to_const_52"], identifier="EVENT_2409_jmp_if_bit_clear_50"),
	SetSyncActionScript(NPC_7, A0690_OPENING_CHEST),
	SetVarToConst(FACTORY_FALL_1, 239, identifier="EVENT_2409_set_var_to_const_52"),
	SetVarToConst(FACTORY_FALL_2, 0),
	SetVarToConst(FACTORY_FALL_3, 0),
	ClearBit(DIRECTIONAL_7045_0),
	FreezeCamera(),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(6),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShiftZDownPixels(19)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkSouthwestPixels(6),
		A_ShiftZDownPixels(19)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_OverwriteSolidity(),
		A_TransferToXYZF(x=20, y=60, z=0, direction=EAST)
	]),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0860_ABYSS_BEFORE_1ST_BOSS_JUMP_BACK_UP),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2592_ABYSS_FALL_OFF_BEFORE_FIRST_BOSS, return_on_level_exit=True),
	UnfreezeCamera(),
	Return()
])
