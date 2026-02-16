#A0714_LANDS_END_SLOW_RANDOM_MOVING_ENEMIES
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
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 457, ["ACTION_714_set_animation_speed_19"]),
	A_SetPriority(3),
	A_SequenceLoopingOn(),
	A_ShadowOff(),
	A_SetSequenceSpeed(NORMAL),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_TurnClockwise45Degrees(identifier="ACTION_714_turn_clockwise_45_degrees_12"),
	A_WalkFDirectionSteps(2),
	A_TurnRandomDirection(),
	A_WalkFDirectionSteps(2),
	A_FaceMario(),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_714_turn_clockwise_45_degrees_12"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_714_set_animation_speed_19"),
	A_SetSequenceSpeed(NORMAL),
	A_FaceMario(identifier="ACTION_714_face_mario_21"),
	A_WalkFDirectionSteps(2),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_TurnClockwise45Degrees(),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_714_face_mario_21"])
])
