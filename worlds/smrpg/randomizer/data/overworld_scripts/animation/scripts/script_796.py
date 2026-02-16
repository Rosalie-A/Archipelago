#A0796_MUSHROOM_DERBY_UNKNOWN
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
	A_SetVarToRandom(PRIMARY_TEMP_700C, 80, identifier="ACTION_796_set_var_to_random_0"),
	A_Compare700CToVar(Y_COORD_2),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_796_jmp_to_subroutine_9"]),
	A_Compare700CToVar(TEMP_702C),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_796_jmp_to_subroutine_13"]),
	A_JmpToSubroutine(["ACTION_796_set_animation_speed_17"]),
	A_JmpToSubroutine(["ACTION_796_dec_42"]),
	A_JmpIfVarEqualsConst(TEMP_702A, 1, ["ACTION_796_shift_northeast_pixels_29"]),
	A_Jmp(["ACTION_796_set_var_to_random_0"]),
	A_JmpToSubroutine(["ACTION_796_set_animation_speed_25"], identifier="ACTION_796_jmp_to_subroutine_9"),
	A_JmpToSubroutine(["ACTION_796_dec_42"]),
	A_JmpIfVarEqualsConst(TEMP_702A, 1, ["ACTION_796_shift_northeast_pixels_29"]),
	A_Jmp(["ACTION_796_set_var_to_random_0"]),
	A_JmpToSubroutine(["ACTION_796_set_animation_speed_21"], identifier="ACTION_796_jmp_to_subroutine_13"),
	A_JmpToSubroutine(["ACTION_796_dec_42"]),
	A_JmpIfVarEqualsConst(TEMP_702A, 1, ["ACTION_796_shift_northeast_pixels_29"]),
	A_Jmp(["ACTION_796_set_var_to_random_0"]),
	A_SetSequenceSpeed(FAST, identifier="ACTION_796_set_animation_speed_17"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Walk1StepNortheast(),
	A_ReturnQueue(),
	A_SetSequenceSpeed(FAST, identifier="ACTION_796_set_animation_speed_21"),
	A_SetWalkingSpeed(SLOW),
	A_Walk1StepNortheast(),
	A_ReturnQueue(),
	A_SetSequenceSpeed(VERY_FAST, identifier="ACTION_796_set_animation_speed_25"),
	A_SetWalkingSpeed(NORMAL),
	A_Walk1StepNortheast(),
	A_ReturnQueue(),
	A_WalkNortheastPixels(8, identifier="ACTION_796_shift_northeast_pixels_29"),
	A_JmpIfBitClear(UNKNOWN_MUSHROOM_DERBY_7085_4, ["ACTION_796_set_animation_speed_39"]),
	A_JmpIfBitSet(TEMP_7043_5, ["ACTION_796_set_animation_speed_39"]),
	A_JmpIfBitSet(TEMP_7043_7, ["ACTION_796_set_animation_speed_39"]),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_796_set_animation_speed_39"]),
	A_SetBit(TEMP_7043_6),
	A_WalkNortheastPixels(8),
	A_SetSequenceSpeed(SLOW),
	A_FaceSouthwest(),
	A_Jmp(["ACTION_677_jmp_if_random_above_66_0"]),
	A_SetSequenceSpeed(SLOW, identifier="ACTION_796_set_animation_speed_39"),
	A_WalkNortheastPixels(8),
	A_ReturnQueue(),
	A_Dec(TEMP_702A, identifier="ACTION_796_dec_42"),
	A_ReturnQueue()
])
