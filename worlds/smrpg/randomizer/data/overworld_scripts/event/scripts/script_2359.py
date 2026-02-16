# E2359_ABYSS_1ST_SAVE_ROOM_LOADER
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
	SummonObjectToSpecificLevel(NPC_10, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_11, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_12, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_13, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_14, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	SummonObjectToSpecificLevel(NPC_15, R222_SMITHY_FACTORY_AREA_03_GLUM_REAPERS),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_2359_set_var_to_const_8"]),
	JmpIfVarEqualsConst(FACTORY_FALL_1, 219, ["EVENT_2359_set_var_to_const_12"]),
	SetVarToConst(FACTORY_FALL_2, 24, identifier="EVENT_2359_set_var_to_const_8"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=8, y=70),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=8, y=69),
		A_ShiftZDownPixels(11)
	]),
	Jmp(["EVENT_2359_set_var_to_const_15"]),
	SetVarToConst(FACTORY_FALL_2, 0, identifier="EVENT_2359_set_var_to_const_12"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	SetVarToConst(FACTORY_FALL_1, 220, identifier="EVENT_2359_set_var_to_const_15"),
	RunBackgroundEvent(event_id=E2379_ABYSS_1ST_SAVE_ROOM_BACKGROUND, return_on_level_exit=True),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_2359_fade_in_from_black_async_24"]),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
	ClearBit(TEMP_7044_4),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2359_ret_23"]),
	RunEventAsSubroutine(E3915_FACTORY_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_2359_ret_23"),
	FadeInFromBlack(sync=False, identifier="EVENT_2359_fade_in_from_black_async_24"),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 220, identifier="EVENT_2359_set_var_to_const_26"),
	SetVarToConst(FACTORY_FALL_2, 0),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestPixels(4),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(10),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_TransferToXYZF(x=7, y=81, z=0, direction=EAST),
		A_OverwriteSolidity()
	]),
	FreezeCamera(),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0414_PLAYER_ENTER_ANGLED_JUMPING_POSE),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2379_ABYSS_1ST_SAVE_ROOM_BACKGROUND, return_on_level_exit=True),
	UnfreezeCamera(),
	Return(),
	SetVarToConst(FACTORY_FALL_1, 220, identifier="EVENT_2359_set_var_to_const_39"),
	SetVarToConst(FACTORY_FALL_2, 24),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShiftToXYCoords(x=8, y=70),
		A_WalkNortheastPixels(6),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=8, y=69),
		A_ShiftZDownPixels(11)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_TransferToXYZF(x=9, y=74, z=0, direction=EAST),
		A_OverwriteSolidity()
	]),
	FreezeCamera(),
	FadeInFromBlack(sync=False),
	SetAsyncActionScript(MARIO, A0415_PLAYER_ENTER_ANGLED_JUMPING_POSE),
	SetAsyncActionScript(MARIO, A0399_JUMPING_FALLING_STATE_IN_FACTORY),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	RunBackgroundEvent(event_id=E2379_ABYSS_1ST_SAVE_ROOM_BACKGROUND, return_on_level_exit=True),
	UnfreezeCamera(),
	Return()
])
