# E0503_PIPE_VAULT_CROUCH_ITEM_CONFIRM
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
	JmpIfBitClear(TEMP_7043_0, ["EVENT_256_ret_0"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	Set7000ToPressedButton(),
	JmpIf7000AnyBitsSet(bits=[0, 3, 6], destinations=["EVENT_503_start_loop_n_times_5"]),
	Return(),
	StartLoopNTimes(7, identifier="EVENT_503_start_loop_n_times_5"),
	Set7000ToPressedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_503_remember_last_object_18"]),
	JmpIf7000AnyBitsSet(bits=[2], destinations=["EVENT_503_enable_controls_until_return_12"]),
	Pause(1),
	EndLoop(),
	Return(),
	EnableControlsUntilReturn([], identifier="EVENT_503_enable_controls_until_return_12"),
	ActionQueueSync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SetSpriteSequence(index=16, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepNortheast(),
		A_SetWalkingSpeed(SLOW),
		A_WalkNortheastPixels(8),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkNortheastPixels(4),
		A_SetWalkingSpeed(NORMAL),
		A_WalkToXYCoords(x=8, y=64)
	]),
	JmpIfObjectNotInSpecificLevel(NPC_5, R125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES, ["EVENT_503_remember_last_object_18"]),
	Pause(10),
	SetVarToConst(ACTIVE_NPC, 25),
	RunEventAsSubroutine(E0236_FREESTANDING_6_GRANT),
	RememberLastObject(identifier="EVENT_503_remember_last_object_18"),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return()
])
