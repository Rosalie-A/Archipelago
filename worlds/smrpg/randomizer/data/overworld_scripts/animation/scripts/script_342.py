#A0342_SHIP_2ND_STAIRWAY_RATS
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
	A_SetPriority(3),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_342_set_animation_speed_15"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_342_set_animation_speed_12"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_342_set_animation_speed_8"]),
	A_SetWalkingSpeed(FAST, identifier="ACTION_342_set_animation_speed_5"),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkSouthwestSteps(7),
	A_SetAllSpeeds(NORMAL, identifier="ACTION_342_set_animation_speed_8"),
	A_WalkSouthwestSteps(2),
	A_Walk1StepSoutheast(),
	A_WalkNortheastSteps(2),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_342_set_animation_speed_12"),
	A_SetSequenceSpeed(FAST),
	A_WalkNortheastSteps(7),
	A_SetAllSpeeds(NORMAL, identifier="ACTION_342_set_animation_speed_15"),
	A_WalkNortheastSteps(3),
	A_Walk1StepNorthwest(),
	A_WalkSouthwestSteps(3),
	A_Jmp(["ACTION_342_set_animation_speed_5"])
])
