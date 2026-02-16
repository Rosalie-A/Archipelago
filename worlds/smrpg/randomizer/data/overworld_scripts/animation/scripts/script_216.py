#A0216_VINES_1ST_ROOM_VERTICAL_FLYING_BIRD
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
	A_JmpIfRandom1of2(["ACTION_216_set_animation_speed_3"]),
	A_SetWalkingSpeed(NORMAL),
	A_Jmp(["ACTION_216_set_var_to_const_6"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_216_set_animation_speed_3"),
	A_Jmp(["ACTION_216_set_var_to_const_6"]),
	A_SetWalkingSpeed(FAST),
	A_SetVarToConst(PRIMARY_TEMP_700C, 3, identifier="ACTION_216_set_var_to_const_6"),
	A_WalkF20Steps(),
	A_JmpIfRandom1of2(["ACTION_216_jmp_if_bit_set_21"]),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_216_turn_clockwise_45_degrees_n_times_12"]),
	A_TurnClockwise45DegreesNTimes(2),
	A_Jmp(["ACTION_216_pause_13"]),
	A_TurnClockwise45DegreesNTimes(6, identifier="ACTION_216_turn_clockwise_45_degrees_n_times_12"),
	A_Pause(10, identifier="ACTION_216_pause_13"),
	A_JmpIfRandom1of2(["ACTION_216_set_animation_speed_17"]),
	A_SetWalkingSpeed(NORMAL),
	A_Jmp(["ACTION_216_set_var_to_const_6"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_216_set_animation_speed_17"),
	A_Jmp(["ACTION_216_set_var_to_const_6"]),
	A_SetWalkingSpeed(FAST),
	A_Jmp(["ACTION_216_set_var_to_const_6"]),
	A_JmpIfBitSet(TEMP_7043_0, ["ACTION_216_turn_clockwise_45_degrees_n_times_28"], identifier="ACTION_216_jmp_if_bit_set_21"),
	A_TurnClockwise45DegreesNTimes(2),
	A_Pause(4),
	A_TurnClockwise45DegreesNTimes(2),
	A_Pause(4),
	A_SetBit(TEMP_7043_0),
	A_Jmp(["ACTION_216_set_var_to_const_6"]),
	A_TurnClockwise45DegreesNTimes(6, identifier="ACTION_216_turn_clockwise_45_degrees_n_times_28"),
	A_Pause(4),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(4),
	A_ClearBit(TEMP_7043_0),
	A_Jmp(["ACTION_216_set_var_to_const_6"])
])
