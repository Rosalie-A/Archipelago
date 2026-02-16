#A0768_LANDS_END_UNDERGROUND_GECKO
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
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 262, ["ACTION_768_set_priority_21"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 270, ["ACTION_768_set_priority_21"]),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(5),
	A_EndLoop(),
	A_SequenceLoopingOn(),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(FAST, identifier="ACTION_768_set_animation_speed_10"),
	A_TurnClockwise45Degrees(),
	A_Walk1StepFDirection(),
	A_SetSequenceSpeed(SLOW),
	A_Pause(60),
	A_SetSequenceSpeed(FAST),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_SetSequenceSpeed(VERY_SLOW),
	A_Pause(30),
	A_Jmp(["ACTION_768_set_animation_speed_10"]),
	A_SetPriority(3, identifier="ACTION_768_set_priority_21"),
	A_SequenceLoopingOn(),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(2),
	A_EndLoop(),
	A_FaceMario(identifier="ACTION_768_face_mario_28"),
	A_SetSequenceSpeed(FAST),
	A_Pause(32),
	A_FaceMario(),
	A_SetSequenceSpeed(VERY_SLOW),
	A_Pause(32),
	A_Jmp(["ACTION_768_face_mario_28"])
])
