# E1919_ABYSS_BIG_CONVEYOR_PLATFORM
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
	DisableObjectTrigger(MEM_70A8),
	PlaySound(sound=SO058_INSERT, channel=6),
	JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_1919_action_queue_7"]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthwestSteps(8)
	]),
	JmpToSubroutine(["EVENT_1919_enable_controls_until_return_11"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSoutheastSteps(8),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	Return(),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_FaceSouthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(8)
	], identifier="EVENT_1919_action_queue_7"),
	JmpToSubroutine(["EVENT_1919_enable_controls_until_return_11"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(8),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	Return(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_1919_enable_controls_until_return_11"),
	Pause(1, identifier="EVENT_1919_pause_12"),
	JmpIfMarioInAir(["EVENT_1919_ret_15"]),
	Jmp(["EVENT_1919_pause_12"]),
	Return(identifier="EVENT_1919_ret_15")
])
