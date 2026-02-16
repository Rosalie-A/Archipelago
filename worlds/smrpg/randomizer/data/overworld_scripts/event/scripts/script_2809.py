# E2809_MUSHROOM_WAY_BOSS_THREATENS_YOU
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
	JmpIfBitSet(TEMP_7044_6, ["EVENT_2809_jmp_if_bit_set_3"], identifier="EVENT_2809_jmp_if_bit_set_0"),
	Pause(1),
	Jmp(["EVENT_2809_jmp_if_bit_set_0"]),
	JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_2809_ret_16"], identifier="EVENT_2809_jmp_if_bit_set_3"),
	ClearBit(TEMP_7044_6),
	FreezeAllNPCsUntilReturn(),
	EnableControls([]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_Pause(16)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=24, y=80)
	]),
	FreezeCamera(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(40),
		A_SetSequenceSpeed(NORMAL)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(5),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(1),
		A_SetWalkingSpeed(NORMAL),
		A_FixedFCoordOff()
	]),
	Pause(10),
	UnfreezeAllNPCs(),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	UnfreezeCamera(),
	Return(identifier="EVENT_2809_ret_16")
])
