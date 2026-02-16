#A0341_SHIP_1ST_STAIRWAY_RATS
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
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_341_set_animation_speed_22"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_341_set_animation_speed_16"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_341_set_animation_speed_8"]),
	A_SetWalkingSpeed(FAST, identifier="ACTION_341_set_animation_speed_5"),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkSoutheastSteps(5),
	A_SetAllSpeeds(NORMAL, identifier="ACTION_341_set_animation_speed_8"),
	A_Walk1StepSoutheast(),
	A_Walk1StepSouthwest(),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(VERY_FAST),
	A_WalkSouthwestSteps(3),
	A_SetAllSpeeds(NORMAL),
	A_Walk1StepSoutheast(),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_341_set_animation_speed_16"),
	A_SetSequenceSpeed(FAST),
	A_WalkNortheastSteps(3),
	A_SetAllSpeeds(NORMAL),
	A_WalkNortheastSteps(2),
	A_WalkNorthwestSteps(2),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_341_set_animation_speed_22"),
	A_SetSequenceSpeed(FAST),
	A_WalkNorthwestSteps(5),
	A_SetWalkingSpeed(NORMAL),
	A_Walk1StepSouthwest(),
	A_Jmp(["ACTION_341_set_animation_speed_5"])
])
