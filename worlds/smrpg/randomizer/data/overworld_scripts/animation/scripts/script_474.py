#A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 78, ["ACTION_474_set_priority_27"]),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(9),
	A_EndLoop(),
	A_SetAllSpeeds(SLOW, identifier="ACTION_474_set_animation_speed_8"),
	A_WalkFDirectionSteps(2),
	A_Pause(21),
	A_TurnClockwise45DegreesNTimes(2),
	A_Walk1StepFDirection(),
	A_TurnClockwise45DegreesNTimes(2),
	A_WalkFDirectionSteps(2),
	A_Pause(37),
	A_StartLoopNTimes(1),
	A_TurnClockwise45DegreesNTimes(6),
	A_Walk1StepFDirection(),
	A_TurnClockwise45DegreesNTimes(6),
	A_WalkFDirectionSteps(2),
	A_Pause(21),
	A_EndLoop(),
	A_TurnClockwise45DegreesNTimes(2),
	A_Walk1StepFDirection(),
	A_TurnClockwise45DegreesNTimes(2),
	A_Jmp(["ACTION_474_set_animation_speed_8"]),
	A_SetPriority(3, identifier="ACTION_474_set_priority_27"),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetSolidityBits(bit_4=True, cant_walk_through=True),
	A_VisibilityOn(),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(16),
	A_EndLoop(),
	A_Jmp(["ACTION_714_turn_clockwise_45_degrees_12"])
])
