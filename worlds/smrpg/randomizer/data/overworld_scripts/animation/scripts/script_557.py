#A0557_MUSHROOM_WAY_LAKITU
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_SequenceLoopingOn(),
	A_SetPriority(3),
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00 \xf0\x03\x00\x01\x00\x00\x00\x08\x80')),
	A_WalkNorthwestSteps(5, identifier="ACTION_557_shift_northwest_steps_4"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_northwest_steps_8"]),
	A_JmpIfRandom1of2(["ACTION_557_shift_northwest_steps_8"]),
	A_SetBit(TEMP_7043_0),
	A_WalkNorthwestSteps(5, identifier="ACTION_557_shift_northwest_steps_8"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_northeast_steps_12"]),
	A_JmpIfRandom1of2(["ACTION_557_shift_northeast_steps_12"]),
	A_SetBit(TEMP_7043_0),
	A_WalkNortheastSteps(5, identifier="ACTION_557_shift_northeast_steps_12"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_northeast_steps_16"]),
	A_JmpIfRandom1of2(["ACTION_557_shift_northeast_steps_16"]),
	A_SetBit(TEMP_7043_0),
	A_WalkNortheastSteps(8, identifier="ACTION_557_shift_northeast_steps_16"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_northeast_steps_20"]),
	A_JmpIfRandom1of2(["ACTION_557_shift_northeast_steps_20"]),
	A_SetBit(TEMP_7043_0),
	A_WalkNortheastSteps(2, identifier="ACTION_557_shift_northeast_steps_20"),
	A_WalkSoutheastSteps(5),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_southeast_steps_25"]),
	A_JmpIfRandom1of2(["ACTION_557_shift_southeast_steps_25"]),
	A_SetBit(TEMP_7043_0),
	A_WalkSoutheastSteps(5, identifier="ACTION_557_shift_southeast_steps_25"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_southwest_steps_29"]),
	A_JmpIfRandom1of2(["ACTION_557_shift_southwest_steps_29"]),
	A_SetBit(TEMP_7043_0),
	A_WalkSouthwestSteps(5, identifier="ACTION_557_shift_southwest_steps_29"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_southwest_steps_33"]),
	A_JmpIfRandom1of2(["ACTION_557_shift_southwest_steps_33"]),
	A_SetBit(TEMP_7043_0),
	A_WalkSouthwestSteps(5, identifier="ACTION_557_shift_southwest_steps_33"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_557_shift_southwest_steps_37"]),
	A_JmpIfRandom1of2(["ACTION_557_shift_southwest_steps_37"]),
	A_SetBit(TEMP_7043_0),
	A_WalkSouthwestSteps(5, identifier="ACTION_557_shift_southwest_steps_37"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_557_jmp_41"]),
	A_JmpIfRandom1of2(["ACTION_557_jmp_41"]),
	A_SetBit(TEMP_7043_0),
	A_Jmp(["ACTION_557_shift_northwest_steps_4"], identifier="ACTION_557_jmp_41")
])
