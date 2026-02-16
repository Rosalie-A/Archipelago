#A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS
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
	A_SetVarToConst(TEMP_70AE, 20, identifier="ACTION_21_set_var_to_const_0"),
	A_SetWalkingSpeed(SLOW),
	A_WalkSoutheastSteps(2),
	A_Inc(TEMP_70AE),
	A_Inc(TEMP_70AE),
	A_Pause(20),
	A_JmpIfRandom1of2(["ACTION_21_turn_random_direction_9"]),
	A_Walk1StepNorthwest(),
	A_Dec(TEMP_70AE),
	A_TurnRandomDirection(identifier="ACTION_21_turn_random_direction_9"),
	A_Pause(10),
	A_Walk1StepSoutheast(),
	A_Inc(TEMP_70AE),
	A_JmpIfRandom2of3(['ACTION_21_turn_random_direction_9', 'ACTION_21_set_animation_speed_29']),
	A_Pause(20, identifier="ACTION_21_pause_14"),
	A_SetWalkingSpeed(VERY_SLOW),
	A_WalkSoutheastSteps(3),
	A_Inc(TEMP_70AE),
	A_Inc(TEMP_70AE),
	A_Inc(TEMP_70AE),
	A_JmpToSubroutine(["ACTION_21_copy_var_to_var_40"]),
	A_JmpIfVarEqualsConst(TEMP_70AF, 1, ["ACTION_21_pause_32"]),
	A_TurnRandomDirection(),
	A_Pause(30),
	A_WalkNorthwestSteps(2),
	A_Dec(TEMP_70AE),
	A_Dec(TEMP_70AE),
	A_JmpIfRandom1of2(["ACTION_21_pause_32"]),
	A_Pause(10),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_21_set_animation_speed_29"),
	A_Walk1StepNorthwest(),
	A_Dec(TEMP_70AE),
	A_Pause(20, identifier="ACTION_21_pause_32"),
	A_WalkNorthwestSteps(3),
	A_Dec(TEMP_70AE),
	A_Dec(TEMP_70AE),
	A_Dec(TEMP_70AE),
	A_JmpToSubroutine(["ACTION_21_copy_var_to_var_40"]),
	A_JmpIfVarEqualsConst(TEMP_70AF, 2, ["ACTION_21_pause_14"]),
	A_Jmp(["ACTION_21_set_var_to_const_0"]),
	A_CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_700C, identifier="ACTION_21_copy_var_to_var_40"),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702C),
	A_CompareVarToConst(TEMP_702C, 28),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_21_set_var_to_const_48"]),
	A_CompareVarToConst(TEMP_702C, 13),
	A_JmpIfComparisonResultIsLesser(["ACTION_21_set_var_to_const_51"]),
	A_SetVarToConst(TEMP_70AF, 0),
	A_ReturnQueue(),
	A_SetVarToConst(TEMP_70AF, 1, identifier="ACTION_21_set_var_to_const_48"),
	A_SetVarToConst(TEMP_70AE, 23),
	A_ReturnQueue(),
	A_SetVarToConst(TEMP_70AF, 2, identifier="ACTION_21_set_var_to_const_51"),
	A_SetVarToConst(TEMP_70AE, 17),
	A_ReturnQueue()
])
