#A0688_BOOSTER_PASS_LAKITU
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
	A_WalkSoutheastSteps(4, identifier="ACTION_688_shift_southeast_steps_4"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southeast_steps_8"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_southeast_steps_8', 'ACTION_688_shift_southeast_steps_8']),
	A_SetBit(TEMP_7043_0),
	A_WalkSoutheastSteps(5, identifier="ACTION_688_shift_southeast_steps_8"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southwest_steps_12"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_southwest_steps_12', 'ACTION_688_shift_southwest_steps_12']),
	A_SetBit(TEMP_7043_0),
	A_WalkSouthwestSteps(4, identifier="ACTION_688_shift_southwest_steps_12"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southwest_steps_16"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_southwest_steps_16', 'ACTION_688_shift_southwest_steps_16']),
	A_SetBit(TEMP_7043_0),
	A_WalkSouthwestSteps(3, identifier="ACTION_688_shift_southwest_steps_16"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northwest_steps_20"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_northwest_steps_20', 'ACTION_688_shift_northwest_steps_20']),
	A_SetBit(TEMP_7043_0),
	A_WalkNorthwestSteps(2, identifier="ACTION_688_shift_northwest_steps_20"),
	A_WalkSouthwestSteps(3),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southwest_steps_25"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_southwest_steps_25', 'ACTION_688_shift_southwest_steps_25']),
	A_SetBit(TEMP_7043_0),
	A_WalkSouthwestSteps(2, identifier="ACTION_688_shift_southwest_steps_25"),
	A_WalkNortheastSteps(3),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northeast_steps_30"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_northeast_steps_30', 'ACTION_688_shift_northeast_steps_30']),
	A_SetBit(TEMP_7043_0),
	A_WalkNortheastSteps(2, identifier="ACTION_688_shift_northeast_steps_30"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_southeast_steps_34"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_southeast_steps_34', 'ACTION_688_shift_southeast_steps_34']),
	A_SetBit(TEMP_7043_0),
	A_WalkSoutheastSteps(2, identifier="ACTION_688_shift_southeast_steps_34"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northeast_steps_38"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_northeast_steps_38', 'ACTION_688_shift_northeast_steps_38']),
	A_SetBit(TEMP_7043_0),
	A_WalkNortheastSteps(4, identifier="ACTION_688_shift_northeast_steps_38"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northeast_steps_42"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_northeast_steps_42', 'ACTION_688_shift_northeast_steps_42']),
	A_SetBit(TEMP_7043_0),
	A_WalkNortheastSteps(3, identifier="ACTION_688_shift_northeast_steps_42"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northwest_steps_46"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_northwest_steps_46', 'ACTION_688_shift_northwest_steps_46']),
	A_SetBit(TEMP_7043_0),
	A_WalkNorthwestSteps(5, identifier="ACTION_688_shift_northwest_steps_46"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_shift_northwest_steps_50"]),
	A_JmpIfRandom2of3(['ACTION_688_shift_northwest_steps_50', 'ACTION_688_shift_northwest_steps_50']),
	A_SetBit(TEMP_7043_0),
	A_WalkNorthwestSteps(4, identifier="ACTION_688_shift_northwest_steps_50"),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_688_jmp_54"]),
	A_JmpIfRandom2of3(['ACTION_688_jmp_54', 'ACTION_688_jmp_54']),
	A_SetBit(TEMP_7043_0),
	A_Jmp(["ACTION_688_shift_southeast_steps_4"], identifier="ACTION_688_jmp_54")
])
